# GNU RISC-V 上游更新跟踪

每周扫一遍 GCC、binutils/GDB 和 glibc 的上游，先用规则挑出和 RISC-V 有关的改动，
再让 LLM 补一段中文说明和打包建议，供 RuyiSDK 维护者评估是否更新工具链版本。

没有 LLM 密钥也能跑，只是报告里少了模型写的那部分。

脚本只用 Python 标准库（3.9 以上就能跑，Actions 里固定用 3.12），不下载源码、不编译，也不自动发布软件包。
报告是给人看的线索，不能当成“上游已经验证过”的依据。

## 本地跑

先跑离线测试和模拟采集：

```bash
python3 -m unittest discover -s tests -v
python3 scripts/run_tracker.py --fixture tests/fixtures/dry_run_updates.json
```

模拟报告写到 `examples/output/`，不联网，也不碰正式状态。
fixture 里那条 K3 提交是编的，不是真实上游进展。

真实采集走 GitHub API。匿名额度很少，建议先在环境变量中设置 `GITHUB_TOKEN`：

```bash
python3 scripts/run_tracker.py --lookback-days 7
```

`--lookback-days` 只在对应仓库还没有成功扫描记录时生效，范围 1–90。
要补扫历史就换一份状态文件和报告目录，别覆盖正在用的进度。
`--config`、`--state`、`--reports-dir` 可以改这三个路径。

## GitHub Actions

工作流位于 `.github/workflows/gnu-upstream-track.yml`，在默认分支上运行。
每周一北京时间 09:00 自动跑，也可以在 Actions 页面手动跑。
工作流先跑离线测试，再采集，最后把报告和状态提交回默认分支；其他分支只留 artifact。

| 名称 | 用途 | 默认值 |
| --- | --- | --- |
| `GITHUB_TOKEN` | GitHub API 认证 | Actions 自带 |
| `LLM_API_KEY` | LLM 密钥，Actions 里配成 Secret | 不配就只用规则 |
| `LLM_API_URL` | LLM 接口，Actions 里配成 Variable | `https://llmapi.isrc.ac.cn/v1/chat/completions` |
| `LLM_MODEL` | 模型名 | `DeepSeek-V4-Pro` |

换 DeepSeek 官方的话，URL 用 `https://api.deepseek.com/chat/completions`，
模型名 `deepseek-v4-pro`，密钥也要换成对应厂商的。接口地址只接受配置好的白名单，
带查询参数、账号密码或别的主机都不会发请求；模型名也会检查格式。提交报告需要 `contents: write`；
分支保护拦住推送时任务会失败，但已经上传的 artifact 还能下载。

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

报告里每条更新都带来源链接、SHA、作者、文件列表和命中的规则，
以及中文摘要、影响和打包建议。JSON 里 `rules` 是规则判断，
`llm_assessment` 单存模型的建议，两者分开，模型改不了规则的结论。

## 需要留意的

- 默认看的是镜像仓库的 master 分支。2026-09-19 查过一次：`bminor/binutils-gdb`
  返回 404、`bminor/glibc` 已归档，所以换成现在这三个。当时 glibc 的 master
  和 Sourceware 的 SHA 是对得上的。
- 提交标了 `merged` 只说明已经进主线，不代表发过版；标签、Release 是另外的事件。
- 标签接口按名字排序，只看第一页 30 个，覆盖可能不全，报告里会提示。
  附注标签用 tagger 时间，轻量标签只能用所指提交的时间顶上。
- 每次扫描和上次重叠一天，并且固定分支 SHA，镜像同步太慢仍然可能漏。
  仓库被归档或停用会直接报错，分支超过 30 天没动会警告。
- 采集失败或状态文件坏了就停下，不推进进度，下次从同一个起点重扫；
  报告成对写成功之后才更新状态。
- 送给 LLM 的只有筛选后的公开元数据，提示词里也写明不执行正文中的指令。
  请求超时 120 秒，每批最多 8 条、每次最多 10 批，工作流上限 45 分钟；
  没有密钥、超时、请求失败或返回格式不对都退回规则报告。
- 规则会误报也会漏报，模型写的中文一样要核对。
  飞书通知、源码分析、编译和自动打包都不在这版里。

仓库里 2026-09-25 的两份报告是单仓库试跑记录，分别扫描 GCC 和 binutils/GDB，不能当作三仓库完整周报；状态文件仍是初始化状态。

需求见 [GNU RISC-V Upstream 情报收集](https://github.com/xijing21/ruyisdk-work/blob/main/ai/gnu-news.md)。
