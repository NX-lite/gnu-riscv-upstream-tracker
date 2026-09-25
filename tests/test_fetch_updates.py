import json
import sys
import unittest
from datetime import datetime, timezone
from email.message import Message
from io import BytesIO
from pathlib import Path
from unittest.mock import patch
from urllib.error import HTTPError, URLError
from urllib.parse import parse_qs, urlsplit
from urllib.request import HTTPSHandler, build_opener
from urllib.response import addinfourl

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from scripts.fetch_updates import (
    GitHubClient, GitHubError, JsonResponse, PullRequestRef, Update,
    fetch_repository_updates, format_utc,
)


SINCE = datetime(2026, 9, 12, tzinfo=timezone.utc)
UNTIL = datetime(2026, 9, 19, tzinfo=timezone.utc)
PREFIX = '/repos/demo/tool'
SHA = 'a' * 40
HEAD = 'b' * 40


def commit(sha=SHA, date='2026-09-18T12:00:00Z', files=None):
    return {
        'sha': sha,
        'html_url': f'https://github.com/demo/tool/commit/{sha}',
        'author': {'login': 'ada'},
        'commit': {
            'message': 'RISC-V: fix vector lowering\n\nFix the matching rule.',
            'author': {'name': 'Ada', 'date': '2020-01-01T00:00:00Z'},
            'committer': {'name': 'Builder', 'date': date},
        },
        'files': files if files is not None else [
            {'filename': 'gcc/config/riscv/riscv.cc', 'patch': '+private code'}
        ],
    }


class FixtureTransport:

    def __init__(self, routes):
        self.routes = routes
        self.calls = []

    def __call__(self, url, headers, timeout):
        parsed = urlsplit(url)
        query = parse_qs(parsed.query)
        self.calls.append((parsed.path, query, headers, timeout))
        key = (parsed.path, int(query.get('page', ['1'])[0]))
        value = self.routes[key]
        if isinstance(value, Exception):
            raise value
        if isinstance(value, JsonResponse):
            return value
        return JsonResponse(value, {})


def routes():
    return {
        (PREFIX, 1): {'full_name': 'demo/tool', 'archived': False, 'disabled': False},
        (PREFIX + '/branches/main', 1): {'commit': {'sha': HEAD}},
        (PREFIX + '/commits', 1): [commit()],
        (PREFIX + '/commits/' + SHA, 1): commit(),
        (PREFIX + '/commits/' + SHA + '/pulls', 1): [],
        (PREFIX + '/tags', 1): [],
        (PREFIX + '/releases', 1): [],
    }


def next_link(path, page):
    return f'<https://api.github.com{path}?page={page}>; rel="next"'


class ModelTests(unittest.TestCase):
    def test_update_serialization_normalizes_time_and_files(self):
        update = Update(
            repository='gcc-mirror/gcc',
            kind='commit',
            status='merged',
            sha='abc123',
            title='RISC-V: add a useful option',
            body='Details',
            author='Ada',
            timestamp=datetime(2026, 9, 18, 8, tzinfo=timezone.utc),
            url='https://example.test/commit/abc123',
            files=('gcc/config/riscv/riscv.cc', 'README', 'gcc/config/riscv/riscv.cc'),
            pull_request=PullRequestRef(number=42, url='https://example.test/pr/42', state='merged'),
        )

        payload = update.to_dict()

        self.assertEqual(payload['timestamp'], '2026-09-18T08:00:00Z')
        self.assertEqual(payload['files'], ['README', 'gcc/config/riscv/riscv.cc'])
        self.assertEqual(payload['pull_request']['number'], 42)
        self.assertEqual(json.loads(json.dumps(payload)), payload)

    def test_format_utc_rejects_naive_datetime(self):
        with self.assertRaises(ValueError):
            format_utc(datetime(2026, 9, 18))
        self.assertEqual(format_utc(datetime(2026, 9, 18, 0, 0, 0, 123456, tzinfo=timezone.utc)),
                         '2026-09-18T00:00:00Z')


class ClientTests(unittest.TestCase):
    def test_retries_after_network_and_rate_limit_errors(self):
        calls = []
        delays = []

        def transport(url, headers, timeout):
            calls.append((url, headers, timeout))
            if len(calls) == 1:
                raise URLError('secret must not appear')
            if len(calls) == 2:
                raise HTTPError(url, 429, 'rate limited', {'Retry-After': '2'}, None)
            return JsonResponse({'ok': True}, {})

        client = GitHubClient(token='secret', transport=transport, sleep=delays.append)

        self.assertEqual(client.request_json('/repos/demo/tool').data, {'ok': True})
        self.assertEqual(delays, [1, 2])
        self.assertEqual(calls[0][1]['Authorization'], 'Bearer secret')
        self.assertEqual(calls[0][2], 15)

    def test_gives_up_after_max_retries_without_leaking_the_body(self):
        calls = []

        def transport(url, headers, timeout):
            calls.append(url)
            raise HTTPError(url, 503, 'secret server body', {}, None)

        client = GitHubClient(transport=transport, max_retries=2, sleep=lambda delay: None)

        with self.assertRaises(GitHubError) as error:
            client.request_json('/repos/demo/tool')
        self.assertEqual(len(calls), 3)
        self.assertIn('503', str(error.exception))
        self.assertNotIn('secret', str(error.exception))

    def test_other_hosts_and_redirects_never_receive_the_token(self):
        redirect_calls = []

        class RedirectServer(HTTPSHandler):
            def https_open(self, request):
                redirect_calls.append(request.full_url)
                headers = Message()
                headers['Location'] = 'https://evil.test/collect'
                response = addinfourl(BytesIO(b''), headers, request.full_url, 302)
                response.msg = 'Found'
                return response

        with patch('scripts.fetch_updates.build_opener', lambda *h: build_opener(*h, RedirectServer())):
            with self.assertRaises(GitHubError):
                GitHubClient(token='secret').request_json('/items')
        self.assertEqual(redirect_calls, ['https://api.github.com/items'])

        paginated = FixtureTransport({
            ('/items', 1): JsonResponse([1], {'Link': '<https://evil.test/items?page=2>; rel="next"'}),
        })
        with self.assertRaises(GitHubError):
            list(GitHubClient(token='secret', transport=paginated).iter_pages('/items'))
        self.assertEqual(len(paginated.calls), 1)

    def test_unparsable_response_text_is_not_echoed(self):
        def transport(*args):
            raise ValueError('secret response')

        with self.assertRaises(GitHubError) as error:
            GitHubClient(transport=transport).request_json('/items')
        self.assertNotIn('secret', str(error.exception))

    def test_pagination_follows_links_and_detects_loops(self):
        fixture = FixtureTransport({
            ('/items', 1): JsonResponse([1], {'link': next_link('/items', 2)}),
            ('/items', 2): JsonResponse([2], {'Link': next_link('/items', 2)}),
        })
        pages = GitHubClient(transport=fixture).iter_pages('/items')

        self.assertEqual(next(pages), [1])
        self.assertEqual(next(pages), [2])
        with self.assertRaises(GitHubError):
            next(pages)

    def test_pagination_limit_warns_instead_of_truncating_silently(self):
        fixture = FixtureTransport({('/items', 1): JsonResponse([1], {'Link': next_link('/items', 2)})})
        client = GitHubClient(transport=fixture)

        self.assertEqual(list(client.iter_pages('/items', max_pages=1)), [[1]])
        self.assertEqual(len(fixture.calls), 1)
        self.assertTrue(client.warnings)

    def test_broken_pagination_link_is_an_error(self):
        fixture = FixtureTransport({('/items', 1): JsonResponse([1], {'Link': 'broken; rel="next"'})})
        with self.assertRaises(GitHubError):
            list(GitHubClient(transport=fixture).iter_pages('/items'))


class CollectorTests(unittest.TestCase):
    def fetch(self, data):
        fixture = FixtureTransport(data)
        client = GitHubClient(transport=fixture, max_retries=0)
        return fetch_repository_updates(client, 'demo/tool', 'main', SINCE, UNTIL), client, fixture

    def test_archived_repository_stops_before_querying_branches(self):
        for flag in ('archived', 'disabled'):
            with self.subTest(flag=flag):
                data = routes()
                data[(PREFIX, 1)][flag] = True
                fixture = FixtureTransport(data)
                with self.assertRaisesRegex(GitHubError, flag):
                    fetch_repository_updates(GitHubClient(transport=fixture, max_retries=0),
                                             'demo/tool', 'main', SINCE, UNTIL)
                self.assertEqual([call[0] for call in fixture.calls], [PREFIX])

    def test_configured_repository_name_must_match_github(self):
        data = routes()
        data[(PREFIX, 1)]['full_name'] = 'DEMO/Tool'
        updates, _, _ = self.fetch(data)
        self.assertEqual(len(updates), 1)

        data[(PREFIX, 1)]['full_name'] = 'other/tool'
        with self.assertRaises(GitHubError):
            self.fetch(data)

    def test_stale_branch_tip_only_warns(self):
        data = routes()
        data[(PREFIX + '/branches/main', 1)] = {
            'commit': {'sha': HEAD, 'commit': {'committer': {'date': '2026-08-01T00:00:00Z'}}},
        }
        updates, client, _ = self.fetch(data)

        self.assertEqual(len(updates), 1)
        self.assertTrue(any('30' in warning for warning in client.warnings))

    def test_collects_commits_with_files_and_merged_pull_request(self):
        data = routes()
        data[(PREFIX + '/commits/' + SHA, 1)] = JsonResponse(commit(), {'Link': next_link(
            PREFIX + '/commits/' + SHA, 2)})
        data[(PREFIX + '/commits/' + SHA, 2)] = commit(files=[
            {'filename': 'gcc/new.md', 'previous_filename': 'gcc/old.md', 'patch': 'secret'}
        ])
        data[(PREFIX + '/commits/' + SHA + '/pulls', 1)] = [{
            'number': 7, 'html_url': 'https://github.com/demo/tool/pull/7', 'state': 'closed',
            'merged_at': '2026-09-19T00:00:00Z', 'title': 'Fix vectors',
        }]

        updates, client, fixture = self.fetch(data)

        self.assertEqual(len(updates), 1)
        update = updates[0]
        self.assertEqual(update.timestamp.isoformat(), '2026-09-18T12:00:00+00:00')
        self.assertEqual(update.status, 'merged')
        self.assertEqual(update.files, ('gcc/config/riscv/riscv.cc', 'gcc/new.md', 'gcc/old.md'))
        self.assertEqual(update.pull_request.number, 7)
        self.assertEqual(update.pull_request.state, 'merged')
        self.assertNotIn('private code', str(update.to_dict()))
        self.assertNotIn('secret', str(update.to_dict()))
        query = next(call[1] for call in fixture.calls if call[0] == PREFIX + '/commits')
        self.assertEqual(query['sha'], [HEAD])
        self.assertFalse(client.warnings)

    def test_commits_outside_the_window_are_dropped_once(self):
        data = routes()
        data[(PREFIX + '/commits', 1)] = JsonResponse([commit()], {'Link': next_link(PREFIX + '/commits', 2)})
        old_sha = 'c' * 40
        data[(PREFIX + '/commits', 2)] = [commit(), commit(old_sha, '2020-01-01T00:00:00Z')]

        updates, _, fixture = self.fetch(data)

        self.assertEqual([item.sha for item in updates], [SHA])
        self.assertEqual(sum(call[0] == PREFIX + '/commits/' + SHA for call in fixture.calls), 1)

    def test_missing_required_metadata_aborts_the_run(self):
        data = routes()
        del data[(PREFIX + '/commits/' + SHA, 1)]['files']
        with self.assertRaises(GitHubError):
            self.fetch(data)

    def test_commit_file_limit_aborts_instead_of_truncating(self):
        data = routes()
        data[(PREFIX + '/commits/' + SHA, 1)] = commit(
            files=[{'filename': f'file-{index}'} for index in range(3000)])
        with self.assertRaises(GitHubError):
            self.fetch(data)

    def test_optional_metadata_failures_keep_the_commit(self):
        data = routes()
        for suffix in ('/commits/' + SHA + '/pulls', '/tags', '/releases'):
            data[(PREFIX + suffix, 1)] = HTTPError('url', 404, 'secret', {}, None)

        updates, client, _ = self.fetch(data)

        self.assertEqual(len(updates), 1)
        self.assertEqual(len(client.warnings), 3)
        self.assertNotIn('secret', str(client.warnings))

    def test_annotated_tag_and_release_keep_their_own_timestamps(self):
        data = routes()
        data[(PREFIX + '/tags', 1)] = [{'name': 'v1', 'commit': {'sha': SHA}}]
        data[(PREFIX + '/git/ref/tags/v1', 1)] = {'object': {'type': 'tag', 'sha': 'd' * 40}}
        data[(PREFIX + '/git/tags/' + 'd' * 40, 1)] = {
            'object': {'type': 'commit', 'sha': SHA},
            'tagger': {'name': 'Ada', 'date': '2026-09-17T00:00:00Z'},
            'message': 'Version 1',
        }
        data[(PREFIX + '/releases', 1)] = [{
            'tag_name': 'v1', 'name': 'Version 1', 'draft': False,
            'published_at': '2026-09-18T18:00:00Z', 'body': 'Release notes',
            'html_url': 'https://github.com/demo/tool/releases/tag/v1', 'author': {'login': 'ada'},
        }]

        updates, _, fixture = self.fetch(data)

        by_kind = {item.kind: item for item in updates}
        self.assertEqual(by_kind['tag'].timestamp.day, 17)
        self.assertEqual(by_kind['release'].timestamp.hour, 18)
        self.assertEqual(by_kind['release'].sha, SHA)
        self.assertEqual(sum(call[0] == PREFIX + '/git/ref/tags/v1' for call in fixture.calls), 1)

    def test_lightweight_tag_warns_about_its_timestamp(self):
        data = routes()
        data[(PREFIX + '/tags', 1)] = [{'name': 'v1', 'commit': {'sha': SHA}}]
        data[(PREFIX + '/git/ref/tags/v1', 1)] = {'object': {'type': 'commit', 'sha': SHA}}

        updates, client, _ = self.fetch(data)

        self.assertEqual(len(updates), 2)
        self.assertTrue(any('轻量标签' in warning for warning in client.warnings))

    def test_broken_optional_pull_request_metadata_is_skipped(self):
        data = routes()
        data[(PREFIX + '/commits/' + SHA + '/pulls', 1)] = [
            {'number': 1, 'merged_at': None},
            {'number': 'bad', 'merged_at': None},
        ]

        updates, client, _ = self.fetch(data)

        self.assertEqual(len(updates), 1)
        self.assertIsNone(updates[0].pull_request)
        self.assertTrue(client.warnings)

    def test_naive_window_is_rejected_before_any_request(self):
        client = GitHubClient(transport=lambda *args: self.fail('unexpected request'))
        with self.assertRaises(ValueError):
            fetch_repository_updates(client, 'demo/tool', 'main', datetime(2026, 9, 12), UNTIL)


if __name__ == '__main__':
    unittest.main()
