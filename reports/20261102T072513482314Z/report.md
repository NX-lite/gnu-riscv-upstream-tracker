# GNU RISC-V 上游更新报告

统计窗口（UTC）：2026-10-25T05:50:24Z 至 2026-11-02T07:25:13Z
生成时间（UTC）：2026-11-02T07:25:13Z

共 37 条相关更新：高 15、中 15、低 7。

优先级和打包候选由规则决定；LLM 辅助分析仅供参考，最终打包需人工评估和构建测试。
提交已合入不代表已经发布；关联 PR 的状态单独列出。

## 仓库采集状态

- RTEMS/sourceware-mirror-binutils-gdb：ok；分支 master
  采集窗口（UTC）：2026-10-25T05:50:24Z 至 2026-11-02T07:25:13Z
- gcc-mirror/gcc：ok；分支 master
  采集窗口（UTC）：2026-10-25T05:50:24Z 至 2026-11-02T07:25:13Z
- sailfishos-mirror/glibc：ok；分支 master
  采集窗口（UTC）：2026-10-25T05:50:24Z 至 2026-11-02T07:25:13Z

## 采集警告

- RTEMS/sourceware-mirror-binutils-gdb：轻量标签没有独立时间，只能用所指提交的时间代替。
- gcc-mirror/gcc：轻量标签没有独立时间，只能用所指提交的时间代替。
- 分页在第 1 页停止，元数据覆盖不完整。
- 未配置 LLM\_API\_KEY，使用规则结果。

## 高优先级

### \[RISC-V\]\[PR target/128139\] Don't create pseudos when !can\_create\_pseudos\_p on RISC-V

- 仓库：gcc-mirror/gcc；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-11-01T22:30:12Z
- 作者：JeffreyALaw；SHA：5acdceb6e77753e54c3de1c7d3a73bf3d457ca85
- 来源：[原始记录](https://github.com/gcc-mirror/gcc/commit/5acdceb6e77753e54c3de1c7d3a73bf3d457ca85)
- 规则判断：high / hardware；打包候选：是，待人工评估
- 命中规则：functional:add、functional:added、functional:improve、keyword:hardware:k3、path:gcc/config/riscv/riscv.cc、path:gcc/testsuite/gcc.target/riscv/pr128139.c、token:risc-v、token:riscv
- 涉及文件：gcc/config/riscv/riscv.cc、gcc/testsuite/gcc.target/riscv/pr128139.c
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V 硬件支持相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为高；未验证构建、运行或发布状态。
- 打包建议：建议人工核对上游状态和适用版本，并完成构建及回归测试后再决定打包。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。

### RISC-V: Add usad patterns.

- 仓库：gcc-mirror/gcc；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-10-30T15:57:35Z
- 作者：Robin Dapp；SHA：cf3eaa0ee525be8ad51bb4cb2e3eea94e9944932
- 来源：[原始记录](https://github.com/gcc-mirror/gcc/commit/cf3eaa0ee525be8ad51bb4cb2e3eea94e9944932)
- 规则判断：high / vector-crypto-hypervisor；打包候选：是，待人工评估
- 命中规则：functional:add、functional:adds、functional:supports、keyword:vector-crypto-hypervisor:vector、path:gcc/config/riscv/autovec.md、path:gcc/config/riscv/vector-iterators.md、token:risc-v、token:riscv
- 涉及文件：gcc/config/riscv/autovec.md、gcc/config/riscv/vector-iterators.md、gcc/testsuite/lib/target-supports.exp
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V 向量、密码学或虚拟化相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为高；未验证构建、运行或发布状态。
- 打包建议：建议人工核对上游状态和适用版本，并完成构建及回归测试后再决定打包。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。

### RISC-V: ".option arch" with unimplemented extensions

- 仓库：RTEMS/sourceware-mirror-binutils-gdb；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-10-30T07:20:57Z
- 作者：jbeulich；SHA：29747f68fb1f1214a43cf406a3a4323c79421416
- 来源：[原始记录](https://github.com/RTEMS/sourceware-mirror-binutils-gdb/commit/29747f68fb1f1214a43cf406a3a4323c79421416)
- 规则判断：high / compiler-option；打包候选：是，待人工评估
- 命中规则：functional:add、keyword:compiler-option:option、path:bfd/elfxx-riscv.c、path:gas/testsuite/gas/riscv/option-arch-fail.l、path:gas/testsuite/gas/riscv/option-arch-fail.s、token:risc-v、token:riscv、token:rv32
- 涉及文件：bfd/elfxx-riscv.c、gas/testsuite/gas/riscv/option-arch-fail.l、gas/testsuite/gas/riscv/option-arch-fail.s
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V 编译选项相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为高；未验证构建、运行或发布状态。
- 打包建议：建议人工核对上游状态和适用版本，并完成构建及回归测试后再决定打包。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。

### RISC-V: Disable RVV register overlap for vwabda\[u\].vv \[PR target/128162\]

- 仓库：gcc-mirror/gcc；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-10-30T00:56:44Z
- 作者：Incarnation-p-lee；SHA：9d6e9f2318ae218e9eb0371bfc89b8164b73473e
- 来源：[原始记录](https://github.com/gcc-mirror/gcc/commit/9d6e9f2318ae218e9eb0371bfc89b8164b73473e)
- 规则判断：high / vector-crypto-hypervisor；打包候选：是，待人工评估
- 命中规则：functional:add、keyword:vector-crypto-hypervisor:vector、path:gcc/config/riscv/vector.md、token:risc-v、token:riscv
- 涉及文件：gcc/config/riscv/vector.md
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V 向量、密码学或虚拟化相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为高；未验证构建、运行或发布状态。
- 打包建议：建议人工核对上游状态和适用版本，并完成构建及回归测试后再决定打包。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。

### RISC-V: Disable RVV register overlap for vwmacc\[u\].vv \[PR target/128162\]

- 仓库：gcc-mirror/gcc；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-10-28T23:18:24Z
- 作者：Incarnation-p-lee；SHA：b20dc9dbc78c52cde85c20cdca0b04e1125a6643
- 来源：[原始记录](https://github.com/gcc-mirror/gcc/commit/b20dc9dbc78c52cde85c20cdca0b04e1125a6643)
- 规则判断：high / vector-crypto-hypervisor；打包候选：是，待人工评估
- 命中规则：functional:add、keyword:vector-crypto-hypervisor:vector、path:gcc/config/riscv/vector.md、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/group\_overlap.h、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmacc\_vv-i16-m1.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmacc\_vv-i16-m2.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmacc\_vv-i16-m4.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmacc\_vv-i16-mf2.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmacc\_vv-i16-mf4.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmacc\_vv-i32-m1.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmacc\_vv-i32-m2.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmacc\_vv-i32-m4.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmacc\_vv-i32-mf2.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmacc\_vv-i8-m1.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmacc\_vv-i8-m2.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmacc\_vv-i8-m4.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmacc\_vv-i8-mf2.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmacc\_vv-i8-mf4.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmacc\_vv-i8-mf8.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccu\_vv-u16-m1.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccu\_vv-u16-m2.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccu\_vv-u16-m4.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccu\_vv-u16-mf2.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccu\_vv-u16-mf4.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccu\_vv-u32-m1.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccu\_vv-u32-m2.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccu\_vv-u32-m4.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccu\_vv-u32-mf2.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccu\_vv-u8-m1.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccu\_vv-u8-m2.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccu\_vv-u8-m4.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccu\_vv-u8-mf2.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccu\_vv-u8-mf4.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccu\_vv-u8-mf8.c、path:gcc/testsuite/gcc.target/riscv/rvv/base/pr112431-49.c、path:gcc/testsuite/gcc.target/riscv/rvv/base/pr112431-50.c、token:risc-v、token:riscv
- 涉及文件：gcc/config/riscv/vector.md、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/group\_overlap.h、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmacc\_vv-i16-m1.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmacc\_vv-i16-m2.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmacc\_vv-i16-m4.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmacc\_vv-i16-mf2.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmacc\_vv-i16-mf4.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmacc\_vv-i32-m1.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmacc\_vv-i32-m2.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmacc\_vv-i32-m4.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmacc\_vv-i32-mf2.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmacc\_vv-i8-m1.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmacc\_vv-i8-m2.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmacc\_vv-i8-m4.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmacc\_vv-i8-mf2.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmacc\_vv-i8-mf4.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmacc\_vv-i8-mf8.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccu\_vv-u16-m1.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccu\_vv-u16-m2.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccu\_vv-u16-m4.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccu\_vv-u16-mf2.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccu\_vv-u16-mf4.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccu\_vv-u32-m1.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccu\_vv-u32-m2.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccu\_vv-u32-m4.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccu\_vv-u32-mf2.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccu\_vv-u8-m1.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccu\_vv-u8-m2.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccu\_vv-u8-m4.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccu\_vv-u8-mf2.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccu\_vv-u8-mf4.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccu\_vv-u8-mf8.c、gcc/testsuite/gcc.target/riscv/rvv/base/pr112431-49.c、gcc/testsuite/gcc.target/riscv/rvv/base/pr112431-50.c
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V 向量、密码学或虚拟化相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为高；未验证构建、运行或发布状态。
- 打包建议：建议人工核对上游状态和适用版本，并完成构建及回归测试后再决定打包。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。

### RISC-V: Disable RVV register overlap for vwmaccsu.vv \[PR target/128162\]

- 仓库：gcc-mirror/gcc；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-10-28T23:18:23Z
- 作者：Incarnation-p-lee；SHA：0c57e34aee5525f19a60e1b90db58d202bc341d1
- 来源：[原始记录](https://github.com/gcc-mirror/gcc/commit/0c57e34aee5525f19a60e1b90db58d202bc341d1)
- 规则判断：high / vector-crypto-hypervisor；打包候选：是，待人工评估
- 命中规则：functional:add、keyword:vector-crypto-hypervisor:vector、path:gcc/config/riscv/vector.md、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/group\_overlap.h、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccsu\_vv-i16-m1.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccsu\_vv-i16-m2.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccsu\_vv-i16-m4.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccsu\_vv-i16-mf2.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccsu\_vv-i16-mf4.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccsu\_vv-i32-m1.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccsu\_vv-i32-m2.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccsu\_vv-i32-m4.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccsu\_vv-i32-mf2.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccsu\_vv-i8-m1.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccsu\_vv-i8-m2.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccsu\_vv-i8-m4.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccsu\_vv-i8-mf2.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccsu\_vv-i8-mf4.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccsu\_vv-i8-mf8.c、path:gcc/testsuite/gcc.target/riscv/rvv/base/pr112431-51.c、token:risc-v、token:riscv
- 涉及文件：gcc/config/riscv/vector.md、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/group\_overlap.h、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccsu\_vv-i16-m1.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccsu\_vv-i16-m2.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccsu\_vv-i16-m4.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccsu\_vv-i16-mf2.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccsu\_vv-i16-mf4.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccsu\_vv-i32-m1.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccsu\_vv-i32-m2.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccsu\_vv-i32-m4.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccsu\_vv-i32-mf2.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccsu\_vv-i8-m1.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccsu\_vv-i8-m2.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccsu\_vv-i8-m4.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccsu\_vv-i8-mf2.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccsu\_vv-i8-mf4.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccsu\_vv-i8-mf8.c、gcc/testsuite/gcc.target/riscv/rvv/base/pr112431-51.c
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V 向量、密码学或虚拟化相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为高；未验证构建、运行或发布状态。
- 打包建议：建议人工核对上游状态和适用版本，并完成构建及回归测试后再决定打包。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。

### RISC-V: Disable RVV register overlap for vfw{macc,msac}.vv \[PR target/128162\]

- 仓库：gcc-mirror/gcc；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-10-28T23:18:23Z
- 作者：Incarnation-p-lee；SHA：62e0fe6ce26047129244e7a1c5f0fb829f67a309
- 来源：[原始记录](https://github.com/gcc-mirror/gcc/commit/62e0fe6ce26047129244e7a1c5f0fb829f67a309)
- 规则判断：high / vector-crypto-hypervisor；打包候选：是，待人工评估
- 命中规则：functional:add、keyword:vector-crypto-hypervisor:vector、path:gcc/config/riscv/vector.md、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwmacc\_vv-f16-m1.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwmacc\_vv-f16-m2.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwmacc\_vv-f16-m4.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwmacc\_vv-f16-mf2.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwmacc\_vv-f16-mf4.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwmacc\_vv-f32-m1.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwmacc\_vv-f32-m2.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwmacc\_vv-f32-m4.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwmacc\_vv-f32-mf2.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwmsac\_vv-f16-m1.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwmsac\_vv-f16-m2.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwmsac\_vv-f16-m4.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwmsac\_vv-f16-mf2.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwmsac\_vv-f16-mf4.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwmsac\_vv-f32-m1.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwmsac\_vv-f32-m2.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwmsac\_vv-f32-m4.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwmsac\_vv-f32-mf2.c、path:gcc/testsuite/gcc.target/riscv/rvv/base/pr112431-61.c、path:gcc/testsuite/gcc.target/riscv/rvv/base/pr112431-62.c、token:risc-v、token:riscv
- 涉及文件：gcc/config/riscv/vector.md、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwmacc\_vv-f16-m1.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwmacc\_vv-f16-m2.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwmacc\_vv-f16-m4.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwmacc\_vv-f16-mf2.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwmacc\_vv-f16-mf4.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwmacc\_vv-f32-m1.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwmacc\_vv-f32-m2.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwmacc\_vv-f32-m4.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwmacc\_vv-f32-mf2.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwmsac\_vv-f16-m1.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwmsac\_vv-f16-m2.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwmsac\_vv-f16-m4.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwmsac\_vv-f16-mf2.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwmsac\_vv-f16-mf4.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwmsac\_vv-f32-m1.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwmsac\_vv-f32-m2.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwmsac\_vv-f32-m4.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwmsac\_vv-f32-mf2.c、gcc/testsuite/gcc.target/riscv/rvv/base/pr112431-61.c、gcc/testsuite/gcc.target/riscv/rvv/base/pr112431-62.c
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V 向量、密码学或虚拟化相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为高；未验证构建、运行或发布状态。
- 打包建议：建议人工核对上游状态和适用版本，并完成构建及回归测试后再决定打包。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。

### RISC-V: Disable RVV register overlap for vwmaccus.vx \[PR target/128162\]

- 仓库：gcc-mirror/gcc；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-10-28T23:18:23Z
- 作者：Incarnation-p-lee；SHA：a890119da9c92bae6d87b7fff77a60f3b33835fb
- 来源：[原始记录](https://github.com/gcc-mirror/gcc/commit/a890119da9c92bae6d87b7fff77a60f3b33835fb)
- 规则判断：high / vector-crypto-hypervisor；打包候选：是，待人工评估
- 命中规则：functional:add、keyword:vector-crypto-hypervisor:vector、path:gcc/config/riscv/vector.md、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccus\_vx-i16-m1.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccus\_vx-i16-m2.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccus\_vx-i16-m4.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccus\_vx-i16-mf2.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccus\_vx-i16-mf4.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccus\_vx-i32-m1.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccus\_vx-i32-m2.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccus\_vx-i32-m4.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccus\_vx-i32-mf2.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccus\_vx-i8-m1.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccus\_vx-i8-m2.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccus\_vx-i8-m4.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccus\_vx-i8-mf2.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccus\_vx-i8-mf4.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccus\_vx-i8-mf8.c、path:gcc/testsuite/gcc.target/riscv/rvv/base/pr112431-37.c、path:gcc/testsuite/gcc.target/riscv/rvv/base/pr112431-57.c、path:gcc/testsuite/gcc.target/riscv/rvv/base/pr112431-58.c、token:risc-v、token:riscv
- 涉及文件：gcc/config/riscv/vector.md、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccus\_vx-i16-m1.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccus\_vx-i16-m2.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccus\_vx-i16-m4.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccus\_vx-i16-mf2.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccus\_vx-i16-mf4.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccus\_vx-i32-m1.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccus\_vx-i32-m2.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccus\_vx-i32-m4.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccus\_vx-i32-mf2.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccus\_vx-i8-m1.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccus\_vx-i8-m2.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccus\_vx-i8-m4.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccus\_vx-i8-mf2.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccus\_vx-i8-mf4.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccus\_vx-i8-mf8.c、gcc/testsuite/gcc.target/riscv/rvv/base/pr112431-37.c、gcc/testsuite/gcc.target/riscv/rvv/base/pr112431-57.c、gcc/testsuite/gcc.target/riscv/rvv/base/pr112431-58.c
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V 向量、密码学或虚拟化相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为高；未验证构建、运行或发布状态。
- 打包建议：建议人工核对上游状态和适用版本，并完成构建及回归测试后再决定打包。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。

### RISC-V: Disable RVV register overlap for vwmaccu.vx undef \[PR target/128162\]

- 仓库：gcc-mirror/gcc；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-10-28T23:18:23Z
- 作者：Incarnation-p-lee；SHA：a8f38d8ca0185580d7c0944809e16e6ba5d0e8c8
- 来源：[原始记录](https://github.com/gcc-mirror/gcc/commit/a8f38d8ca0185580d7c0944809e16e6ba5d0e8c8)
- 规则判断：high / vector-crypto-hypervisor；打包候选：是，待人工评估
- 命中规则：functional:add、keyword:vector-crypto-hypervisor:vector、path:gcc/config/riscv/vector.md、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccu\_vx\_undef-u16-m1.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccu\_vx\_undef-u16-m2.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccu\_vx\_undef-u16-m4.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccu\_vx\_undef-u16-mf2.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccu\_vx\_undef-u16-mf4.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccu\_vx\_undef-u32-m1.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccu\_vx\_undef-u32-m2.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccu\_vx\_undef-u32-m4.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccu\_vx\_undef-u32-mf2.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccu\_vx\_undef-u8-m1.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccu\_vx\_undef-u8-m2.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccu\_vx\_undef-u8-m4.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccu\_vx\_undef-u8-mf2.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccu\_vx\_undef-u8-mf4.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccu\_vx\_undef-u8-mf8.c、path:gcc/testsuite/gcc.target/riscv/rvv/base/pr112431-59.c、token:risc-v、token:riscv
- 涉及文件：gcc/config/riscv/vector.md、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccu\_vx\_undef-u16-m1.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccu\_vx\_undef-u16-m2.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccu\_vx\_undef-u16-m4.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccu\_vx\_undef-u16-mf2.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccu\_vx\_undef-u16-mf4.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccu\_vx\_undef-u32-m1.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccu\_vx\_undef-u32-m2.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccu\_vx\_undef-u32-m4.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccu\_vx\_undef-u32-mf2.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccu\_vx\_undef-u8-m1.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccu\_vx\_undef-u8-m2.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccu\_vx\_undef-u8-m4.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccu\_vx\_undef-u8-mf2.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccu\_vx\_undef-u8-mf4.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccu\_vx\_undef-u8-mf8.c、gcc/testsuite/gcc.target/riscv/rvv/base/pr112431-59.c
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V 向量、密码学或虚拟化相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为高；未验证构建、运行或发布状态。
- 打包建议：建议人工核对上游状态和适用版本，并完成构建及回归测试后再决定打包。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。

### RISC-V: Disable RVV register overlap for vwmaccsu.vx \[PR target/128162\]

- 仓库：gcc-mirror/gcc；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-10-28T23:18:23Z
- 作者：Incarnation-p-lee；SHA：c3c3977e691a99d0e86d6059d7a4d583f77f89cc
- 来源：[原始记录](https://github.com/gcc-mirror/gcc/commit/c3c3977e691a99d0e86d6059d7a4d583f77f89cc)
- 规则判断：high / vector-crypto-hypervisor；打包候选：是，待人工评估
- 命中规则：functional:add、keyword:vector-crypto-hypervisor:vector、path:gcc/config/riscv/vector.md、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/group\_overlap.h、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccsu\_vx-i16-m1.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccsu\_vx-i16-m2.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccsu\_vx-i16-m4.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccsu\_vx-i16-mf2.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccsu\_vx-i16-mf4.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccsu\_vx-i32-m1.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccsu\_vx-i32-m2.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccsu\_vx-i32-m4.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccsu\_vx-i32-mf2.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccsu\_vx-i8-m1.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccsu\_vx-i8-m2.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccsu\_vx-i8-m4.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccsu\_vx-i8-mf2.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccsu\_vx-i8-mf4.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccsu\_vx-i8-mf8.c、path:gcc/testsuite/gcc.target/riscv/rvv/base/pr112431-55.c、path:gcc/testsuite/gcc.target/riscv/rvv/base/pr112431-56.c、token:risc-v、token:riscv
- 涉及文件：gcc/config/riscv/vector.md、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/group\_overlap.h、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccsu\_vx-i16-m1.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccsu\_vx-i16-m2.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccsu\_vx-i16-m4.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccsu\_vx-i16-mf2.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccsu\_vx-i16-mf4.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccsu\_vx-i32-m1.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccsu\_vx-i32-m2.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccsu\_vx-i32-m4.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccsu\_vx-i32-mf2.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccsu\_vx-i8-m1.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccsu\_vx-i8-m2.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccsu\_vx-i8-m4.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccsu\_vx-i8-mf2.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccsu\_vx-i8-mf4.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccsu\_vx-i8-mf8.c、gcc/testsuite/gcc.target/riscv/rvv/base/pr112431-55.c、gcc/testsuite/gcc.target/riscv/rvv/base/pr112431-56.c
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V 向量、密码学或虚拟化相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为高；未验证构建、运行或发布状态。
- 打包建议：建议人工核对上游状态和适用版本，并完成构建及回归测试后再决定打包。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。

### RISC-V: Disable RVV register overlap for vwmacc\[u\].vx \[PR target/128162\]

- 仓库：gcc-mirror/gcc；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-10-28T23:18:23Z
- 作者：Incarnation-p-lee；SHA：f304860a0dc0c3c5b46afeea96ecf0af5ea17e0e
- 来源：[原始记录](https://github.com/gcc-mirror/gcc/commit/f304860a0dc0c3c5b46afeea96ecf0af5ea17e0e)
- 规则判断：high / vector-crypto-hypervisor；打包候选：是，待人工评估
- 命中规则：functional:add、keyword:vector-crypto-hypervisor:vector、path:gcc/config/riscv/vector.md、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/group\_overlap.h、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmacc\_vx-i16-m1.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmacc\_vx-i16-m2.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmacc\_vx-i16-m4.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmacc\_vx-i16-mf2.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmacc\_vx-i16-mf4.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmacc\_vx-i32-m1.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmacc\_vx-i32-m2.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmacc\_vx-i32-m4.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmacc\_vx-i32-mf2.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmacc\_vx-i8-m1.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmacc\_vx-i8-m2.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmacc\_vx-i8-m4.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmacc\_vx-i8-mf2.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmacc\_vx-i8-mf4.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmacc\_vx-i8-mf8.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccu\_vx-u16-m1.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccu\_vx-u16-m2.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccu\_vx-u16-m4.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccu\_vx-u16-mf2.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccu\_vx-u16-mf4.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccu\_vx-u32-m1.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccu\_vx-u32-m2.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccu\_vx-u32-m4.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccu\_vx-u32-mf2.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccu\_vx-u8-m1.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccu\_vx-u8-m2.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccu\_vx-u8-m4.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccu\_vx-u8-mf2.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccu\_vx-u8-mf4.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccu\_vx-u8-mf8.c、path:gcc/testsuite/gcc.target/riscv/rvv/base/pr112431-53.c、path:gcc/testsuite/gcc.target/riscv/rvv/base/pr112431-54.c、token:risc-v、token:riscv
- 涉及文件：gcc/config/riscv/vector.md、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/group\_overlap.h、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmacc\_vx-i16-m1.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmacc\_vx-i16-m2.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmacc\_vx-i16-m4.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmacc\_vx-i16-mf2.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmacc\_vx-i16-mf4.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmacc\_vx-i32-m1.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmacc\_vx-i32-m2.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmacc\_vx-i32-m4.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmacc\_vx-i32-mf2.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmacc\_vx-i8-m1.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmacc\_vx-i8-m2.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmacc\_vx-i8-m4.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmacc\_vx-i8-mf2.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmacc\_vx-i8-mf4.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmacc\_vx-i8-mf8.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccu\_vx-u16-m1.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccu\_vx-u16-m2.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccu\_vx-u16-m4.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccu\_vx-u16-mf2.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccu\_vx-u16-mf4.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccu\_vx-u32-m1.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccu\_vx-u32-m2.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccu\_vx-u32-m4.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccu\_vx-u32-mf2.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccu\_vx-u8-m1.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccu\_vx-u8-m2.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccu\_vx-u8-m4.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccu\_vx-u8-mf2.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccu\_vx-u8-mf4.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccu\_vx-u8-mf8.c、gcc/testsuite/gcc.target/riscv/rvv/base/pr112431-53.c、gcc/testsuite/gcc.target/riscv/rvv/base/pr112431-54.c
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V 向量、密码学或虚拟化相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为高；未验证构建、运行或发布状态。
- 打包建议：建议人工核对上游状态和适用版本，并完成构建及回归测试后再决定打包。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。

### RISC-V: Add support for xxtvarith

- 仓库：gcc-mirror/gcc；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-10-28T16:17:13Z
- 作者：garthlei；SHA：4de866e5f4c9c626c0d725c3d7bc4c7071565122
- 来源：[原始记录](https://github.com/gcc-mirror/gcc/commit/4de866e5f4c9c626c0d725c3d7bc4c7071565122)
- 规则判断：high / hardware；打包候选：是，待人工评估
- 命中规则：functional:add、functional:adds、functional:support、functional:supports、keyword:compiler-option:options、keyword:hardware:spacemit、keyword:isa-extension:extension、keyword:isa-extension:zabha、keyword:isa-extension:zacas、keyword:isa-extension:zfh、keyword:isa-extension:zvzip、keyword:vector-crypto-hypervisor:vector、keyword:vector-crypto-hypervisor:vectorization、path:gcc/config/riscv/andes-23-series.md、path:gcc/config/riscv/andes-25-series.md、path:gcc/config/riscv/andes-45-series.md、path:gcc/config/riscv/arcv-rhx100.md、path:gcc/config/riscv/arcv-rmx100.md、path:gcc/config/riscv/generic-vector-ooo.md、path:gcc/config/riscv/mips-p8700.md、path:gcc/config/riscv/riscv-avlprop.cc、path:gcc/config/riscv/riscv-cores.def、path:gcc/config/riscv/riscv-ext-xuantie.def、path:gcc/config/riscv/riscv-ext.def、path:gcc/config/riscv/riscv-ext.opt、path:gcc/config/riscv/riscv-v.cc、path:gcc/config/riscv/riscv-vector-builtins-types.def、path:gcc/config/riscv/riscv-vector-builtins.cc、path:gcc/config/riscv/riscv-vector-builtins.h、path:gcc/config/riscv/riscv.md、path:gcc/config/riscv/sifive-7.md、path:gcc/config/riscv/sifive-p400.md、path:gcc/config/riscv/sifive-p600.md、path:gcc/config/riscv/spacemit-x60.md、path:gcc/config/riscv/t-riscv、path:gcc/config/riscv/tt-ascalon-d8.md、path:gcc/config/riscv/vector.md、path:gcc/config/riscv/xiangshan.md、path:gcc/config/riscv/xt-c908.md、path:gcc/config/riscv/xuantie-vector-builtins-bases.cc、path:gcc/config/riscv/xuantie-vector-builtins-bases.h、path:gcc/config/riscv/xuantie-vector-builtins-functions.def、path:gcc/config/riscv/xuantie-vector.md、path:gcc/config/riscv/xuantie\_vector.h、path:gcc/doc/riscv-ext.texi、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/vls-vlmax/shuffle-interleave-evenodd-run.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/vls-vlmax/shuffle-interleave-evenodd-xxtvarith-run.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/vls-vlmax/shuffle-interleave-evenodd-xxtvarith.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/vls-vlmax/shuffle-interleave-evenodd.c、path:gcc/testsuite/gcc.target/riscv/rvv/base/intrinsic-detection.c、path:gcc/testsuite/gcc.target/riscv/rvv/rvv.exp、path:gcc/testsuite/gcc.target/riscv/rvv/xxtvector/xuantie\_vector.h、path:gcc/testsuite/gcc.target/riscv/rvv/xxtvector/xxtvarith\_vcrcfoldn\_vv\_non\_overloaded.c、path:gcc/testsuite/gcc.target/riscv/rvv/xxtvector/xxtvarith\_vcrcfoldn\_vv\_overloaded.c、path:gcc/testsuite/gcc.target/riscv/rvv/xxtvector/xxtvarith\_vcrcfoldr\_vv\_non\_overloaded.c、path:gcc/testsuite/gcc.target/riscv/rvv/xxtvector/xxtvarith\_vcrcfoldr\_vv\_overloaded.c、path:gcc/testsuite/gcc.target/riscv/rvv/xxtvector/xxtvarith\_vgmulxor\_vv\_non\_overloaded.c、path:gcc/testsuite/gcc.target/riscv/rvv/xxtvector/xxtvarith\_vgmulxor\_vv\_overloaded.c、path:gcc/testsuite/gcc.target/riscv/rvv/xxtvector/xxtvarith\_vile\_vv\_non\_overloaded.c、path:gcc/testsuite/gcc.target/riscv/rvv/xxtvector/xxtvarith\_vile\_vv\_overloaded.c、path:gcc/testsuite/gcc.target/riscv/rvv/xxtvector/xxtvarith\_vilo\_vv\_non\_overloaded.c、path:gcc/testsuite/gcc.target/riscv/rvv/xxtvector/xxtvarith\_vilo\_vv\_overloaded.c、token:risc-v、token:riscv、token:rv32、token:rv64
- 涉及文件：gcc/config.gcc、gcc/config/riscv/andes-23-series.md、gcc/config/riscv/andes-25-series.md、gcc/config/riscv/andes-45-series.md、gcc/config/riscv/arcv-rhx100.md、gcc/config/riscv/arcv-rmx100.md、gcc/config/riscv/generic-vector-ooo.md、gcc/config/riscv/mips-p8700.md、gcc/config/riscv/riscv-avlprop.cc、gcc/config/riscv/riscv-cores.def、gcc/config/riscv/riscv-ext-xuantie.def、gcc/config/riscv/riscv-ext.def、gcc/config/riscv/riscv-ext.opt、gcc/config/riscv/riscv-v.cc、gcc/config/riscv/riscv-vector-builtins-types.def、gcc/config/riscv/riscv-vector-builtins.cc、gcc/config/riscv/riscv-vector-builtins.h、gcc/config/riscv/riscv.md、gcc/config/riscv/sifive-7.md、gcc/config/riscv/sifive-p400.md、gcc/config/riscv/sifive-p600.md、gcc/config/riscv/spacemit-x60.md、gcc/config/riscv/t-riscv、gcc/config/riscv/tt-ascalon-d8.md、gcc/config/riscv/vector.md、gcc/config/riscv/xiangshan.md、gcc/config/riscv/xt-c908.md、gcc/config/riscv/xuantie-vector-builtins-bases.cc、gcc/config/riscv/xuantie-vector-builtins-bases.h、gcc/config/riscv/xuantie-vector-builtins-functions.def、gcc/config/riscv/xuantie-vector.md、gcc/config/riscv/xuantie\_vector.h、gcc/doc/riscv-ext.texi、gcc/testsuite/gcc.target/riscv/rvv/autovec/vls-vlmax/shuffle-interleave-evenodd-run.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/vls-vlmax/shuffle-interleave-evenodd-xxtvarith-run.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/vls-vlmax/shuffle-interleave-evenodd-xxtvarith.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/vls-vlmax/shuffle-interleave-evenodd.c、gcc/testsuite/gcc.target/riscv/rvv/base/intrinsic-detection.c、gcc/testsuite/gcc.target/riscv/rvv/rvv.exp、gcc/testsuite/gcc.target/riscv/rvv/xxtvector/xuantie\_vector.h、gcc/testsuite/gcc.target/riscv/rvv/xxtvector/xxtvarith\_vcrcfoldn\_vv\_non\_overloaded.c、gcc/testsuite/gcc.target/riscv/rvv/xxtvector/xxtvarith\_vcrcfoldn\_vv\_overloaded.c、gcc/testsuite/gcc.target/riscv/rvv/xxtvector/xxtvarith\_vcrcfoldr\_vv\_non\_overloaded.c、gcc/testsuite/gcc.target/riscv/rvv/xxtvector/xxtvarith\_vcrcfoldr\_vv\_overloaded.c、gcc/testsuite/gcc.target/riscv/rvv/xxtvector/xxtvarith\_vgmulxor\_vv\_non\_overloaded.c、gcc/testsuite/gcc.target/riscv/rvv/xxtvector/xxtvarith\_vgmulxor\_vv\_overloaded.c、gcc/testsuite/gcc.target/riscv/rvv/xxtvector/xxtvarith\_vile\_vv\_non\_overloaded.c、gcc/testsuite/gcc.target/riscv/rvv/xxtvector/xxtvarith\_vile\_vv\_overloaded.c、gcc/testsuite/gcc.target/riscv/rvv/xxtvector/xxtvarith\_vilo\_vv\_non\_overloaded.c、gcc/testsuite/gcc.target/riscv/rvv/xxtvector/xxtvarith\_vilo\_vv\_overloaded.c、gcc/testsuite/lib/target-supports.exp
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V 硬件支持相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为高；未验证构建、运行或发布状态。
- 打包建议：建议人工核对上游状态和适用版本，并完成构建及回归测试后再决定打包。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。

### \[PATCH 2/3\] RISC-V: Eliminate redundant masks on Zbs bclr indices

- 仓库：gcc-mirror/gcc；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-10-27T15:09:05Z
- 作者：pz9115；SHA：282087fbab2d230a103c844316ac9c48db4e3b94
- 来源：[原始记录](https://github.com/gcc-mirror/gcc/commit/282087fbab2d230a103c844316ac9c48db4e3b94)
- 规则判断：high / compiler-option；打包候选：是，待人工评估
- 命中规则：functional:add、keyword:compiler-option:options、path:gcc/config/riscv/bitmanip.md、path:gcc/testsuite/gcc.target/riscv/zbs-bclr.c、token:risc-v、token:riscv、token:rv32、token:rv64
- 涉及文件：gcc/config/riscv/bitmanip.md、gcc/testsuite/gcc.target/riscv/zbs-bclr.c
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V 编译选项相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为高；未验证构建、运行或发布状态。
- 打包建议：建议人工核对上游状态和适用版本，并完成构建及回归测试后再决定打包。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。

### \[PATCH 1/3\] RISC-V: Combine Zba shift-add with word division and remainder

- 仓库：gcc-mirror/gcc；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-10-27T15:08:06Z
- 作者：pz9115；SHA：cfbc8c48ae78c69401e8bc70d80eacbea8b47ec5
- 来源：[原始记录](https://github.com/gcc-mirror/gcc/commit/cfbc8c48ae78c69401e8bc70d80eacbea8b47ec5)
- 规则判断：high / isa-extension；打包候选：是，待人工评估
- 命中规则：functional:add、functional:extend、keyword:isa-extension:zba、path:gcc/config/riscv/bitmanip.md、path:gcc/testsuite/gcc.target/riscv/zba-shNadd-05.c、path:gcc/testsuite/gcc.target/riscv/zba-shNadd-12.c、token:risc-v、token:riscv
- 涉及文件：gcc/config/riscv/bitmanip.md、gcc/testsuite/gcc.target/riscv/zba-shNadd-05.c、gcc/testsuite/gcc.target/riscv/zba-shNadd-12.c
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V ISA 扩展相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为高；未验证构建、运行或发布状态。
- 打包建议：建议人工核对上游状态和适用版本，并完成构建及回归测试后再决定打包。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。

### RISC-V: add an "arch=" disassembler option

- 仓库：RTEMS/sourceware-mirror-binutils-gdb；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-10-27T13:57:48Z
- 作者：fkhaidari；SHA：6f52aa942cb016131d6ebc1895b9d32fe395f697
- 来源：[原始记录](https://github.com/RTEMS/sourceware-mirror-binutils-gdb/commit/6f52aa942cb016131d6ebc1895b9d32fe395f697)
- 规则判断：high / compiler-option；打包候选：是，待人工评估
- 命中规则：functional:add、keyword:compiler-option:option、path:gas/testsuite/gas/riscv/dis-arch-option-mapping.d、path:gas/testsuite/gas/riscv/dis-arch-option.d、path:gas/testsuite/gas/riscv/dis-arch-option.s、path:opcodes/riscv-dis.c、token:risc-v、token:rv64
- 涉及文件：binutils/NEWS、binutils/doc/binutils.texi、gas/testsuite/gas/riscv/dis-arch-option-mapping.d、gas/testsuite/gas/riscv/dis-arch-option.d、gas/testsuite/gas/riscv/dis-arch-option.s、opcodes/riscv-dis.c
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V 编译选项相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为高；未验证构建、运行或发布状态。
- 打包建议：建议人工核对上游状态和适用版本，并完成构建及回归测试后再决定打包。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。


## 中优先级

### \[PATCH\] RISC-V: Keep whole-word tails in block-move group

- 仓库：gcc-mirror/gcc；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-11-01T22:21:07Z
- 作者：e0001533；SHA：a7a46d303ca5a4f5b4862bbbfd89a8751eadf69a
- 来源：[原始记录](https://github.com/gcc-mirror/gcc/commit/a7a46d303ca5a4f5b4862bbbfd89a8751eadf69a)
- 规则判断：medium / other；打包候选：否
- 命中规则：path:gcc/config/riscv/riscv-string.cc、path:gcc/testsuite/gcc.target/riscv/cpymem-dse-1.c、token:risc-v、token:riscv、token:rv32、token:rv64
- 涉及文件：gcc/config/riscv/riscv-string.cc、gcc/testsuite/gcc.target/riscv/cpymem-dse-1.c
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V 其他变更相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为中；未验证构建、运行或发布状态。
- 打包建议：保留跟踪，暂不列为优先打包候选；需结合实际版本和测试结果人工评估。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。

### \[RISC-V\]\[PR target/127908\] Properly recognize additional UNSPECs that may trap for RISC-v

- 仓库：gcc-mirror/gcc；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-11-01T17:21:24Z
- 作者：JeffreyALaw；SHA：02018d606e8ae483cdf2f5ea3f222fc582ce3090
- 来源：[原始记录](https://github.com/gcc-mirror/gcc/commit/02018d606e8ae483cdf2f5ea3f222fc582ce3090)
- 规则判断：medium / hardware；打包候选：是，待人工评估
- 命中规则：keyword:hardware:k3、path:gcc/config/riscv/riscv.cc、path:gcc/testsuite/gcc.target/riscv/pr127908.c、token:risc-v、token:riscv
- 涉及文件：gcc/config/riscv/riscv.cc、gcc/testsuite/gcc.target/riscv/pr127908.c
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V 硬件支持相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为中；未验证构建、运行或发布状态。
- 打包建议：建议人工核对上游状态和适用版本，并完成构建及回归测试后再决定打包。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。

### RISC-V: Fix bootstrap.

- 仓库：gcc-mirror/gcc；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-10-30T15:57:35Z
- 作者：Robin Dapp；SHA：508bc4b94939cc6b2b178dd987bd19790985fdcd
- 来源：[原始记录](https://github.com/gcc-mirror/gcc/commit/508bc4b94939cc6b2b178dd987bd19790985fdcd)
- 规则判断：medium / bugfix；打包候选：是，待人工评估
- 命中规则：keyword:bugfix:fix、keyword:vector-crypto-hypervisor:vector、path:gcc/config/riscv/riscv-v.cc、token:risc-v、token:riscv
- 涉及文件：gcc/config/riscv/riscv-v.cc
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V 问题修复相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为中；未验证构建、运行或发布状态。
- 打包建议：建议人工核对上游状态和适用版本，并完成构建及回归测试后再决定打包。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。

### ivopts: Count register pressure in hard registers, not values

- 仓库：gcc-mirror/gcc；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-10-29T13:27:38Z
- 作者：parras；SHA：17337464cf334e44ff3ecbf05062e665d256d242
- 来源：[原始记录](https://github.com/gcc-mirror/gcc/commit/17337464cf334e44ff3ecbf05062e665d256d242)
- 规则判断：medium / other；打包候选：否
- 命中规则：token:rv32、token:rv64
- 涉及文件：gcc/testsuite/gcc.dg/tree-ssa/ivopts-reg-units-1.c、gcc/testsuite/gcc.target/gcn/ivopts-reg-units-1.c、gcc/tree-ssa-loop-ivopts.cc
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V 其他变更相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为中；未验证构建、运行或发布状态。
- 打包建议：保留跟踪，暂不列为优先打包候选；需结合实际版本和测试结果人工评估。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。

### Format elf\_link\_read\_relocs calls

- 仓库：RTEMS/sourceware-mirror-binutils-gdb；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-10-28T22:35:44Z
- 作者：amodra；SHA：1d00124bd735ebe32600ebfe9ae975828893d621
- 来源：[原始记录](https://github.com/RTEMS/sourceware-mirror-binutils-gdb/commit/1d00124bd735ebe32600ebfe9ae975828893d621)
- 规则判断：medium / other；打包候选：否
- 命中规则：path:bfd/elfnn-riscv.c
- 涉及文件：bfd/elf-m10200.c、bfd/elf-m10300.c、bfd/elf32-arc.c、bfd/elf32-arm.c、bfd/elf32-avr.c、bfd/elf32-bfin.c、bfd/elf32-cr16.c、bfd/elf32-crx.c、bfd/elf32-csky.c、bfd/elf32-h8300.c、bfd/elf32-lm32.c、bfd/elf32-m32c.c、bfd/elf32-m68hc11.c、bfd/elf32-m68hc1x.c、bfd/elf32-m68k.c、bfd/elf32-microblaze.c、bfd/elf32-msp430.c、bfd/elf32-nds32.c、bfd/elf32-rl78.c、bfd/elf32-rx.c、bfd/elf32-score.c、bfd/elf32-score7.c、bfd/elf32-sh.c、bfd/elf32-v850.c、bfd/elf32-xtensa.c、bfd/elf64-alpha.c、bfd/elf64-ia64-vms.c、bfd/elf64-mmix.c、bfd/elflink.c、bfd/elfnn-ia64.c、bfd/elfnn-kvx.c、bfd/elfnn-riscv.c、bfd/elfxx-mips.c、bfd/elfxx-x86.c
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V 其他变更相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为中；未验证构建、运行或发布状态。
- 打包建议：保留跟踪，暂不列为优先打包候选；需结合实际版本和测试结果人工评估。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。

### Constify Elf\_Internal\_Sym in check\_relocs and relocate\_section

- 仓库：RTEMS/sourceware-mirror-binutils-gdb；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-10-28T22:35:44Z
- 作者：amodra；SHA：dc3dffcccc1585e74e8535b7b9e92d5eb63f107e
- 来源：[原始记录](https://github.com/RTEMS/sourceware-mirror-binutils-gdb/commit/dc3dffcccc1585e74e8535b7b9e92d5eb63f107e)
- 规则判断：medium / other；打包候选：否
- 命中规则：path:bfd/elfnn-riscv.c
- 涉及文件：bfd/elf-bfd.h、bfd/elf-m10200.c、bfd/elf.c、bfd/elf32-arc.c、bfd/elf32-arm.c、bfd/elf32-avr.c、bfd/elf32-bfin.c、bfd/elf32-cr16.c、bfd/elf32-cris.c、bfd/elf32-crx.c、bfd/elf32-csky.c、bfd/elf32-d10v.c、bfd/elf32-epiphany.c、bfd/elf32-fr30.c、bfd/elf32-frv.c、bfd/elf32-ft32.c、bfd/elf32-h8300.c、bfd/elf32-hppa.c、bfd/elf32-i386.c、bfd/elf32-ip2k.c、bfd/elf32-iq2000.c、bfd/elf32-lm32.c、bfd/elf32-m68hc1x.c、bfd/elf32-m68k.c、bfd/elf32-mcore.c、bfd/elf32-mep.c、bfd/elf32-metag.c、bfd/elf32-microblaze.c、bfd/elf32-moxie.c、bfd/elf32-msp430.c、bfd/elf32-mt.c、bfd/elf32-nds32.c、bfd/elf32-or1k.c、bfd/elf32-ppc.c、bfd/elf32-pru.c、bfd/elf32-rl78.c、bfd/elf32-rx.c、bfd/elf32-s390.c、bfd/elf32-sh.c、bfd/elf32-tic6x.c、bfd/elf32-tilepro.c、bfd/elf32-v850.c、bfd/elf32-vax.c、bfd/elf32-visium.c、bfd/elf32-xstormy16.c、bfd/elf32-xtensa.c、bfd/elf32-z80.c、bfd/elf64-alpha.c、bfd/elf64-bpf.c、bfd/elf64-ia64-vms.c、bfd/elf64-mmix.c、bfd/elf64-ppc.c、bfd/elf64-s390.c、bfd/elf64-x86-64.c、bfd/elfnn-aarch64.c、bfd/elfnn-ia64.c、bfd/elfnn-kvx.c、bfd/elfnn-loongarch.c、bfd/elfnn-riscv.c、bfd/elfxx-sparc.c、bfd/elfxx-tilegx.c、bfd/elfxx-x86.c、bfd/elfxx-x86.h
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V 其他变更相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为中；未验证构建、运行或发布状态。
- 打包建议：保留跟踪，暂不列为优先打包候选；需结合实际版本和测试结果人工评估。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。

### Duplicate bfd\_sym\_from\_r\_symndx lookup

- 仓库：RTEMS/sourceware-mirror-binutils-gdb；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-10-28T22:35:44Z
- 作者：amodra；SHA：f2fa1a5ec2e1a7ae206ed3790e9b2ff975b88aec
- 来源：[原始记录](https://github.com/RTEMS/sourceware-mirror-binutils-gdb/commit/f2fa1a5ec2e1a7ae206ed3790e9b2ff975b88aec)
- 规则判断：medium / bugfix；打包候选：是，待人工评估
- 命中规则：keyword:bugfix:fix、path:bfd/elfnn-riscv.c、token:riscv
- 涉及文件：bfd/elf32-arm.c、bfd/elf32-csky.c、bfd/elf32-hppa.c、bfd/elf32-i386.c、bfd/elf32-microblaze.c、bfd/elf32-or1k.c、bfd/elf32-ppc.c、bfd/elf32-s390.c、bfd/elf32-tic6x.c、bfd/elf32-tilepro.c、bfd/elf64-s390.c、bfd/elf64-x86-64.c、bfd/elfnn-aarch64.c、bfd/elfnn-kvx.c、bfd/elfnn-loongarch.c、bfd/elfnn-riscv.c、bfd/elfxx-sparc.c、bfd/elfxx-tilegx.c
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V 问题修复相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为中；未验证构建、运行或发布状态。
- 打包建议：建议人工核对上游状态和适用版本，并完成构建及回归测试后再决定打包。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。

### Delete redundant check\_relocs symndx upper bound checks

- 仓库：RTEMS/sourceware-mirror-binutils-gdb；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-10-28T22:35:43Z
- 作者：amodra；SHA：9dff5cb1aa18a779d952bffee9177590603ec394
- 来源：[原始记录](https://github.com/RTEMS/sourceware-mirror-binutils-gdb/commit/9dff5cb1aa18a779d952bffee9177590603ec394)
- 规则判断：medium / other；打包候选：否
- 命中规则：path:bfd/elfnn-riscv.c、token:riscv
- 涉及文件：bfd/elf32-arm.c、bfd/elf32-i386.c、bfd/elf32-s390.c、bfd/elf32-score.c、bfd/elf32-score7.c、bfd/elf32-tic6x.c、bfd/elf32-tilepro.c、bfd/elf32-xtensa.c、bfd/elf64-s390.c、bfd/elf64-x86-64.c、bfd/elfnn-aarch64.c、bfd/elfnn-kvx.c、bfd/elfnn-loongarch.c、bfd/elfnn-riscv.c、bfd/elfxx-mips.c、bfd/elfxx-sparc.c、bfd/elfxx-tilegx.c
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V 其他变更相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为中；未验证构建、运行或发布状态。
- 打包建议：保留跟踪，暂不列为优先打包候选；需结合实际版本和测试结果人工评估。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。

### \[RISC-V\] Fix multiple small RISC-V bugs discovered during LLM review

- 仓库：gcc-mirror/gcc；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-10-28T13:11:44Z
- 作者：JeffreyALaw；SHA：31eb899f30c51f03e9dcae76ff92c53928345d7c
- 来源：[原始记录](https://github.com/gcc-mirror/gcc/commit/31eb899f30c51f03e9dcae76ff92c53928345d7c)
- 规则判断：medium / bugfix；打包候选：是，待人工评估
- 命中规则：keyword:bugfix:fix、keyword:hardware:k3、keyword:isa-extension:zbb、path:gcc/config/riscv/riscv.cc、path:gcc/config/riscv/riscv.md、path:gcc/testsuite/gcc.target/riscv/xor-synthesis-5.c、path:gcc/testsuite/gcc.target/riscv/zbkb-zext.c、token:risc-v、token:riscv
- 涉及文件：gcc/config/riscv/riscv.cc、gcc/config/riscv/riscv.md、gcc/testsuite/gcc.target/riscv/xor-synthesis-5.c、gcc/testsuite/gcc.target/riscv/zbkb-zext.c
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V 问题修复相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为中；未验证构建、运行或发布状态。
- 打包建议：建议人工核对上游状态和适用版本，并完成构建及回归测试后再决定打包。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。

### \[RiscV\] Alphabetize ISA X extensions

- 仓库：RTEMS/sourceware-mirror-binutils-gdb；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-10-28T12:35:50Z
- 作者：urnathan；SHA：aeed64b39aed57729f66ad51560d8964e8201e6e
- 来源：[原始记录](https://github.com/RTEMS/sourceware-mirror-binutils-gdb/commit/aeed64b39aed57729f66ad51560d8964e8201e6e)
- 规则判断：medium / bugfix；打包候选：是，待人工评估
- 命中规则：keyword:bugfix:fixes、path:bfd/elfxx-riscv.c、path:gas/testsuite/gas/riscv/imply.d、path:gas/testsuite/gas/riscv/march-help.l、path:include/opcode/riscv.h、token:riscv
- 涉及文件：bfd/elfxx-riscv.c、gas/testsuite/gas/riscv/imply.d、gas/testsuite/gas/riscv/march-help.l、include/opcode/riscv.h
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V 问题修复相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为中；未验证构建、运行或发布状态。
- 打包建议：建议人工核对上游状态和适用版本，并完成构建及回归测试后再决定打包。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。

### \[RISC-V\] Fix miscellaneous bugs found by LLM review in RISC-V port

- 仓库：gcc-mirror/gcc；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-10-27T16:50:50Z
- 作者：JeffreyALaw；SHA：9a8f57d7713b4816a77144c5ef121989d9fd4a09
- 来源：[原始记录](https://github.com/gcc-mirror/gcc/commit/9a8f57d7713b4816a77144c5ef121989d9fd4a09)
- 规则判断：medium / bugfix；打包候选：是，待人工评估
- 命中规则：keyword:bugfix:fix、keyword:hardware:k3、keyword:isa-extension:extension、keyword:isa-extension:zicond、path:gcc/config/riscv/bitmanip.md、path:gcc/config/riscv/riscv.md、path:gcc/config/riscv/zicond.md、token:risc-v、token:riscv、token:rv32
- 涉及文件：gcc/config/riscv/bitmanip.md、gcc/config/riscv/riscv.md、gcc/config/riscv/zicond.md
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V 问题修复相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为中；未验证构建、运行或发布状态。
- 打包建议：建议人工核对上游状态和适用版本，并完成构建及回归测试后再决定打包。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。

### \[PATCH 3/3\] RISC-V: Fix Zbkb packh cost and instruction selection

- 仓库：gcc-mirror/gcc；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-10-27T15:09:18Z
- 作者：pz9115；SHA：635d3209171d20bce4de35041097064a3afeff66
- 来源：[原始记录](https://github.com/gcc-mirror/gcc/commit/635d3209171d20bce4de35041097064a3afeff66)
- 规则判断：medium / bugfix；打包候选：是，待人工评估
- 命中规则：keyword:bugfix:fix、keyword:isa-extension:zbb、path:gcc/config/riscv/riscv.cc、path:gcc/config/riscv/riscv.md、path:gcc/testsuite/gcc.target/riscv/packh32.c、token:risc-v、token:riscv
- 涉及文件：gcc/config/riscv/riscv.cc、gcc/config/riscv/riscv.md、gcc/testsuite/gcc.target/riscv/packh32.c
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V 问题修复相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为中；未验证构建、运行或发布状态。
- 打包建议：建议人工核对上游状态和适用版本，并完成构建及回归测试后再决定打包。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。

### RISC-V: Allow RVV register overlap for vfw{macc,msac}.vv

- 仓库：gcc-mirror/gcc；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-10-27T02:19:32Z
- 作者：Incarnation-p-lee；SHA：dafa6930eb51ef8ec9144c3747d741ce5cd2afeb
- 来源：[原始记录](https://github.com/gcc-mirror/gcc/commit/dafa6930eb51ef8ec9144c3747d741ce5cd2afeb)
- 规则判断：medium / vector-crypto-hypervisor；打包候选：是，待人工评估
- 命中规则：keyword:vector-crypto-hypervisor:vector、path:gcc/config/riscv/vector.md、token:risc-v、token:riscv
- 涉及文件：gcc/config/riscv/vector.md
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V 向量、密码学或虚拟化相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为中；未验证构建、运行或发布状态。
- 打包建议：建议人工核对上游状态和适用版本，并完成构建及回归测试后再决定打包。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。

### \[RISC-V\] Fix/simplify patterns for masked comparisons against zero

- 仓库：gcc-mirror/gcc；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-10-26T17:03:11Z
- 作者：JeffreyALaw；SHA：7df74ad63dc03768c6339911ac1ed93c5c09158e
- 来源：[原始记录](https://github.com/gcc-mirror/gcc/commit/7df74ad63dc03768c6339911ac1ed93c5c09158e)
- 规则判断：medium / bugfix；打包候选：是，待人工评估
- 命中规则：keyword:bugfix:fix、keyword:isa-extension:extension、path:gcc/config/riscv/riscv.md、token:risc-v、token:riscv
- 涉及文件：gcc/config/riscv/riscv.md
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V 问题修复相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为中；未验证构建、运行或发布状态。
- 打包建议：建议人工核对上游状态和适用版本，并完成构建及回归测试后再决定打包。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。

### \[RISC-V\] Fix various length problems in RISC-V port

- 仓库：gcc-mirror/gcc；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-10-26T16:44:41Z
- 作者：Jeff Law；SHA：e90131c387a6842586318830df9dfed351abcb07
- 来源：[原始记录](https://github.com/gcc-mirror/gcc/commit/e90131c387a6842586318830df9dfed351abcb07)
- 规则判断：medium / bugfix；打包候选：是，待人工评估
- 命中规则：keyword:bugfix:fix、keyword:isa-extension:zba、keyword:isa-extension:zfa、path:gcc/config/riscv/riscv.md、token:risc-v、token:riscv
- 涉及文件：gcc/config/riscv/riscv.md
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V 问题修复相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为中；未验证构建、运行或发布状态。
- 打包建议：建议人工核对上游状态和适用版本，并完成构建及回归测试后再决定打包。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。


## 低优先级

### RISC-V: Add tests for no reg overlap of fp widen ternary \[PR target/128162\]

- 仓库：gcc-mirror/gcc；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-11-02T00:10:24Z
- 作者：Incarnation-p-lee；SHA：c0e167041b054400959aa8b3923df76934197fec
- 来源：[原始记录](https://github.com/gcc-mirror/gcc/commit/c0e167041b054400959aa8b3923df76934197fec)
- 规则判断：low / other；打包候选：否
- 命中规则：low-value:tests、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwmacc\_vf-f16-m1.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwmacc\_vf-f16-m2.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwmacc\_vf-f16-m4.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwmacc\_vf-f32-m1.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwmacc\_vf-f32-m2.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwmacc\_vf-f32-m4.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwmacc\_vv-f16-m1.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwmacc\_vv-f16-m2.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwmacc\_vv-f16-m4.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwmacc\_vv-f32-m1.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwmacc\_vv-f32-m2.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwmacc\_vv-f32-m4.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwmaccbf16\_vf-bf16-m1.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwmaccbf16\_vf-bf16-m2.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwmaccbf16\_vf-bf16-m4.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwmaccbf16\_vv-bf16-m1.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwmaccbf16\_vv-bf16-m2.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwmaccbf16\_vv-bf16-m4.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwmsac\_vf-f16-m1.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwmsac\_vf-f16-m2.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwmsac\_vf-f16-m4.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwmsac\_vf-f32-m1.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwmsac\_vf-f32-m2.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwmsac\_vf-f32-m4.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwmsac\_vv-f16-m1.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwmsac\_vv-f16-m2.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwmsac\_vv-f16-m4.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwmsac\_vv-f32-m1.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwmsac\_vv-f32-m2.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwmsac\_vv-f32-m4.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwnmacc\_vf-f16-m1.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwnmacc\_vf-f16-m2.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwnmacc\_vf-f16-m4.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwnmacc\_vf-f32-m1.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwnmacc\_vf-f32-m2.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwnmacc\_vf-f32-m4.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwnmacc\_vv-f16-m1.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwnmacc\_vv-f16-m2.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwnmacc\_vv-f16-m4.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwnmacc\_vv-f32-m1.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwnmacc\_vv-f32-m2.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwnmacc\_vv-f32-m4.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwnmsac\_vf-f16-m1.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwnmsac\_vf-f16-m2.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwnmsac\_vf-f16-m4.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwnmsac\_vf-f32-m1.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwnmsac\_vf-f32-m2.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwnmsac\_vf-f32-m4.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwnmsac\_vv-f16-m1.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwnmsac\_vv-f16-m2.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwnmsac\_vv-f16-m4.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwnmsac\_vv-f32-m1.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwnmsac\_vv-f32-m2.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwnmsac\_vv-f32-m4.c、test-only、token:risc-v、token:riscv
- 涉及文件：gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwmacc\_vf-f16-m1.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwmacc\_vf-f16-m2.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwmacc\_vf-f16-m4.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwmacc\_vf-f32-m1.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwmacc\_vf-f32-m2.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwmacc\_vf-f32-m4.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwmacc\_vv-f16-m1.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwmacc\_vv-f16-m2.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwmacc\_vv-f16-m4.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwmacc\_vv-f32-m1.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwmacc\_vv-f32-m2.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwmacc\_vv-f32-m4.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwmaccbf16\_vf-bf16-m1.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwmaccbf16\_vf-bf16-m2.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwmaccbf16\_vf-bf16-m4.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwmaccbf16\_vv-bf16-m1.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwmaccbf16\_vv-bf16-m2.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwmaccbf16\_vv-bf16-m4.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwmsac\_vf-f16-m1.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwmsac\_vf-f16-m2.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwmsac\_vf-f16-m4.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwmsac\_vf-f32-m1.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwmsac\_vf-f32-m2.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwmsac\_vf-f32-m4.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwmsac\_vv-f16-m1.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwmsac\_vv-f16-m2.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwmsac\_vv-f16-m4.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwmsac\_vv-f32-m1.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwmsac\_vv-f32-m2.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwmsac\_vv-f32-m4.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwnmacc\_vf-f16-m1.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwnmacc\_vf-f16-m2.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwnmacc\_vf-f16-m4.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwnmacc\_vf-f32-m1.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwnmacc\_vf-f32-m2.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwnmacc\_vf-f32-m4.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwnmacc\_vv-f16-m1.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwnmacc\_vv-f16-m2.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwnmacc\_vv-f16-m4.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwnmacc\_vv-f32-m1.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwnmacc\_vv-f32-m2.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwnmacc\_vv-f32-m4.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwnmsac\_vf-f16-m1.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwnmsac\_vf-f16-m2.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwnmsac\_vf-f16-m4.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwnmsac\_vf-f32-m1.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwnmsac\_vf-f32-m2.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwnmsac\_vf-f32-m4.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwnmsac\_vv-f16-m1.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwnmsac\_vv-f16-m2.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwnmsac\_vv-f16-m4.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwnmsac\_vv-f32-m1.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwnmsac\_vv-f32-m2.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwnmsac\_vv-f32-m4.c
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V 其他变更相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为低；未验证构建、运行或发布状态。
- 打包建议：保留跟踪，暂不列为优先打包候选；需结合实际版本和测试结果人工评估。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。

### RISC-V: Add tests for no reg overlap of int widen ternary \[PR target/128162\]

- 仓库：gcc-mirror/gcc；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-11-02T00:10:23Z
- 作者：Incarnation-p-lee；SHA：8495f6c4a66decb68c39c14dafb0ce7b2093acf8
- 来源：[原始记录](https://github.com/gcc-mirror/gcc/commit/8495f6c4a66decb68c39c14dafb0ce7b2093acf8)
- 规则判断：low / other；打包候选：否
- 命中规则：low-value:tests、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/group\_overlap.h、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/nds\_vd4dots\_vv-i16-m1.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/nds\_vd4dots\_vv-i16-m2.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/nds\_vd4dots\_vv-i16-m4.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/nds\_vd4dots\_vv-i16-m8.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/nds\_vd4dots\_vv-i8-m1.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/nds\_vd4dots\_vv-i8-m2.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/nds\_vd4dots\_vv-i8-m4.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/nds\_vd4dots\_vv-i8-m8.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/nds\_vd4dotsu\_vv-u16-m1.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/nds\_vd4dotsu\_vv-u16-m2.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/nds\_vd4dotsu\_vv-u16-m4.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/nds\_vd4dotsu\_vv-u16-m8.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/nds\_vd4dotsu\_vv-u8-m1.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/nds\_vd4dotsu\_vv-u8-m2.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/nds\_vd4dotsu\_vv-u8-m4.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/nds\_vd4dotsu\_vv-u8-m8.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/nds\_vd4dotu\_vv-u16-m1.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/nds\_vd4dotu\_vv-u16-m2.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/nds\_vd4dotu\_vv-u16-m4.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/nds\_vd4dotu\_vv-u16-m8.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/nds\_vd4dotu\_vv-u8-m1.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/nds\_vd4dotu\_vv-u8-m2.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/nds\_vd4dotu\_vv-u8-m4.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/nds\_vd4dotu\_vv-u8-m8.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/sf\_vqmacc\_2x8x2-i8-m1.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/sf\_vqmacc\_2x8x2-i8-m2.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/sf\_vqmacc\_2x8x2-i8-m4.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/sf\_vqmacc\_2x8x2-i8-m8.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/sf\_vqmacc\_4x8x4-i8-m1.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/sf\_vqmacc\_4x8x4-i8-m2.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/sf\_vqmacc\_4x8x4-i8-m4.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/sf\_vqmaccsu\_2x8x2-u8-m1.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/sf\_vqmaccsu\_2x8x2-u8-m2.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/sf\_vqmaccsu\_2x8x2-u8-m4.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/sf\_vqmaccsu\_2x8x2-u8-m8.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/sf\_vqmaccsu\_4x8x4-u8-m1.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/sf\_vqmaccsu\_4x8x4-u8-m2.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/sf\_vqmaccsu\_4x8x4-u8-m4.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/sf\_vqmaccu\_2x8x2-u8-m1.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/sf\_vqmaccu\_2x8x2-u8-m2.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/sf\_vqmaccu\_2x8x2-u8-m4.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/sf\_vqmaccu\_2x8x2-u8-m8.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/sf\_vqmaccu\_4x8x4-u8-m1.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/sf\_vqmaccu\_4x8x4-u8-m2.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/sf\_vqmaccu\_4x8x4-u8-m4.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/sf\_vqmaccus\_2x8x2-i8-m1.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/sf\_vqmaccus\_2x8x2-i8-m2.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/sf\_vqmaccus\_2x8x2-i8-m4.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/sf\_vqmaccus\_2x8x2-i8-m8.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/sf\_vqmaccus\_4x8x4-i8-m1.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/sf\_vqmaccus\_4x8x4-i8-m2.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/sf\_vqmaccus\_4x8x4-i8-m4.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmacc\_vv-i16-m1.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmacc\_vv-i16-m2.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmacc\_vv-i16-m4.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmacc\_vv-i32-m1.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmacc\_vv-i32-m2.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmacc\_vv-i32-m4.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmacc\_vv-i8-m1.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmacc\_vv-i8-m2.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmacc\_vv-i8-m4.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmacc\_vx-i16-m1.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmacc\_vx-i16-m2.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmacc\_vx-i16-m4.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmacc\_vx-i32-m1.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmacc\_vx-i32-m2.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmacc\_vx-i32-m4.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmacc\_vx-i8-m1.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmacc\_vx-i8-m2.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmacc\_vx-i8-m4.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccsu\_vv-i16-m1.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccsu\_vv-i16-m2.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccsu\_vv-i16-m4.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccsu\_vv-i32-m1.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccsu\_vv-i32-m2.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccsu\_vv-i32-m4.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccsu\_vv-i8-m1.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccsu\_vv-i8-m2.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccsu\_vv-i8-m4.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccsu\_vx-u16-m1.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccsu\_vx-u16-m2.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccsu\_vx-u16-m4.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccsu\_vx-u32-m1.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccsu\_vx-u32-m2.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccsu\_vx-u32-m4.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccsu\_vx-u8-m1.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccsu\_vx-u8-m2.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccsu\_vx-u8-m4.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccu\_vv-u16-m1.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccu\_vv-u16-m2.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccu\_vv-u16-m4.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccu\_vv-u32-m1.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccu\_vv-u32-m2.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccu\_vv-u32-m4.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccu\_vv-u8-m1.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccu\_vv-u8-m2.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccu\_vv-u8-m4.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccu\_vx-u16-m1.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccu\_vx-u16-m2.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccu\_vx-u16-m4.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccu\_vx-u32-m1.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccu\_vx-u32-m2.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccu\_vx-u32-m4.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccu\_vx-u8-m1.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccu\_vx-u8-m2.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccu\_vx-u8-m4.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccu\_vx\_undef-u16-m1.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccu\_vx\_undef-u16-m2.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccu\_vx\_undef-u16-m4.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccu\_vx\_undef-u32-m1.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccu\_vx\_undef-u32-m2.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccu\_vx\_undef-u32-m4.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccu\_vx\_undef-u8-m1.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccu\_vx\_undef-u8-m2.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccu\_vx\_undef-u8-m4.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccus\_vx-i16-m1.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccus\_vx-i16-m2.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccus\_vx-i16-m4.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccus\_vx-i32-m1.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccus\_vx-i32-m2.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccus\_vx-i32-m4.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccus\_vx-i8-m1.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccus\_vx-i8-m2.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccus\_vx-i8-m4.c、test-only、token:risc-v、token:riscv
- 涉及文件：gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/group\_overlap.h、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/nds\_vd4dots\_vv-i16-m1.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/nds\_vd4dots\_vv-i16-m2.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/nds\_vd4dots\_vv-i16-m4.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/nds\_vd4dots\_vv-i16-m8.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/nds\_vd4dots\_vv-i8-m1.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/nds\_vd4dots\_vv-i8-m2.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/nds\_vd4dots\_vv-i8-m4.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/nds\_vd4dots\_vv-i8-m8.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/nds\_vd4dotsu\_vv-u16-m1.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/nds\_vd4dotsu\_vv-u16-m2.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/nds\_vd4dotsu\_vv-u16-m4.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/nds\_vd4dotsu\_vv-u16-m8.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/nds\_vd4dotsu\_vv-u8-m1.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/nds\_vd4dotsu\_vv-u8-m2.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/nds\_vd4dotsu\_vv-u8-m4.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/nds\_vd4dotsu\_vv-u8-m8.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/nds\_vd4dotu\_vv-u16-m1.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/nds\_vd4dotu\_vv-u16-m2.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/nds\_vd4dotu\_vv-u16-m4.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/nds\_vd4dotu\_vv-u16-m8.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/nds\_vd4dotu\_vv-u8-m1.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/nds\_vd4dotu\_vv-u8-m2.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/nds\_vd4dotu\_vv-u8-m4.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/nds\_vd4dotu\_vv-u8-m8.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/sf\_vqmacc\_2x8x2-i8-m1.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/sf\_vqmacc\_2x8x2-i8-m2.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/sf\_vqmacc\_2x8x2-i8-m4.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/sf\_vqmacc\_2x8x2-i8-m8.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/sf\_vqmacc\_4x8x4-i8-m1.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/sf\_vqmacc\_4x8x4-i8-m2.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/sf\_vqmacc\_4x8x4-i8-m4.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/sf\_vqmaccsu\_2x8x2-u8-m1.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/sf\_vqmaccsu\_2x8x2-u8-m2.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/sf\_vqmaccsu\_2x8x2-u8-m4.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/sf\_vqmaccsu\_2x8x2-u8-m8.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/sf\_vqmaccsu\_4x8x4-u8-m1.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/sf\_vqmaccsu\_4x8x4-u8-m2.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/sf\_vqmaccsu\_4x8x4-u8-m4.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/sf\_vqmaccu\_2x8x2-u8-m1.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/sf\_vqmaccu\_2x8x2-u8-m2.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/sf\_vqmaccu\_2x8x2-u8-m4.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/sf\_vqmaccu\_2x8x2-u8-m8.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/sf\_vqmaccu\_4x8x4-u8-m1.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/sf\_vqmaccu\_4x8x4-u8-m2.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/sf\_vqmaccu\_4x8x4-u8-m4.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/sf\_vqmaccus\_2x8x2-i8-m1.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/sf\_vqmaccus\_2x8x2-i8-m2.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/sf\_vqmaccus\_2x8x2-i8-m4.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/sf\_vqmaccus\_2x8x2-i8-m8.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/sf\_vqmaccus\_4x8x4-i8-m1.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/sf\_vqmaccus\_4x8x4-i8-m2.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/sf\_vqmaccus\_4x8x4-i8-m4.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmacc\_vv-i16-m1.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmacc\_vv-i16-m2.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmacc\_vv-i16-m4.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmacc\_vv-i32-m1.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmacc\_vv-i32-m2.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmacc\_vv-i32-m4.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmacc\_vv-i8-m1.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmacc\_vv-i8-m2.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmacc\_vv-i8-m4.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmacc\_vx-i16-m1.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmacc\_vx-i16-m2.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmacc\_vx-i16-m4.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmacc\_vx-i32-m1.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmacc\_vx-i32-m2.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmacc\_vx-i32-m4.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmacc\_vx-i8-m1.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmacc\_vx-i8-m2.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmacc\_vx-i8-m4.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccsu\_vv-i16-m1.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccsu\_vv-i16-m2.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccsu\_vv-i16-m4.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccsu\_vv-i32-m1.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccsu\_vv-i32-m2.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccsu\_vv-i32-m4.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccsu\_vv-i8-m1.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccsu\_vv-i8-m2.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccsu\_vv-i8-m4.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccsu\_vx-u16-m1.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccsu\_vx-u16-m2.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccsu\_vx-u16-m4.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccsu\_vx-u32-m1.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccsu\_vx-u32-m2.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccsu\_vx-u32-m4.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccsu\_vx-u8-m1.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccsu\_vx-u8-m2.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccsu\_vx-u8-m4.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccu\_vv-u16-m1.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccu\_vv-u16-m2.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccu\_vv-u16-m4.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccu\_vv-u32-m1.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccu\_vv-u32-m2.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccu\_vv-u32-m4.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccu\_vv-u8-m1.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccu\_vv-u8-m2.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccu\_vv-u8-m4.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccu\_vx-u16-m1.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccu\_vx-u16-m2.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccu\_vx-u16-m4.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccu\_vx-u32-m1.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccu\_vx-u32-m2.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccu\_vx-u32-m4.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccu\_vx-u8-m1.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccu\_vx-u8-m2.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccu\_vx-u8-m4.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccu\_vx\_undef-u16-m1.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccu\_vx\_undef-u16-m2.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccu\_vx\_undef-u16-m4.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccu\_vx\_undef-u32-m1.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccu\_vx\_undef-u32-m2.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccu\_vx\_undef-u32-m4.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccu\_vx\_undef-u8-m1.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccu\_vx\_undef-u8-m2.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccu\_vx\_undef-u8-m4.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccus\_vx-i16-m1.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccus\_vx-i16-m2.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccus\_vx-i16-m4.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccus\_vx-i32-m1.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccus\_vx-i32-m2.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccus\_vx-i32-m4.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccus\_vx-i8-m1.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccus\_vx-i8-m2.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwmaccus\_vx-i8-m4.c
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V 其他变更相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为低；未验证构建、运行或发布状态。
- 打包建议：保留跟踪，暂不列为优先打包候选；需结合实际版本和测试结果人工评估。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。

### RISC-V: Add test cases to ensure no reg overlap for vwabda.vv \[PR target/128162\]

- 仓库：gcc-mirror/gcc；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-10-30T00:56:44Z
- 作者：Incarnation-p-lee；SHA：b71062341c90ce952e0a07103d6aed9a5c5917d6
- 来源：[原始记录](https://github.com/gcc-mirror/gcc/commit/b71062341c90ce952e0a07103d6aed9a5c5917d6)
- 规则判断：low / other；打包候选：否
- 命中规则：low-value:test、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/group\_overlap.h、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwabda\_vv-i16-m1.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwabda\_vv-i16-m2.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwabda\_vv-i16-m4.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwabda\_vv-i8-m1.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwabda\_vv-i8-m2.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwabda\_vv-i8-m4.c、path:gcc/testsuite/gcc.target/riscv/rvv/base/pr128162-1.c、test-only、token:risc-v、token:riscv
- 涉及文件：gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/group\_overlap.h、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwabda\_vv-i16-m1.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwabda\_vv-i16-m2.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwabda\_vv-i16-m4.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwabda\_vv-i8-m1.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwabda\_vv-i8-m2.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwabda\_vv-i8-m4.c、gcc/testsuite/gcc.target/riscv/rvv/base/pr128162-1.c
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V 其他变更相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为低；未验证构建、运行或发布状态。
- 打包建议：保留跟踪，暂不列为优先打包候选；需结合实际版本和测试结果人工评估。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。

### RISC-V: Add test cases to ensure no reg overlap for vwabdau.vv \[PR target/128162\]

- 仓库：gcc-mirror/gcc；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-10-30T00:56:44Z
- 作者：Incarnation-p-lee；SHA：b76d14f773375487e534233fa2b3a5bcdb81da11
- 来源：[原始记录](https://github.com/gcc-mirror/gcc/commit/b76d14f773375487e534233fa2b3a5bcdb81da11)
- 规则判断：low / other；打包候选：否
- 命中规则：low-value:test、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwabdau\_vv-u16-m1.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwabdau\_vv-u16-m2.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwabdau\_vv-u16-m4.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwabdau\_vv-u8-m1.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwabdau\_vv-u8-m2.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwabdau\_vv-u8-m4.c、path:gcc/testsuite/gcc.target/riscv/rvv/base/pr128162-2.c、test-only、token:risc-v、token:riscv
- 涉及文件：gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwabdau\_vv-u16-m1.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwabdau\_vv-u16-m2.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwabdau\_vv-u16-m4.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwabdau\_vv-u8-m1.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwabdau\_vv-u8-m2.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwabdau\_vv-u8-m4.c、gcc/testsuite/gcc.target/riscv/rvv/base/pr128162-2.c
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V 其他变更相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为低；未验证构建、运行或发布状态。
- 打包建议：保留跟踪，暂不列为优先打包候选；需结合实际版本和测试结果人工评估。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。

### RISC-V: Add test cases for vfwmsac.vv reg overlap

- 仓库：gcc-mirror/gcc；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-10-27T02:19:32Z
- 作者：Incarnation-p-lee；SHA：4c8452662e95e3fa68543fb00ec6d6905bbd19c8
- 来源：[原始记录](https://github.com/gcc-mirror/gcc/commit/4c8452662e95e3fa68543fb00ec6d6905bbd19c8)
- 规则判断：low / other；打包候选：否
- 命中规则：low-value:test、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwmsac\_vv-f16-m1.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwmsac\_vv-f16-m2.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwmsac\_vv-f16-m4.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwmsac\_vv-f16-mf2.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwmsac\_vv-f16-mf4.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwmsac\_vv-f32-m1.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwmsac\_vv-f32-m2.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwmsac\_vv-f32-m4.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwmsac\_vv-f32-mf2.c、test-only、token:risc-v、token:riscv
- 涉及文件：gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwmsac\_vv-f16-m1.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwmsac\_vv-f16-m2.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwmsac\_vv-f16-m4.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwmsac\_vv-f16-mf2.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwmsac\_vv-f16-mf4.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwmsac\_vv-f32-m1.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwmsac\_vv-f32-m2.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwmsac\_vv-f32-m4.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwmsac\_vv-f32-mf2.c
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V 其他变更相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为低；未验证构建、运行或发布状态。
- 打包建议：保留跟踪，暂不列为优先打包候选；需结合实际版本和测试结果人工评估。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。

### RISC-V: Add more test cases for vfw{macc,msac}.vv

- 仓库：gcc-mirror/gcc；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-10-27T02:19:32Z
- 作者：Incarnation-p-lee；SHA：9c73440b6f8b81040379de62dc040aa8d2fd0803
- 来源：[原始记录](https://github.com/gcc-mirror/gcc/commit/9c73440b6f8b81040379de62dc040aa8d2fd0803)
- 规则判断：low / other；打包候选：否
- 命中规则：low-value:test、path:gcc/testsuite/gcc.target/riscv/rvv/base/pr112431-61.c、path:gcc/testsuite/gcc.target/riscv/rvv/base/pr112431-62.c、test-only、token:risc-v、token:riscv
- 涉及文件：gcc/testsuite/gcc.target/riscv/rvv/base/pr112431-61.c、gcc/testsuite/gcc.target/riscv/rvv/base/pr112431-62.c
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V 其他变更相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为低；未验证构建、运行或发布状态。
- 打包建议：保留跟踪，暂不列为优先打包候选；需结合实际版本和测试结果人工评估。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。

### RISC-V: Add test cases for vfwmacc.vv reg overlap

- 仓库：gcc-mirror/gcc；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-10-27T02:19:32Z
- 作者：Incarnation-p-lee；SHA：cfb973b34417a6075b7c86278e76397738c042a9
- 来源：[原始记录](https://github.com/gcc-mirror/gcc/commit/cfb973b34417a6075b7c86278e76397738c042a9)
- 规则判断：low / other；打包候选：否
- 命中规则：low-value:test、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwmacc\_vv-f16-m1.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwmacc\_vv-f16-m2.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwmacc\_vv-f16-m4.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwmacc\_vv-f16-mf2.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwmacc\_vv-f16-mf4.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwmacc\_vv-f32-m1.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwmacc\_vv-f32-m2.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwmacc\_vv-f32-m4.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwmacc\_vv-f32-mf2.c、test-only、token:risc-v、token:riscv
- 涉及文件：gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwmacc\_vv-f16-m1.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwmacc\_vv-f16-m2.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwmacc\_vv-f16-m4.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwmacc\_vv-f16-mf2.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwmacc\_vv-f16-mf4.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwmacc\_vv-f32-m1.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwmacc\_vv-f32-m2.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwmacc\_vv-f32-m4.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwmacc\_vv-f32-mf2.c
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V 其他变更相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为低；未验证构建、运行或发布状态。
- 打包建议：保留跟踪，暂不列为优先打包候选；需结合实际版本和测试结果人工评估。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。
