# GNU RISC-V 上游更新报告

统计窗口（UTC）：2026-11-08T07:43:14Z 至 2026-11-16T07:43:50Z
生成时间（UTC）：2026-11-16T07:43:50Z

共 14 条相关更新：高 2、中 8、低 4。

优先级和打包候选由规则决定；LLM 辅助分析仅供参考，最终打包需人工评估和构建测试。
提交已合入不代表已经发布；关联 PR 的状态单独列出。

## 仓库采集状态

- RTEMS/sourceware-mirror-binutils-gdb：ok；分支 master
  采集窗口（UTC）：2026-11-08T07:43:14Z 至 2026-11-16T07:43:50Z
- gcc-mirror/gcc：ok；分支 master
  采集窗口（UTC）：2026-11-08T07:43:14Z 至 2026-11-16T07:43:50Z
- sailfishos-mirror/glibc：ok；分支 master
  采集窗口（UTC）：2026-11-08T07:43:14Z 至 2026-11-16T07:43:50Z

## 采集警告

- RTEMS/sourceware-mirror-binutils-gdb：轻量标签没有独立时间，只能用所指提交的时间代替。
- gcc-mirror/gcc：轻量标签没有独立时间，只能用所指提交的时间代替。
- 分页在第 1 页停止，元数据覆盖不完整。
- 未配置 LLM\_API\_KEY，使用规则结果。

## 高优先级

### Use tighter insn types for variables that already hold insns

- 仓库：gcc-mirror/gcc；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-11-12T20:37:43Z
- 作者：tbsaunde；SHA：8c43a22e05a93b9c131632f8f9b7199cfa4c8f87
- 来源：[原始记录](https://github.com/gcc-mirror/gcc/commit/8c43a22e05a93b9c131632f8f9b7199cfa4c8f87)
- 规则判断：high / hardware；打包候选：是，待人工评估
- 命中规则：functional:optimize、keyword:hardware:tune、path:gcc/config/riscv/riscv.cc、token:riscv
- 涉及文件：gcc/cfgexpand.cc、gcc/config/arm/arm.cc、gcc/config/arm/arm.h、gcc/config/arm/thumb2.md、gcc/config/bfin/bfin.cc、gcc/config/c6x/c6x.cc、gcc/config/i386/x86-tune-sched-bd.cc、gcc/config/m68k/m68k.cc、gcc/config/mcore/mcore.cc、gcc/config/pa/pa.cc、gcc/config/riscv/riscv.cc、gcc/config/rs6000/rs6000-logue.cc、gcc/hw-doloop.h、gcc/reorg.cc、gcc/stmt.cc
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V 硬件支持相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为高；未验证构建、运行或发布状态。
- 打包建议：建议人工核对上游状态和适用版本，并完成构建及回归测试后再决定打包。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。

### RISC-V: Add pipeline description for MIPS i8500 processor

- 仓库：gcc-mirror/gcc；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-11-10T15:11:40Z
- 作者：mgoudar；SHA：917da9c6e019407c9d469455ad4c50c062470d6c
- 来源：[原始记录](https://github.com/gcc-mirror/gcc/commit/917da9c6e019407c9d469455ad4c50c062470d6c)
- 规则判断：high / hardware；打包候选：是，待人工评估
- 命中规则：functional:add、keyword:hardware:microarchitecture、keyword:hardware:processor、keyword:hardware:tune、path:gcc/config/riscv/mips-i8500.md、path:gcc/config/riscv/riscv-cores.def、path:gcc/config/riscv/riscv-opts.h、path:gcc/config/riscv/riscv.cc、path:gcc/config/riscv/riscv.md、path:gcc/doc/riscv-mtune.texi、token:risc-v、token:riscv
- 涉及文件：gcc/config/riscv/mips-i8500.md、gcc/config/riscv/riscv-cores.def、gcc/config/riscv/riscv-opts.h、gcc/config/riscv/riscv.cc、gcc/config/riscv/riscv.md、gcc/doc/riscv-mtune.texi
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V 硬件支持相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为高；未验证构建、运行或发布状态。
- 打包建议：建议人工核对上游状态和适用版本，并完成构建及回归测试后再决定打包。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。


## 中优先级

### Regenerate configure with autoconf 2.73

- 仓库：sailfishos-mirror/glibc；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-11-14T15:05:39Z
- 作者：fweimer-rh；SHA：6dc664245b7063f97626896dfbb4efe1e8d5146c
- 来源：[原始记录](https://github.com/sailfishos-mirror/glibc/commit/6dc664245b7063f97626896dfbb4efe1e8d5146c)
- 规则判断：medium / bugfix；打包候选：是，待人工评估
- 命中规则：keyword:bugfix:bug、keyword:bugfix:fixes、path:sysdeps/riscv/configure、path:sysdeps/riscv/preconfigure、path:sysdeps/unix/sysv/linux/riscv/configure
- 涉及文件：INSTALL、aclocal.m4、configure、manual/install.texi、sysdeps/aarch64/configure、sysdeps/alpha/configure、sysdeps/arc/configure、sysdeps/arm/configure、sysdeps/arm/preconfigure、sysdeps/csky/configure、sysdeps/csky/preconfigure、sysdeps/hppa/configure、sysdeps/htl/configure、sysdeps/i386/configure、sysdeps/ieee754/ldbl-opt/configure、sysdeps/loongarch/configure、sysdeps/loongarch/preconfigure、sysdeps/m68k/configure、sysdeps/mach/configure、sysdeps/mach/hurd/configure、sysdeps/microblaze/configure、sysdeps/microblaze/preconfigure、sysdeps/mips/configure、sysdeps/nptl/configure、sysdeps/powerpc/powerpc32/configure、sysdeps/powerpc/powerpc32/fpu/configure、sysdeps/powerpc/powerpc64/configure、sysdeps/powerpc/powerpc64/le/configure、sysdeps/powerpc/powerpc64/le/fpu/multiarch/configure、sysdeps/riscv/configure、sysdeps/riscv/preconfigure、sysdeps/s390/configure、sysdeps/sh/preconfigure、sysdeps/sparc/sparc32/configure、sysdeps/unix/sysv/linux/configure、sysdeps/unix/sysv/linux/loongarch/configure、sysdeps/unix/sysv/linux/mips/configure、sysdeps/unix/sysv/linux/powerpc/configure、sysdeps/unix/sysv/linux/powerpc/powerpc64/configure、sysdeps/unix/sysv/linux/riscv/configure、sysdeps/x86/configure、sysdeps/x86\_64/configure、sysdeps/x86\_64/preconfigure
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V 问题修复相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为中；未验证构建、运行或发布状态。
- 打包建议：建议人工核对上游状态和适用版本，并完成构建及回归测试后再决定打包。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。

### simplify-rtx: Reverse rotations with masked negative counts

- 仓库：gcc-mirror/gcc；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-11-14T05:54:32Z
- 作者：pz9115；SHA：9ef00f3c4784e2e4fb10eaa720dbde3afbb5baf4
- 来源：[原始记录](https://github.com/gcc-mirror/gcc/commit/9ef00f3c4784e2e4fb10eaa720dbde3afbb5baf4)
- 规则判断：medium / isa-extension；打包候选：是，待人工评估
- 命中规则：keyword:isa-extension:zbb、path:gcc/testsuite/gcc.target/riscv/zbb-rol-ror-10.c、token:riscv
- 涉及文件：gcc/simplify-rtx.cc、gcc/testsuite/gcc.target/aarch64/rotate-neg-mask.c、gcc/testsuite/gcc.target/riscv/zbb-rol-ror-10.c
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V ISA 扩展相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为中；未验证构建、运行或发布状态。
- 打包建议：建议人工核对上游状态和适用版本，并完成构建及回归测试后再决定打包。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。

### RISC-V: Fold masked counts in inverted bit extraction

- 仓库：gcc-mirror/gcc；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-11-13T05:01:28Z
- 作者：pz9115；SHA：72288e39290eb70bffbe5e47beb9da6426d53a41
- 来源：[原始记录](https://github.com/gcc-mirror/gcc/commit/72288e39290eb70bffbe5e47beb9da6426d53a41)
- 规则判断：medium / bugfix；打包候选：是，待人工评估
- 命中规则：keyword:bugfix:correctness、path:gcc/config/riscv/bitmanip.md、path:gcc/testsuite/gcc.target/riscv/zbs-bext-3.c、token:risc-v、token:riscv、token:rv32、token:rv64
- 涉及文件：gcc/config/riscv/bitmanip.md、gcc/testsuite/gcc.target/riscv/zbs-bext-3.c
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V 问题修复相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为中；未验证构建、运行或发布状态。
- 打包建议：建议人工核对上游状态和适用版本，并完成构建及回归测试后再决定打包。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。

### Use dyn\_cast for insn class checks

- 仓库：gcc-mirror/gcc；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-11-12T20:37:43Z
- 作者：tbsaunde；SHA：186151547abd8ec0a8d16c5e51813353096f71cb
- 来源：[原始记录](https://github.com/gcc-mirror/gcc/commit/186151547abd8ec0a8d16c5e51813353096f71cb)
- 规则判断：medium / other；打包候选：否
- 命中规则：path:gcc/config/riscv/riscv-sr.cc、path:gcc/config/riscv/riscv.cc、token:riscv
- 涉及文件：gcc/caller-save.cc、gcc/calls.cc、gcc/cfgbuild.cc、gcc/cfgcleanup.cc、gcc/cfgrtl.cc、gcc/combine.cc、gcc/config/aarch64/aarch64.cc、gcc/config/arm/aarch-bti-insert.cc、gcc/config/avr/avr.cc、gcc/config/c6x/c6x.cc、gcc/config/i386/i386-features.cc、gcc/config/i386/i386.cc、gcc/config/loongarch/loongarch.cc、gcc/config/pa/pa.cc、gcc/config/riscv/riscv-sr.cc、gcc/config/riscv/riscv.cc、gcc/config/rs6000/rs6000-logue.cc、gcc/config/sh/sh.cc、gcc/config/sparc/sparc.cc、gcc/cse.cc、gcc/cselib.cc、gcc/dce.cc、gcc/df-problems.cc、gcc/dse.cc、gcc/dwarf2cfi.cc、gcc/dwarf2out.cc、gcc/early-remat.cc、gcc/emit-rtl.cc、gcc/except.cc、gcc/ext-dce.cc、gcc/final.cc、gcc/function.cc、gcc/gcse.cc、gcc/ira-lives.cc、gcc/ira.cc、gcc/loop-invariant.cc、gcc/loop-iv.cc、gcc/lra-constraints.cc、gcc/lra-lives.cc、gcc/lra-remat.cc、gcc/lra-spills.cc、gcc/lra.cc、gcc/postreload-gcse.cc、gcc/postreload.cc、gcc/print-rtl.cc、gcc/reg-stack.cc、gcc/regcprop.cc、gcc/regrename.cc、gcc/reload.cc、gcc/reload1.cc、gcc/reorg.cc、gcc/resource.cc、gcc/rtlanal.cc、gcc/sched-deps.cc、gcc/sel-sched.cc、gcc/store-motion.cc、gcc/var-tracking.cc
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V 其他变更相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为中；未验证构建、运行或发布状态。
- 打包建议：保留跟踪，暂不列为优先打包候选；需结合实际版本和测试结果人工评估。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。

### tree: Avoid building a zero tree for poly\_int coefficients

- 仓库：gcc-mirror/gcc；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-11-12T15:02:39Z
- 作者：ktkachov；SHA：fada0de3559a530fa643a5de5fcee4f328699c0a
- 来源：[原始记录](https://github.com/gcc-mirror/gcc/commit/fada0de3559a530fa643a5de5fcee4f328699c0a)
- 规则判断：medium / profile-abi；打包候选：是，待人工评估
- 命中规则：keyword:profile-abi:profile、token:risc-v
- 涉及文件：gcc/tree.h
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V Profile 或 ABI相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为中；未验证构建、运行或发布状态。
- 打包建议：建议人工核对上游状态和适用版本，并完成构建及回归测试后再决定打包。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。

### RISC-V: Return the matched macro-fusion operation

- 仓库：gcc-mirror/gcc；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-11-12T07:18:50Z
- 作者：majin2020；SHA：56ea963549ef4eeba0d6d3fe01ef5ad9a62e334e
- 来源：[原始记录](https://github.com/gcc-mirror/gcc/commit/56ea963549ef4eeba0d6d3fe01ef5ad9a62e334e)
- 规则判断：medium / other；打包候选：否
- 命中规则：path:gcc/config/riscv/riscv-fusion.cc、path:gcc/config/riscv/riscv-protos.h、token:risc-v、token:riscv
- 涉及文件：gcc/config/riscv/riscv-fusion.cc、gcc/config/riscv/riscv-protos.h
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V 其他变更相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为中；未验证构建、运行或发布状态。
- 打包建议：保留跟踪，暂不列为优先打包候选；需结合实际版本和测试结果人工评估。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。

### RISC-V: Fix reg overlap for vs1 of vwadd\[u\].wv

- 仓库：gcc-mirror/gcc；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-11-11T01:58:00Z
- 作者：Incarnation-p-lee；SHA：2e046596d270a5c61b8a02e18e69211a04453d16
- 来源：[原始记录](https://github.com/gcc-mirror/gcc/commit/2e046596d270a5c61b8a02e18e69211a04453d16)
- 规则判断：medium / bugfix；打包候选：是，待人工评估
- 命中规则：keyword:bugfix:fix、keyword:vector-crypto-hypervisor:vector、path:gcc/config/riscv/vector.md、token:risc-v、token:riscv
- 涉及文件：gcc/config/riscv/vector.md
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V 问题修复相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为中；未验证构建、运行或发布状态。
- 打包建议：建议人工核对上游状态和适用版本，并完成构建及回归测试后再决定打包。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。

### RISC-V: Fix memory leak in permconst pass

- 仓库：gcc-mirror/gcc；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-11-10T01:43:00Z
- 作者：garthlei；SHA：6cecf3235b239bb854e6f90e515196c2a0785cd3
- 来源：[原始记录](https://github.com/gcc-mirror/gcc/commit/6cecf3235b239bb854e6f90e515196c2a0785cd3)
- 规则判断：medium / bugfix；打包候选：是，待人工评估
- 命中规则：keyword:bugfix:fix、keyword:vector-crypto-hypervisor:vector、path:gcc/config/riscv/riscv-vect-permconst.cc、token:risc-v、token:riscv、token:rv32、token:rv64
- 涉及文件：gcc/config/riscv/riscv-vect-permconst.cc
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V 问题修复相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为中；未验证构建、运行或发布状态。
- 打包建议：建议人工核对上游状态和适用版本，并完成构建及回归测试后再决定打包。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。


## 低优先级

### RISC-V: Add test cases for vwadd.wv vs1 reg overlap

- 仓库：gcc-mirror/gcc；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-11-11T01:58:00Z
- 作者：Incarnation-p-lee；SHA：759916c4bd250d5a96320e06cdafa5a16e9ea38f
- 来源：[原始记录](https://github.com/gcc-mirror/gcc/commit/759916c4bd250d5a96320e06cdafa5a16e9ea38f)
- 规则判断：low / other；打包候选：否
- 命中规则：low-value:test、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/group\_overlap.h、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwadd\_wv\_vs1-i16-m1.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwadd\_wv\_vs1-i16-m2.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwadd\_wv\_vs1-i16-m4.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwadd\_wv\_vs1-i16-mf2.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwadd\_wv\_vs1-i16-mf4.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwadd\_wv\_vs1-i32-m1.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwadd\_wv\_vs1-i32-m2.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwadd\_wv\_vs1-i32-m4.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwadd\_wv\_vs1-i32-mf2.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwadd\_wv\_vs1-i8-m1.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwadd\_wv\_vs1-i8-m2.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwadd\_wv\_vs1-i8-m4.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwadd\_wv\_vs1-i8-mf2.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwadd\_wv\_vs1-i8-mf4.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwadd\_wv\_vs1-i8-mf8.c、test-only、token:risc-v、token:riscv
- 涉及文件：gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/group\_overlap.h、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwadd\_wv\_vs1-i16-m1.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwadd\_wv\_vs1-i16-m2.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwadd\_wv\_vs1-i16-m4.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwadd\_wv\_vs1-i16-mf2.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwadd\_wv\_vs1-i16-mf4.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwadd\_wv\_vs1-i32-m1.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwadd\_wv\_vs1-i32-m2.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwadd\_wv\_vs1-i32-m4.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwadd\_wv\_vs1-i32-mf2.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwadd\_wv\_vs1-i8-m1.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwadd\_wv\_vs1-i8-m2.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwadd\_wv\_vs1-i8-m4.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwadd\_wv\_vs1-i8-mf2.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwadd\_wv\_vs1-i8-mf4.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwadd\_wv\_vs1-i8-mf8.c
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V 其他变更相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为低；未验证构建、运行或发布状态。
- 打包建议：保留跟踪，暂不列为优先打包候选；需结合实际版本和测试结果人工评估。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。

### RISC-V: Add test cases for vwaddu.wv vs1 reg overlap

- 仓库：gcc-mirror/gcc；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-11-11T01:58:00Z
- 作者：Incarnation-p-lee；SHA：81584f5a499f20283f151c66679b93f7cabea40d
- 来源：[原始记录](https://github.com/gcc-mirror/gcc/commit/81584f5a499f20283f151c66679b93f7cabea40d)
- 规则判断：low / other；打包候选：否
- 命中规则：low-value:test、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwaddu\_wv\_vs1-u16-m1.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwaddu\_wv\_vs1-u16-m2.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwaddu\_wv\_vs1-u16-m4.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwaddu\_wv\_vs1-u16-mf2.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwaddu\_wv\_vs1-u16-mf4.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwaddu\_wv\_vs1-u32-m1.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwaddu\_wv\_vs1-u32-m2.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwaddu\_wv\_vs1-u32-m4.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwaddu\_wv\_vs1-u32-mf2.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwaddu\_wv\_vs1-u8-m1.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwaddu\_wv\_vs1-u8-m2.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwaddu\_wv\_vs1-u8-m4.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwaddu\_wv\_vs1-u8-mf2.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwaddu\_wv\_vs1-u8-mf4.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwaddu\_wv\_vs1-u8-mf8.c、test-only、token:risc-v、token:riscv
- 涉及文件：gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwaddu\_wv\_vs1-u16-m1.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwaddu\_wv\_vs1-u16-m2.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwaddu\_wv\_vs1-u16-m4.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwaddu\_wv\_vs1-u16-mf2.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwaddu\_wv\_vs1-u16-mf4.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwaddu\_wv\_vs1-u32-m1.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwaddu\_wv\_vs1-u32-m2.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwaddu\_wv\_vs1-u32-m4.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwaddu\_wv\_vs1-u32-mf2.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwaddu\_wv\_vs1-u8-m1.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwaddu\_wv\_vs1-u8-m2.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwaddu\_wv\_vs1-u8-m4.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwaddu\_wv\_vs1-u8-mf2.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwaddu\_wv\_vs1-u8-mf4.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwaddu\_wv\_vs1-u8-mf8.c
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V 其他变更相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为低；未验证构建、运行或发布状态。
- 打包建议：保留跟踪，暂不列为优先打包候选；需结合实际版本和测试结果人工评估。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。

### RISC-V: Add more test cases for vwadd\[u\].wv

- 仓库：gcc-mirror/gcc；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-11-11T01:58:00Z
- 作者：Incarnation-p-lee；SHA：a2a11abfad353f3e39c3a46abf278ad6258e5547
- 来源：[原始记录](https://github.com/gcc-mirror/gcc/commit/a2a11abfad353f3e39c3a46abf278ad6258e5547)
- 规则判断：low / other；打包候选：否
- 命中规则：low-value:test、path:gcc/testsuite/gcc.target/riscv/rvv/base/pr112431-65.c、path:gcc/testsuite/gcc.target/riscv/rvv/base/pr112431-66.c、test-only、token:risc-v、token:riscv
- 涉及文件：gcc/testsuite/gcc.target/riscv/rvv/base/pr112431-65.c、gcc/testsuite/gcc.target/riscv/rvv/base/pr112431-66.c
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V 其他变更相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为低；未验证构建、运行或发布状态。
- 打包建议：保留跟踪，暂不列为优先打包候选；需结合实际版本和测试结果人工评估。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。

### RISC-V: Adjust vwadd\[u\].wv m4 test cases for reg overlap

- 仓库：gcc-mirror/gcc；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-11-11T01:58:00Z
- 作者：Incarnation-p-lee；SHA：ac96a764cc995f35362a49250fd31b7caafbce39
- 来源：[原始记录](https://github.com/gcc-mirror/gcc/commit/ac96a764cc995f35362a49250fd31b7caafbce39)
- 规则判断：low / other；打包候选：否
- 命中规则：low-value:test、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwadd\_wv-i16-m4.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwadd\_wv-i32-m4.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwadd\_wv-i8-m4.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwaddu\_wv-u16-m4.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwaddu\_wv-u32-m4.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwaddu\_wv-u8-m4.c、test-only、token:risc-v、token:riscv
- 涉及文件：gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwadd\_wv-i16-m4.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwadd\_wv-i32-m4.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwadd\_wv-i8-m4.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwaddu\_wv-u16-m4.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwaddu\_wv-u32-m4.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vwaddu\_wv-u8-m4.c
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V 其他变更相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为低；未验证构建、运行或发布状态。
- 打包建议：保留跟踪，暂不列为优先打包候选；需结合实际版本和测试结果人工评估。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。
