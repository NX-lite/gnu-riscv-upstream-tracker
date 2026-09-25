# GNU RISC-V 上游更新跟踪

每周扫一遍 GCC、binutils/GDB 和 glibc 的上游，先用规则挑出和 RISC-V 有关的改动，
再让 LLM 补一段中文说明和打包建议，供 RuyiSDK 维护者评估是否更新工具链版本。

没有 LLM 密钥也能跑，只是报告里少了模型写的那部分。

## 本地跑

先跑离线测试和模拟采集：

```bash
python3 -m unittest discover -s tests -v
python3 scripts/run_tracker.py --fixture tests/fixtures/dry_run_updates.json
```

模拟报告写到 `examples/output/`

真实采集走 GitHub API。建议先在环境变量中设置 `GITHUB_TOKEN`：

```bash
python3 scripts/run_tracker.py --lookback-days 7
```

`--lookback-days` 只在对应仓库还没有成功扫描记录时生效，范围 1–90。
`--config`、`--state`、`--reports-dir` 可以改这三个路径。

## GitHub Actions

工作流位于 `.github/workflows/gnu-upstream-track.yml`，在默认分支上运行。
每周一北京时间 09:00 自动跑，也可以在 Actions 页面手动跑。
| 名称 | 用途 | 默认值 |
| --- | --- | --- |
| `GITHUB_TOKEN` | GitHub API 认证 | Actions 自带 |
| `LLM_API_KEY` | LLM 密钥，Actions 里配成 Secret | 不配就只用规则 |
| `LLM_API_URL` | LLM 接口，Actions 里配成 Variable | `https://llmapi.isrc.ac.cn/v1/chat/completions` |
| `LLM_MODEL` | 模型名 | `DeepSeek-V4-Pro` |

换 DeepSeek 官方的话，URL 用 `https://api.deepseek.com/chat/completions`，
模型名 `deepseek-v4-pro`，密钥也要换成对应厂商的。接口地址只接受配置好的白名单，
带查询参数、账号密码或别的主机都不会发请求；模型名也会检查格式。提交报告需要 `contents: write`；

## 文件

| 文件 | 说明 |
| --- | --- |
| `scripts/fetch_updates.py` | GitHub 请求、重试、分页和元数据采集 |
| `scripts/analyze_updates.py` | 规则筛选、LLM 分析和失败降级 |
| `scripts/run_tracker.py` | 命令行入口、去重、状态和报告 |
| `tests/` | 离线测试和一个 fixture |
| `config/repos.json`、`prompts/analyze-updates.md` | 仓库清单、筛选规则和提示词 |
| `state/last-success.json` | 上次成功时间和 90 天去重记录 |
| `reports/<运行时间>/report.md`、`report.json` | 每次运行的独立报告 |

