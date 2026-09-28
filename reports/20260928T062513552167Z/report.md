# GNU RISC-V 上游更新报告

统计窗口（UTC）：2026-09-24T13:47:00Z 至 2026-09-28T06:25:13Z
生成时间（UTC）：2026-09-28T06:25:13Z

共 8 条相关更新：高 1、中 5、低 2。

优先级和打包候选由规则决定；LLM 辅助分析仅供参考，最终打包需人工评估和构建测试。
提交已合入不代表已经发布；关联 PR 的状态单独列出。

## 仓库采集状态

- RTEMS/sourceware-mirror-binutils-gdb：ok；分支 master
  采集窗口（UTC）：2026-09-24T13:47:00Z 至 2026-09-28T06:25:13Z
- gcc-mirror/gcc：ok；分支 master
  采集窗口（UTC）：2026-09-24T13:47:00Z 至 2026-09-28T06:25:13Z
- sailfishos-mirror/glibc：ok；分支 master
  采集窗口（UTC）：2026-09-24T13:47:00Z 至 2026-09-28T06:25:13Z

## 采集警告

- RTEMS/sourceware-mirror-binutils-gdb：轻量标签没有独立时间，只能用所指提交的时间代替。
- gcc-mirror/gcc：轻量标签没有独立时间，只能用所指提交的时间代替。
- 分页在第 1 页停止，元数据覆盖不完整。
- 未配置 LLM\_API\_KEY，使用规则结果。

## 高优先级

### \[PATCH v2\] vect: Look through promotions for SAT\_TRUNC

- 仓库：gcc-mirror/gcc；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-09-27T17:34:07Z
- 作者：wangjue；SHA：19378ecd3851564bb168dd7779cb52c79193cb2d
- 来源：[原始记录](https://github.com/gcc-mirror/gcc/commit/19378ecd3851564bb168dd7779cb52c79193cb2d)
- 规则判断：high / vector-crypto-hypervisor；打包候选：是，待人工评估
- 命中规则：functional:add、functional:support、keyword:vector-crypto-hypervisor:vector、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/pr120378-3.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/pr120378-4.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/sat-trunc-promote-1.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/sat-trunc-promote-run-1.c、token:riscv、token:rv32、token:rv64
- 涉及文件：gcc/testsuite/gcc.target/riscv/rvv/autovec/pr120378-3.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/pr120378-4.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/sat-trunc-promote-1.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/sat-trunc-promote-run-1.c、gcc/tree-vect-patterns.cc
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V 向量、密码学或虚拟化相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为高；未验证构建、运行或发布状态。
- 打包建议：建议人工核对上游状态和适用版本，并完成构建及回归测试后再决定打包。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。


## 中优先级

### RISC-V: Add conditional negate expansion \[PR126245\]

- 仓库：gcc-mirror/gcc；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-09-28T04:29:20Z
- 作者：naveengowda-gcc；SHA：ec09d7005033eb1f28304af80d888b81bb3063c7
- 来源：[原始记录](https://github.com/gcc-mirror/gcc/commit/ec09d7005033eb1f28304af80d888b81bb3063c7)
- 规则判断：medium / other；打包候选：否
- 命中规则：path:gcc/config/riscv/riscv.md、path:gcc/testsuite/gcc.target/riscv/pr126245-negcc.c、token:risc-v、token:riscv
- 涉及文件：gcc/config/riscv/riscv.md、gcc/testsuite/gcc.target/riscv/pr126245-negcc.c
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V 其他变更相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为中；未验证构建、运行或发布状态。
- 打包建议：保留跟踪，暂不列为优先打包候选；需结合实际版本和测试结果人工评估。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。

### \[PATCH\]\[PR tree-optimization/126462\] Fix reassociation exposing rotate+xor to work correctly for int128 and BitInt

- 仓库：gcc-mirror/gcc；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-09-27T14:54:33Z
- 作者：JeffreyALaw；SHA：55867c37ec0dd0c4f1872183a6e43ea7dc16d479
- 来源：[原始记录](https://github.com/gcc-mirror/gcc/commit/55867c37ec0dd0c4f1872183a6e43ea7dc16d479)
- 规则判断：medium / bugfix；打包候选：是，待人工评估
- 命中规则：keyword:bugfix:fix、token:riscv
- 涉及文件：gcc/match.pd、gcc/testsuite/gcc.dg/torture/pr126462.c
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V 问题修复相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为中；未验证构建、运行或发布状态。
- 打包建议：建议人工核对上游状态和适用版本，并完成构建及回归测试后再决定打包。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。

### LoongArch: Enable shared library and PIE support for loongarch\*-elf

- 仓库：RTEMS/sourceware-mirror-binutils-gdb；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-09-27T01:45:26Z
- 作者：Mintsuki；SHA：196286d25ccc652dc086ae173d1cfa836bed0618
- 来源：[原始记录](https://github.com/RTEMS/sourceware-mirror-binutils-gdb/commit/196286d25ccc652dc086ae173d1cfa836bed0618)
- 规则判断：medium / other；打包候选：否
- 命中规则：token:risc-v
- 涉及文件：ld/emulparams/elf32loongarch-defs.sh、ld/emulparams/elf64loongarch-defs.sh
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V 其他变更相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为中；未验证构建、运行或发布状态。
- 打包建议：保留跟踪，暂不列为优先打包候选；需结合实际版本和测试结果人工评估。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。

### RISC-V: Update ARC-V RMX-100 load latency

- 仓库：gcc-mirror/gcc；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-09-25T21:08:37Z
- 作者：MichielDerhaeg；SHA：0de4790181fcf74665c3c27e901559a16d3e4991
- 来源：[原始记录](https://github.com/gcc-mirror/gcc/commit/0de4790181fcf74665c3c27e901559a16d3e4991)
- 规则判断：medium / other；打包候选：否
- 命中规则：path:gcc/config/riscv/arcv-rmx100.md、token:risc-v、token:riscv
- 涉及文件：gcc/config/riscv/arcv-rmx100.md
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V 其他变更相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为中；未验证构建、运行或发布状态。
- 打包建议：保留跟踪，暂不列为优先打包候选；需结合实际版本和测试结果人工评估。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。

### string: Drop always\_inline from tst-xbzero-opt \[BZ \#23130\]

- 仓库：sailfishos-mirror/glibc；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-09-25T11:13:56Z
- 作者：shalseth；SHA：e066af409a8de7c6ceea099a4ff6810c021f341f
- 来源：[原始记录](https://github.com/sailfishos-mirror/glibc/commit/e066af409a8de7c6ceea099a4ff6810c021f341f)
- 规则判断：medium / other；打包候选：否
- 命中规则：token:risc-v
- 涉及文件：string/tst-xbzero-opt.c
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V 其他变更相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为中；未验证构建、运行或发布状态。
- 打包建议：保留跟踪，暂不列为优先打包候选；需结合实际版本和测试结果人工评估。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。


## 低优先级

### \[RISC-V\] Fix typo and minor bugs in recently added bclr test

- 仓库：gcc-mirror/gcc；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-09-27T17:35:55Z
- 作者：JeffreyALaw；SHA：56805976a1cb252253118e8da40873857d6b0c9f
- 来源：[原始记录](https://github.com/gcc-mirror/gcc/commit/56805976a1cb252253118e8da40873857d6b0c9f)
- 规则判断：low / other；打包候选：否
- 命中规则：low-value:test、low-value:typo、path:gcc/testsuite/gcc.target/riscv/bclr-lowest-set-bit-2.c、test-only、token:risc-v、token:riscv、token:rv32、token:rv64
- 涉及文件：gcc/testsuite/gcc.target/riscv/bclr-lowest-set-bit-2.c
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V 其他变更相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为低；未验证构建、运行或发布状态。
- 打包建议：保留跟踪，暂不列为优先打包候选；需结合实际版本和测试结果人工评估。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。

### middle-end: fix self-test fails \[PR127618\]

- 仓库：gcc-mirror/gcc；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-09-26T16:18:43Z
- 作者：TamarChristinaArm；SHA：090ff9c73c79ab83eea66a010887a0ca8002ec6e
- 来源：[原始记录](https://github.com/gcc-mirror/gcc/commit/090ff9c73c79ab83eea66a010887a0ca8002ec6e)
- 规则判断：low / other；打包候选：否
- 命中规则：low-value:test、token:rv64
- 涉及文件：gcc/fold-const.cc
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V 其他变更相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为低；未验证构建、运行或发布状态。
- 打包建议：保留跟踪，暂不列为优先打包候选；需结合实际版本和测试结果人工评估。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。
