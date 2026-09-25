from __future__ import annotations

import argparse
import hashlib
import html
import json
import os
import re
import shutil
import sys
import tempfile
import unicodedata
from datetime import datetime, timedelta, timezone
from pathlib import Path
from urllib.parse import quote, urlsplit

if __package__ in (None, ''):
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from scripts.analyze_updates import IMPORTANCE_ORDER, analyze_updates, filter_updates
from scripts.fetch_updates import GitHubClient, GitHubError, PullRequestRef, Update, fetch_repository_updates, format_utc

ROOT = Path(__file__).resolve().parents[1]

SEEN_RETENTION_DAYS = 90

WINDOW_OVERLAP_DAYS = 1


def build_report_data(items, *, since, until, generated_at, repositories, warnings=None) -> dict:
    since_text = format_utc(since)
    until_text = format_utc(until)
    if since > until:
        raise ValueError('报告窗口的开始时间晚于结束时间')
    data = [item.to_dict() for item in items]
    data.sort(key=lambda item: (
        IMPORTANCE_ORDER[item['rules']['importance']],
        -datetime.fromisoformat(item['update']['timestamp'].replace('Z', '+00:00')).timestamp(),
        item['update']['repository'], item['update']['sha'], item['update']['kind'], item['update']['url'],
    ))
    counts = {'total': len(data)}
    for level in IMPORTANCE_ORDER:
        counts[level] = sum(item['rules']['importance'] == level for item in data)
    counts['packaging_candidates'] = sum(item['rules']['packaging_candidate'] for item in data)
    counts['llm'] = sum(item['analysis_mode'] == 'llm' for item in data)
    counts['rules_only'] = sum(item['analysis_mode'] == 'rules-only' for item in data)
    return {
        'schema_version': 1,
        'window': {'since': since_text, 'until': until_text},
        'generated_at': format_utc(generated_at),
        'repositories': sorted((dict(repo) for repo in repositories), key=lambda repo: repo['repo']),
        'counts': counts,
        'warnings': sorted(set(warnings or [])),
        'items': data,
    }


def escape_markdown(value):
    text = ''.join(' ' if unicodedata.category(char) in ('Cc', 'Cf', 'Cs') else char for char in str(value))
    text = html.escape(' '.join(text.split()), quote=False)
    return re.sub(r'([\\`*_\[\]()#|>])', r'\\\1', text)


def source_link(url, label='原始记录'):
    if not isinstance(url, str) or any(char.isspace() or unicodedata.category(char).startswith('C') for char in url):
        return '来源链接不可用'
    try:
        parsed = urlsplit(url)
    except ValueError:
        return '来源链接不可用'
    if parsed.scheme != 'https' or parsed.netloc.lower() != 'github.com':
        return '来源链接不可用'
    return f'[{label}]({quote(url, safe=":/?&=#%+-._~")})'


def render_markdown(report: dict) -> str:
    escape = escape_markdown
    window = report['window']
    counts = report['counts']
    lines = [
        '# GNU RISC-V 上游更新报告',
        '',
        f'统计窗口（UTC）：{escape(window["since"])} 至 {escape(window["until"])}',
        f'生成时间（UTC）：{escape(report["generated_at"])}',
        '',
        f'共 {counts["total"]} 条相关更新：高 {counts["high"]}、中 {counts["medium"]}、低 {counts["low"]}。',
        '',
        '优先级和打包候选由规则决定；LLM 辅助分析仅供参考，最终打包需人工评估和构建测试。',
        '提交已合入不代表已经发布；关联 PR 的状态单独列出。',
        '',
        '## 仓库采集状态',
        '',
    ]
    for repo in report['repositories']:
        lines.append(f'- {escape(repo["repo"])}：{escape(repo.get("status", "unknown"))}；'
                     f'分支 {escape(repo.get("branch", "未提供"))}')
        if 'since' in repo and 'until' in repo:
            lines.append(f'  采集窗口（UTC）：{escape(repo["since"])} 至 {escape(repo["until"])}')
    if report['warnings']:
        lines.extend(['', '## 采集警告', ''])
        lines.extend(f'- {escape(warning)}' for warning in report['warnings'])
    if not counts['high']:
        lines.extend(['', '本周期未发现高价值 RISC-V 更新。'])
    statuses = {'merged': '已合入', 'open': '尚未合并', 'closed': '已关闭未合并',
                'published': '已发布', 'tagged': '标签引用'}
    for level, heading in (('high', '高优先级'), ('medium', '中优先级'), ('low', '低优先级')):
        lines.extend(['', f'## {heading}', ''])
        items = [item for item in report['items'] if item['rules']['importance'] == level]
        if not items:
            lines.append('无。')
        for item in items:
            update = item['update']
            rules = item['rules']
            kind = update['kind']
            status = statuses.get(update['status'], update['status'])
            time_label = {
                'commit': '提交时间（committer date）',
                'pull_request': 'PR 合并时间' if update['status'] == 'merged' else 'PR 更新时间',
                'release': 'Release 发布时间',
                'tag': '标签时间（附注标签使用 tagger date；轻量标签使用所指提交时间，不代表标签创建时间）',
            }.get(kind, '记录时间')
            mode = 'LLM 辅助分析' if item['analysis_mode'] == 'llm' else '仅规则分析'
            lines.extend([
                f'### {escape(update["title"])}',
                '',
                f'- 仓库：{escape(update["repository"])}；类型：{escape(kind)}；状态：{escape(status)}',
                f'- {time_label}（UTC）：{escape(update["timestamp"])}',
                f'- 作者：{escape(update["author"])}；SHA：{escape(update["sha"])}',
                f'- 来源：{source_link(update["url"])}',
            ])
            pr = update.get('pull_request')
            if pr:
                pr_status = statuses.get(pr['state'], pr['state'])
                lines.append(f'- 关联 PR {escape(pr["number"])}：{escape(pr_status)}；'
                             f'{source_link(pr["url"], "查看 PR")}')
            candidate = '是，待人工评估' if rules['packaging_candidate'] else '否'
            lines.extend([
                f'- 规则判断：{escape(rules["importance"])} / {escape(rules["category"])}；打包候选：{candidate}',
                f'- 命中规则：{"、".join(escape(rule) for rule in rules["matched_rules"]) or "无"}',
                f'- 涉及文件：{"、".join(escape(path) for path in update["files"]) or "未提供"}',
                f'- 分析方式：{mode}',
            ])
            llm = item.get('llm_assessment')
            if llm:
                lines.append(f'- LLM 分类建议：{escape(llm["importance"])} / {escape(llm["category"])}'
                             f'（不改变规则判断）')
            lines.extend([
                f'- 中文摘要：{escape(item["summary_zh"])}',
                f'- 影响：{escape(item["impact_zh"])}',
                f'- 打包建议：{escape(item["packaging_advice_zh"])}',
            ])
            if item.get('analysis_warning'):
                lines.append(f'- 分析警告：{escape(item["analysis_warning"])}')
            lines.append('')
    return '\n'.join(lines).rstrip() + '\n'


def write_reports_atomic(report, output_dir, date_slug) -> tuple[Path, Path]:
    if not isinstance(date_slug, str) or not re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9_.-]*', date_slug):
        raise ValueError('报告目录名不合法')
    output_dir = Path(output_dir)
    destination = output_dir / date_slug
    if destination.exists() or destination.is_symlink():
        raise FileExistsError('同名报告已经存在')
    markdown = render_markdown(report)
    json_text = json.dumps(report, ensure_ascii=False, indent=2, allow_nan=False) + '\n'
    output_dir.mkdir(parents=True, exist_ok=True)
    staging = Path(tempfile.mkdtemp(prefix='.report-', dir=output_dir))
    try:
        for name, content in (('report.md', markdown), ('report.json', json_text)):
            with (staging / name).open('w', encoding='utf-8') as output:
                output.write(content)
                output.flush()
                os.fsync(output.fileno())
        if destination.exists() or destination.is_symlink():
            raise FileExistsError('同名报告已经存在')
        os.rename(staging, destination)
    finally:
        if staging.exists():
            shutil.rmtree(staging)
    return destination / 'report.md', destination / 'report.json'


def parse_time(value):
    parsed = datetime.fromisoformat(value.replace('Z', '+00:00'))
    if parsed.tzinfo is None or parsed.utcoffset() is None:
        raise ValueError('时间必须包含时区')
    return parsed.astimezone(timezone.utc)


def load_config(path):
    config = json.loads(Path(path).read_text(encoding='utf-8'))
    days = config.get('default_lookback_days')
    if type(days) is not int or not 1 <= days <= 90:
        raise ValueError('回溯天数必须为 1 到 90 的整数')
    repositories = config.get('repositories')
    if not isinstance(repositories, list) or not repositories:
        raise ValueError('需要配置监控仓库')
    names = set()
    for entry in repositories:
        name = entry.get('repo', '')
        if not re.fullmatch(r'[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+', name):
            raise ValueError('仓库名称格式不正确')
        if name in names or not isinstance(entry.get('branch'), str) or not entry['branch']:
            raise ValueError('仓库重复或缺少分支')
        names.add(name)
    if not isinstance(config.get('rules'), dict):
        raise ValueError('需要配置筛选规则')
    return config


def read_state(path):
    path = Path(path)
    if not path.exists():
        return {'schema_version': 1, 'repositories': {}}
    data = json.loads(path.read_text(encoding='utf-8'))
    if not isinstance(data, dict) or data.get('schema_version') != 1:
        raise ValueError('不支持的状态文件格式')
    entries = data.get('repositories')
    if not isinstance(entries, dict):
        raise ValueError('状态文件缺少仓库信息')
    for entry in entries.values():
        if not isinstance(entry, dict) or 'until' not in entry:
            raise ValueError('状态文件缺少扫描时间')
        parse_time(entry['until'])
        if not isinstance(entry.get('seen'), dict):
            raise ValueError('状态文件缺少去重记录')
        for key, value in entry['seen'].items():
            if not isinstance(key, str):
                raise ValueError('去重记录格式不正确')
            parse_time(value)
    return data


def save_state(path, data):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(mode='w', encoding='utf-8', dir=path.parent,
                                         prefix='.state-', delete=False) as stream:
            temporary = Path(stream.name)
            json.dump(data, stream, ensure_ascii=False, indent=2, sort_keys=True)
            stream.write('\n')
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temporary, path)
    finally:
        if temporary is not None:
            temporary.unlink(missing_ok=True)


def item_key(update):
    identity = [update.repository, update.kind, update.sha, update.url]
    return hashlib.sha256(json.dumps(identity).encode('utf-8')).hexdigest()


def read_fixture(path):
    records = json.loads(Path(path).read_text(encoding='utf-8'))['items']
    items = []
    for record in records:
        record = dict(record)
        record['timestamp'] = parse_time(record['timestamp'])
        record['files'] = tuple(record.get('files', []))
        if record.get('pull_request'):
            record['pull_request'] = PullRequestRef(**record['pull_request'])
        items.append(Update(**record))
    return items


def run_tracker(config, state_path, reports_dir, now, github_client, llm_post,
                api_key, fixture_path=None):
    if now.tzinfo is None:
        raise ValueError('运行时间必须包含时区')
    now = now.astimezone(timezone.utc)
    lookback = timedelta(days=config['default_lookback_days'])
    warnings = []
    repositories = []
    next_state = {'schema_version': 1, 'repositories': {}}
    items = []
    windows = []
    if fixture_path is not None:
        items = read_fixture(fixture_path)
        since = min((item.timestamp for item in items), default=now - lookback)
        until = max([now] + [item.timestamp for item in items])
        windows.append(since)
        warnings.append('模拟数据，仅用于离线测试，不代表真实上游进展。')
        repositories = [{'repo': name, 'status': 'fixture'}
                        for name in sorted({item.repository for item in items})]
        api_key = None
    else:
        state = read_state(state_path)
        until = now
        for repository in config['repositories']:
            name = repository['repo']
            previous = state['repositories'].get(name)
            since = now - lookback
            seen = {}
            if previous:
                cutoff = parse_time(previous['until'])
                if cutoff > now:
                    raise ValueError('状态时间晚于本次运行时间')
                since = cutoff - timedelta(days=WINDOW_OVERLAP_DAYS)
                seen = dict(previous['seen'])
            windows.append(since)
            try:
                fetched = fetch_repository_updates(github_client, name, repository['branch'], since, until)
            except GitHubError as error:
                raise GitHubError(f'{name}: {error}') from None
            new = []
            for update in fetched:
                key = item_key(update)
                if key not in seen:
                    new.append(update)
                seen[key] = format_utc(now)
            items.extend(new)
            seen = {key: value for key, value in seen.items()
                    if parse_time(value) >= now - timedelta(days=SEEN_RETENTION_DAYS)}
            next_state['repositories'][name] = {'until': format_utc(until), 'seen': seen}
            repositories.append({'repo': name, 'branch': repository['branch'], 'status': 'ok',
                                 'since': format_utc(since), 'until': format_utc(until),
                                 'collected': len(fetched), 'new': len(new)})
        warnings.extend(github_client.warnings)
    assessed = filter_updates(items, config['rules'])
    prompt = (ROOT / 'prompts/analyze-updates.md').read_text(encoding='utf-8')
    analyzed = analyze_updates(assessed, api_key=api_key, prompt=prompt, post_json=llm_post,
                               api_url=os.environ.get('LLM_API_URL'), model=os.environ.get('LLM_MODEL'))
    warnings.extend(item.analysis_warning for item in analyzed if item.analysis_warning)
    report = build_report_data(analyzed, since=min(windows), until=until,
                               generated_at=now, repositories=repositories, warnings=warnings)
    slug = now.strftime('%Y%m%dT%H%M%S%fZ')
    if fixture_path is not None:
        slug += '-fixture'
    paths = write_reports_atomic(report, reports_dir, slug)
    if fixture_path is None:
        save_state(state_path, next_state)
    return paths


def main(argv=None):
    parser = argparse.ArgumentParser(description='收集 GNU RISC-V 上游更新')
    parser.add_argument('--config', type=Path, default=ROOT / 'config/repos.json')
    parser.add_argument('--state', type=Path, default=ROOT / 'state/last-success.json')
    parser.add_argument('--reports-dir', type=Path)
    parser.add_argument('--fixture', type=Path)
    parser.add_argument('--lookback-days', type=int)
    args = parser.parse_args(argv)
    try:
        config = load_config(args.config)
        if args.lookback_days is not None:
            if not 1 <= args.lookback_days <= 90:
                raise ValueError('回溯天数必须为 1 到 90 的整数')
            config['default_lookback_days'] = args.lookback_days
        output = args.reports_dir or ROOT / ('examples/output' if args.fixture else 'reports')
        client = None if args.fixture else GitHubClient(token=os.environ.get('GITHUB_TOKEN'))
        paths = run_tracker(config, args.state, output, datetime.now(timezone.utc),
                            client, None, os.environ.get('LLM_API_KEY'), args.fixture)
    except GitHubError as error:
        print(f'采集失败：{error}；扫描进度未更新。', file=sys.stderr)
        return 1
    except Exception as error:
        print(f'运行失败（{type(error).__name__}），请检查配置、网络和写入权限；未跳过失败的扫描窗口。',
              file=sys.stderr)
        return 1
    for path in paths:
        print(path)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
