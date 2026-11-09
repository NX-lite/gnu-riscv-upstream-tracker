# GNU RISC-V 上游更新报告

统计窗口（UTC）：2026-11-01T07:25:13Z 至 2026-11-09T07:43:14Z
生成时间（UTC）：2026-11-09T07:43:14Z

共 37 条相关更新：高 13、中 19、低 5。

优先级和打包候选由规则决定；LLM 辅助分析仅供参考，最终打包需人工评估和构建测试。
提交已合入不代表已经发布；关联 PR 的状态单独列出。

## 仓库采集状态

- RTEMS/sourceware-mirror-binutils-gdb：ok；分支 master
  采集窗口（UTC）：2026-11-01T07:25:13Z 至 2026-11-09T07:43:14Z
- gcc-mirror/gcc：ok；分支 master
  采集窗口（UTC）：2026-11-01T07:25:13Z 至 2026-11-09T07:43:14Z
- sailfishos-mirror/glibc：ok；分支 master
  采集窗口（UTC）：2026-11-01T07:25:13Z 至 2026-11-09T07:43:14Z

## 采集警告

- RTEMS/sourceware-mirror-binutils-gdb：轻量标签没有独立时间，只能用所指提交的时间代替。
- gcc-mirror/gcc：轻量标签没有独立时间，只能用所指提交的时间代替。
- 分页在第 1 页停止，元数据覆盖不完整。
- 未配置 LLM\_API\_KEY，使用规则结果。

## 高优先级

### \[RISC-V\] Drop unnecessary shifting when upper bits are not read after bitfield extraction

- 仓库：gcc-mirror/gcc；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-11-08T05:24:41Z
- 作者：JeffreyALaw；SHA：ae820c0e4c2e13177bdb5d811c9a76f6fa955248
- 来源：[原始记录](https://github.com/gcc-mirror/gcc/commit/ae820c0e4c2e13177bdb5d811c9a76f6fa955248)
- 规则判断：high / hardware；打包候选：是，待人工评估
- 命中规则：functional:add、keyword:hardware:k3、path:gcc/config/riscv/riscv.md、path:gcc/testsuite/gcc.target/riscv/shift-shift-8.c、token:risc-v、token:riscv
- 涉及文件：gcc/config/riscv/riscv.md、gcc/testsuite/gcc.target/riscv/shift-shift-8.c
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V 硬件支持相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为高；未验证构建、运行或发布状态。
- 打包建议：建议人工核对上游状态和适用版本，并完成构建及回归测试后再决定打包。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。

### \[committed\]\[RISC-V\] Use bseti rather than li+add when safe to do so and split more intelligently

- 仓库：gcc-mirror/gcc；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-11-08T05:08:43Z
- 作者：JeffreyALaw；SHA：13b88db79f8a63a9a64138ae72e1ed3580196b2c
- 来源：[原始记录](https://github.com/gcc-mirror/gcc/commit/13b88db79f8a63a9a64138ae72e1ed3580196b2c)
- 规则判断：high / hardware；打包候选：是，待人工评估
- 命中规则：functional:add、functional:extend、keyword:hardware:k3、keyword:isa-extension:extension、path:gcc/config/riscv/bitmanip.md、path:gcc/config/riscv/iterators.md、path:gcc/config/riscv/predicates.md、path:gcc/config/riscv/riscv.md、path:gcc/testsuite/gcc.target/riscv/zbs-bseti-disjoint-add.c、token:risc-v、token:riscv、token:rv64
- 涉及文件：gcc/config/riscv/bitmanip.md、gcc/config/riscv/iterators.md、gcc/config/riscv/predicates.md、gcc/config/riscv/riscv.md、gcc/testsuite/gcc.target/riscv/zbs-bseti-disjoint-add.c
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V 硬件支持相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为高；未验证构建、运行或发布状态。
- 打包建议：建议人工核对上游状态和适用版本，并完成构建及回归测试后再决定打包。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。

### \[RISC-V\] Add splitter to enable narrowing load in a load-&gt;shift-&gt;store sequence

- 仓库：gcc-mirror/gcc；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-11-07T15:09:06Z
- 作者：JeffreyALaw；SHA：b9b7ba1475201499aae35b1aaf7a797d5a9c4d6f
- 来源：[原始记录](https://github.com/gcc-mirror/gcc/commit/b9b7ba1475201499aae35b1aaf7a797d5a9c4d6f)
- 规则判断：high / hardware；打包候选：是，待人工评估
- 命中规则：functional:add、functional:enable、functional:supports、keyword:hardware:k3、path:gcc/config/riscv/riscv.md、path:gcc/testsuite/gcc.target/riscv/load-no-shift.c、token:risc-v、token:riscv
- 涉及文件：gcc/config/riscv/riscv.md、gcc/testsuite/gcc.target/riscv/load-no-shift.c
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V 硬件支持相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为高；未验证构建、运行或发布状态。
- 打包建议：建议人工核对上游状态和适用版本，并完成构建及回归测试后再决定打包。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。

### c, c++, middle-end, i386: Introduce \_\_builtin\_clmulg builtin \[PR128111\]

- 仓库：gcc-mirror/gcc；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-11-07T08:47:44Z
- 作者：jakubjelinek；SHA：58f804554996fe057e5ca4fc814449640a6e816c
- 来源：[原始记录](https://github.com/gcc-mirror/gcc/commit/58f804554996fe057e5ca4fc814449640a6e816c)
- 规则判断：high / vector-crypto-hypervisor；打包候选：是，待人工评估
- 命中规则：functional:add、functional:added、functional:extend、functional:implement、functional:introduce、functional:support、keyword:vector-crypto-hypervisor:vector、token:riscv
- 涉及文件：gcc/builtins.cc、gcc/builtins.h、gcc/c-family/c-common.cc、gcc/c-family/c-common.h、gcc/c/c-decl.cc、gcc/c/c-parser.cc、gcc/config/i386/sse.md、gcc/cp/constexpr.cc、gcc/cp/cp-gimplify.cc、gcc/cp/cp-objcp-common.cc、gcc/cp/cp-tree.h、gcc/cp/mangle.cc、gcc/cp/parser.cc、gcc/cp/pt.cc、gcc/cp/typeck.cc、gcc/doc/extend.texi、gcc/fold-const-call.cc、gcc/fold-const.cc、gcc/genmatch.cc、gcc/gimple-lower-bitint.cc、gcc/internal-fn.cc、gcc/internal-fn.def、gcc/internal-fn.h、gcc/match.pd、gcc/optabs.def、gcc/testsuite/c-c++-common/builtin-clmulg-1.c、gcc/testsuite/c-c++-common/builtin-clmulg-2.c、gcc/testsuite/g++.dg/ext/builtin-clmulg-1.C、gcc/testsuite/gcc.target/i386/pclmul-builtin-clmulg-1.c、gcc/wide-int.cc、gcc/wide-int.h
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V 向量、密码学或虚拟化相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为高；未验证构建、运行或发布状态。
- 打包建议：建议人工核对上游状态和适用版本，并完成构建及回归测试后再决定打包。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。

### \[RISC-V\] Add missing splitters for zicond sequences

- 仓库：gcc-mirror/gcc；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-11-05T14:24:58Z
- 作者：JeffreyALaw；SHA：21737cb4a88facdf0a039ff5785f84ce8329b9fc
- 来源：[原始记录](https://github.com/gcc-mirror/gcc/commit/21737cb4a88facdf0a039ff5785f84ce8329b9fc)
- 规则判断：high / hardware；打包候选：是，待人工评估
- 命中规则：functional:add、functional:adds、keyword:hardware:k3、keyword:isa-extension:zicond、path:gcc/config/riscv/zicond.md、path:gcc/testsuite/gcc.target/riscv/pr57650-2.c、token:risc-v、token:riscv
- 涉及文件：gcc/config/riscv/zicond.md、gcc/testsuite/gcc.target/riscv/pr57650-2.c
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V 硬件支持相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为高；未验证构建、运行或发布状态。
- 打包建议：建议人工核对上游状态和适用版本，并完成构建及回归测试后再决定打包。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。

### RISC-V: Extract subvectors via vec\_perm\_const.

- 仓库：gcc-mirror/gcc；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-11-05T14:06:45Z
- 作者：Robin Dapp；SHA：8ce5e39048138fb92ebebc4a72114d9e55fa7a91
- 来源：[原始记录](https://github.com/gcc-mirror/gcc/commit/8ce5e39048138fb92ebebc4a72114d9e55fa7a91)
- 规则判断：high / vector-crypto-hypervisor；打包候选：是，待人工评估
- 命中规则：functional:adds、keyword:vector-crypto-hypervisor:vector、path:gcc/config/riscv/autovec.md、path:gcc/config/riscv/riscv-v.cc、path:gcc/config/riscv/vector-iterators.md、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/subreg-extract.c、token:risc-v、token:riscv
- 涉及文件：gcc/config/riscv/autovec.md、gcc/config/riscv/riscv-v.cc、gcc/config/riscv/vector-iterators.md、gcc/testsuite/gcc.target/riscv/rvv/autovec/subreg-extract.c
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V 向量、密码学或虚拟化相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为高；未验证构建、运行或发布状态。
- 打包建议：建议人工核对上游状态和适用版本，并完成构建及回归测试后再决定打包。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。

### \[RISC-V\] Reorder sequence for \(plus \(reg\) \(const\_int\)\) for nontrivial constants

- 仓库：gcc-mirror/gcc；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-11-04T13:49:39Z
- 作者：JeffreyALaw；SHA：495c38ed4c31c3c1e41c651850408fb4f5ca5f9c
- 来源：[原始记录](https://github.com/gcc-mirror/gcc/commit/495c38ed4c31c3c1e41c651850408fb4f5ca5f9c)
- 规则判断：high / hardware；打包候选：是，待人工评估
- 命中规则：functional:add、keyword:hardware:k3、path:gcc/config/riscv/riscv.cc、token:risc-v、token:riscv
- 涉及文件：gcc/config/riscv/riscv.cc
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V 硬件支持相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为高；未验证构建、运行或发布状态。
- 打包建议：建议人工核对上游状态和适用版本，并完成构建及回归测试后再决定打包。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。

### RISC-V: Support per-LMUL vector permute cost

- 仓库：gcc-mirror/gcc；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-11-04T08:23:39Z
- 作者：ZhongyaoChen；SHA：fa20d1603db32449ffe51e54849f6d67eb7c7965
- 来源：[原始记录](https://github.com/gcc-mirror/gcc/commit/fa20d1603db32449ffe51e54849f6d67eb7c7965)
- 规则判断：high / vector-crypto-hypervisor；打包候选：是，待人工评估
- 命中规则：functional:introduce、functional:support、keyword:vector-crypto-hypervisor:vector、keyword:vector-crypto-hypervisor:vectorization、path:gcc/config/riscv/riscv-protos.h、path:gcc/config/riscv/riscv-vector-costs.cc、path:gcc/config/riscv/riscv.cc、token:risc-v、token:riscv、token:rv64
- 涉及文件：gcc/config/riscv/riscv-protos.h、gcc/config/riscv/riscv-vector-costs.cc、gcc/config/riscv/riscv.cc
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V 向量、密码学或虚拟化相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为高；未验证构建、运行或发布状态。
- 打包建议：建议人工核对上游状态和适用版本，并完成构建及回归测试后再决定打包。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。

### \[committed\]\[PR target/128420\] Convert RISC-V define\_insn\_and\_split to simpler define\_split

- 仓库：gcc-mirror/gcc；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-11-04T05:15:29Z
- 作者：JeffreyALaw；SHA：d692d443714fd75ee70e0378f8a0db14b1dcbef6
- 来源：[原始记录](https://github.com/gcc-mirror/gcc/commit/d692d443714fd75ee70e0378f8a0db14b1dcbef6)
- 规则判断：high / hardware；打包候选：是，待人工评估
- 命中规则：functional:add、keyword:hardware:k3、path:gcc/config/riscv/bitmanip.md、token:risc-v、token:riscv
- 涉及文件：gcc/config/riscv/bitmanip.md
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V 硬件支持相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为高；未验证构建、运行或发布状态。
- 打包建议：建议人工核对上游状态和适用版本，并完成构建及回归测试后再决定打包。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。

### RISC-V: Add ARC-V RPX-100 series pipeline description

- 仓库：gcc-mirror/gcc；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-11-03T18:41:47Z
- 作者：exur00；SHA：b88c2821e219244d18df873b0bfb344d3dc0b2a7
- 来源：[原始记录](https://github.com/gcc-mirror/gcc/commit/b88c2821e219244d18df873b0bfb344d3dc0b2a7)
- 规则判断：high / hardware；打包候选：是，待人工评估
- 命中规则：functional:add、functional:adds、keyword:hardware:microarchitecture、keyword:hardware:tune、path:gcc/config/riscv/arcv-rhx100.md、path:gcc/config/riscv/riscv-cores.def、path:gcc/config/riscv/riscv-opts.h、path:gcc/config/riscv/riscv.md、path:gcc/doc/riscv-mtune.texi、path:gcc/testsuite/gcc.target/riscv/arcv-sched-mul-mem-rpx100.c、token:risc-v、token:riscv、token:rv32、token:rv64
- 涉及文件：gcc/config/riscv/arcv-rhx100.md、gcc/config/riscv/riscv-cores.def、gcc/config/riscv/riscv-opts.h、gcc/config/riscv/riscv.md、gcc/doc/riscv-mtune.texi、gcc/testsuite/gcc.target/riscv/arcv-sched-mul-mem-rpx100.c
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V 硬件支持相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为高；未验证构建、运行或发布状态。
- 打包建议：建议人工核对上游状态和适用版本，并完成构建及回归测试后再决定打包。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。

### \[RISC-V\] Improve saturating truncation sequences for RISC-V when Zbb is enabled

- 仓库：gcc-mirror/gcc；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-11-03T16:03:53Z
- 作者：Jeff Law；SHA：73225095de4c3b873841aea8a73cc14d2f067b72
- 来源：[原始记录](https://github.com/gcc-mirror/gcc/commit/73225095de4c3b873841aea8a73cc14d2f067b72)
- 规则判断：high / hardware；打包候选：是，待人工评估
- 命中规则：functional:enabled、functional:extend、functional:improve、keyword:hardware:k3、keyword:isa-extension:extension、keyword:isa-extension:zbb、path:gcc/config/riscv/riscv.cc、path:gcc/testsuite/gcc.target/riscv/ustrunc-zbb-1.c、path:gcc/testsuite/gcc.target/riscv/ustrunc-zbb-run.c、path:gcc/testsuite/gcc.target/riscv/ustrunc-zbb.h、token:risc-v、token:riscv
- 涉及文件：gcc/config/riscv/riscv.cc、gcc/testsuite/gcc.target/riscv/ustrunc-zbb-1.c、gcc/testsuite/gcc.target/riscv/ustrunc-zbb-run.c、gcc/testsuite/gcc.target/riscv/ustrunc-zbb.h
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V 硬件支持相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为高；未验证构建、运行或发布状态。
- 打包建议：建议人工核对上游状态和适用版本，并完成构建及回归测试后再决定打包。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。

### RISC-V: Add NEWS entries for the privileged spec deprecation

- 仓库：RTEMS/sourceware-mirror-binutils-gdb；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-11-03T14:31:26Z
- 作者：kito-cheng；SHA：10ae2343ac322dab390dbe6d83e14d065a381e07
- 来源：[原始记录](https://github.com/RTEMS/sourceware-mirror-binutils-gdb/commit/10ae2343ac322dab390dbe6d83e14d065a381e07)
- 规则判断：high / compiler-option；打包候选：是，待人工评估
- 命中规则：functional:add、keyword:compiler-option:options、token:risc-v
- 涉及文件：binutils/NEWS、gas/NEWS、ld/NEWS
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V 编译选项相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为高；未验证构建、运行或发布状态。
- 打包建议：建议人工核对上游状态和适用版本，并完成构建及回归测试后再决定打包。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。

### RISC-V: Document that PR\_RISCV\_V\_SET\_CONTROL is unsupported

- 仓库：sailfishos-mirror/glibc；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-11-03T11:50:27Z
- 作者：palmer-dabbelt；SHA：b941c17c0356f03946afb9c080242f89557bc0b2
- 来源：[原始记录](https://github.com/sailfishos-mirror/glibc/commit/b941c17c0356f03946afb9c080242f89557bc0b2)
- 规则判断：high / vector-crypto-hypervisor；打包候选：是，待人工评估
- 命中规则：functional:support、keyword:vector-crypto-hypervisor:vector、token:risc-v、token:riscv
- 涉及文件：manual/platform.texi
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V 向量、密码学或虚拟化相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为高；未验证构建、运行或发布状态。
- 打包建议：建议人工核对上游状态和适用版本，并完成构建及回归测试后再决定打包。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。


## 中优先级

### RISC-V: Adjust VLS subreg handling.

- 仓库：gcc-mirror/gcc；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-11-06T09:27:53Z
- 作者：Robin Dapp；SHA：6ef27c311e317485760a6ffc1759cde241e396de
- 来源：[原始记录](https://github.com/gcc-mirror/gcc/commit/6ef27c311e317485760a6ffc1759cde241e396de)
- 规则判断：medium / vector-crypto-hypervisor；打包候选：是，待人工评估
- 命中规则：keyword:vector-crypto-hypervisor:vector、path:gcc/config/riscv/riscv.cc、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/vec-concat-1.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/vls/extract-3.c、token:risc-v、token:riscv
- 涉及文件：gcc/config/riscv/riscv.cc、gcc/testsuite/gcc.target/riscv/rvv/autovec/vec-concat-1.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/vls/extract-3.c
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V 向量、密码学或虚拟化相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为中；未验证构建、运行或发布状态。
- 打包建议：建议人工核对上游状态和适用版本，并完成构建及回归测试后再决定打包。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。

### Change \`...'-style quoting in gdb

- 仓库：RTEMS/sourceware-mirror-binutils-gdb；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-11-05T20:23:58Z
- 作者：tromey；SHA：b32f06001cf75870b76a66a4e084bbeac11fa106
- 来源：[原始记录](https://github.com/RTEMS/sourceware-mirror-binutils-gdb/commit/b32f06001cf75870b76a66a4e084bbeac11fa106)
- 规则判断：medium / bugfix；打包候选：是，待人工评估
- 命中规则：keyword:bugfix:bug、path:gdb/riscv-tdep.c
- 涉及文件：gdb/aarch64-linux-tdep.c、gdb/ada-exp-parser.c、gdb/ada-lang.c、gdb/alpha-tdep.c、gdb/arch-utils.c、gdb/arm-linux-tdep.c、gdb/async-event.c、gdb/auto-load.c、gdb/ax-gdb.c、gdb/breakpoint.c、gdb/build-id.c、gdb/c-exp-parser.c、gdb/c-exp-parser.y、gdb/c-lang.c、gdb/charset.c、gdb/cli/cli-cmds.c、gdb/cli/cli-option.c、gdb/cli/cli-script.c、gdb/corefile.c、gdb/corelow.c、gdb/cp-namespace.c、gdb/d-exp-parser.y、gdb/darwin-nat.c、gdb/dtrace-probe.c、gdb/dwarf2/expr.c、gdb/dwarf2/index-write.c、gdb/dwarf2/line-header.c、gdb/dwarf2/loc.c、gdb/dwarf2/macro.c、gdb/eval.c、gdb/exec.c、gdb/filesystem.c、gdb/findvar.c、gdb/gdb-demangle.c、gdb/gnu-nat.c、gdb/gnu-v3-abi.c、gdb/go-exp-parser.c、gdb/go-exp-parser.y、gdb/go32-nat.c、gdb/guile/guile.c、gdb/i386-fbsd-tdep.c、gdb/i386-linux-tdep.c、gdb/i386-tdep.c、gdb/ia64-tdep.c、gdb/infcmd.c、gdb/infrun.c、gdb/interps.c、gdb/language.c、gdb/m2-lang.c、gdb/machoread.c、gdb/macrocmd.c、gdb/macroexp.c、gdb/macroscope.c、gdb/macrotab.c、gdb/main.c、gdb/maint.c、gdb/mi/mi-main.c、gdb/mips-tdep.c、gdb/objfiles.c、gdb/p-exp-parser.y、gdb/parse.c、gdb/ppc-linux-tdep.c、gdb/printcmd.c、gdb/probe.c、gdb/python/py-breakpoint.c、gdb/python/py-finishbreakpoint.c、gdb/python/py-infthread.c、gdb/python/python.c、gdb/remote-fileio.c、gdb/remote.c、gdb/riscv-tdep.c、gdb/solib-aix.c、gdb/solib-darwin.c、gdb/solib-rocm.c、gdb/solib.c、gdb/source.c、gdb/stack.c、gdb/stap-probe.c、gdb/symfile.c、gdb/symtab.c、gdb/target.c、gdb/testsuite/gdb.ada/bp\_c\_mixed\_case.exp、gdb/testsuite/gdb.ada/catch\_ex.exp、gdb/testsuite/gdb.ada/catch\_ex\_std.exp、gdb/testsuite/gdb.ada/excep\_handle.exp、gdb/testsuite/gdb.ada/limited-length.exp、gdb/testsuite/gdb.ada/literals.exp、gdb/testsuite/gdb.ada/mi\_catch\_ex.exp、gdb/testsuite/gdb.ada/mi\_catch\_ex\_hand.exp、gdb/testsuite/gdb.ada/mi\_ex\_cond.exp、gdb/testsuite/gdb.arch/amd64-stap-optional-prefix.exp、gdb/testsuite/gdb.arch/amd64-stap-wrong-subexp.exp、gdb/testsuite/gdb.arch/s390-multiarch.exp、gdb/testsuite/gdb.base/attach.exp、gdb/testsuite/gdb.base/break-unload-file.exp、gdb/testsuite/gdb.base/cached-source-file.exp、gdb/testsuite/gdb.base/define.exp、gdb/testsuite/gdb.base/exprs.exp、gdb/testsuite/gdb.base/gdb-index-err.exp、gdb/testsuite/gdb.base/help.exp、gdb/testsuite/gdb.base/info-macros.exp、gdb/testsuite/gdb.base/jump-inline.exp、gdb/testsuite/gdb.base/jump.exp、gdb/testsuite/gdb.base/macscp.exp、gdb/testsuite/gdb.base/maint-info-sections.exp、gdb/testsuite/gdb.base/new-ui.exp、gdb/testsuite/gdb.base/options.exp、gdb/testsuite/gdb.base/settings.exp、gdb/testsuite/gdb.base/subst.exp、gdb/testsuite/gdb.base/tls-nothreads.exp、gdb/testsuite/gdb.base/watch\_thread\_num.exp、gdb/testsuite/gdb.base/watchpoint.exp、gdb/testsuite/gdb.cp/maint.exp、gdb/testsuite/gdb.cp/namespace-enum.exp、gdb/testsuite/gdb.cp/overload.exp、gdb/testsuite/gdb.dlang/expression.exp、gdb/testsuite/gdb.dwarf2/macro-complaints.exp、gdb/testsuite/gdb.server/bkpt-other-inferior.exp、gdb/testsuite/gdb.server/server-exec-info.exp、gdb/testsuite/gdb.server/target-exec-file.exp、gdb/testsuite/gdb.trace/actions.exp、gdb/testsuite/lib/gdb.exp、gdb/thread.c、gdb/tracefile-tfile.c、gdb/tracefile.c、gdb/tracepoint.c、gdb/tui/tui-win.c、gdb/tui/tui-winsource.c、gdb/utils.c、gdb/valarith.c、gdb/valops.c、gdb/value.c、gdb/windows-nat.c、gdb/xml-syscall.c、gdb/z80-tdep.c
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V 问题修复相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为中；未验证构建、运行或发布状态。
- 打包建议：建议人工核对上游状态和适用版本，并完成构建及回归测试后再决定打包。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。

### RISC-V: Remove redundant VLA niters check in better\_main\_loop\_than\_p

- 仓库：gcc-mirror/gcc；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-11-05T12:06:22Z
- 作者：ZhongyaoChen；SHA：78873c4dcee4b92347501b898f426d4302e374c0
- 来源：[原始记录](https://github.com/gcc-mirror/gcc/commit/78873c4dcee4b92347501b898f426d4302e374c0)
- 规则判断：medium / bugfix；打包候选：是，待人工评估
- 命中规则：keyword:bugfix:fixes、keyword:vector-crypto-hypervisor:vector、path:gcc/config/riscv/riscv-vector-costs.cc、path:gcc/testsuite/gcc.dg/vect/costmodel/riscv/rvv/pr113112-3.c、token:risc-v、token:riscv
- 涉及文件：gcc/config/riscv/riscv-vector-costs.cc、gcc/testsuite/gcc.dg/vect/costmodel/riscv/rvv/pr113112-3.c
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V 问题修复相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为中；未验证构建、运行或发布状态。
- 打包建议：建议人工核对上游状态和适用版本，并完成构建及回归测试后再决定打包。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。

### RISC-V: Fix reg overlap for vs1 of the widening float reduction

- 仓库：gcc-mirror/gcc；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-11-04T06:15:40Z
- 作者：Incarnation-p-lee；SHA：b95850f0c0df9e90f7a5bad61f76627bff5501c9
- 来源：[原始记录](https://github.com/gcc-mirror/gcc/commit/b95850f0c0df9e90f7a5bad61f76627bff5501c9)
- 规则判断：medium / bugfix；打包候选：是，待人工评估
- 命中规则：keyword:bugfix:fix、keyword:vector-crypto-hypervisor:vector、path:gcc/config/riscv/vector.md、token:risc-v、token:riscv
- 涉及文件：gcc/config/riscv/vector.md
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V 问题修复相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为中；未验证构建、运行或发布状态。
- 打包建议：建议人工核对上游状态和适用版本，并完成构建及回归测试后再决定打包。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。

### RISC-V: Ignore the deprecated privileged spec attributes

- 仓库：RTEMS/sourceware-mirror-binutils-gdb；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-11-03T14:31:16Z
- 作者：kito-cheng；SHA：2394c2445caa44e30dd58f0b08d7a6a5cc2c33da
- 来源：[原始记录](https://github.com/RTEMS/sourceware-mirror-binutils-gdb/commit/2394c2445caa44e30dd58f0b08d7a6a5cc2c33da)
- 规则判断：medium / profile-abi；打包候选：是，待人工评估
- 命中规则：keyword:profile-abi:psabi、path:bfd/elfxx-riscv.c、path:gas/config/tc-riscv.c、path:gas/doc/c-riscv.texi、path:gas/testsuite/gas/riscv/attribute-11.d、path:gas/testsuite/gas/riscv/attribute-11.s、path:gas/testsuite/gas/riscv/attribute-12.d、path:gas/testsuite/gas/riscv/attribute-14.s、path:gas/testsuite/gas/riscv/attribute-14a.d、path:gas/testsuite/gas/riscv/attribute-14b.d、path:gas/testsuite/gas/riscv/attribute-14c.d、path:gas/testsuite/gas/riscv/attribute-14d.d、path:gas/testsuite/gas/riscv/attribute-15.d、path:gas/testsuite/gas/riscv/attribute-16.d、path:gas/testsuite/gas/riscv/attribute-priv-ignored.d、path:ld/testsuite/ld-riscv-elf/attr-merge-priv-spec-01.d、path:ld/testsuite/ld-riscv-elf/attr-merge-priv-spec-02.d、path:ld/testsuite/ld-riscv-elf/attr-merge-priv-spec-03.d、path:ld/testsuite/ld-riscv-elf/attr-merge-priv-spec-b.s、path:ld/testsuite/ld-riscv-elf/attr-merge-priv-spec-d.s、path:ld/testsuite/ld-riscv-elf/ld-riscv-elf.exp、token:risc-v、token:riscv
- 涉及文件：bfd/elfxx-riscv.c、gas/config/tc-riscv.c、gas/doc/c-riscv.texi、gas/testsuite/gas/riscv/attribute-11.d、gas/testsuite/gas/riscv/attribute-11.s、gas/testsuite/gas/riscv/attribute-12.d、gas/testsuite/gas/riscv/attribute-14.s、gas/testsuite/gas/riscv/attribute-14a.d、gas/testsuite/gas/riscv/attribute-14b.d、gas/testsuite/gas/riscv/attribute-14c.d、gas/testsuite/gas/riscv/attribute-14d.d、gas/testsuite/gas/riscv/attribute-15.d、gas/testsuite/gas/riscv/attribute-16.d、gas/testsuite/gas/riscv/attribute-priv-ignored.d、ld/testsuite/ld-riscv-elf/attr-merge-priv-spec-01.d、ld/testsuite/ld-riscv-elf/attr-merge-priv-spec-02.d、ld/testsuite/ld-riscv-elf/attr-merge-priv-spec-03.d、ld/testsuite/ld-riscv-elf/attr-merge-priv-spec-b.s、ld/testsuite/ld-riscv-elf/attr-merge-priv-spec-d.s、ld/testsuite/ld-riscv-elf/ld-riscv-elf.exp
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V Profile 或 ABI相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为中；未验证构建、运行或发布状态。
- 打包建议：建议人工核对上游状态和适用版本，并完成构建及回归测试后再决定打包。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。

### RISC-V: Remove the privileged spec classes

- 仓库：RTEMS/sourceware-mirror-binutils-gdb；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-11-03T14:31:16Z
- 作者：kito-cheng；SHA：57327e464212915d9bfc0d8d2ec587d201895c27
- 来源：[原始记录](https://github.com/RTEMS/sourceware-mirror-binutils-gdb/commit/57327e464212915d9bfc0d8d2ec587d201895c27)
- 规则判断：medium / compiler-option；打包候选：是，待人工评估
- 命中规则：keyword:compiler-option:option、path:bfd/cpu-riscv.c、path:bfd/cpu-riscv.h、path:gas/config/tc-riscv.c、path:gdb/riscv-tdep.c、path:gdb/riscv-tdep.h、path:include/opcode/riscv-opc.h、path:opcodes/riscv-dis.c、token:risc-v、token:riscv
- 涉及文件：bfd/cpu-riscv.c、bfd/cpu-riscv.h、binutils/dwarf.c、gas/config/tc-riscv.c、gdb/riscv-tdep.c、gdb/riscv-tdep.h、include/opcode/riscv-opc.h、opcodes/riscv-dis.c
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V 编译选项相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为中；未验证构建、运行或发布状态。
- 打包建议：建议人工核对上游状态和适用版本，并完成构建及回归测试后再决定打包。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。

### RISC-V: Deprecate the privileged spec version selection

- 仓库：RTEMS/sourceware-mirror-binutils-gdb；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-11-03T14:31:06Z
- 作者：kito-cheng；SHA：22eaa6766f849ae888800454a9c191cde1583d90
- 来源：[原始记录](https://github.com/RTEMS/sourceware-mirror-binutils-gdb/commit/22eaa6766f849ae888800454a9c191cde1583d90)
- 规则判断：medium / other；打包候选：否
- 命中规则：path:gas/config/tc-riscv.c、path:gas/doc/c-riscv.texi、path:gas/testsuite/gas/riscv/attribute-05.d、path:gas/testsuite/gas/riscv/attribute-05.l、path:gas/testsuite/gas/riscv/attribute-12.d、path:gas/testsuite/gas/riscv/attribute-13.d、path:gas/testsuite/gas/riscv/attribute-15.d、path:gas/testsuite/gas/riscv/attribute-16.d、path:gas/testsuite/gas/riscv/attribute-priv-ignored.d、path:gas/testsuite/gas/riscv/attribute-priv-ignored.l、path:gas/testsuite/gas/riscv/attribute-priv-ignored.s、path:gas/testsuite/gas/riscv/csr-dw-regnums.d、path:gas/testsuite/gas/riscv/csr-dw-regnums.s、path:gas/testsuite/gas/riscv/csr-insns-pseudo-noalias.d、path:gas/testsuite/gas/riscv/csr-insns-pseudo-zfinx.d、path:gas/testsuite/gas/riscv/csr-insns-pseudo.d、path:gas/testsuite/gas/riscv/csr-insns-pseudo.s、path:gas/testsuite/gas/riscv/csr-insns-read-only.d、path:gas/testsuite/gas/riscv/csr-insns-read-only.s、path:gas/testsuite/gas/riscv/csr-version-1p10.d、path:gas/testsuite/gas/riscv/csr-version-1p10.l、path:gas/testsuite/gas/riscv/csr-version-1p11.d、path:gas/testsuite/gas/riscv/csr-version-1p11.l、path:gas/testsuite/gas/riscv/csr-version-1p12.d、path:gas/testsuite/gas/riscv/csr-version-1p12.l、path:gas/testsuite/gas/riscv/csr-version-1p13.d、path:gas/testsuite/gas/riscv/csr-version-1p13.l、path:gas/testsuite/gas/riscv/csr.d、path:gas/testsuite/gas/riscv/csr.l、path:gas/testsuite/gas/riscv/csr.s、path:gas/testsuite/gas/riscv/imply-zicsr-zifencei-i2p1-misa-spec-20191213.d、path:gas/testsuite/gas/riscv/imply-zicsr-zifencei.s、path:gas/testsuite/gas/riscv/priv-spec-deprecated.l、path:gas/testsuite/gas/riscv/spmpen-rv32.d、path:ld/testsuite/ld-riscv-elf/attr-merge-priv-spec-01.d、path:ld/testsuite/ld-riscv-elf/attr-merge-priv-spec-02.d、path:ld/testsuite/ld-riscv-elf/attr-merge-priv-spec-03.d、path:ld/testsuite/ld-riscv-elf/attr-merge-priv-spec-a.s、path:ld/testsuite/ld-riscv-elf/attr-merge-priv-spec-b.s、path:ld/testsuite/ld-riscv-elf/attr-merge-priv-spec-c.s、path:opcodes/riscv-dis.c、token:risc-v
- 涉及文件：binutils/doc/binutils.texi、gas/config.in、gas/config/tc-riscv.c、gas/configure、gas/configure.ac、gas/doc/c-riscv.texi、gas/testsuite/gas/riscv/attribute-05.d、gas/testsuite/gas/riscv/attribute-05.l、gas/testsuite/gas/riscv/attribute-12.d、gas/testsuite/gas/riscv/attribute-13.d、gas/testsuite/gas/riscv/attribute-15.d、gas/testsuite/gas/riscv/attribute-16.d、gas/testsuite/gas/riscv/attribute-priv-ignored.d、gas/testsuite/gas/riscv/attribute-priv-ignored.l、gas/testsuite/gas/riscv/attribute-priv-ignored.s、gas/testsuite/gas/riscv/csr-dw-regnums.d、gas/testsuite/gas/riscv/csr-dw-regnums.s、gas/testsuite/gas/riscv/csr-insns-pseudo-noalias.d、gas/testsuite/gas/riscv/csr-insns-pseudo-zfinx.d、gas/testsuite/gas/riscv/csr-insns-pseudo.d、gas/testsuite/gas/riscv/csr-insns-pseudo.s、gas/testsuite/gas/riscv/csr-insns-read-only.d、gas/testsuite/gas/riscv/csr-insns-read-only.s、gas/testsuite/gas/riscv/csr-version-1p10.d、gas/testsuite/gas/riscv/csr-version-1p10.l、gas/testsuite/gas/riscv/csr-version-1p11.d、gas/testsuite/gas/riscv/csr-version-1p11.l、gas/testsuite/gas/riscv/csr-version-1p12.d、gas/testsuite/gas/riscv/csr-version-1p12.l、gas/testsuite/gas/riscv/csr-version-1p13.d、gas/testsuite/gas/riscv/csr-version-1p13.l、gas/testsuite/gas/riscv/csr.d、gas/testsuite/gas/riscv/csr.l、gas/testsuite/gas/riscv/csr.s、gas/testsuite/gas/riscv/imply-zicsr-zifencei-i2p1-misa-spec-20191213.d、gas/testsuite/gas/riscv/imply-zicsr-zifencei.s、gas/testsuite/gas/riscv/priv-spec-deprecated.l、gas/testsuite/gas/riscv/spmpen-rv32.d、ld/testsuite/ld-riscv-elf/attr-merge-priv-spec-01.d、ld/testsuite/ld-riscv-elf/attr-merge-priv-spec-02.d、ld/testsuite/ld-riscv-elf/attr-merge-priv-spec-03.d、ld/testsuite/ld-riscv-elf/attr-merge-priv-spec-a.s、ld/testsuite/ld-riscv-elf/attr-merge-priv-spec-b.s、ld/testsuite/ld-riscv-elf/attr-merge-priv-spec-c.s、opcodes/riscv-dis.c
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V 其他变更相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为中；未验证构建、运行或发布状态。
- 打包建议：保留跟踪，暂不列为优先打包候选；需结合实际版本和测试结果人工评估。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。

### RISC-V: Remove the N extension CSRs

- 仓库：RTEMS/sourceware-mirror-binutils-gdb；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-11-03T14:31:06Z
- 作者：kito-cheng；SHA：62766e1b169d6d4f6fbd14697c66947a07b84dee
- 来源：[原始记录](https://github.com/RTEMS/sourceware-mirror-binutils-gdb/commit/62766e1b169d6d4f6fbd14697c66947a07b84dee)
- 规则判断：medium / isa-extension；打包候选：是，待人工评估
- 命中规则：keyword:isa-extension:extension、path:include/opcode/riscv-opc.h、token:risc-v
- 涉及文件：include/opcode/riscv-opc.h
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V ISA 扩展相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为中；未验证构建、运行或发布状态。
- 打包建议：建议人工核对上游状态和适用版本，并完成构建及回归测试后再决定打包。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。

### Use add\_reg\_note instead of a hand-built note

- 仓库：gcc-mirror/gcc；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-11-03T00:50:32Z
- 作者：tbsaunde；SHA：78a34222c6368cfab3e750427f8354a3176e4d6d
- 来源：[原始记录](https://github.com/gcc-mirror/gcc/commit/78a34222c6368cfab3e750427f8354a3176e4d6d)
- 规则判断：medium / other；打包候选：否
- 命中规则：path:gcc/config/riscv/riscv.cc、token:riscv
- 涉及文件：gcc/config/arm/arm.cc、gcc/config/cris/cris.cc、gcc/config/frv/frv.cc、gcc/config/loongarch/loongarch.cc、gcc/config/riscv/riscv.cc、gcc/config/stormy16/stormy16.cc
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V 其他变更相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为中；未验证构建、运行或发布状态。
- 打包建议：保留跟踪，暂不列为优先打包候选；需结合实际版本和测试结果人工评估。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。

### Use rtx\_insn \* and rtx\_code\_label \* where the value already has that type

- 仓库：gcc-mirror/gcc；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-11-03T00:50:30Z
- 作者：tbsaunde；SHA：043a79ac094e4c5078d12b22dc6a38ab624b1fbb
- 来源：[原始记录](https://github.com/gcc-mirror/gcc/commit/043a79ac094e4c5078d12b22dc6a38ab624b1fbb)
- 规则判断：medium / other；打包候选：否
- 命中规则：path:gcc/config/riscv/riscv-string.cc、token:riscv
- 涉及文件：gcc/config/aarch64/aarch64.cc、gcc/config/arm/arm.cc、gcc/config/bfin/bfin.cc、gcc/config/c6x/c6x.cc、gcc/config/i386/i386-features.cc、gcc/config/i386/i386-features.h、gcc/config/ia64/ia64.cc、gcc/config/m68k/m68k.md、gcc/config/mips/mips.cc、gcc/config/pru/pru.md、gcc/config/riscv/riscv-string.cc、gcc/config/rl78/rl78.cc、gcc/config/rs6000/rs6000-p8swap.cc、gcc/config/rs6000/rs6000-string.cc、gcc/config/rs6000/rs6000.cc、gcc/config/rs6000/rs6000.md、gcc/config/s390/s390.cc、gcc/config/sh/sh.cc、gcc/config/sh/sh.md、gcc/config/sh/sh\_treg\_combine.cc、gcc/explow.cc、gcc/explow.h、gcc/haifa-sched.cc、gcc/optabs.cc
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V 其他变更相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为中；未验证构建、运行或发布状态。
- 打包建议：保留跟踪，暂不列为优先打包候选；需结合实际版本和测试结果人工评估。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。

### Hold emitted insns in rtx\_insn \* locals

- 仓库：gcc-mirror/gcc；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-11-03T00:50:29Z
- 作者：tbsaunde；SHA：fa8d8dfca73ee82720c90a9daad5c573fc2a3c8f
- 来源：[原始记录](https://github.com/gcc-mirror/gcc/commit/fa8d8dfca73ee82720c90a9daad5c573fc2a3c8f)
- 规则判断：medium / other；打包候选：否
- 命中规则：path:gcc/config/riscv/riscv.cc、token:riscv
- 涉及文件：gcc/config/arc/arc.cc、gcc/config/arm/arm.cc、gcc/config/msp430/msp430.cc、gcc/config/riscv/riscv.cc、gcc/config/rl78/rl78.cc、gcc/config/s390/s390.cc、gcc/config/sh/sh\_treg\_combine.cc
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V 其他变更相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为中；未验证构建、运行或发布状态。
- 打包建议：保留跟踪，暂不列为优先打包候选；需结合实际版本和测试结果人工评估。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。

### Use rtx\_insn \* for locals set from insn returns

- 仓库：gcc-mirror/gcc；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-11-03T00:50:27Z
- 作者：tbsaunde；SHA：5f9900ec00fcaa7a44d8bdc69b77c8be5b18012e
- 来源：[原始记录](https://github.com/gcc-mirror/gcc/commit/5f9900ec00fcaa7a44d8bdc69b77c8be5b18012e)
- 规则判断：medium / other；打包候选：否
- 命中规则：path:gcc/config/riscv/riscv.cc、token:riscv
- 涉及文件：gcc/compare-elim.cc、gcc/config/alpha/alpha.md、gcc/config/arc/arc.cc、gcc/config/arm/arm.cc、gcc/config/cris/cris.cc、gcc/config/lm32/lm32.cc、gcc/config/loongarch/loongarch.cc、gcc/config/riscv/riscv.cc、gcc/config/s390/s390.cc、gcc/config/sh/sh\_treg\_combine.cc、gcc/config/stormy16/stormy16.cc、gcc/config/visium/visium.cc
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V 其他变更相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为中；未验证构建、运行或发布状态。
- 打包建议：保留跟踪，暂不列为优先打包候选；需结合实际版本和测试结果人工评估。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。

### Use rtx\_insn \* for returns that are already an insn

- 仓库：gcc-mirror/gcc；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-11-03T00:50:27Z
- 作者：tbsaunde；SHA：f1c2610b7bbba75c7f8cdff7b347f20aa7966960
- 来源：[原始记录](https://github.com/gcc-mirror/gcc/commit/f1c2610b7bbba75c7f8cdff7b347f20aa7966960)
- 规则判断：medium / other；打包候选：否
- 命中规则：path:gcc/config/riscv/riscv-protos.h、path:gcc/config/riscv/riscv.cc、token:riscv
- 涉及文件：gcc/compare-elim.cc、gcc/config/aarch64/aarch64.cc、gcc/config/alpha/alpha-protos.h、gcc/config/alpha/alpha.cc、gcc/config/arc/arc.cc、gcc/config/arm/arm.cc、gcc/config/cris/cris-protos.h、gcc/config/cris/cris.cc、gcc/config/csky/csky.cc、gcc/config/fr30/fr30-protos.h、gcc/config/fr30/fr30.cc、gcc/config/frv/frv-protos.h、gcc/config/frv/frv.cc、gcc/config/h8300/h8300.cc、gcc/config/i386/i386.cc、gcc/config/lm32/lm32.cc、gcc/config/loongarch/loongarch-protos.h、gcc/config/loongarch/loongarch.cc、gcc/config/m32r/m32r-protos.h、gcc/config/m32r/m32r.cc、gcc/config/pru/pru.cc、gcc/config/riscv/riscv-protos.h、gcc/config/riscv/riscv.cc、gcc/config/rs6000/rs6000-logue.cc、gcc/config/s390/s390.cc、gcc/config/sh/sh.cc、gcc/config/sh/sh\_treg\_combine.cc、gcc/config/stormy16/stormy16.cc、gcc/config/visium/visium.cc
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V 其他变更相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为中；未验证构建、运行或发布状态。
- 打包建议：保留跟踪，暂不列为优先打包候选；需结合实际版本和测试结果人工评估。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。

### Use rtx\_insn \* for locals that already hold an insn

- 仓库：gcc-mirror/gcc；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-11-03T00:50:26Z
- 作者：tbsaunde；SHA：2df90e844e1ad833ac336ccedd4c30472b22f345
- 来源：[原始记录](https://github.com/gcc-mirror/gcc/commit/2df90e844e1ad833ac336ccedd4c30472b22f345)
- 规则判断：medium / other；打包候选：否
- 命中规则：path:gcc/config/riscv/riscv.cc、path:gcc/config/riscv/thead.cc、token:riscv
- 涉及文件：gcc/config/aarch64/aarch64.cc、gcc/config/alpha/alpha.cc、gcc/config/arc/arc.cc、gcc/config/arm/arm.cc、gcc/config/bfin/bfin.cc、gcc/config/c6x/c6x.cc、gcc/config/cris/cris.cc、gcc/config/cris/cris.md、gcc/config/csky/csky.cc、gcc/config/fr30/fr30.cc、gcc/config/frv/frv.cc、gcc/config/ft32/ft32.cc、gcc/config/gcn/gcn.cc、gcc/config/ia64/ia64.cc、gcc/config/lm32/lm32.cc、gcc/config/loongarch/loongarch.cc、gcc/config/loongarch/loongarch.md、gcc/config/m32r/m32r.cc、gcc/config/mmix/mmix.cc、gcc/config/moxie/moxie.cc、gcc/config/nds32/nds32-md-auxiliary.cc、gcc/config/nds32/nds32.cc、gcc/config/nds32/nds32.md、gcc/config/nvptx/nvptx.cc、gcc/config/or1k/or1k.cc、gcc/config/pru/pru.cc、gcc/config/pru/pru.md、gcc/config/riscv/riscv.cc、gcc/config/riscv/thead.cc、gcc/config/rs6000/rs6000-logue.cc、gcc/config/rs6000/rs6000-string.cc、gcc/config/rx/rx.cc、gcc/config/s390/s390.cc、gcc/config/sh/sh.cc、gcc/config/sh/sh\_treg\_combine.cc、gcc/config/sparc/sparc.cc、gcc/config/stormy16/stormy16.cc、gcc/config/v850/v850.cc、gcc/config/vax/vax.cc、gcc/config/visium/visium.cc、gcc/config/xtensa/xtensa.cc、gcc/final.cc、gcc/reorg.cc、gcc/tree-outof-ssa.cc
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V 其他变更相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为中；未验证构建、运行或发布状态。
- 打包建议：保留跟踪，暂不列为优先打包候选；需结合实际版本和测试结果人工评估。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。

### Use rtx\_code\_label \* for locals set by gen\_label\_rtx

- 仓库：gcc-mirror/gcc；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-11-03T00:50:25Z
- 作者：tbsaunde；SHA：cea82e41d3db61fbd0d181d113967b83ed69070c
- 来源：[原始记录](https://github.com/gcc-mirror/gcc/commit/cea82e41d3db61fbd0d181d113967b83ed69070c)
- 规则判断：medium / other；打包候选：否
- 命中规则：path:gcc/config/riscv/riscv-string.cc、path:gcc/config/riscv/riscv-v.cc、path:gcc/config/riscv/riscv.cc、path:gcc/config/riscv/riscv.md、token:riscv
- 涉及文件：gcc/calls.cc、gcc/config/aarch64/aarch64.cc、gcc/config/alpha/alpha.cc、gcc/config/alpha/alpha.md、gcc/config/arc/arc.cc、gcc/config/avr/avr.cc、gcc/config/avr/avr.md、gcc/config/bfin/bfin.cc、gcc/config/cris/cris.cc、gcc/config/csky/csky.cc、gcc/config/csky/csky.md、gcc/config/gcn/gcn-valu.md、gcc/config/gcn/gcn.cc、gcc/config/gcn/gcn.md、gcc/config/i386/i386-expand.cc、gcc/config/ia64/ia64.cc、gcc/config/nds32/nds32-memory-manipulation.cc、gcc/config/pa/pa.cc、gcc/config/pa/pa.md、gcc/config/pru/pru.md、gcc/config/riscv/riscv-string.cc、gcc/config/riscv/riscv-v.cc、gcc/config/riscv/riscv.cc、gcc/config/riscv/riscv.md、gcc/config/rs6000/rs6000-builtin.cc、gcc/config/rs6000/rs6000-call.cc、gcc/config/rs6000/rs6000-logue.cc、gcc/config/rs6000/rs6000-string.cc、gcc/config/rs6000/rs6000.cc、gcc/config/rs6000/rs6000.md、gcc/config/s390/s390.cc、gcc/config/stormy16/stormy16.cc、gcc/config/vax/builtins.md、gcc/config/xtensa/xtensa.cc、gcc/explow.cc、gcc/rtl-tests.cc
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V 其他变更相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为中；未验证构建、运行或发布状态。
- 打包建议：保留跟踪，暂不列为优先打包候选；需结合实际版本和测试结果人工评估。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。

### \[gdb/NEWS\] Move item from gdb 17 to gdb 18 \(part 3\)

- 仓库：RTEMS/sourceware-mirror-binutils-gdb；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-11-02T15:18:51Z
- 作者：vries；SHA：3eb0c867d9afbc08338c9ac540acced54fa2cacc
- 来源：[原始记录](https://github.com/RTEMS/sourceware-mirror-binutils-gdb/commit/3eb0c867d9afbc08338c9ac540acced54fa2cacc)
- 规则判断：medium / bugfix；打包候选：是，待人工评估
- 命中规则：keyword:bugfix:bug、token:riscv
- 涉及文件：gdb/NEWS
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V 问题修复相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为中；未验证构建、运行或发布状态。
- 打包建议：建议人工核对上游状态和适用版本，并完成构建及回归测试后再决定打包。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。

### c++: let the target see the attributes that wait for instantiation

- 仓库：gcc-mirror/gcc；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-11-02T13:24:00Z
- 作者：kito-cheng；SHA：d0d6b4b045bc9663b6d2ddb78a9154cce8dc19d2
- 来源：[原始记录](https://github.com/gcc-mirror/gcc/commit/d0d6b4b045bc9663b6d2ddb78a9154cce8dc19d2)
- 规则判断：medium / profile-abi；打包候选：是，待人工评估
- 命中规则：keyword:profile-abi:abi、keyword:profile-abi:psabi、path:gcc/testsuite/g++.target/riscv/mangle-vls-cc.C、token:risc-v、token:riscv
- 涉及文件：gcc/cp/decl2.cc、gcc/testsuite/g++.target/riscv/mangle-vls-cc.C
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V Profile 或 ABI相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为中；未验证构建、运行或发布状态。
- 打包建议：建议人工核对上游状态和适用版本，并完成构建及回归测试后再决定打包。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。

### RISC-V: Mangle the ABI tag of a standard calling convention variant

- 仓库：gcc-mirror/gcc；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-11-02T13:23:59Z
- 作者：kito-cheng；SHA：d3726407bde51b93deef248863192b3c9e09c9ae
- 来源：[原始记录](https://github.com/gcc-mirror/gcc/commit/d3726407bde51b93deef248863192b3c9e09c9ae)
- 规则判断：medium / profile-abi；打包候选：是，待人工评估
- 命中规则：keyword:profile-abi:abi、keyword:profile-abi:psabi、keyword:vector-crypto-hypervisor:vector、keyword:vector-crypto-hypervisor:vlen、path:gcc/config/riscv/riscv.cc、path:gcc/testsuite/g++.target/riscv/mangle-vls-cc.C、token:risc-v、token:riscv
- 涉及文件：gcc/config/riscv/riscv.cc、gcc/testsuite/g++.target/riscv/mangle-vls-cc.C
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V Profile 或 ABI相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为中；未验证构建、运行或发布状态。
- 打包建议：建议人工核对上游状态和适用版本，并完成构建及回归测试后再决定打包。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。

### RISC-V: Avoid vsetvl insertion on shared table edges \[PR middle-end/126236\]

- 仓库：gcc-mirror/gcc；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-11-02T10:08:33Z
- 作者：ktkachov；SHA：bb55bb62fc8a8eabb928653fc38cbe1fde3ab773
- 来源：[原始记录](https://github.com/gcc-mirror/gcc/commit/bb55bb62fc8a8eabb928653fc38cbe1fde3ab773)
- 规则判断：medium / vector-crypto-hypervisor；打包候选：是，待人工评估
- 命中规则：keyword:vector-crypto-hypervisor:vlen、path:gcc/config/riscv/riscv-vsetvl.cc、path:gcc/testsuite/gcc.target/riscv/rvv/vsetvl/pr126236.c、token:risc-v、token:riscv
- 涉及文件：gcc/config/riscv/riscv-vsetvl.cc、gcc/testsuite/gcc.target/riscv/rvv/vsetvl/pr126236.c
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V 向量、密码学或虚拟化相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为中；未验证构建、运行或发布状态。
- 打包建议：建议人工核对上游状态和适用版本，并完成构建及回归测试后再决定打包。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。


## 低优先级

### \[gdb/testsuite\] Handle updated quoting style in some test-cases

- 仓库：RTEMS/sourceware-mirror-binutils-gdb；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-11-06T12:56:36Z
- 作者：vries；SHA：a73130077e78606049fbc92b6be190e29ea956ce
- 来源：[原始记录](https://github.com/RTEMS/sourceware-mirror-binutils-gdb/commit/a73130077e78606049fbc92b6be190e29ea956ce)
- 规则判断：low / other；打包候选：否
- 命中规则：low-value:test、low-value:testsuite、path:gdb/testsuite/gdb.arch/riscv-reg-aliases.exp、path:gdb/testsuite/gdb.arch/riscv-tdesc-regs.exp、test-only
- 涉及文件：gdb/testsuite/gdb.arch/riscv-reg-aliases.exp、gdb/testsuite/gdb.arch/riscv-tdesc-regs.exp、gdb/testsuite/gdb.arch/s390-multiarch.exp、gdb/testsuite/gdb.base/corefile-buildid.exp、gdb/testsuite/gdb.base/corefile-exec-context.exp、gdb/testsuite/gdb.base/corefile-find-exec.exp、gdb/testsuite/gdb.base/corefile-no-threads.exp、gdb/testsuite/gdb.base/corefile.exp、gdb/testsuite/gdb.threads/thread-leader-exited.exp
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V 其他变更相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为低；未验证构建、运行或发布状态。
- 打包建议：保留跟踪，暂不列为优先打包候选；需结合实际版本和测试结果人工评估。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。

### testsuite: Fix tail-call checks in \_BitInt tests \[PR127848\]

- 仓库：gcc-mirror/gcc；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-11-06T10:13:02Z
- 作者：Torbjorn-Svensson；SHA：66c66fe317b9e5ba0fea75ee9220be2a0eacc1d1
- 来源：[原始记录](https://github.com/gcc-mirror/gcc/commit/66c66fe317b9e5ba0fea75ee9220be2a0eacc1d1)
- 规则判断：low / other；打包候选：否
- 命中规则：low-value:tests、low-value:testsuite、test-only、token:risc-v
- 涉及文件：gcc/testsuite/gcc.dg/pr127848-4.c、gcc/testsuite/gcc.dg/pr127848-5.c
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V 其他变更相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为低；未验证构建、运行或发布状态。
- 打包建议：保留跟踪，暂不列为优先打包候选；需结合实际版本和测试结果人工评估。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。

### RISC-V: Add more test cases for vfwred\[ou\]sum.vs

- 仓库：gcc-mirror/gcc；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-11-04T06:15:40Z
- 作者：Incarnation-p-lee；SHA：04f042f50ed44c7360c840949f71fb805fc982b8
- 来源：[原始记录](https://github.com/gcc-mirror/gcc/commit/04f042f50ed44c7360c840949f71fb805fc982b8)
- 规则判断：low / other；打包候选：否
- 命中规则：low-value:test、path:gcc/testsuite/gcc.target/riscv/rvv/base/pr112431-63.c、path:gcc/testsuite/gcc.target/riscv/rvv/base/pr112431-64.c、test-only、token:risc-v、token:riscv
- 涉及文件：gcc/testsuite/gcc.target/riscv/rvv/base/pr112431-63.c、gcc/testsuite/gcc.target/riscv/rvv/base/pr112431-64.c
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V 其他变更相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为低；未验证构建、运行或发布状态。
- 打包建议：保留跟踪，暂不列为优先打包候选；需结合实际版本和测试结果人工评估。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。

### RISC-V: Add test cases for vfwredosum.vs reg overlap

- 仓库：gcc-mirror/gcc；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-11-04T06:15:40Z
- 作者：Incarnation-p-lee；SHA：4710c505b10c7f6faac3c6315c307b8db10169e8
- 来源：[原始记录](https://github.com/gcc-mirror/gcc/commit/4710c505b10c7f6faac3c6315c307b8db10169e8)
- 规则判断：low / other；打包候选：否
- 命中规则：low-value:test、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwredosum\_vs-f16-m1.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwredosum\_vs-f16-m2.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwredosum\_vs-f16-m4.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwredosum\_vs-f16-m8.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwredosum\_vs-f32-m1.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwredosum\_vs-f32-m2.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwredosum\_vs-f32-m4.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwredosum\_vs-f32-m8.c、test-only、token:risc-v、token:riscv
- 涉及文件：gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwredosum\_vs-f16-m1.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwredosum\_vs-f16-m2.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwredosum\_vs-f16-m4.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwredosum\_vs-f16-m8.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwredosum\_vs-f32-m1.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwredosum\_vs-f32-m2.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwredosum\_vs-f32-m4.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwredosum\_vs-f32-m8.c
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V 其他变更相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为低；未验证构建、运行或发布状态。
- 打包建议：保留跟踪，暂不列为优先打包候选；需结合实际版本和测试结果人工评估。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。

### RISC-V: Add test cases for vfwredusum.vs reg overlap

- 仓库：gcc-mirror/gcc；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-11-04T06:15:40Z
- 作者：Incarnation-p-lee；SHA：fb1abdf96ba0fb9fe0656fbad5805083b74c49f9
- 来源：[原始记录](https://github.com/gcc-mirror/gcc/commit/fb1abdf96ba0fb9fe0656fbad5805083b74c49f9)
- 规则判断：low / other；打包候选：否
- 命中规则：low-value:test、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwredusum\_vs-f16-m1.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwredusum\_vs-f16-m2.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwredusum\_vs-f16-m4.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwredusum\_vs-f16-m8.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwredusum\_vs-f32-m1.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwredusum\_vs-f32-m2.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwredusum\_vs-f32-m4.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwredusum\_vs-f32-m8.c、test-only、token:risc-v、token:riscv
- 涉及文件：gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwredusum\_vs-f16-m1.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwredusum\_vs-f16-m2.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwredusum\_vs-f16-m4.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwredusum\_vs-f16-m8.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwredusum\_vs-f32-m1.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwredusum\_vs-f32-m2.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwredusum\_vs-f32-m4.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwredusum\_vs-f32-m8.c
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V 其他变更相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为低；未验证构建、运行或发布状态。
- 打包建议：保留跟踪，暂不列为优先打包候选；需结合实际版本和测试结果人工评估。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。
