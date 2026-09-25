from __future__ import annotations

import json
import re
import urllib.error
import urllib.request
from collections.abc import Callable, Iterable, Sequence
from dataclasses import asdict, dataclass

from .fetch_updates import NoRedirects as NoRedirectHandler, Update, format_utc


API_URL = 'https://llmapi.isrc.ac.cn/v1/chat/completions'
MODEL = 'DeepSeek-V4-Pro'

ALLOWED_API_URLS = {
    'https://llmapi.isrc.ac.cn/v1/chat/completions',
    'https://api.deepseek.com/chat/completions',
    'https://api.deepseek.com/v1/chat/completions',
}

BATCH_SIZE = 8
MAX_BATCHES = 10
REQUEST_TIMEOUT = 120
MAX_REQUEST_BYTES = 65536
MAX_RESPONSE_BYTES = 131072
MAX_FIELD_LENGTH = 1000

CATEGORIES = {
    'hardware', 'isa-extension', 'profile-abi', 'compiler-option',
    'vector-crypto-hypervisor', 'bugfix', 'other',
}
RESPONSE_FIELDS = {'id', 'summary_zh', 'impact_zh', 'importance', 'category', 'packaging_advice_zh'}
CATEGORY_NAMES = {
    'hardware': '硬件支持',
    'isa-extension': 'ISA 扩展',
    'profile-abi': 'Profile 或 ABI',
    'compiler-option': '编译选项',
    'vector-crypto-hypervisor': '向量、密码学或虚拟化',
    'bugfix': '问题修复',
    'other': '其他变更',
}
CATEGORY_ORDER = (
    'hardware', 'profile-abi', 'compiler-option', 'isa-extension', 'vector-crypto-hypervisor',
)
IMPORTANCE_ORDER = {'high': 0, 'medium': 1, 'low': 2}


@dataclass(frozen=True)
class RuleAssessment:
    category: str
    importance: str
    matched_rules: tuple[str, ...]
    packaging_candidate: bool

    def to_dict(self) -> dict:
        data = asdict(self)
        data['matched_rules'] = sorted(set(self.matched_rules))
        return data


@dataclass(frozen=True)
class AnalyzedUpdate:
    update: Update
    rules: RuleAssessment
    analysis_mode: str
    summary_zh: str
    impact_zh: str
    packaging_advice_zh: str
    analysis_warning: str | None = None
    llm_assessment: dict[str, str] | None = None

    def to_dict(self) -> dict:
        data = asdict(self)
        data['update'] = self.update.to_dict()
        data['rules'] = self.rules.to_dict()
        return data


def contains_keyword(text: str, keyword: str) -> bool:
    return re.search(r'(?<![a-z0-9])' + re.escape(keyword) + r'(?![a-z0-9])', text) is not None


def matching_keywords(text: str, keywords: list[str]) -> list[str]:
    return [keyword.lower() for keyword in keywords if contains_keyword(text, keyword.lower())]


def is_test_only(files: tuple[str, ...]) -> bool:
    source_files = [path.lower() for path in files if not path.rsplit('/', 1)[-1].lower().startswith('changelog')]
    return bool(source_files) and all(re.search(r'(^|/)(tests?|testsuite)(/|$)', path) for path in source_files)


def category_keywords(text: str, configured_keywords: dict) -> dict[str, list[str]]:
    matches = {category: matching_keywords(text, configured_keywords.get(category, [])) for category in CATEGORY_ORDER}
    matches['isa-extension'].extend(re.findall(r'\bz(?:v[a-z0-9]+|k[a-z0-9]+|ce)\b', text))
    matches['profile-abi'].extend(re.findall(r'\brv[ai]\d{2}[a-z0-9]*\b', text))
    return matches


def is_maintenance_title(title: str, rules: dict) -> bool:
    low_keywords = rules.get('low_value_keywords', [])
    if not matching_keywords(title, low_keywords):
        return False
    configured_keywords = rules.get('category_keywords', {})
    for clause in re.split(r'\s+and\s+|\s+with\s+(?=(?:new\s+)?tests?\b)|[;,]', title):
        if matching_keywords(clause, low_keywords):
            continue
        if matching_keywords(clause, configured_keywords.get('bugfix', [])):
            return False
        has_functional_keyword = matching_keywords(clause, rules.get('functional_keywords', []))
        if has_functional_keyword and any(category_keywords(clause, configured_keywords).values()):
            return False
    return True


def assess_update(update: Update, rules: dict[str, object]) -> RuleAssessment | None:
    title = update.title.lower().replace('\u2011', '-').replace('\u2013', '-')
    text = title + '\n' + (update.body or '').lower().replace('\u2011', '-').replace('\u2013', '-')
    evidence = []
    for path in sorted(set(update.files)):
        if any(fragment.lower() in path.lower() for fragment in rules.get('riscv_path_fragments', [])):
            evidence.append('path:' + path)
    for token in rules.get('riscv_tokens', []):
        pattern = re.escape(token.lower())
        if token.lower() in ('rv32', 'rv64'):
            pattern += '[a-z0-9]*'
        if re.search(r'(?<![a-z0-9])' + pattern + r'(?![a-z0-9])', text):
            evidence.append('token:' + token.lower())
    if not evidence:
        return None
    low_keywords = matching_keywords(title, rules.get('low_value_keywords', []))
    test_only = is_test_only(update.files)
    if is_maintenance_title(title, rules) or test_only:
        evidence.extend('low-value:' + keyword for keyword in low_keywords)
        if test_only:
            evidence.append('test-only')
        return RuleAssessment('other', 'low', tuple(evidence), False)
    configured_keywords = rules.get('category_keywords', {})
    category_matches = category_keywords(text, configured_keywords)
    for category, keywords in category_matches.items():
        evidence.extend('keyword:' + category + ':' + keyword for keyword in sorted(set(keywords)))
    bug_keywords = configured_keywords.get('bugfix', [])
    title_fixes = matching_keywords(title, bug_keywords)
    body_fixes = matching_keywords(text, bug_keywords)
    functional = matching_keywords(text, rules.get('functional_keywords', []))
    category = next((name for name in CATEGORY_ORDER if category_matches[name]), 'other')
    importance = 'medium'
    if title_fixes:
        category = 'bugfix'
        evidence.extend('keyword:bugfix:' + keyword for keyword in title_fixes)
    elif category != 'other' and functional:
        importance = 'high'
        evidence.extend('functional:' + keyword for keyword in functional)
    elif body_fixes:
        category = 'bugfix'
        evidence.extend('keyword:bugfix:' + keyword for keyword in body_fixes)
    packaging_candidate = category in rules.get('packaging_candidate_categories', [])
    return RuleAssessment(category, importance, tuple(sorted(set(evidence))), packaging_candidate)


def filter_updates(updates: Iterable[Update], rules: dict[str, object]) -> list[tuple[Update, RuleAssessment]]:
    assessed = []
    for update in updates:
        result = assess_update(update, rules)
        if result is not None:
            assessed.append((update, result))
    return sorted(assessed, key=lambda item: (
        IMPORTANCE_ORDER[item[1].importance], -item[0].timestamp.timestamp(),
        item[0].repository, item[0].sha, item[0].kind, item[0].url,
    ))


def post_json_request(url: str, headers: dict, payload: dict) -> dict:
    request = urllib.request.Request(
        url,
        data=json.dumps(payload, ensure_ascii=False).encode('utf-8'),
        headers=headers,
        method='POST',
    )
    opener = urllib.request.build_opener(NoRedirectHandler())
    try:
        with opener.open(request, timeout=REQUEST_TIMEOUT) as response:
            body = response.read(MAX_RESPONSE_BYTES + 1)
    except urllib.error.HTTPError as error:
        error.close()
        raise ValueError('LLM 接口请求失败') from None
    if len(body) > MAX_RESPONSE_BYTES:
        raise ValueError('响应超过大小上限')
    return json.loads(body)


def rules_only(update: Update, rules: RuleAssessment, warning: str) -> AnalyzedUpdate:
    category = CATEGORY_NAMES.get(rules.category, '其他变更')
    importance = {'high': '高', 'medium': '中', 'low': '低'}[rules.importance]
    advice = '建议人工核对上游状态和适用版本，并完成构建及回归测试后再决定打包。'
    if not rules.packaging_candidate:
        advice = '保留跟踪，暂不列为优先打包候选；需结合实际版本和测试结果人工评估。'
    return AnalyzedUpdate(
        update=update,
        rules=rules,
        analysis_mode='rules-only',
        summary_zh=f'检测到 RISC-V {category}相关更新，请结合原始标题和链接核对。',
        impact_zh=f'规则优先级为{importance}；未验证构建、运行或发布状态。',
        packaging_advice_zh=advice,
        analysis_warning=warning,
    )


def request_item(index: int, update: Update, rules: RuleAssessment) -> dict:
    pull_request = None
    if update.pull_request is not None:
        pull_request = {
            'number': update.pull_request.number,
            'state': update.pull_request.state[:32],
            'title': (update.pull_request.title or '')[:300],
        }
    return {
        'id': f'update-{index}',
        'repository': update.repository[:200],
        'kind': update.kind[:32],
        'status': update.status[:32],
        'sha': update.sha[:128],
        'title': update.title[:300],
        'body': (update.body or '')[:1200],
        'timestamp': format_utc(update.timestamp),
        'files': [path[:200] for path in sorted(set(update.files))[:10]],
        'pull_request': pull_request,
        'rules': {
            'category': rules.category,
            'importance': rules.importance,
            'matched_rules': [rule[:200] for rule in rules.matched_rules[:20]],
            'packaging_candidate': rules.packaging_candidate,
        },
    }


def request_payload(prompt: str, items: list[dict], model: str | None = None) -> dict:
    return {
        'model': (model or '').strip() or MODEL,
        'temperature': 0.1,
        'max_tokens': 8192,
        'messages': [
            {'role': 'system', 'content': prompt},
            {'role': 'user', 'content': json.dumps({'updates': items}, ensure_ascii=False)},
        ],
    }


def validate_response(response: dict, items: list[dict], api_key: str) -> dict[str, dict]:
    encoded = json.dumps(response, ensure_ascii=False).encode('utf-8')
    if len(encoded) > MAX_RESPONSE_BYTES:
        raise ValueError('响应超过大小上限')
    choices = response['choices']
    if not isinstance(choices, list) or len(choices) != 1:
        raise ValueError('返回的 choices 不合法')
    content = choices[0]['message']['content']
    if not isinstance(content, str) or api_key in content:
        raise ValueError('返回内容不合法')
    parsed = json.loads(content)
    if not isinstance(parsed, dict) or set(parsed) != {'updates'}:
        raise ValueError('返回的 JSON 结构不对')
    updates = parsed['updates']
    if not isinstance(updates, list) or len(updates) != len(items):
        raise ValueError('返回的条数和请求不一致')
    expected_ids = {item['id'] for item in items}
    validated = {}
    for update in updates:
        if not isinstance(update, dict) or set(update) != RESPONSE_FIELDS:
            raise ValueError('返回的字段不符合约定')
        item_id = update['id']
        if not isinstance(item_id, str) or item_id not in expected_ids or item_id in validated:
            raise ValueError('返回的 id 无法对应')
        if update['importance'] not in ('high', 'medium', 'low') or update['category'] not in CATEGORIES:
            raise ValueError('返回的分类不合法')
        for field in ('summary_zh', 'impact_zh', 'packaging_advice_zh'):
            value = update[field]
            if not isinstance(value, str) or not value.strip() or len(value) > MAX_FIELD_LENGTH:
                raise ValueError('返回的说明字段不合法')
            if api_key in value:
                raise ValueError('返回的说明字段不合法')
            if not re.search(r'[\u3400-\u9fff]', value):
                raise ValueError('说明字段必须是中文')
        validated[item_id] = update
    if set(validated) != expected_ids:
        raise ValueError('返回的 id 无法对应')
    return validated


def analyze_updates(
    assessed: Sequence[tuple[Update, RuleAssessment]],
    *,
    api_key: str | None,
    prompt: str,
    post_json: Callable | None = None,
    api_url: str | None = None,
    model: str | None = None,
) -> list[AnalyzedUpdate]:
    if not assessed:
        return []
    if not api_key or not api_key.strip():
        return [rules_only(update, rules, '未配置 LLM_API_KEY，使用规则结果。') for update, rules in assessed]
    api_url = (api_url or '').strip() or API_URL
    model = (model or '').strip() or MODEL
    if api_url not in ALLOWED_API_URLS or not re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9._-]{0,99}', model):
        return [rules_only(update, rules, 'LLM_API_URL 或 LLM_MODEL 配置无效，使用规则结果。')
                for update, rules in assessed]
    transport = post_json or post_json_request
    headers = {'Authorization': 'Bearer ' + api_key, 'Content-Type': 'application/json'}
    results = []
    index = 0
    batch_count = 0
    while index < len(assessed):
        if batch_count >= MAX_BATCHES:
            results.extend(rules_only(update, rules, '达到本次 LLM 分析批次上限，使用规则结果。')
                           for update, rules in assessed[index:])
            break
        batch = []
        while len(batch) < BATCH_SIZE and index + len(batch) < len(assessed):
            item_index = index + len(batch)
            update, rules = assessed[item_index]
            candidate = batch + [request_item(item_index, update, rules)]
            payload = request_payload(prompt, candidate, model)
            if len(json.dumps(payload, ensure_ascii=False).encode('utf-8')) > MAX_REQUEST_BYTES:
                break
            batch = candidate
        if not batch:
            update, rules = assessed[index]
            results.append(rules_only(update, rules, '分析输入超过大小限制，使用规则结果。'))
            index += 1
            continue
        batch_count += 1
        pairs = assessed[index:index + len(batch)]
        try:
            response = transport(api_url, headers, request_payload(prompt, batch, model))
            validated = validate_response(response, batch, api_key)
        except TimeoutError:
            results.extend(rules_only(update, rules, 'LLM 请求超时，使用规则结果。') for update, rules in pairs)
        except Exception:
            results.extend(rules_only(update, rules, 'LLM 请求失败或响应无效，使用规则结果。') for update, rules in pairs)
        else:
            for item, (update, rules) in zip(batch, pairs):
                advice = validated[item['id']]
                results.append(AnalyzedUpdate(
                    update=update,
                    rules=rules,
                    analysis_mode='llm',
                    summary_zh=advice['summary_zh'].strip(),
                    impact_zh=advice['impact_zh'].strip(),
                    packaging_advice_zh=advice['packaging_advice_zh'].strip(),
                    llm_assessment={'importance': advice['importance'], 'category': advice['category']},
                ))
        index += len(batch)
    return results
