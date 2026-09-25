import contextlib
import io
import json
import os
import subprocess
import sys
import tempfile
import unittest
from dataclasses import replace
from datetime import datetime, timedelta, timezone
from pathlib import Path
from unittest.mock import patch

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from scripts.analyze_updates import AnalyzedUpdate, RuleAssessment
from scripts.fetch_updates import GitHubError, PullRequestRef, Update
from scripts.run_tracker import (
    ROOT, build_report_data, load_config, main, read_state,
    render_markdown, run_tracker, write_reports_atomic,
)


SINCE = datetime(2026, 9, 12, tzinfo=timezone.utc)
UNTIL = datetime(2026, 9, 19, tzinfo=timezone.utc)


def make_item(importance='high', sha='abc123', timestamp=UNTIL):
    return AnalyzedUpdate(
        update=Update(
            repository='gcc-mirror/gcc',
            kind='commit',
            status='merged',
            sha=sha,
            title='RISC-V: add vector support',
            body='Full upstream details',
            author='Ada',
            timestamp=timestamp,
            url=f'https://github.com/gcc-mirror/gcc/commit/{sha}',
            files=('gcc/config/riscv/riscv.cc',),
            pull_request=PullRequestRef(7, 'https://github.com/gcc-mirror/gcc/pull/7', 'open'),
        ),
        rules=RuleAssessment('isa-extension', importance, ('path:riscv', 'keyword:vector'),
                             importance == 'high'),
        analysis_mode='rules-only',
        summary_zh='增加向量支持',
        impact_zh='需要进一步核对元数据与上游实现',
        packaging_advice_zh='建议人工评估',
        analysis_warning=None,
    )


def make_report(items=(), warnings=None):
    return build_report_data(
        items,
        since=SINCE,
        until=UNTIL,
        generated_at=UNTIL + timedelta(minutes=2),
        repositories=[{'repo': 'gcc-mirror/gcc', 'branch': 'master', 'status': 'ok'}],
        warnings=warnings,
    )


class ReportDataTests(unittest.TestCase):
    def test_report_keeps_full_metadata_and_counts(self):
        item = make_item()
        report = make_report([item], ['辅助标签查询失败'])

        self.assertEqual(report['schema_version'], 1)
        self.assertEqual(report['window'],
                         {'since': '2026-09-12T00:00:00Z', 'until': '2026-09-19T00:00:00Z'})
        self.assertEqual(report['generated_at'], '2026-09-19T00:02:00Z')
        self.assertEqual(report['items'], [item.to_dict()])
        self.assertEqual(report['warnings'], ['辅助标签查询失败'])
        self.assertEqual(report['counts'], {
            'total': 1, 'high': 1, 'medium': 0, 'low': 0,
            'packaging_candidates': 1, 'llm': 0, 'rules_only': 1,
        })
        self.assertEqual(json.loads(json.dumps(report)), report)

    def test_report_order_does_not_depend_on_input_order(self):
        high_old = make_item('high', 'a', UNTIL - timedelta(days=1))
        high_new = make_item('high', 'b')
        medium = make_item('medium', 'c')
        low = make_item('low', 'd')

        report = make_report([low, high_old, medium, high_new], ['z', 'a', 'z'])
        reversed_report = make_report([high_new, medium, high_old, low], ['a', 'z'])

        self.assertEqual(report, reversed_report)
        self.assertEqual([item['update']['sha'] for item in report['items']], ['b', 'a', 'c', 'd'])
        self.assertEqual(render_markdown(report), render_markdown(reversed_report))

    def test_empty_or_quiet_window_says_so_explicitly(self):
        markdown = render_markdown(make_report())
        self.assertIn('本周期未发现高价值 RISC-V 更新', markdown)
        for heading in ('## 高优先级', '## 中优先级', '## 低优先级'):
            self.assertIn(heading, markdown)

        quiet = render_markdown(make_report([make_item('low')]))
        self.assertIn('本周期未发现高价值 RISC-V 更新', quiet)

    def test_invalid_windows_are_rejected(self):
        with self.assertRaises(ValueError):
            build_report_data([], since=UNTIL, until=SINCE, generated_at=UNTIL, repositories=[])
        with self.assertRaises(ValueError):
            build_report_data([], since=SINCE.replace(tzinfo=None), until=UNTIL,
                              generated_at=UNTIL, repositories=[])


class MarkdownTests(unittest.TestCase):
    def test_report_shows_rules_sources_and_analysis(self):
        item = replace(make_item(), analysis_mode='llm', analysis_warning='模型建议需复核')
        markdown = render_markdown(make_report([item]))

        for value in ('gcc-mirror/gcc', '2026-09-19T00:00:00Z', item.update.url,
                      'keyword:vector', 'path:riscv', '规则判断', 'LLM 辅助分析',
                      item.summary_zh, item.impact_zh, item.packaging_advice_zh,
                      '模型建议需复核', 'committer date', '尚未合并'):
            self.assertIn(value, markdown)
        self.assertIn('不代表已经发布', markdown)

    def test_model_advice_never_moves_an_item_between_sections(self):
        report = make_report([make_item('low')])
        report['items'][0]['llm_assessment'] = {'importance': 'high', 'category': 'hardware'}
        report['items'][0]['analysis_mode'] = 'llm'

        markdown = render_markdown(report)

        self.assertIn('规则判断：low / isa-extension', markdown)
        self.assertIn('LLM 分类建议：high / hardware', markdown)
        self.assertGreater(markdown.index('### RISC-V'), markdown.index('## 低优先级'))

    def test_timestamps_are_labelled_per_event_type(self):
        base = make_item()
        items = [
            replace(base, update=replace(base.update, kind='pull_request', status='merged', sha='pr')),
            replace(base, update=replace(base.update, kind='release', status='published', sha='release')),
            replace(base, update=replace(base.update, kind='tag', status='tagged', sha='tag')),
        ]

        markdown = render_markdown(make_report(items))

        for label in ('PR 合并时间', 'Release 发布时间', '不代表标签创建时间'):
            self.assertIn(label, markdown)

    def test_untrusted_text_cannot_inject_markup(self):
        bad = '<img src=x onerror=alert(1)>|[click](javascript:x)\n# Header\x00\u202e'
        item = make_item()
        item = replace(
            item,
            update=replace(item.update, title=bad, author=bad, files=(bad,)),
            summary_zh=bad,
            impact_zh=bad,
            packaging_advice_zh=bad,
        )
        report = make_report([item], [bad])
        report['repositories'][0]['branch'] = bad

        markdown = render_markdown(report)

        self.assertNotIn('<img', markdown)
        self.assertNotIn('[click](javascript:x)', markdown)
        self.assertNotIn('\n# Header', markdown)
        self.assertNotIn('\x00', markdown)
        self.assertNotIn('\u202e', markdown)
        self.assertIn('&lt;img', markdown)
        self.assertEqual(report['items'][0]['summary_zh'], bad)

    def test_only_https_github_links_are_rendered(self):
        item = make_item()
        for url in ('javascript:alert(1)', 'http://github.com/x/y', 'https://github.com.evil.test/x/y',
                    'https://github.com@evil.test/x/y', 'https://evil.test/x/y', 'https://github.com/\nx'):
            with self.subTest(url=url):
                update = replace(item.update, url=url, pull_request=PullRequestRef(2, url, 'open'))
                markdown = render_markdown(make_report([replace(item, update=update)]))
                self.assertNotIn(f']({url})', markdown)
                self.assertIn('来源链接不可用', markdown)

        update = replace(item.update, url='https://github.com/gcc-mirror/gcc/commit/x)y(')
        markdown = render_markdown(make_report([replace(item, update=update)]))
        self.assertIn('https://github.com/gcc-mirror/gcc/commit/x%29y%28', markdown)


class AtomicWriteTests(unittest.TestCase):
    def test_writes_a_pair_into_its_own_directory(self):
        report = make_report([make_item()])
        with tempfile.TemporaryDirectory() as directory:
            markdown_path, json_path = write_reports_atomic(report, Path(directory), '2026-09-19-001')

            self.assertEqual(markdown_path, Path(directory) / '2026-09-19-001' / 'report.md')
            self.assertEqual(json_path, markdown_path.with_suffix('.json'))
            self.assertEqual(markdown_path.read_text(encoding='utf-8'), render_markdown(report))
            self.assertEqual(json.loads(json_path.read_text(encoding='utf-8')), report)
            self.assertEqual([path.name for path in Path(directory).iterdir()], ['2026-09-19-001'])

    def test_a_failed_write_leaves_nothing_behind(self):
        failures = [
            patch('scripts.run_tracker.os.fsync', side_effect=[None, OSError('写盘失败')]),
            patch('scripts.run_tracker.os.rename', side_effect=OSError('改名失败')),
        ]
        for failure in failures:
            with self.subTest(failure=str(failure)), tempfile.TemporaryDirectory() as directory:
                with failure:
                    with self.assertRaises(OSError):
                        write_reports_atomic(make_report(), Path(directory), '2026-09-19')
                self.assertEqual(list(Path(directory).iterdir()), [])

    def test_existing_archive_is_never_overwritten(self):
        with tempfile.TemporaryDirectory() as directory:
            markdown_path, json_path = write_reports_atomic(make_report(), Path(directory), '2026-09-19')
            before = (markdown_path.read_bytes(), json_path.read_bytes())

            with self.assertRaises(FileExistsError):
                write_reports_atomic(make_report([make_item()]), Path(directory), '2026-09-19')
            self.assertEqual((markdown_path.read_bytes(), json_path.read_bytes()), before)

    def test_slug_cannot_escape_the_output_directory(self):
        with tempfile.TemporaryDirectory() as directory:
            for slug in ('', '.', '..', '../escape', '/absolute', 'a/b'):
                with self.subTest(slug=slug), self.assertRaises(ValueError):
                    write_reports_atomic(make_report(), Path(directory), slug)


class StateTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.state = self.root / 'state.json'

    def test_missing_state_file_means_first_run(self):
        self.assertEqual(read_state(self.state), {'schema_version': 1, 'repositories': {}})

    def test_a_broken_state_file_is_fatal(self):
        broken = [
            '{',
            json.dumps({'schema_version': 2, 'repositories': {}}),
            json.dumps({'schema_version': 1, 'repositories': {
                'gcc-mirror/gcc': {'until': '2026-09-19T00:00:00', 'seen': {}}}}),
            json.dumps({'schema_version': 1, 'repositories': {'gcc-mirror/gcc': {}}}),
        ]
        for content in broken:
            with self.subTest(content=content[:30]):
                self.state.write_text(content)
                with self.assertRaises(ValueError):
                    read_state(self.state)


class RunnerTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.state = self.root / 'state.json'
        self.reports = self.root / 'reports'
        self.now = datetime(2026, 9, 19, tzinfo=timezone.utc)
        self.config = load_config(PROJECT_ROOT / 'config/repos.json')
        self.config['repositories'] = [{'repo': 'gcc-mirror/gcc', 'branch': 'master'}]
        self.client = type('Client', (), {'warnings': []})()
        self.item = Update('gcc-mirror/gcc', 'commit', 'merged', 'a' * 40,
                           'RISC-V: Add SpacemiT K3 support', '', 'Example',
                           self.now - timedelta(hours=2),
                           'https://github.com/gcc-mirror/gcc/commit/' + 'a' * 40,
                           ('gcc/config/riscv/riscv.cc',))

    def run_tracker(self, **kwargs):
        return run_tracker(self.config, self.state, self.reports, self.now,
                           self.client, None, None, **kwargs)

    def test_success_writes_report_and_checkpoint(self):
        with patch('scripts.run_tracker.fetch_repository_updates', return_value=[self.item]) as fetch:
            markdown_path, json_path = self.run_tracker()

        self.assertTrue(markdown_path.is_file())
        self.assertEqual(read_state(self.state)['repositories']['gcc-mirror/gcc']['until'],
                         '2026-09-19T00:00:00Z')
        self.assertEqual(fetch.call_args.args[3], self.now - timedelta(days=7))
        self.assertEqual(len(json.loads(json_path.read_text())['items']), 1)

    def test_second_run_dedups_and_overlaps_one_day(self):
        with patch('scripts.run_tracker.fetch_repository_updates', return_value=[self.item]) as fetch:
            self.run_tracker()
            self.now += timedelta(days=7)
            _, json_path = self.run_tracker()

        self.assertEqual(json.loads(json_path.read_text())['items'], [])
        self.assertEqual(fetch.call_args.args[3], self.now - timedelta(days=8))

    def test_repository_failure_keeps_the_previous_state(self):
        self.config['repositories'].append({'repo': 'sailfishos-mirror/glibc', 'branch': 'master'})
        old = '{"schema_version": 1, "repositories": {}}'
        self.state.write_text(old)

        with patch('scripts.run_tracker.fetch_repository_updates',
                   side_effect=[[self.item], RuntimeError('采集挂了')]):
            with self.assertRaises(RuntimeError):
                self.run_tracker()

        self.assertEqual(self.state.read_text(), old)
        self.assertFalse(self.reports.exists())

    def test_report_failure_does_not_advance_the_state(self):
        with patch('scripts.run_tracker.fetch_repository_updates', return_value=[self.item]):
            with patch('scripts.run_tracker.write_reports_atomic', side_effect=OSError('disk full')):
                with self.assertRaises(OSError):
                    self.run_tracker()

        self.assertFalse(self.state.exists())

    def test_future_checkpoint_stops_before_any_request(self):
        self.state.write_text(json.dumps({'schema_version': 1, 'repositories': {
            'gcc-mirror/gcc': {'until': '2099-01-01T00:00:00Z', 'seen': {}}}}))

        with patch('scripts.run_tracker.fetch_repository_updates') as fetch:
            with self.assertRaises(ValueError):
                self.run_tracker()

        fetch.assert_not_called()

    def test_fixture_run_never_touches_live_state(self):
        self.state.write_text('deliberately invalid live state')
        fixture = self.root / 'fixture.json'
        fixture.write_text(json.dumps({'items': [self.item.to_dict()]}))

        with patch('scripts.run_tracker.fetch_repository_updates', side_effect=AssertionError('network')):
            _, json_path = self.run_tracker(fixture_path=fixture)

        self.assertEqual(self.state.read_text(), 'deliberately invalid live state')
        report = json.loads(json_path.read_text())
        self.assertEqual(report['items'][0]['analysis_mode'], 'rules-only')
        self.assertTrue(any('模拟' in warning for warning in report['warnings']))


class CliTests(unittest.TestCase):
    def test_fixture_run_needs_no_network_and_leaves_state_alone(self):
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / 'reports'
            state = Path(directory) / 'state.json'
            state.write_text('untouched')
            stream = io.StringIO()

            with patch('socket.socket.connect', side_effect=AssertionError('network called')):
                with patch('scripts.run_tracker.GitHubClient', side_effect=AssertionError('GitHub called')) as client:
                    with patch.dict(os.environ, {'LLM_API_KEY': 'fake-secret-not-for-output'}):
                        with contextlib.redirect_stdout(stream):
                            result = main(['--fixture', str(ROOT / 'tests/fixtures/dry_run_updates.json'),
                                           '--reports-dir', str(output), '--state', str(state)])

            self.assertEqual(result, 0)
            paths = [Path(line) for line in stream.getvalue().splitlines()]
            self.assertEqual(len(paths), 2)
            report = json.loads(paths[1].read_text())
            self.assertEqual(report['counts']['total'], 3)
            self.assertEqual([report['counts'][key] for key in ('high', 'medium', 'low')], [1, 1, 1])
            self.assertEqual(report['counts']['llm'], 0)
            self.assertNotIn('fake-secret', paths[1].read_text())
            self.assertEqual(state.read_text(), 'untouched')
            client.assert_not_called()

    def test_invalid_lookback_fails_before_any_request(self):
        with patch('scripts.run_tracker.GitHubClient') as client:
            for value in ('0', '-1', '91'):
                with self.subTest(value=value), contextlib.redirect_stderr(io.StringIO()):
                    self.assertEqual(main(['--lookback-days', value]), 1)
        client.assert_not_called()

    def test_cli_hides_raw_failures_but_keeps_github_reasons(self):
        with patch('scripts.run_tracker.run_tracker', side_effect=RuntimeError('fake-secret')):
            with patch('scripts.run_tracker.GitHubClient'):
                stream = io.StringIO()
                with contextlib.redirect_stderr(stream):
                    self.assertEqual(main([]), 1)
        self.assertNotIn('fake-secret', stream.getvalue())
        self.assertIn('运行失败', stream.getvalue())

        with patch('scripts.run_tracker.run_tracker',
                   side_effect=GitHubError('GitHub 接口请求失败（HTTP 403）')):
            with patch('scripts.run_tracker.GitHubClient'):
                stream = io.StringIO()
                with contextlib.redirect_stderr(stream):
                    self.assertEqual(main([]), 1)
        self.assertIn('HTTP 403', stream.getvalue())

    def test_script_runs_even_with_an_unrelated_scripts_package(self):
        with tempfile.TemporaryDirectory() as directory:
            package = Path(directory) / 'scripts'
            package.mkdir()
            (package / '__init__.py').touch()
            result = subprocess.run(
                [sys.executable, str(ROOT / 'scripts/run_tracker.py'), '--help'],
                env={**os.environ, 'PYTHONPATH': directory},
                capture_output=True, text=True, timeout=10,
            )

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn('--fixture', result.stdout)


if __name__ == '__main__':
    unittest.main()
