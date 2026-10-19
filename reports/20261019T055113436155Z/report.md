# GNU RISC-V 上游更新报告

统计窗口（UTC）：2026-10-11T07:02:43Z 至 2026-10-19T05:51:13Z
生成时间（UTC）：2026-10-19T05:51:13Z

共 13 条相关更新：高 4、中 9、低 0。

优先级和打包候选由规则决定；LLM 辅助分析仅供参考，最终打包需人工评估和构建测试。
提交已合入不代表已经发布；关联 PR 的状态单独列出。

## 仓库采集状态

- RTEMS/sourceware-mirror-binutils-gdb：ok；分支 master
  采集窗口（UTC）：2026-10-11T07:02:43Z 至 2026-10-19T05:51:13Z
- gcc-mirror/gcc：ok；分支 master
  采集窗口（UTC）：2026-10-11T07:02:43Z 至 2026-10-19T05:51:13Z
- sailfishos-mirror/glibc：ok；分支 master
  采集窗口（UTC）：2026-10-11T07:02:43Z 至 2026-10-19T05:51:13Z

## 采集警告

- RTEMS/sourceware-mirror-binutils-gdb：轻量标签没有独立时间，只能用所指提交的时间代替。
- gcc-mirror/gcc：轻量标签没有独立时间，只能用所指提交的时间代替。
- 分页在第 1 页停止，元数据覆盖不完整。
- 未配置 LLM\_API\_KEY，使用规则结果。

## 高优先级

### RISC-V: Support vector initialization from two halves

- 仓库：gcc-mirror/gcc；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-10-16T13:06:58Z
- 作者：ZhongyaoChen；SHA：5dbc6f027e972f9311caa291b01d38f6ea4284af
- 来源：[原始记录](https://github.com/gcc-mirror/gcc/commit/5dbc6f027e972f9311caa291b01d38f6ea4284af)
- 规则判断：high / vector-crypto-hypervisor；打包候选：是，待人工评估
- 命中规则：functional:add、functional:adds、functional:extend、functional:implement、functional:support、keyword:vector-crypto-hypervisor:vector、path:gcc/config/riscv/autovec.md、path:gcc/config/riscv/riscv-v.cc、path:gcc/config/riscv/vector-iterators.md、path:gcc/config/riscv/vector.md、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/vec-concat-1.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/vec-concat-2.c、token:risc-v、token:riscv、token:rv64
- 涉及文件：gcc/config/riscv/autovec.md、gcc/config/riscv/riscv-v.cc、gcc/config/riscv/vector-iterators.md、gcc/config/riscv/vector.md、gcc/testsuite/gcc.target/riscv/rvv/autovec/vec-concat-1.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/vec-concat-2.c
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V 向量、密码学或虚拟化相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为高；未验证构建、运行或发布状态。
- 打包建议：建议人工核对上游状态和适用版本，并完成构建及回归测试后再决定打包。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。

### sched: Avoid creating fusion groups during selective scheduling

- 仓库：gcc-mirror/gcc；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-10-14T09:51:25Z
- 作者：majin2020；SHA：3518a4892d0dd65ca841b82519832147d626ca2e
- 来源：[原始记录](https://github.com/gcc-mirror/gcc/commit/3518a4892d0dd65ca841b82519832147d626ca2e)
- 规则判断：high / isa-extension；打包候选：是，待人工评估
- 命中规则：functional:add、functional:enabled、keyword:isa-extension:extension、path:gcc/testsuite/gcc.target/riscv/sched-fusion-selective-ice.c、path:gcc/testsuite/gcc.target/riscv/sched-fusion-selective.c、token:riscv
- 涉及文件：gcc/sched-deps.cc、gcc/testsuite/gcc.target/riscv/sched-fusion-selective-ice.c、gcc/testsuite/gcc.target/riscv/sched-fusion-selective.c
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V ISA 扩展相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为高；未验证构建、运行或发布状态。
- 打包建议：建议人工核对上游状态和适用版本，并完成构建及回归测试后再决定打包。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。

### \[RISC-V\]\[PR 127813\] Add more czero patterns/splitters for RISC-V

- 仓库：gcc-mirror/gcc；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-10-13T02:53:41Z
- 作者：JeffreyALaw；SHA：cebcce44cccc6829dd4854556c60cc6d2f59b28c
- 来源：[原始记录](https://github.com/gcc-mirror/gcc/commit/cebcce44cccc6829dd4854556c60cc6d2f59b28c)
- 规则判断：high / hardware；打包候选：是，待人工评估
- 命中规则：functional:add、keyword:hardware:k3、keyword:isa-extension:zicond、path:gcc/config/riscv/zicond.md、path:gcc/testsuite/gcc.target/riscv/pr127813.c、token:risc-v、token:riscv
- 涉及文件：gcc/config/riscv/zicond.md、gcc/testsuite/gcc.target/riscv/pr127813.c
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V 硬件支持相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为高；未验证构建、运行或发布状态。
- 打包建议：建议人工核对上游状态和适用版本，并完成构建及回归测试后再决定打包。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。

### RISC-V: Consider scalar loads/stores for LMUL ratio. \[PR127662\]

- 仓库：gcc-mirror/gcc；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-10-12T13:01:09Z
- 作者：Robin Dapp；SHA：cfa4979a2c2f91c5077bf5d1c1500518581b2627
- 来源：[原始记录](https://github.com/gcc-mirror/gcc/commit/cfa4979a2c2f91c5077bf5d1c1500518581b2627)
- 规则判断：high / vector-crypto-hypervisor；打包候选：是，待人工评估
- 命中规则：functional:add、functional:adds、keyword:vector-crypto-hypervisor:vector、path:gcc/config/riscv/riscv-vector-costs.cc、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/pr127662.c、token:risc-v、token:riscv
- 涉及文件：gcc/config/riscv/riscv-vector-costs.cc、gcc/testsuite/gcc.target/riscv/rvv/autovec/pr127662.c
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V 向量、密码学或虚拟化相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为高；未验证构建、运行或发布状态。
- 打包建议：建议人工核对上游状态和适用版本，并完成构建及回归测试后再决定打包。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。


## 中优先级

### \[RISC-V\] Fix mode goofs in RISC-V's bitmanip.md

- 仓库：gcc-mirror/gcc；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-10-18T17:45:09Z
- 作者：JeffreyALaw；SHA：c7d983e54c1dbcf7906a0f359920cb5b54aa9bba
- 来源：[原始记录](https://github.com/gcc-mirror/gcc/commit/c7d983e54c1dbcf7906a0f359920cb5b54aa9bba)
- 规则判断：medium / bugfix；打包候选：是，待人工评估
- 命中规则：keyword:bugfix:fix、keyword:hardware:k3、path:gcc/config/riscv/bitmanip.md、token:risc-v、token:riscv
- 涉及文件：gcc/config/riscv/bitmanip.md
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V 问题修复相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为中；未验证构建、运行或发布状态。
- 打包建议：建议人工核对上游状态和适用版本，并完成构建及回归测试后再决定打包。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。

### \[RISC-V\] Fix LLM identified bugs in RISC-V bitmanip.md file

- 仓库：gcc-mirror/gcc；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-10-17T16:55:19Z
- 作者：Jeff Law；SHA：4af99f0796e6bb65d4413f9d73e0f792722dd3b2
- 来源：[原始记录](https://github.com/gcc-mirror/gcc/commit/4af99f0796e6bb65d4413f9d73e0f792722dd3b2)
- 规则判断：medium / bugfix；打包候选：是，待人工评估
- 命中规则：keyword:bugfix:fix、path:gcc/config/riscv/bitmanip.md、token:risc-v、token:riscv
- 涉及文件：gcc/config/riscv/bitmanip.md
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V 问题修复相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为中；未验证构建、运行或发布状态。
- 打包建议：建议人工核对上游状态和适用版本，并完成构建及回归测试后再决定打包。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。

### \[PATCH\] rtl, aarch64, riscv: Ignore leading debug insns \[PR127934, PR127936\]

- 仓库：gcc-mirror/gcc；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-10-17T14:41:16Z
- 作者：yqtian-se；SHA：97b691c72ba88be598dfb49d5cb6546df966519c
- 来源：[原始记录](https://github.com/gcc-mirror/gcc/commit/97b691c72ba88be598dfb49d5cb6546df966519c)
- 规则判断：medium / bugfix；打包候选：是，待人工评估
- 命中规则：keyword:bugfix:regression、path:gcc/config/riscv/riscv.cc、path:gcc/testsuite/gcc.target/riscv/rvv/base/vxrm-debug-1.c、token:risc-v、token:riscv
- 涉及文件：gcc/config/arm/aarch-bti-insert.cc、gcc/config/riscv/riscv.cc、gcc/emit-rtl.cc、gcc/rtl.h、gcc/testsuite/gcc.target/aarch64/bti-debug-1.c、gcc/testsuite/gcc.target/riscv/rvv/base/vxrm-debug-1.c
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V 问题修复相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为中；未验证构建、运行或发布状态。
- 打包建议：建议人工核对上游状态和适用版本，并完成构建及回归测试后再决定打包。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。

### riscv: Avoid R\_RISCV\_JAL for \_\_sigjmp\_save

- 仓库：sailfishos-mirror/glibc；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-10-16T20:38:14Z
- 作者：renndong；SHA：0aff8d4a6651ec7090090f9be3e1c5d4a76005f5
- 来源：[原始记录](https://github.com/sailfishos-mirror/glibc/commit/0aff8d4a6651ec7090090f9be3e1c5d4a76005f5)
- 规则判断：medium / other；打包候选：否
- 命中规则：path:sysdeps/riscv/setjmp.S、token:riscv
- 涉及文件：sysdeps/riscv/setjmp.S
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V 其他变更相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为中；未验证构建、运行或发布状态。
- 打包建议：保留跟踪，暂不列为优先打包候选；需结合实际版本和测试结果人工评估。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。

### RISC-V/bfd: correct canonical extension order \(again\)

- 仓库：RTEMS/sourceware-mirror-binutils-gdb；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-10-16T07:58:29Z
- 作者：jbeulich；SHA：40b6f4be64c3945fab62f4bf986f7b59132db848
- 来源：[原始记录](https://github.com/RTEMS/sourceware-mirror-binutils-gdb/commit/40b6f4be64c3945fab62f4bf986f7b59132db848)
- 规则判断：medium / bugfix；打包候选：是，待人工评估
- 命中规则：keyword:bugfix:correct、keyword:isa-extension:extension、path:bfd/elfxx-riscv.c、path:gas/testsuite/gas/riscv/march-fail-isa-spec.d、path:gas/testsuite/gas/riscv/march-fail-isa-spec.l、token:risc-v
- 涉及文件：bfd/elfxx-riscv.c、gas/testsuite/gas/riscv/march-fail-isa-spec.d、gas/testsuite/gas/riscv/march-fail-isa-spec.l
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V 问题修复相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为中；未验证构建、运行或发布状态。
- 打包建议：建议人工核对上游状态和适用版本，并完成构建及回归测试后再决定打包。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。

### Revert "RISC-V: Add conditional negate expansion \[PR126245\]"

- 仓库：gcc-mirror/gcc；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-10-14T07:49:13Z
- 作者：naveengowda-gcc；SHA：19e4245e0d6f38cc628924119f7e953446838835
- 来源：[原始记录](https://github.com/gcc-mirror/gcc/commit/19e4245e0d6f38cc628924119f7e953446838835)
- 规则判断：medium / bugfix；打包候选：是，待人工评估
- 命中规则：keyword:bugfix:regression、path:gcc/config/riscv/riscv.md、path:gcc/testsuite/gcc.target/riscv/pr126245-negcc.c、token:risc-v、token:riscv
- 涉及文件：gcc/config/riscv/riscv.md、gcc/testsuite/gcc.target/riscv/pr126245-negcc.c
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V 问题修复相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为中；未验证构建、运行或发布状态。
- 打包建议：建议人工核对上游状态和适用版本，并完成构建及回归测试后再决定打包。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。

### RISC-V: Model ALU insn scheduling as ALU0 or ALU1 for SpacemiT-X60

- 仓库：gcc-mirror/gcc；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-10-13T13:34:12Z
- 作者：dusan-s；SHA：3a418df15825ac8ee26ca4e1405ece8558d29da9
- 来源：[原始记录](https://github.com/gcc-mirror/gcc/commit/3a418df15825ac8ee26ca4e1405ece8558d29da9)
- 规则判断：medium / hardware；打包候选：是，待人工评估
- 命中规则：keyword:compiler-option:-march、keyword:compiler-option:-mcpu、keyword:hardware:cpu、keyword:hardware:spacemit、keyword:isa-extension:zba、keyword:isa-extension:zbb、keyword:vector-crypto-hypervisor:vector、path:gcc/config/riscv/spacemit-x60.md、token:risc-v、token:riscv、token:rv64
- 涉及文件：gcc/config/riscv/spacemit-x60.md
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V 硬件支持相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为中；未验证构建、运行或发布状态。
- 打包建议：建议人工核对上游状态和适用版本，并完成构建及回归测试后再决定打包。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。

### \[RISC-V\]\[PR target/127778\] Use synthesize\_add more on RISC-V

- 仓库：gcc-mirror/gcc；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-10-13T13:17:57Z
- 作者：JeffreyALaw；SHA：8ebf07db4065afb654756ae77d397e2024fef436
- 来源：[原始记录](https://github.com/gcc-mirror/gcc/commit/8ebf07db4065afb654756ae77d397e2024fef436)
- 规则判断：medium / bugfix；打包候选：是，待人工评估
- 命中规则：keyword:bugfix:bug、path:gcc/config/riscv/riscv.cc、path:gcc/testsuite/gcc.target/riscv/pr127778.c、token:risc-v、token:riscv
- 涉及文件：gcc/config/riscv/riscv.cc、gcc/testsuite/gcc.target/riscv/pr127778.c
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V 问题修复相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为中；未验证构建、运行或发布状态。
- 打包建议：建议人工核对上游状态和适用版本，并完成构建及回归测试后再决定打包。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。

### lower-subreg: Don't decompose pre-existing concatns. \[PR127443\]

- 仓库：gcc-mirror/gcc；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-10-12T13:01:09Z
- 作者：Robin Dapp；SHA：87eeb9ed5d5932c4777f1a4358f21fec76cc420b
- 来源：[原始记录](https://github.com/gcc-mirror/gcc/commit/87eeb9ed5d5932c4777f1a4358f21fec76cc420b)
- 规则判断：medium / other；打包候选：否
- 命中规则：path:gcc/testsuite/gcc.target/riscv/rvv/autovec/pr127443.c、token:riscv
- 涉及文件：gcc/lower-subreg.cc、gcc/rtl.h、gcc/testsuite/gcc.target/riscv/rvv/autovec/pr127443.c
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V 其他变更相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为中；未验证构建、运行或发布状态。
- 打包建议：保留跟踪，暂不列为优先打包候选；需结合实际版本和测试结果人工评估。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。


## 低优先级

无。
