# GNU RISC-V 上游更新报告

统计窗口（UTC）：2026-10-18T05:51:13Z 至 2026-10-26T05:50:24Z
生成时间（UTC）：2026-10-26T05:50:24Z

共 18 条相关更新：高 5、中 11、低 2。

优先级和打包候选由规则决定；LLM 辅助分析仅供参考，最终打包需人工评估和构建测试。
提交已合入不代表已经发布；关联 PR 的状态单独列出。

## 仓库采集状态

- RTEMS/sourceware-mirror-binutils-gdb：ok；分支 master
  采集窗口（UTC）：2026-10-18T05:51:13Z 至 2026-10-26T05:50:24Z
- gcc-mirror/gcc：ok；分支 master
  采集窗口（UTC）：2026-10-18T05:51:13Z 至 2026-10-26T05:50:24Z
- sailfishos-mirror/glibc：ok；分支 master
  采集窗口（UTC）：2026-10-18T05:51:13Z 至 2026-10-26T05:50:24Z

## 采集警告

- RTEMS/sourceware-mirror-binutils-gdb：轻量标签没有独立时间，只能用所指提交的时间代替。
- gcc-mirror/gcc：轻量标签没有独立时间，只能用所指提交的时间代替。
- 分页在第 1 页停止，元数据覆盖不完整。
- 未配置 LLM\_API\_KEY，使用规则结果。

## 高优先级

### \[PATCH v2 1/2\] sparc: Enable -fasynchronous-unwind-tables by default on sparc64 Linux \[PR128091\]

- 仓库：gcc-mirror/gcc；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-10-24T13:34:11Z
- 作者：shalseth；SHA：31c410d9141f6d1d96541ee5ccbdd1ee73b1f255
- 来源：[原始记录](https://github.com/gcc-mirror/gcc/commit/31c410d9141f6d1d96541ee5ccbdd1ee73b1f255)
- 规则判断：high / compiler-option；打包候选：是，待人工评估
- 命中规则：functional:enable、keyword:compiler-option:option、token:riscv
- 涉及文件：gcc/common/config/sparc/sparc-common.cc、gcc/config.gcc
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V 编译选项相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为高；未验证构建、运行或发布状态。
- 打包建议：建议人工核对上游状态和适用版本，并完成构建及回归测试后再决定打包。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。

### expand: Improve tuple-extraction handling.

- 仓库：gcc-mirror/gcc；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-10-22T10:22:25Z
- 作者：Robin Dapp；SHA：d5ac76d8da87236519d4ee9144ae993302814981
- 来源：[原始记录](https://github.com/gcc-mirror/gcc/commit/d5ac76d8da87236519d4ee9144ae993302814981)
- 规则判断：high / vector-crypto-hypervisor；打包候选：是，待人工评估
- 命中规则：functional:adds、functional:improve、keyword:vector-crypto-hypervisor:vector、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/pr125390.c、token:riscv
- 涉及文件：gcc/expmed.cc、gcc/testsuite/gcc.target/riscv/rvv/autovec/pr125390.c
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V 向量、密码学或虚拟化相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为高；未验证构建、运行或发布状态。
- 打包建议：建议人工核对上游状态和适用版本，并完成构建及回归测试后再决定打包。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。

### RISC-V: Support ".option \[no\]exact" assembler directives

- 仓库：RTEMS/sourceware-mirror-binutils-gdb；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-10-22T08:15:08Z
- 作者：a4lg；SHA：21cffe7c0955c6bdb0c14ded96939d409f3c21f0
- 来源：[原始记录](https://github.com/RTEMS/sourceware-mirror-binutils-gdb/commit/21cffe7c0955c6bdb0c14ded96939d409f3c21f0)
- 规则判断：high / compiler-option；打包候选：是，待人工评估
- 命中规则：functional:add、functional:adds、functional:enable、functional:enabled、functional:support、keyword:compiler-option:option、keyword:compiler-option:options、path:gas/config/tc-riscv.c、path:gas/doc/c-riscv.texi、path:gas/testsuite/gas/riscv/exact-branch-extern-exact.d、path:gas/testsuite/gas/riscv/exact-branch-extern-noexact.d、path:gas/testsuite/gas/riscv/exact-branch-extern.s、path:gas/testsuite/gas/riscv/exact-branch-local-exact-fail.d、path:gas/testsuite/gas/riscv/exact-branch-local-exact-fail.l、path:gas/testsuite/gas/riscv/exact-branch-local-exact-ok.d、path:gas/testsuite/gas/riscv/exact-branch-local-noexact.d、path:gas/testsuite/gas/riscv/exact-branch-local.s、path:gas/testsuite/gas/riscv/exact-li32.d、path:gas/testsuite/gas/riscv/exact-li64.d、path:gas/testsuite/gas/riscv/exact.d、path:gas/testsuite/gas/riscv/exact.s、path:gas/testsuite/gas/riscv/li32.s、path:gas/testsuite/gas/riscv/li64.s、path:gas/testsuite/gas/riscv/no-relax-branch-offset-fail.l、path:gas/testsuite/gas/riscv/no-relax-branch-offset-fail.s、path:include/opcode/riscv.h、path:opcodes/riscv-opc.c、token:risc-v、token:riscv
- 涉及文件：gas/config/tc-riscv.c、gas/doc/c-riscv.texi、gas/testsuite/gas/riscv/exact-branch-extern-exact.d、gas/testsuite/gas/riscv/exact-branch-extern-noexact.d、gas/testsuite/gas/riscv/exact-branch-extern.s、gas/testsuite/gas/riscv/exact-branch-local-exact-fail.d、gas/testsuite/gas/riscv/exact-branch-local-exact-fail.l、gas/testsuite/gas/riscv/exact-branch-local-exact-ok.d、gas/testsuite/gas/riscv/exact-branch-local-noexact.d、gas/testsuite/gas/riscv/exact-branch-local.s、gas/testsuite/gas/riscv/exact-li32.d、gas/testsuite/gas/riscv/exact-li64.d、gas/testsuite/gas/riscv/exact.d、gas/testsuite/gas/riscv/exact.s、gas/testsuite/gas/riscv/li32.s、gas/testsuite/gas/riscv/li64.s、gas/testsuite/gas/riscv/no-relax-branch-offset-fail.l、gas/testsuite/gas/riscv/no-relax-branch-offset-fail.s、include/opcode/riscv.h、opcodes/riscv-opc.c
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V 编译选项相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为高；未验证构建、运行或发布状态。
- 打包建议：建议人工核对上游状态和适用版本，并完成构建及回归测试后再决定打包。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。

### PR rtl-optimization/123905 - Failure to optimize away sign extension on RISC-V

- 仓库：gcc-mirror/gcc；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-10-21T22:35:53Z
- 作者：MilanTripkovic02；SHA：5827af4ea1ea11036b336e1029b4a25ca670b594
- 来源：[原始记录](https://github.com/gcc-mirror/gcc/commit/5827af4ea1ea11036b336e1029b4a25ca670b594)
- 规则判断：high / isa-extension；打包候选：是，待人工评估
- 命中规则：functional:improve、functional:optimize、keyword:isa-extension:extension、path:gcc/testsuite/gcc.target/riscv/pr123905.c、token:risc-v、token:riscv
- 涉及文件：gcc/ext-dce.cc、gcc/rtlanal.cc、gcc/testsuite/gcc.target/riscv/pr123905.c
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V ISA 扩展相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为高；未验证构建、运行或发布状态。
- 打包建议：建议人工核对上游状态和适用版本，并完成构建及回归测试后再决定打包。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。

### \[RiscV\] Add ECF flags to builtins

- 仓库：gcc-mirror/gcc；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-10-21T15:02:09Z
- 作者：urnathan；SHA：8f606245e96ee370d6aed593dea350dd0502be94
- 来源：[原始记录](https://github.com/gcc-mirror/gcc/commit/8f606245e96ee370d6aed593dea350dd0502be94)
- 规则判断：high / vector-crypto-hypervisor；打包候选：是，待人工评估
- 命中规则：functional:add、keyword:vector-crypto-hypervisor:crypto、path:gcc/config/riscv/andes.def、path:gcc/config/riscv/corev.def、path:gcc/config/riscv/riscv-builtins.cc、path:gcc/config/riscv/riscv-cmo.def、path:gcc/config/riscv/riscv-scalar-crypto.def、path:gcc/testsuite/gcc.target/riscv/builtin-ecf.c、token:riscv
- 涉及文件：gcc/config/riscv/andes.def、gcc/config/riscv/corev.def、gcc/config/riscv/riscv-builtins.cc、gcc/config/riscv/riscv-cmo.def、gcc/config/riscv/riscv-scalar-crypto.def、gcc/testsuite/gcc.target/riscv/builtin-ecf.c
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V 向量、密码学或虚拟化相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为高；未验证构建、运行或发布状态。
- 打包建议：建议人工核对上游状态和适用版本，并完成构建及回归测试后再决定打包。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。


## 中优先级

### \[RISC-V\] Fix long branch sequences for Andes extensions

- 仓库：gcc-mirror/gcc；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-10-26T04:16:25Z
- 作者：JeffreyALaw；SHA：1205507f6f358710418e9e9d742b3bbc780b9d61
- 来源：[原始记录](https://github.com/gcc-mirror/gcc/commit/1205507f6f358710418e9e9d742b3bbc780b9d61)
- 规则判断：medium / bugfix；打包候选：是，待人工评估
- 命中规则：keyword:bugfix:fix、path:gcc/config/riscv/andes.md、path:gcc/config/riscv/iterators.md、token:risc-v、token:riscv
- 涉及文件：gcc/config/riscv/andes.md、gcc/config/riscv/iterators.md
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V 问题修复相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为中；未验证构建、运行或发布状态。
- 打包建议：建议人工核对上游状态和适用版本，并完成构建及回归测试后再决定打包。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。

### \[V850\] Fix length computation for branches in V850 port

- 仓库：gcc-mirror/gcc；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-10-26T04:05:23Z
- 作者：JeffreyALaw；SHA：b31c358dd66fda84de3eb55e5d5924dfda8dc68a
- 来源：[原始记录](https://github.com/gcc-mirror/gcc/commit/b31c358dd66fda84de3eb55e5d5924dfda8dc68a)
- 规则判断：medium / bugfix；打包候选：是，待人工评估
- 命中规则：keyword:bugfix:fix、token:risc-v
- 涉及文件：gcc/config/v850/v850.md、gcc/testsuite/gcc.target/v850/min\_bit.c
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V 问题修复相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为中；未验证构建、运行或发布状态。
- 打包建议：建议人工核对上游状态和适用版本，并完成构建及回归测试后再决定打包。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。

### \[RISC-V\] Remove unused and buggy pattern for testing &gt;= 1

- 仓库：gcc-mirror/gcc；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-10-26T04:00:12Z
- 作者：JeffreyALaw；SHA：0ac3a264c9675d8aac3907bd6f33a1d38c8d72b1
- 来源：[原始记录](https://github.com/gcc-mirror/gcc/commit/0ac3a264c9675d8aac3907bd6f33a1d38c8d72b1)
- 规则判断：medium / other；打包候选：否
- 命中规则：path:gcc/config/riscv/riscv.md、token:risc-v、token:riscv
- 涉及文件：gcc/config/riscv/riscv.md
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V 其他变更相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为中；未验证构建、运行或发布状态。
- 打包建议：保留跟踪，暂不列为优先打包候选；需结合实际版本和测试结果人工评估。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。

### \[RISC-V\] Fix incorrect long branch sequence for Andes and REGNO reference in peephole

- 仓库：gcc-mirror/gcc；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-10-24T16:28:13Z
- 作者：JeffreyALaw；SHA：cada5a5bcdc4ec5e1d8e56fed922330e8b95887c
- 来源：[原始记录](https://github.com/gcc-mirror/gcc/commit/cada5a5bcdc4ec5e1d8e56fed922330e8b95887c)
- 规则判断：medium / bugfix；打包候选：是，待人工评估
- 命中规则：keyword:bugfix:fix、path:gcc/config/riscv/andes.md、path:gcc/config/riscv/peephole.md、token:risc-v、token:riscv
- 涉及文件：gcc/config/riscv/andes.md、gcc/config/riscv/peephole.md
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V 问题修复相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为中；未验证构建、运行或发布状态。
- 打包建议：建议人工核对上游状态和适用版本，并完成构建及回归测试后再决定打包。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。

### RISC-V: Allow RVV register overlap for vfwsub.wv

- 仓库：gcc-mirror/gcc；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-10-24T06:16:38Z
- 作者：Incarnation-p-lee；SHA：83672fad13bb8789d742046bc1f37ad8f06a9fda
- 来源：[原始记录](https://github.com/gcc-mirror/gcc/commit/83672fad13bb8789d742046bc1f37ad8f06a9fda)
- 规则判断：medium / vector-crypto-hypervisor；打包候选：是，待人工评估
- 命中规则：keyword:vector-crypto-hypervisor:vector、path:gcc/config/riscv/vector.md、token:risc-v、token:riscv
- 涉及文件：gcc/config/riscv/vector.md
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V 向量、密码学或虚拟化相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为中；未验证构建、运行或发布状态。
- 打包建议：建议人工核对上游状态和适用版本，并完成构建及回归测试后再决定打包。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。

### \[RISC-V\] Fix a couple more issues with unsafe \[U\]INTVAL checks in RISC-V backend

- 仓库：gcc-mirror/gcc；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-10-23T17:04:38Z
- 作者：JeffreyALaw；SHA：8d3bac71a9433f90161a22dd13812457d32c2352
- 来源：[原始记录](https://github.com/gcc-mirror/gcc/commit/8d3bac71a9433f90161a22dd13812457d32c2352)
- 规则判断：medium / bugfix；打包候选：是，待人工评估
- 命中规则：keyword:bugfix:fix、keyword:hardware:k3、keyword:isa-extension:zicond、keyword:vector-crypto-hypervisor:crypto、path:gcc/config/riscv/crypto.md、path:gcc/config/riscv/zicond.md、token:risc-v、token:riscv
- 涉及文件：gcc/config/riscv/crypto.md、gcc/config/riscv/zicond.md
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V 问题修复相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为中；未验证构建、运行或发布状态。
- 打包建议：建议人工核对上游状态和适用版本，并完成构建及回归测试后再决定打包。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。

### RISC-V: Use clmulr for reversed crc64 on rv64

- 仓库：gcc-mirror/gcc；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-10-23T13:27:32Z
- 作者：exur00；SHA：84fddf4484bb948049a2f39280da2d107b068e9f
- 来源：[原始记录](https://github.com/gcc-mirror/gcc/commit/84fddf4484bb948049a2f39280da2d107b068e9f)
- 规则判断：medium / other；打包候选：否
- 命中规则：path:gcc/config/riscv/bitmanip.md、path:gcc/config/riscv/riscv.cc、path:gcc/testsuite/gcc.target/riscv/crc-builtin-zbc64.c、path:gcc/testsuite/gcc.target/riscv/crc-rev-crc64-rv64-zbc.c、token:risc-v、token:riscv、token:rv32、token:rv64
- 涉及文件：gcc/config/riscv/bitmanip.md、gcc/config/riscv/riscv.cc、gcc/testsuite/gcc.target/riscv/crc-builtin-zbc64.c、gcc/testsuite/gcc.target/riscv/crc-rev-crc64-rv64-zbc.c
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V 其他变更相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为中；未验证构建、运行或发布状态。
- 打包建议：保留跟踪，暂不列为优先打包候选；需结合实际版本和测试结果人工评估。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。

### \[RISC-V\]\[PR target/121268\] Fix splitter for pr121268

- 仓库：gcc-mirror/gcc；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-10-23T13:00:16Z
- 作者：JeffreyALaw；SHA：892195ef99cb6cf899f480d13a125bb5bfe62313
- 来源：[原始记录](https://github.com/gcc-mirror/gcc/commit/892195ef99cb6cf899f480d13a125bb5bfe62313)
- 规则判断：medium / bugfix；打包候选：是，待人工评估
- 命中规则：keyword:bugfix:fix、keyword:hardware:k3、path:gcc/config/riscv/bitmanip.md、path:gcc/testsuite/gcc.target/riscv/pr121268-2.c、path:gcc/testsuite/gcc.target/riscv/pr121268.c、token:risc-v、token:riscv
- 涉及文件：gcc/config/riscv/bitmanip.md、gcc/testsuite/gcc.target/riscv/pr121268-2.c、gcc/testsuite/gcc.target/riscv/pr121268.c
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V 问题修复相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为中；未验证构建、运行或发布状态。
- 打包建议：建议人工核对上游状态和适用版本，并完成构建及回归测试后再决定打包。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。

### \[RISC-V\] Fix invalid accessor macro use in RISC-V bitmanip support

- 仓库：gcc-mirror/gcc；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-10-21T14:47:16Z
- 作者：JeffreyALaw；SHA：f8d28739227adabf200b674c22a35599fe87b53d
- 来源：[原始记录](https://github.com/gcc-mirror/gcc/commit/f8d28739227adabf200b674c22a35599fe87b53d)
- 规则判断：medium / bugfix；打包候选：是，待人工评估
- 命中规则：keyword:bugfix:fix、keyword:hardware:k3、path:gcc/config/riscv/bitmanip.md、path:gcc/config/riscv/predicates.md、token:risc-v、token:riscv
- 涉及文件：gcc/config/riscv/bitmanip.md、gcc/config/riscv/predicates.md
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V 问题修复相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为中；未验证构建、运行或发布状态。
- 打包建议：建议人工核对上游状态和适用版本，并完成构建及回归测试后再决定打包。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。

### \[PR target/127865\]\[RISC-V\] Refine selection of AOP for RISC-V

- 仓库：gcc-mirror/gcc；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-10-19T16:03:43Z
- 作者：JeffreyALaw；SHA：48ae7b09bc6b61bd383c45c25ddb36224a86c712
- 来源：[原始记录](https://github.com/gcc-mirror/gcc/commit/48ae7b09bc6b61bd383c45c25ddb36224a86c712)
- 规则判断：medium / bugfix；打包候选：是，待人工评估
- 命中规则：keyword:bugfix:regression、keyword:hardware:k3、keyword:isa-extension:extension、path:gcc/config/riscv/riscv.md、path:gcc/testsuite/gcc.target/riscv/pr127865.c、token:risc-v、token:riscv、token:rv64
- 涉及文件：gcc/config/riscv/riscv.md、gcc/testsuite/gcc.target/riscv/pr127865.c
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V 问题修复相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为中；未验证构建、运行或发布状态。
- 打包建议：建议人工核对上游状态和适用版本，并完成构建及回归测试后再决定打包。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。

### \[RISC-V\] Fix two RISC-V bitmanip bugs spotted by LLM review

- 仓库：gcc-mirror/gcc；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-10-19T15:21:23Z
- 作者：JeffreyALaw；SHA：5601e5ce49fa66811bb065a53ff3007ea5c8a224
- 来源：[原始记录](https://github.com/gcc-mirror/gcc/commit/5601e5ce49fa66811bb065a53ff3007ea5c8a224)
- 规则判断：medium / bugfix；打包候选：是，待人工评估
- 命中规则：keyword:bugfix:fix、keyword:hardware:k3、keyword:isa-extension:extension、path:gcc/config/riscv/bitmanip.md、token:risc-v、token:riscv
- 涉及文件：gcc/config/riscv/bitmanip.md
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V 问题修复相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为中；未验证构建、运行或发布状态。
- 打包建议：建议人工核对上游状态和适用版本，并完成构建及回归测试后再决定打包。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。


## 低优先级

### RISC-V: Add one more test case for vfwsub.wv

- 仓库：gcc-mirror/gcc；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-10-24T06:16:39Z
- 作者：Incarnation-p-lee；SHA：590068c52cb2b1bb4a30ad01834f369e8e628671
- 来源：[原始记录](https://github.com/gcc-mirror/gcc/commit/590068c52cb2b1bb4a30ad01834f369e8e628671)
- 规则判断：low / other；打包候选：否
- 命中规则：low-value:test、path:gcc/testsuite/gcc.target/riscv/rvv/base/pr112431-60.c、test-only、token:risc-v、token:riscv
- 涉及文件：gcc/testsuite/gcc.target/riscv/rvv/base/pr112431-60.c
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V 其他变更相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为低；未验证构建、运行或发布状态。
- 打包建议：保留跟踪，暂不列为优先打包候选；需结合实际版本和测试结果人工评估。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。

### RISC-V: Add test cases for vfwsub.wv reg overlap

- 仓库：gcc-mirror/gcc；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-10-24T06:16:39Z
- 作者：Incarnation-p-lee；SHA：6b4a225f7f8f1c3a0b00aeab9210e3a764aa2780
- 来源：[原始记录](https://github.com/gcc-mirror/gcc/commit/6b4a225f7f8f1c3a0b00aeab9210e3a764aa2780)
- 规则判断：low / other；打包候选：否
- 命中规则：low-value:test、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwsub\_wv-f16-m1.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwsub\_wv-f16-m2.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwsub\_wv-f16-m4.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwsub\_wv-f16-mf2.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwsub\_wv-f16-mf4.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwsub\_wv-f32-m1.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwsub\_wv-f32-m2.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwsub\_wv-f32-m4.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwsub\_wv-f32-mf2.c、test-only、token:risc-v、token:riscv
- 涉及文件：gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwsub\_wv-f16-m1.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwsub\_wv-f16-m2.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwsub\_wv-f16-m4.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwsub\_wv-f16-mf2.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwsub\_wv-f16-mf4.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwsub\_wv-f32-m1.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwsub\_wv-f32-m2.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwsub\_wv-f32-m4.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwsub\_wv-f32-mf2.c
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V 其他变更相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为低；未验证构建、运行或发布状态。
- 打包建议：保留跟踪，暂不列为优先打包候选；需结合实际版本和测试结果人工评估。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。
