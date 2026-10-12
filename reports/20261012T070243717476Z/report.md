# GNU RISC-V 上游更新报告

统计窗口（UTC）：2026-10-04T06:37:39Z 至 2026-10-12T07:02:43Z
生成时间（UTC）：2026-10-12T07:02:43Z

共 16 条相关更新：高 3、中 11、低 2。

优先级和打包候选由规则决定；LLM 辅助分析仅供参考，最终打包需人工评估和构建测试。
提交已合入不代表已经发布；关联 PR 的状态单独列出。

## 仓库采集状态

- RTEMS/sourceware-mirror-binutils-gdb：ok；分支 master
  采集窗口（UTC）：2026-10-04T06:37:39Z 至 2026-10-12T07:02:43Z
- gcc-mirror/gcc：ok；分支 master
  采集窗口（UTC）：2026-10-04T06:37:39Z 至 2026-10-12T07:02:43Z
- sailfishos-mirror/glibc：ok；分支 master
  采集窗口（UTC）：2026-10-04T06:37:39Z 至 2026-10-12T07:02:43Z

## 采集警告

- RTEMS/sourceware-mirror-binutils-gdb：轻量标签没有独立时间，只能用所指提交的时间代替。
- gcc-mirror/gcc：轻量标签没有独立时间，只能用所指提交的时间代替。
- 分页在第 1 页停止，元数据覆盖不完整。
- 未配置 LLM\_API\_KEY，使用规则结果。

## 高优先级

### \[RISC-V\] Remove obsolete, never taken to silicon xventanacondops extension

- 仓库：gcc-mirror/gcc；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-10-11T18:32:31Z
- 作者：JeffreyALaw；SHA：06cee27b6943fdfe6082dbee4c260b2efe22a193
- 来源：[原始记录](https://github.com/gcc-mirror/gcc/commit/06cee27b6943fdfe6082dbee4c260b2efe22a193)
- 规则判断：high / compiler-option；打包候选：是，待人工评估
- 命中规则：functional:support、keyword:compiler-option:options、keyword:isa-extension:extension、keyword:isa-extension:zicond、path:gcc/config/riscv/predicates.md、path:gcc/config/riscv/riscv-ext-ventana.def、path:gcc/config/riscv/riscv-ext.def、path:gcc/config/riscv/riscv-ext.opt、path:gcc/config/riscv/riscv-opts.h、path:gcc/config/riscv/riscv.cc、path:gcc/config/riscv/riscv.md、path:gcc/config/riscv/t-riscv、path:gcc/config/riscv/zicond.md、path:gcc/doc/riscv-ext.texi、path:gcc/testsuite/gcc.target/riscv/cset-sext-ventana-rtl.c、path:gcc/testsuite/gcc.target/riscv/cset-sext-ventana.c、path:gcc/testsuite/gcc.target/riscv/movdibeq-ventana.c、path:gcc/testsuite/gcc.target/riscv/movdibfeq-ventana.c、path:gcc/testsuite/gcc.target/riscv/movdibfge-ventana.c、path:gcc/testsuite/gcc.target/riscv/movdibfgt-ventana.c、path:gcc/testsuite/gcc.target/riscv/movdibfle-ventana.c、path:gcc/testsuite/gcc.target/riscv/movdibflt-ventana.c、path:gcc/testsuite/gcc.target/riscv/movdibfne-ventana.c、path:gcc/testsuite/gcc.target/riscv/movdibge-ventana.c、path:gcc/testsuite/gcc.target/riscv/movdibgeu-ventana.c、path:gcc/testsuite/gcc.target/riscv/movdibgt-ventana.c、path:gcc/testsuite/gcc.target/riscv/movdibgtu-ventana.c、path:gcc/testsuite/gcc.target/riscv/movdible-ventana.c、path:gcc/testsuite/gcc.target/riscv/movdibleu-ventana.c、path:gcc/testsuite/gcc.target/riscv/movdiblt-ventana.c、path:gcc/testsuite/gcc.target/riscv/movdibltu-ventana.c、path:gcc/testsuite/gcc.target/riscv/movdibne-ventana.c、path:gcc/testsuite/gcc.target/riscv/movdieq-ventana.c、path:gcc/testsuite/gcc.target/riscv/movdifeq-ventana.c、path:gcc/testsuite/gcc.target/riscv/movdifge-ventana.c、path:gcc/testsuite/gcc.target/riscv/movdifgt-ventana.c、path:gcc/testsuite/gcc.target/riscv/movdifle-ventana.c、path:gcc/testsuite/gcc.target/riscv/movdiflt-ventana.c、path:gcc/testsuite/gcc.target/riscv/movdifne-ventana.c、path:gcc/testsuite/gcc.target/riscv/movdige-ventana.c、path:gcc/testsuite/gcc.target/riscv/movdigeu-ventana.c、path:gcc/testsuite/gcc.target/riscv/movdigt-ventana.c、path:gcc/testsuite/gcc.target/riscv/movdigtu-ventana.c、path:gcc/testsuite/gcc.target/riscv/movdile-ventana.c、path:gcc/testsuite/gcc.target/riscv/movdileu-ventana.c、path:gcc/testsuite/gcc.target/riscv/movdilt-ventana.c、path:gcc/testsuite/gcc.target/riscv/movdiltu-ventana.c、path:gcc/testsuite/gcc.target/riscv/movdine-ventana.c、path:gcc/testsuite/gcc.target/riscv/movsibeq-ventana.c、path:gcc/testsuite/gcc.target/riscv/movsibfeq-ventana.c、path:gcc/testsuite/gcc.target/riscv/movsibfge-ventana.c、path:gcc/testsuite/gcc.target/riscv/movsibfgt-ventana.c、path:gcc/testsuite/gcc.target/riscv/movsibfle-ventana.c、path:gcc/testsuite/gcc.target/riscv/movsibflt-ventana.c、path:gcc/testsuite/gcc.target/riscv/movsibfne-ventana.c、path:gcc/testsuite/gcc.target/riscv/movsibge-ventana.c、path:gcc/testsuite/gcc.target/riscv/movsibgeu-ventana.c、path:gcc/testsuite/gcc.target/riscv/movsibgt-ventana.c、path:gcc/testsuite/gcc.target/riscv/movsibgtu-ventana.c、path:gcc/testsuite/gcc.target/riscv/movsible-ventana.c、path:gcc/testsuite/gcc.target/riscv/movsibleu-ventana.c、path:gcc/testsuite/gcc.target/riscv/movsiblt-ventana.c、path:gcc/testsuite/gcc.target/riscv/movsibltu-ventana.c、path:gcc/testsuite/gcc.target/riscv/movsibne-ventana.c、path:gcc/testsuite/gcc.target/riscv/movsieq-ventana.c、path:gcc/testsuite/gcc.target/riscv/movsifeq-ventana.c、path:gcc/testsuite/gcc.target/riscv/movsifge-ventana.c、path:gcc/testsuite/gcc.target/riscv/movsifgt-ventana.c、path:gcc/testsuite/gcc.target/riscv/movsifle-ventana.c、path:gcc/testsuite/gcc.target/riscv/movsiflt-ventana.c、path:gcc/testsuite/gcc.target/riscv/movsifne-ventana.c、path:gcc/testsuite/gcc.target/riscv/movsige-ventana.c、path:gcc/testsuite/gcc.target/riscv/movsigeu-ventana.c、path:gcc/testsuite/gcc.target/riscv/movsigt-ventana.c、path:gcc/testsuite/gcc.target/riscv/movsigtu-ventana.c、path:gcc/testsuite/gcc.target/riscv/movsile-ventana.c、path:gcc/testsuite/gcc.target/riscv/movsileu-ventana.c、path:gcc/testsuite/gcc.target/riscv/movsilt-ventana.c、path:gcc/testsuite/gcc.target/riscv/movsiltu-ventana.c、path:gcc/testsuite/gcc.target/riscv/movsine-ventana.c、path:gcc/testsuite/gcc.target/riscv/pr116240.c、path:gcc/testsuite/gcc.target/riscv/predef-30.c、path:gcc/testsuite/gcc.target/riscv/ventana-16122.c、path:gcc/testsuite/gcc.target/riscv/xventanacondops-primitiveSemantics-rv32.c、path:gcc/testsuite/gcc.target/riscv/xventanacondops-primitiveSemantics.c、path:gcc/testsuite/gcc.target/riscv/xventanacondops-xor-01.c、token:risc-v、token:riscv、token:rv32
- 涉及文件：gcc/config/riscv/predicates.md、gcc/config/riscv/riscv-ext-ventana.def、gcc/config/riscv/riscv-ext.def、gcc/config/riscv/riscv-ext.opt、gcc/config/riscv/riscv-opts.h、gcc/config/riscv/riscv.cc、gcc/config/riscv/riscv.md、gcc/config/riscv/t-riscv、gcc/config/riscv/zicond.md、gcc/doc/riscv-ext.texi、gcc/testsuite/gcc.target/riscv/cset-sext-ventana-rtl.c、gcc/testsuite/gcc.target/riscv/cset-sext-ventana.c、gcc/testsuite/gcc.target/riscv/movdibeq-ventana.c、gcc/testsuite/gcc.target/riscv/movdibfeq-ventana.c、gcc/testsuite/gcc.target/riscv/movdibfge-ventana.c、gcc/testsuite/gcc.target/riscv/movdibfgt-ventana.c、gcc/testsuite/gcc.target/riscv/movdibfle-ventana.c、gcc/testsuite/gcc.target/riscv/movdibflt-ventana.c、gcc/testsuite/gcc.target/riscv/movdibfne-ventana.c、gcc/testsuite/gcc.target/riscv/movdibge-ventana.c、gcc/testsuite/gcc.target/riscv/movdibgeu-ventana.c、gcc/testsuite/gcc.target/riscv/movdibgt-ventana.c、gcc/testsuite/gcc.target/riscv/movdibgtu-ventana.c、gcc/testsuite/gcc.target/riscv/movdible-ventana.c、gcc/testsuite/gcc.target/riscv/movdibleu-ventana.c、gcc/testsuite/gcc.target/riscv/movdiblt-ventana.c、gcc/testsuite/gcc.target/riscv/movdibltu-ventana.c、gcc/testsuite/gcc.target/riscv/movdibne-ventana.c、gcc/testsuite/gcc.target/riscv/movdieq-ventana.c、gcc/testsuite/gcc.target/riscv/movdifeq-ventana.c、gcc/testsuite/gcc.target/riscv/movdifge-ventana.c、gcc/testsuite/gcc.target/riscv/movdifgt-ventana.c、gcc/testsuite/gcc.target/riscv/movdifle-ventana.c、gcc/testsuite/gcc.target/riscv/movdiflt-ventana.c、gcc/testsuite/gcc.target/riscv/movdifne-ventana.c、gcc/testsuite/gcc.target/riscv/movdige-ventana.c、gcc/testsuite/gcc.target/riscv/movdigeu-ventana.c、gcc/testsuite/gcc.target/riscv/movdigt-ventana.c、gcc/testsuite/gcc.target/riscv/movdigtu-ventana.c、gcc/testsuite/gcc.target/riscv/movdile-ventana.c、gcc/testsuite/gcc.target/riscv/movdileu-ventana.c、gcc/testsuite/gcc.target/riscv/movdilt-ventana.c、gcc/testsuite/gcc.target/riscv/movdiltu-ventana.c、gcc/testsuite/gcc.target/riscv/movdine-ventana.c、gcc/testsuite/gcc.target/riscv/movsibeq-ventana.c、gcc/testsuite/gcc.target/riscv/movsibfeq-ventana.c、gcc/testsuite/gcc.target/riscv/movsibfge-ventana.c、gcc/testsuite/gcc.target/riscv/movsibfgt-ventana.c、gcc/testsuite/gcc.target/riscv/movsibfle-ventana.c、gcc/testsuite/gcc.target/riscv/movsibflt-ventana.c、gcc/testsuite/gcc.target/riscv/movsibfne-ventana.c、gcc/testsuite/gcc.target/riscv/movsibge-ventana.c、gcc/testsuite/gcc.target/riscv/movsibgeu-ventana.c、gcc/testsuite/gcc.target/riscv/movsibgt-ventana.c、gcc/testsuite/gcc.target/riscv/movsibgtu-ventana.c、gcc/testsuite/gcc.target/riscv/movsible-ventana.c、gcc/testsuite/gcc.target/riscv/movsibleu-ventana.c、gcc/testsuite/gcc.target/riscv/movsiblt-ventana.c、gcc/testsuite/gcc.target/riscv/movsibltu-ventana.c、gcc/testsuite/gcc.target/riscv/movsibne-ventana.c、gcc/testsuite/gcc.target/riscv/movsieq-ventana.c、gcc/testsuite/gcc.target/riscv/movsifeq-ventana.c、gcc/testsuite/gcc.target/riscv/movsifge-ventana.c、gcc/testsuite/gcc.target/riscv/movsifgt-ventana.c、gcc/testsuite/gcc.target/riscv/movsifle-ventana.c、gcc/testsuite/gcc.target/riscv/movsiflt-ventana.c、gcc/testsuite/gcc.target/riscv/movsifne-ventana.c、gcc/testsuite/gcc.target/riscv/movsige-ventana.c、gcc/testsuite/gcc.target/riscv/movsigeu-ventana.c、gcc/testsuite/gcc.target/riscv/movsigt-ventana.c、gcc/testsuite/gcc.target/riscv/movsigtu-ventana.c、gcc/testsuite/gcc.target/riscv/movsile-ventana.c、gcc/testsuite/gcc.target/riscv/movsileu-ventana.c、gcc/testsuite/gcc.target/riscv/movsilt-ventana.c、gcc/testsuite/gcc.target/riscv/movsiltu-ventana.c、gcc/testsuite/gcc.target/riscv/movsine-ventana.c、gcc/testsuite/gcc.target/riscv/pr116240.c、gcc/testsuite/gcc.target/riscv/predef-30.c、gcc/testsuite/gcc.target/riscv/ventana-16122.c、gcc/testsuite/gcc.target/riscv/xventanacondops-primitiveSemantics-rv32.c、gcc/testsuite/gcc.target/riscv/xventanacondops-primitiveSemantics.c、gcc/testsuite/gcc.target/riscv/xventanacondops-xor-01.c
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V 编译选项相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为高；未验证构建、运行或发布状态。
- 打包建议：建议人工核对上游状态和适用版本，并完成构建及回归测试后再决定打包。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。

### RISC-V: Add -z zicfilp=, -z zicfiss= and the CFI report options

- 仓库：RTEMS/sourceware-mirror-binutils-gdb；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-10-08T07:51:12Z
- 作者：kito-cheng；SHA：5c624ad4aa3cc5290da28a5c5bcd6bae51b7b0f5
- 来源：[原始记录](https://github.com/RTEMS/sourceware-mirror-binutils-gdb/commit/5c624ad4aa3cc5290da28a5c5bcd6bae51b7b0f5)
- 规则判断：high / compiler-option；打包候选：是，待人工评估
- 命中规则：functional:add、keyword:compiler-option:options、keyword:isa-extension:zicfilp、keyword:isa-extension:zicfiss、path:bfd/elfnn-riscv.c、path:bfd/elfxx-riscv.h、path:ld/emultempl/riscvelf.em、path:ld/testsuite/ld-riscv-elf/ld-riscv-elf.exp、path:ld/testsuite/ld-riscv-elf/property-cfi-never.d、path:ld/testsuite/ld-riscv-elf/property-zicfilp-bad.d、path:ld/testsuite/ld-riscv-elf/property-zicfilp-never.d、path:ld/testsuite/ld-riscv-elf/property-zicfilp-unlabeled-report-single.d、path:ld/testsuite/ld-riscv-elf/property-zicfilp-unlabeled-report.d、path:ld/testsuite/ld-riscv-elf/property-zicfiss-never.d、path:ld/testsuite/ld-riscv-elf/property-zicfiss-report-error.d、path:ld/testsuite/ld-riscv-elf/property-zicfiss-report.d、path:ld/testsuite/ld-riscv-elf/zicfilp-force-plt.d、path:ld/testsuite/ld-riscv-elf/zicfilp-force-plt.s、path:ld/testsuite/ld-riscv-elf/zicfilp-never-plt.d、token:risc-v、token:riscv
- 涉及文件：bfd/elfnn-riscv.c、bfd/elfxx-riscv.h、ld/NEWS、ld/emultempl/riscvelf.em、ld/ld.texi、ld/testsuite/ld-riscv-elf/ld-riscv-elf.exp、ld/testsuite/ld-riscv-elf/property-cfi-never.d、ld/testsuite/ld-riscv-elf/property-zicfilp-bad.d、ld/testsuite/ld-riscv-elf/property-zicfilp-never.d、ld/testsuite/ld-riscv-elf/property-zicfilp-unlabeled-report-single.d、ld/testsuite/ld-riscv-elf/property-zicfilp-unlabeled-report.d、ld/testsuite/ld-riscv-elf/property-zicfiss-never.d、ld/testsuite/ld-riscv-elf/property-zicfiss-report-error.d、ld/testsuite/ld-riscv-elf/property-zicfiss-report.d、ld/testsuite/ld-riscv-elf/zicfilp-force-plt.d、ld/testsuite/ld-riscv-elf/zicfilp-force-plt.s、ld/testsuite/ld-riscv-elf/zicfilp-never-plt.d
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V 编译选项相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为高；未验证构建、运行或发布状态。
- 打包建议：建议人工核对上游状态和适用版本，并完成构建及回归测试后再决定打包。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。

### RISC-V: Name the missing extension for the MIPS vendor instructions

- 仓库：RTEMS/sourceware-mirror-binutils-gdb；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-10-08T07:24:34Z
- 作者：kito-cheng；SHA：55c6fd1d3ac54ca36983d657e5692b6e9e412148
- 来源：[原始记录](https://github.com/RTEMS/sourceware-mirror-binutils-gdb/commit/55c6fd1d3ac54ca36983d657e5692b6e9e412148)
- 规则判断：high / isa-extension；打包候选：是，待人工评估
- 命中规则：functional:add、functional:supports、keyword:isa-extension:extension、path:bfd/elfxx-riscv.c、path:gas/testsuite/gas/riscv/mips-insns-fail.d、path:gas/testsuite/gas/riscv/mips-insns-fail.l、path:gas/testsuite/gas/riscv/mips-insns-fail.s、token:risc-v、token:riscv
- 涉及文件：bfd/elfxx-riscv.c、gas/testsuite/gas/riscv/mips-insns-fail.d、gas/testsuite/gas/riscv/mips-insns-fail.l、gas/testsuite/gas/riscv/mips-insns-fail.s
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V ISA 扩展相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为高；未验证构建、运行或发布状态。
- 打包建议：建议人工核对上游状态和适用版本，并完成构建及回归测试后再决定打包。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。


## 中优先级

### \[RISC-V\] Fix remaining AOP related regressions on the RISC-V port

- 仓库：gcc-mirror/gcc；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-10-11T15:19:22Z
- 作者：Jeff Law；SHA：de2ea1f8b15f05264310a5e7c29328591c13de49
- 来源：[原始记录](https://github.com/gcc-mirror/gcc/commit/de2ea1f8b15f05264310a5e7c29328591c13de49)
- 规则判断：medium / bugfix；打包候选：是，待人工评估
- 命中规则：keyword:bugfix:fix、keyword:hardware:k3、keyword:isa-extension:zba、path:gcc/config/riscv/riscv.md、token:risc-v、token:riscv、token:rv32、token:rv64
- 涉及文件：gcc/config/riscv/riscv.md
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V 问题修复相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为中；未验证构建、运行或发布状态。
- 打包建议：建议人工核对上游状态和适用版本，并完成构建及回归测试后再决定打包。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。

### \[RISC-V\] Fix pr58727 code quality regression on RISC-V

- 仓库：gcc-mirror/gcc；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-10-11T14:43:39Z
- 作者：Jeff Law；SHA：9613bdb1922e62e20da5a2893d27a9f6ef296afc
- 来源：[原始记录](https://github.com/gcc-mirror/gcc/commit/9613bdb1922e62e20da5a2893d27a9f6ef296afc)
- 规则判断：medium / bugfix；打包候选：是，待人工评估
- 命中规则：keyword:bugfix:fix、keyword:bugfix:regression、keyword:hardware:k3、path:gcc/config/riscv/bitmanip.md、token:risc-v、token:riscv
- 涉及文件：gcc/config/riscv/bitmanip.md
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V 问题修复相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为中；未验证构建、运行或发布状态。
- 打包建议：建议人工核对上游状态和适用版本，并完成构建及回归测试后再决定打包。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。

### xtensa: compare SEC\_MERGE literals by their merged addresses

- 仓库：RTEMS/sourceware-mirror-binutils-gdb；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-10-09T11:03:43Z
- 作者：Lapshin；SHA：527a092ac82424791b15c6db14bfcdcfc56e052c
- 来源：[原始记录](https://github.com/RTEMS/sourceware-mirror-binutils-gdb/commit/527a092ac82424791b15c6db14bfcdcfc56e052c)
- 规则判断：medium / other；打包候选：否
- 命中规则：token:risc-v
- 涉及文件：bfd/elf32-xtensa.c、ld/testsuite/ld-xtensa/coalesce-merge-1.s、ld/testsuite/ld-xtensa/coalesce-merge-2.s、ld/testsuite/ld-xtensa/coalesce-merge.d、ld/testsuite/ld-xtensa/coalesce-merge.t、ld/testsuite/ld-xtensa/xtensa.exp
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V 其他变更相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为中；未验证构建、运行或发布状态。
- 打包建议：保留跟踪，暂不列为优先打包候选；需结合实际版本和测试结果人工评估。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。

### RISC-V: Suppress may be used uninitialized warning

- 仓库：RTEMS/sourceware-mirror-binutils-gdb；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-10-08T13:56:53Z
- 作者：kito-cheng；SHA：079dc6f5083e3614d52c49de896f33a6c87d4e09
- 来源：[原始记录](https://github.com/RTEMS/sourceware-mirror-binutils-gdb/commit/079dc6f5083e3614d52c49de896f33a6c87d4e09)
- 规则判断：medium / other；打包候选：否
- 命中规则：path:bfd/elfnn-riscv.c、token:risc-v、token:riscv
- 涉及文件：bfd/elfnn-riscv.c
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V 其他变更相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为中；未验证构建、运行或发布状态。
- 打包建议：保留跟踪，暂不列为优先打包候选；需结合实际版本和测试结果人工评估。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。

### RISC-V: Introduce TLSDESC relaxation.

- 仓库：RTEMS/sourceware-mirror-binutils-gdb；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-10-08T08:11:21Z
- 作者：ishitatsuyuki；SHA：2c4ccb8103d73917d769cf6c35fa8b71424f20ca
- 来源：[原始记录](https://github.com/RTEMS/sourceware-mirror-binutils-gdb/commit/2c4ccb8103d73917d769cf6c35fa8b71424f20ca)
- 规则判断：medium / other；打包候选：否
- 命中规则：path:bfd/elfnn-riscv.c、path:bfd/elfxx-riscv.c、path:include/elf/riscv.h、path:ld/testsuite/ld-riscv-elf/ld-riscv-elf.exp、path:ld/testsuite/ld-riscv-elf/tlsbin.d、path:ld/testsuite/ld-riscv-elf/tlsdesc-ie-32-dyn.d、path:ld/testsuite/ld-riscv-elf/tlsdesc-ie-32-norelax.d、path:ld/testsuite/ld-riscv-elf/tlsdesc-ie-32.d、path:ld/testsuite/ld-riscv-elf/tlsdesc-ie-32.s、path:ld/testsuite/ld-riscv-elf/tlsdesc-ie-dyn.d、path:ld/testsuite/ld-riscv-elf/tlsdesc-ie-norelax.d、path:ld/testsuite/ld-riscv-elf/tlsdesc-ie.d、path:ld/testsuite/ld-riscv-elf/tlsdesc-ie.s、path:ld/testsuite/ld-riscv-elf/tlsdesc-le-norelax.d、path:ld/testsuite/ld-riscv-elf/tlsdesc-le.d、path:ld/testsuite/ld-riscv-elf/tlsdesc-le.s、path:ld/testsuite/ld-riscv-elf/tlsdesc-lib.s、path:ld/testsuite/ld-riscv-elf/tlsdesc-unrelaxed-le.d、path:ld/testsuite/ld-riscv-elf/tlsdesc-unrelaxed-le.s、path:ld/testsuite/ld-riscv-elf/tlsdesc-unrelaxed.d、path:ld/testsuite/ld-riscv-elf/tlsdesc-unrelaxed.s、token:risc-v、token:riscv
- 涉及文件：bfd/elfnn-riscv.c、bfd/elfxx-riscv.c、include/elf/riscv.h、ld/testsuite/ld-riscv-elf/ld-riscv-elf.exp、ld/testsuite/ld-riscv-elf/tlsbin.d、ld/testsuite/ld-riscv-elf/tlsdesc-ie-32-dyn.d、ld/testsuite/ld-riscv-elf/tlsdesc-ie-32-norelax.d、ld/testsuite/ld-riscv-elf/tlsdesc-ie-32.d、ld/testsuite/ld-riscv-elf/tlsdesc-ie-32.s、ld/testsuite/ld-riscv-elf/tlsdesc-ie-dyn.d、ld/testsuite/ld-riscv-elf/tlsdesc-ie-norelax.d、ld/testsuite/ld-riscv-elf/tlsdesc-ie.d、ld/testsuite/ld-riscv-elf/tlsdesc-ie.s、ld/testsuite/ld-riscv-elf/tlsdesc-le-norelax.d、ld/testsuite/ld-riscv-elf/tlsdesc-le.d、ld/testsuite/ld-riscv-elf/tlsdesc-le.s、ld/testsuite/ld-riscv-elf/tlsdesc-lib.s、ld/testsuite/ld-riscv-elf/tlsdesc-unrelaxed-le.d、ld/testsuite/ld-riscv-elf/tlsdesc-unrelaxed-le.s、ld/testsuite/ld-riscv-elf/tlsdesc-unrelaxed.d、ld/testsuite/ld-riscv-elf/tlsdesc-unrelaxed.s
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V 其他变更相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为中；未验证构建、运行或发布状态。
- 打包建议：保留跟踪，暂不列为优先打包候选；需结合实际版本和测试结果人工评估。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。

### RISC-V: Move STATIC\_TLS handling into record\_tls\_type.

- 仓库：RTEMS/sourceware-mirror-binutils-gdb；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-10-08T07:59:49Z
- 作者：ishitatsuyuki；SHA：34ee5769160d92f958feb286dece925747a47719
- 来源：[原始记录](https://github.com/RTEMS/sourceware-mirror-binutils-gdb/commit/34ee5769160d92f958feb286dece925747a47719)
- 规则判断：medium / other；打包候选：否
- 命中规则：path:bfd/elfnn-riscv.c、token:risc-v、token:riscv
- 涉及文件：bfd/elfnn-riscv.c
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V 其他变更相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为中；未验证构建、运行或发布状态。
- 打包建议：保留跟踪，暂不列为优先打包候选；需结合实际版本和测试结果人工评估。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。

### RISC-V: Add elf\_link\_hash\_entry to relax\_func args.

- 仓库：RTEMS/sourceware-mirror-binutils-gdb；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-10-08T07:59:49Z
- 作者：ishitatsuyuki；SHA：60b08e6b3adf81fbd95cc69511cac640714174e2
- 来源：[原始记录](https://github.com/RTEMS/sourceware-mirror-binutils-gdb/commit/60b08e6b3adf81fbd95cc69511cac640714174e2)
- 规则判断：medium / other；打包候选：否
- 命中规则：path:bfd/elfnn-riscv.c、token:risc-v、token:riscv
- 涉及文件：bfd/elfnn-riscv.c
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V 其他变更相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为中；未验证构建、运行或发布状态。
- 打包建议：保留跟踪，暂不列为优先打包候选；需结合实际版本和测试结果人工评估。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。

### RISC-V: Unify TLS handling in check\_relocs.

- 仓库：RTEMS/sourceware-mirror-binutils-gdb；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-10-08T07:59:49Z
- 作者：ishitatsuyuki；SHA：701b5cda0b47af1db756addb8a5dc6c9710b0d9c
- 来源：[原始记录](https://github.com/RTEMS/sourceware-mirror-binutils-gdb/commit/701b5cda0b47af1db756addb8a5dc6c9710b0d9c)
- 规则判断：medium / other；打包候选：否
- 命中规则：path:bfd/elfnn-riscv.c、token:risc-v、token:riscv
- 涉及文件：bfd/elfnn-riscv.c
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V 其他变更相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为中；未验证构建、运行或发布状态。
- 打包建议：保留跟踪，暂不列为优先打包候选；需结合实际版本和测试结果人工评估。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。

### RISC-V: Update the unlabeled landing pad PLT to the latest psABI

- 仓库：RTEMS/sourceware-mirror-binutils-gdb；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-10-08T07:51:12Z
- 作者：kito-cheng；SHA：d3eea828943c60cfe135c2830a6e7a23e82b11e6
- 来源：[原始记录](https://github.com/RTEMS/sourceware-mirror-binutils-gdb/commit/d3eea828943c60cfe135c2830a6e7a23e82b11e6)
- 规则判断：medium / profile-abi；打包候选：是，待人工评估
- 命中规则：keyword:isa-extension:zicfilp、keyword:profile-abi:psabi、path:bfd/elfnn-riscv.c、path:ld/testsuite/ld-riscv-elf/zicfilp-unlabeled-plt.d、token:risc-v、token:riscv
- 涉及文件：bfd/elfnn-riscv.c、ld/testsuite/ld-riscv-elf/zicfilp-unlabeled-plt.d
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V Profile 或 ABI相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为中；未验证构建、运行或发布状态。
- 打包建议：建议人工核对上游状态和适用版本，并完成构建及回归测试后再决定打包。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。

### RISC-V: Fix the implied extensions of xsmtvdotii

- 仓库：RTEMS/sourceware-mirror-binutils-gdb；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-10-08T07:24:34Z
- 作者：kito-cheng；SHA：cb663c0073900e7ed764459c1d659c1c85d9d155
- 来源：[原始记录](https://github.com/RTEMS/sourceware-mirror-binutils-gdb/commit/cb663c0073900e7ed764459c1d659c1c85d9d155)
- 规则判断：medium / bugfix；打包候选：是，待人工评估
- 命中规则：keyword:bugfix:fix、keyword:compiler-option:-march、keyword:isa-extension:extension、keyword:isa-extension:zve32x、path:bfd/elfxx-riscv.c、path:gas/testsuite/gas/riscv/imply.d、path:gas/testsuite/gas/riscv/imply.s、token:risc-v、token:riscv、token:rv64
- 涉及文件：bfd/elfxx-riscv.c、gas/testsuite/gas/riscv/imply.d、gas/testsuite/gas/riscv/imply.s
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V 问题修复相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为中；未验证构建、运行或发布状态。
- 打包建议：建议人工核对上游状态和适用版本，并完成构建及回归测试后再决定打包。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。

### OpenMP: Add the 'scaled' modifier to the 'simdlen' clause \[PR127723\]

- 仓库：gcc-mirror/gcc；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-10-07T04:37:19Z
- 作者：tob2；SHA：fbcafeec06a66175108be68c34aceafba7a453b9
- 来源：[原始记录](https://github.com/gcc-mirror/gcc/commit/fbcafeec06a66175108be68c34aceafba7a453b9)
- 规则判断：medium / bugfix；打包候选：是，待人工评估
- 命中规则：keyword:bugfix:fix、token:risc-v
- 涉及文件：gcc/attribs.cc、gcc/c/c-parser.cc、gcc/c/c-typeck.cc、gcc/cp/parser.cc、gcc/cp/pt.cc、gcc/cp/semantics.cc、gcc/gimplify.cc、gcc/omp-general.cc、gcc/omp-simd-clone.cc、gcc/testsuite/c-c++-common/gomp/simdlen-scaled-1.c、gcc/testsuite/c-c++-common/gomp/simdlen-scaled-2.c、gcc/testsuite/c-c++-common/gomp/simdlen-scaled-3.c、gcc/testsuite/c-c++-common/gomp/simdlen-scaled-4.c、gcc/testsuite/g++.dg/gomp/simdlen-scaled-1.C、gcc/testsuite/g++.dg/gomp/simdlen-scaled-2.C、gcc/tree-core.h、gcc/tree-pretty-print.cc、gcc/tree.cc、gcc/tree.h
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V 问题修复相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为中；未验证构建、运行或发布状态。
- 打包建议：建议人工核对上游状态和适用版本，并完成构建及回归测试后再决定打包。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。


## 低优先级

### \[committed\]\[RISC-V\] Fix one more test fallout from AOP work on RISC-V

- 仓库：gcc-mirror/gcc；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-10-11T20:11:28Z
- 作者：Jeff Law；SHA：be2755d55421ace63363402901b4e0e2f07f798c
- 来源：[原始记录](https://github.com/gcc-mirror/gcc/commit/be2755d55421ace63363402901b4e0e2f07f798c)
- 规则判断：low / other；打包候选：否
- 命中规则：low-value:test、path:gcc/config/riscv/riscv.md、token:risc-v、token:riscv
- 涉及文件：gcc/config/riscv/riscv.md
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V 其他变更相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为低；未验证构建、运行或发布状态。
- 打包建议：保留跟踪，暂不列为优先打包候选；需结合实际版本和测试结果人工评估。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。

### \[RISC-V\] Fix pack\* tests for RISC-V after any-or-plus changes

- 仓库：gcc-mirror/gcc；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-10-11T14:30:52Z
- 作者：Jeff Law；SHA：9d11ed33f54b395948521654218e2eb98c237b0e
- 来源：[原始记录](https://github.com/gcc-mirror/gcc/commit/9d11ed33f54b395948521654218e2eb98c237b0e)
- 规则判断：low / other；打包候选：否
- 命中规则：low-value:tests、path:gcc/config/riscv/crypto.md、path:gcc/config/riscv/iterators.md、path:gcc/config/riscv/riscv.cc、token:risc-v、token:riscv
- 涉及文件：gcc/config/riscv/crypto.md、gcc/config/riscv/iterators.md、gcc/config/riscv/riscv.cc
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V 其他变更相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为低；未验证构建、运行或发布状态。
- 打包建议：保留跟踪，暂不列为优先打包候选；需结合实际版本和测试结果人工评估。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。
