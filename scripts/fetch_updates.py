from __future__ import annotations

import json
import re
import time
from dataclasses import asdict, dataclass, replace
from datetime import datetime, timedelta, timezone
from http.client import HTTPException
from urllib.error import HTTPError, URLError
from urllib.parse import quote, urlencode, urlsplit
from urllib.request import HTTPRedirectHandler, Request, build_opener


TAG_PAGE_SIZE = 30
TAG_MAX_PAGES = 1

STALE_BRANCH_DAYS = 30

COMMIT_FILE_LIMIT = 3000


def format_utc(value: datetime) -> str:
    if value.tzinfo is None or value.utcoffset() is None:
        raise ValueError('时间必须包含时区')
    return value.astimezone(timezone.utc).isoformat(timespec='seconds').replace('+00:00', 'Z')


@dataclass(frozen=True)
class PullRequestRef:
    number: int
    url: str
    state: str
    title: str | None = None

    def to_dict(self) -> dict:
        return asdict(self)


@dataclass(frozen=True)
class Update:
    repository: str
    kind: str
    status: str
    sha: str
    title: str
    body: str | None
    author: str
    timestamp: datetime
    url: str
    files: tuple[str, ...]
    pull_request: PullRequestRef | None = None

    def to_dict(self) -> dict:
        data = asdict(self)
        data['timestamp'] = format_utc(self.timestamp)
        data['files'] = sorted(set(self.files))
        return data


class GitHubError(RuntimeError):
    pass


@dataclass
class JsonResponse:
    data: object
    headers: dict


class NoRedirects(HTTPRedirectHandler):
    def redirect_request(self, request, response, code, message, headers, new_url):
        return None


class GitHubClient:
    def __init__(self, token=None, transport=None, timeout=15, max_retries=3, sleep=None):
        if timeout <= 0 or max_retries < 0:
            raise ValueError('timeout 必须为正数，max_retries 不能为负数')
        self.token = token
        self.transport = transport or self._request
        self.timeout = timeout
        self.max_retries = max_retries
        self.sleep = sleep or time.sleep
        self.warnings = []

    def _request(self, url, headers, timeout):
        request = Request(url, headers=headers)
        with build_opener(NoRedirects()).open(request, timeout=timeout) as response:
            return JsonResponse(json.load(response), dict(response.headers.items()))

    def _url(self, path, params):
        if path.startswith('/') and not path.startswith('//'):
            path = 'https://api.github.com' + path
        try:
            parsed = urlsplit(path)
            valid = (
                parsed.scheme == 'https'
                and parsed.hostname == 'api.github.com'
                and parsed.port in (None, 443)
                and parsed.username is None
                and parsed.password is None
                and not parsed.fragment
            )
        except ValueError:
            valid = False
        if not valid:
            raise GitHubError('拒绝访问非 api.github.com 的地址，避免把令牌带出去')
        if params:
            query = parsed.query + ('&' if parsed.query else '') + urlencode(params)
            return parsed._replace(query=query).geturl()
        return path

    def request_json(self, path, params=None):
        url = self._url(path, params)
        headers = {
            'Accept': 'application/vnd.github+json',
            'X-GitHub-Api-Version': '2022-11-28',
            'User-Agent': 'gnu-upstream-tracker',
        }
        if self.token:
            headers['Authorization'] = 'Bearer ' + self.token
        for attempt in range(self.max_retries + 1):
            delay = min(2 ** attempt, 60)
            try:
                result = self.transport(url, headers, self.timeout)
                if not isinstance(result, JsonResponse):
                    raise GitHubError('GitHub 返回了非预期的响应对象')
                return result
            except HTTPError as error:
                response_headers = {key.lower(): value for key, value in (error.headers or {}).items()}
                status = error.code
                if error.fp is not None:
                    error.close()
                retryable = status == 429 or 500 <= status < 600
                if status == 403:
                    retryable = (response_headers.get('x-ratelimit-remaining') == '0'
                                 or 'retry-after' in response_headers)
                if not retryable or attempt == self.max_retries:
                    raise GitHubError(f'GitHub 接口请求失败（HTTP {status}）') from None
                try:
                    if 'retry-after' in response_headers:
                        delay = min(60, max(0, float(response_headers['retry-after'])))
                    elif 'x-ratelimit-reset' in response_headers:
                        delay = min(60, max(0, float(response_headers['x-ratelimit-reset']) - time.time()))
                except ValueError:
                    pass
            except (URLError, OSError, HTTPException):
                if attempt == self.max_retries:
                    raise GitHubError('GitHub 接口在网络重试后仍然失败') from None
            except (ValueError, UnicodeError):
                raise GitHubError('GitHub 返回的内容不是合法 JSON') from None
            self.sleep(delay)

    def iter_pages(self, path, params=None, max_pages=None):
        if max_pages is not None and max_pages < 1:
            raise ValueError('max_pages 必须为正数')
        next_url = self._url(path, params)
        visited = set()
        page_count = 0
        while next_url:
            next_url = self._url(next_url, None)
            if next_url in visited:
                raise GitHubError('GitHub 分页出现了循环')
            visited.add(next_url)
            response = self.request_json(next_url)
            yield response.data
            page_count += 1
            link = next((value for key, value in response.headers.items() if key.lower() == 'link'), '')
            next_url = None
            for match in re.finditer(r'<([^>]+)>\s*;\s*rel="([^"]+)"', link):
                if 'next' in match.group(2).split():
                    next_url = match.group(1)
                    break
            if re.search(r'\brel="[^"]*\bnext\b', link) and next_url is None:
                raise GitHubError('GitHub 返回的分页链接不合法')
            if next_url and max_pages is not None and page_count >= max_pages:
                self.warnings.append(f'分页在第 {max_pages} 页停止，元数据覆盖不完整。')
                break


def required_text(data, key):
    value = data.get(key) if isinstance(data, dict) else None
    if not isinstance(value, str) or not value.strip():
        raise GitHubError(f'GitHub 元数据缺少有效的 {key}')
    return value


def optional_text(data, key):
    value = data.get(key)
    if value is not None and not isinstance(value, str):
        raise GitHubError(f'GitHub 元数据的 {key} 不是文本')
    return value


def parse_date(value):
    try:
        result = datetime.fromisoformat(value.replace('Z', '+00:00'))
        if result.tzinfo is None or result.utcoffset() is None:
            raise ValueError
        return result.astimezone(timezone.utc)
    except (AttributeError, ValueError, TypeError):
        raise GitHubError('GitHub 返回的时间格式无法解析') from None


def list_page(value):
    if not isinstance(value, list) or any(not isinstance(item, dict) for item in value):
        raise GitHubError('GitHub 返回的元数据列表不合法')
    return value


def commit_date(value):
    metadata = value.get('commit', {})
    if not isinstance(metadata, dict):
        raise GitHubError('GitHub 返回的提交元数据不合法')
    return parse_date(required_text(metadata.get('committer'), 'date'))


def fetch_commit(client, repository, sha):
    path = f'/repos/{repository}/commits/{quote(sha, safe="")}'
    details = None
    filenames = set()
    file_count = 0
    for page in client.iter_pages(path, {'per_page': 100}):
        if not isinstance(page, dict) or page.get('sha') != sha:
            raise GitHubError('提交详情和请求的 SHA 对不上')
        if details is None:
            details = page
        files = list_page(page.get('files'))
        file_count += len(files)
        if file_count >= COMMIT_FILE_LIMIT:
            raise GitHubError('提交触及的文件数达到 GitHub 的 3000 文件上限，无法保证元数据完整')
        for changed_file in files:
            filenames.add(required_text(changed_file, 'filename'))
            previous = changed_file.get('previous_filename')
            if previous:
                filenames.add(required_text(changed_file, 'previous_filename'))
    if details is None:
        raise GitHubError('GitHub 没有返回提交详情')
    metadata = details.get('commit')
    message = required_text(metadata, 'message')
    title, _, body = message.partition('\n')
    author_info = details.get('author')
    if author_info is not None and not isinstance(author_info, dict):
        raise GitHubError('GitHub 返回的提交作者信息不合法')
    author = optional_text(author_info or {}, 'login')
    if not author:
        author = required_text(metadata.get('author'), 'name')
    return Update(
        repository=repository, kind='commit', status='merged', sha=sha,
        title=title, body=body.strip() or None, author=author,
        timestamp=commit_date(details), url=required_text(details, 'html_url'),
        files=tuple(sorted(filenames)),
    )


def fetch_pull_request(client, repository, sha):
    candidates = []
    for page in client.iter_pages(f'/repos/{repository}/commits/{sha}/pulls', {'per_page': 100}):
        candidates.extend(list_page(page))
    if not candidates:
        return None
    for item in candidates:
        number = item.get('number')
        if not isinstance(number, int) or isinstance(number, bool) or number < 1:
            raise GitHubError('GitHub 返回的 PR 编号不合法')
    candidates.sort(key=lambda item: (not bool(item.get('merged_at')), item.get('number', 0)))
    item = candidates[0]
    return PullRequestRef(
        number=item['number'], url=required_text(item, 'html_url'),
        state='merged' if item.get('merged_at') else required_text(item, 'state'),
        title=optional_text(item, 'title'),
    )


def resolve_tag(client, repository, name, commits, tags):
    if name in tags:
        return tags[name]
    base = f'/repos/{repository}'
    ref = client.request_json(f'{base}/git/ref/tags/{quote(name, safe="")}').data
    obj = ref.get('object') if isinstance(ref, dict) else None
    tag_date = None
    author = None
    message = None
    for depth in range(6):
        sha = required_text(obj, 'sha')
        kind = required_text(obj, 'type')
        if kind == 'commit':
            break
        if kind != 'tag' or depth == 5:
            raise GitHubError('标签在五层 tag 对象内没有解析到提交')
        annotated = client.request_json(f'{base}/git/tags/{quote(sha, safe="")}').data
        if not isinstance(annotated, dict):
            raise GitHubError('GitHub 返回的附注标签元数据不合法')
        if tag_date is None:
            tagger = annotated.get('tagger')
            tag_date = parse_date(required_text(tagger, 'date'))
            author = required_text(tagger, 'name')
            message = optional_text(annotated, 'message')
        obj = annotated.get('object')
    if tag_date is None:
        warning = f'{repository}：轻量标签没有独立时间，只能用所指提交的时间代替。'
        if warning not in client.warnings:
            client.warnings.append(warning)
        if sha in commits:
            tag_date = commits[sha].timestamp
            author = commits[sha].author
        else:
            target = client.request_json(f'{base}/git/commits/{quote(sha, safe="")}').data
            if not isinstance(target, dict):
                raise GitHubError('GitHub 返回的标签指向元数据不合法')
            tag_date = parse_date(required_text(target.get('committer'), 'date'))
            author = required_text(target.get('author'), 'name')
    tags[name] = (sha, tag_date, author, message)
    return tags[name]


def fetch_repository_updates(client, repository, branch, since, until):
    format_utc(since)
    format_utc(until)
    if since > until:
        raise ValueError('since 不能晚于 until')
    if not re.fullmatch(r'[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+', repository):
        raise ValueError('仓库名必须是 owner/name 形式')
    if not isinstance(branch, str) or not branch.strip():
        raise ValueError('分支名不能为空')
    base = f'/repos/{repository}'
    repository_info = client.request_json(base).data
    if not isinstance(repository_info, dict):
        raise GitHubError('GitHub 返回的仓库元数据不合法')
    for flag in ('archived', 'disabled'):
        if repository_info.get(flag) is True:
            raise GitHubError(f'{repository} 已 {flag}，需要先确认配置的镜像源')
    if 'full_name' in repository_info:
        if required_text(repository_info, 'full_name').casefold() != repository.casefold():
            raise GitHubError('GitHub 返回的仓库名和配置不一致')
    snapshot = client.request_json(f'{base}/branches/{quote(branch, safe="")}').data
    snapshot_sha = required_text(snapshot.get('commit') if isinstance(snapshot, dict) else None, 'sha')
    tip_metadata = snapshot['commit'].get('commit')
    if isinstance(tip_metadata, dict) and isinstance(tip_metadata.get('committer'), dict):
        tip_date = tip_metadata['committer'].get('date')
        if tip_date is not None:
            try:
                if parse_date(tip_date) < until - timedelta(days=STALE_BRANCH_DAYS):
                    client.warnings.append(
                        f'{repository}：分支顶端超过 {STALE_BRANCH_DAYS} 天没有更新，请确认镜像是否正常。')
            except GitHubError:
                client.warnings.append(f'{repository}：分支顶端时间不合法，无法确认镜像新鲜度。')
    params = {'sha': snapshot_sha, 'since': format_utc(since), 'until': format_utc(until), 'per_page': 100}
    commits = {}
    for page in client.iter_pages(f'{base}/commits', params):
        for item in list_page(page):
            sha = required_text(item, 'sha')
            if sha in commits or not since <= commit_date(item) <= until:
                continue
            update = fetch_commit(client, repository, sha)
            if not since <= update.timestamp <= until:
                raise GitHubError('提交时间在列表和详情接口之间发生了变化')
            try:
                pull_request = fetch_pull_request(client, repository, sha)
            except GitHubError as error:
                client.warnings.append(f'{repository}：{sha[:12]} 的 PR 元数据不可用：{error}')
                pull_request = None
            if pull_request is not None:
                update = replace(update, pull_request=pull_request)
            commits[sha] = update
    updates = list(commits.values())
    tags = {}
    try:
        for page in client.iter_pages(f'{base}/tags', {'per_page': TAG_PAGE_SIZE}, max_pages=TAG_MAX_PAGES):
            for item in list_page(page):
                name = required_text(item, 'name')
                sha, timestamp, author, message = resolve_tag(client, repository, name, commits, tags)
                if since <= timestamp <= until:
                    updates.append(Update(
                        repository=repository, kind='tag', status='tagged', sha=sha,
                        title=f'Tag {name}', body=message, author=author, timestamp=timestamp,
                        url=f'https://github.com/{repository}/releases/tag/{quote(name, safe="")}', files=(),
                    ))
    except GitHubError as error:
        client.warnings.append(f'{repository}：标签元数据不完整：{error}')
    try:
        for page in client.iter_pages(f'{base}/releases', {'per_page': 100}):
            for item in list_page(page):
                if item.get('draft'):
                    continue
                timestamp = parse_date(required_text(item, 'published_at'))
                if not since <= timestamp <= until:
                    continue
                name = required_text(item, 'tag_name')
                title = optional_text(item, 'name') or name
                body = optional_text(item, 'body')
                sha, _, _, _ = resolve_tag(client, repository, name, commits, tags)
                updates.append(Update(
                    repository=repository, kind='release', status='published', sha=sha,
                    title=title, body=body,
                    author=required_text(item.get('author'), 'login'), timestamp=timestamp,
                    url=required_text(item, 'html_url'), files=(),
                ))
    except GitHubError as error:
        client.warnings.append(f'{repository}：Release 元数据不完整：{error}')
    return sorted(updates, key=lambda item: (item.timestamp, item.kind, item.sha, item.url))
