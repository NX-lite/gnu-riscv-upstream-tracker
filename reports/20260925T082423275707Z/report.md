# GNU RISC-V 上游更新报告

统计窗口（UTC）：2026-09-24T08:24:23Z 至 2026-09-25T08:24:23Z
生成时间（UTC）：2026-09-25T08:24:23Z

共 2 条相关更新：高 0、中 2、低 0。

优先级和打包候选由规则决定；LLM 辅助分析仅供参考，最终打包需人工评估和构建测试。
提交已合入不代表已经发布；关联 PR 的状态单独列出。

## 仓库采集状态

- RTEMS/sourceware-mirror-binutils-gdb：ok；分支 master
  采集窗口（UTC）：2026-09-24T08:24:23Z 至 2026-09-25T08:24:23Z

## 采集警告

- RTEMS/sourceware-mirror-binutils-gdb：Release 元数据不完整：GitHub 接口请求失败（HTTP 403）
- RTEMS/sourceware-mirror-binutils-gdb：标签元数据不完整：GitHub 接口请求失败（HTTP 403）
- RTEMS/sourceware-mirror-binutils-gdb：轻量标签没有独立时间，只能用所指提交的时间代替。

本周期未发现高价值 RISC-V 更新。

## 高优先级

无。

## 中优先级

### RISC-V: Describe relax passes with a pass table

- 仓库：RTEMS/sourceware-mirror-binutils-gdb；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-09-24T12:52:21Z
- 作者：kito-cheng；SHA：86f36538c5bba33aeec762b4907f37553c1a3173
- 来源：[原始记录](https://github.com/RTEMS/sourceware-mirror-binutils-gdb/commit/86f36538c5bba33aeec762b4907f37553c1a3173)
- 规则判断：medium / other；打包候选：否
- 命中规则：path:bfd/elfnn-riscv.c、path:bfd/elfxx-riscv.h、path:ld/emultempl/riscvelf.em、token:risc-v、token:riscv
- 涉及文件：bfd/elfnn-riscv.c、bfd/elfxx-riscv.h、ld/emultempl/riscvelf.em
- 分析方式：LLM 辅助分析
- LLM 分类建议：medium / other（不改变规则判断）
- 中文摘要：上游 binutils-gdb 已合入提交：将 RISC-V 的 relax pass 选择逻辑从分支链重构为 riscv\_relax\_pass 表驱动形式，并把 pass 数量存入 link\_info.relax\_pass；提交说明称现有 pass 与原先相同，链接输出无变化。
- 影响：主要影响上游 RISC-V 链接器的代码结构和可维护性，为后续 vendor-specific 或 Zcmt table jump 等新 relax pass 提供扩展点；据提交描述当前不改变链接输出。局限：仅依据上游元数据判断，不能确认该变更已经构建、测试或已进入 RuyiSDK 工具链，实际影响需在目标版本中人工核对。
- 打包建议：建议打包 binutils/gdb 时先人工确认目标源码版本是否合入该提交及后续修复；由于是重构且上游声明无输出变化，可侧重回归 RISC-V 链接结果和 relax 相关用例，确认没有意外差异；若 RuyiSDK 使用固定版本，应评估是否需要回溯或等待正式发布，不能直接视为已测试通过。

### RISC-V: Enable shared library and PIE support for riscv\*-elf

- 仓库：RTEMS/sourceware-mirror-binutils-gdb；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-09-24T10:20:57Z
- 作者：Mintsuki；SHA：b73d23cccf5568321cabaad3a8ec5cddafdef4ec
- 来源：[原始记录](https://github.com/RTEMS/sourceware-mirror-binutils-gdb/commit/b73d23cccf5568321cabaad3a8ec5cddafdef4ec)
- 规则判断：medium / other；打包候选：否
- 命中规则：path:ld/emulparams/elf32lriscv-defs.sh、token:risc-v、token:riscv
- 涉及文件：ld/emulparams/elf32lriscv-defs.sh
- 分析方式：LLM 辅助分析
- LLM 分类建议：medium / other（不改变规则判断）
- 中文摘要：上游 binutils-gdb 已合入提交：修改 ld/emulparams/elf32lriscv-defs.sh，使 riscv\*-elf 目标也生成共享库脚本和 PIE 脚本，从而允许 ld 接受 -shared 与 -pie；此前该目标被排除在外，本次变更与 aarch64\*-elf、arm-elf 等裸机 ELF 目标的做法对齐。
- 影响：对 riscv\*-elf 裸机/嵌入式工具链而言，链接器能力发生变化，可生成 ET\_DYN 的共享对象或 PIE 镜像，可能属于功能增强，也可能影响原有嵌入式链接行为。局限：仅依据上游提交，不能确认在 RuyiSDK 工具链中已合入、构建或测试通过，需人工验证实际支持情况。
- 打包建议：需人工核实所用 binutils 版本或分支是否包含该提交，并检查 RuyiSDK 对 riscv\*-elf 工具链的定位；建议回归 -shared、-pie 及常规静态链接场景，确认链接脚本生成和 ELF 头符合预期；若面向嵌入式场景，应评估 ET\_DYN 镜像是否会被误用或与引导/烧写流程冲突，不能仅凭上游提交即认为已受支持。


## 低优先级

无。
