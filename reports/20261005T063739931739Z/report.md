# GNU RISC-V 上游更新报告

统计窗口（UTC）：2026-09-27T06:25:13Z 至 2026-10-05T06:37:39Z
生成时间（UTC）：2026-10-05T06:37:39Z

共 18 条相关更新：高 6、中 7、低 5。

优先级和打包候选由规则决定；LLM 辅助分析仅供参考，最终打包需人工评估和构建测试。
提交已合入不代表已经发布；关联 PR 的状态单独列出。

## 仓库采集状态

- RTEMS/sourceware-mirror-binutils-gdb：ok；分支 master
  采集窗口（UTC）：2026-09-27T06:25:13Z 至 2026-10-05T06:37:39Z
- gcc-mirror/gcc：ok；分支 master
  采集窗口（UTC）：2026-09-27T06:25:13Z 至 2026-10-05T06:37:39Z
- sailfishos-mirror/glibc：ok；分支 master
  采集窗口（UTC）：2026-09-27T06:25:13Z 至 2026-10-05T06:37:39Z

## 采集警告

- RTEMS/sourceware-mirror-binutils-gdb：轻量标签没有独立时间，只能用所指提交的时间代替。
- gcc-mirror/gcc：轻量标签没有独立时间，只能用所指提交的时间代替。
- 分页在第 1 页停止，元数据覆盖不完整。
- 未配置 LLM\_API\_KEY，使用规则结果。

## 高优先级

### RISC-V: Decode Zcmt JVT entries in objdump

- 仓库：RTEMS/sourceware-mirror-binutils-gdb；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-10-01T09:35:04Z
- 作者：pz9115；SHA：7310b8560eae5292a1e2a5ff8c8b969506e1cece
- 来源：[原始记录](https://github.com/RTEMS/sourceware-mirror-binutils-gdb/commit/7310b8560eae5292a1e2a5ff8c8b969506e1cece)
- 规则判断：high / isa-extension；打包候选：是，待人工评估
- 命中规则：functional:add、keyword:isa-extension:zdinx、path:binutils/testsuite/binutils-all/riscv/zcmt-jvt-base-rv32.d、path:binutils/testsuite/binutils-all/riscv/zcmt-jvt-base-rv64.d、path:binutils/testsuite/binutils-all/riscv/zcmt-jvt-rv32.d、path:binutils/testsuite/binutils-all/riscv/zcmt-jvt-rv64.d、path:binutils/testsuite/binutils-all/riscv/zcmt-jvt.ld、path:binutils/testsuite/binutils-all/riscv/zcmt-jvt.s、path:opcodes/riscv-dis.c、token:risc-v、token:riscv、token:rv32、token:rv64
- 涉及文件：binutils/testsuite/binutils-all/riscv/zcmt-jvt-base-rv32.d、binutils/testsuite/binutils-all/riscv/zcmt-jvt-base-rv64.d、binutils/testsuite/binutils-all/riscv/zcmt-jvt-rv32.d、binutils/testsuite/binutils-all/riscv/zcmt-jvt-rv64.d、binutils/testsuite/binutils-all/riscv/zcmt-jvt.ld、binutils/testsuite/binutils-all/riscv/zcmt-jvt.s、opcodes/riscv-dis.c
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V ISA 扩展相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为高；未验证构建、运行或发布状态。
- 打包建议：建议人工核对上游状态和适用版本，并完成构建及回归测试后再决定打包。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。

### RISC-V: Add supervisor architecture support

- 仓库：RTEMS/sourceware-mirror-binutils-gdb；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-10-01T09:02:58Z
- 作者：jerryzj；SHA：6963071aac9ac1433ca3dc7558c300b9d43c1ef1
- 来源：[原始记录](https://github.com/RTEMS/sourceware-mirror-binutils-gdb/commit/6963071aac9ac1433ca3dc7558c300b9d43c1ef1)
- 规则判断：high / profile-abi；打包候选：是，待人工评估
- 命中规则：functional:add、functional:support、keyword:profile-abi:profile、path:bfd/elfxx-riscv.c、path:gas/testsuite/gas/riscv/march-help.l、token:risc-v、token:riscv
- 涉及文件：bfd/elfxx-riscv.c、gas/testsuite/gas/riscv/march-help.l
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V Profile 或 ABI相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为高；未验证构建、运行或发布状态。
- 打包建议：建议人工核对上游状态和适用版本，并完成构建及回归测试后再决定打包。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。

### RISC-V: Allow RVV register overlap for vfw{add,sub,mul}.vf

- 仓库：gcc-mirror/gcc；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-09-29T01:45:31Z
- 作者：Incarnation-p-lee；SHA：a3f5541bcf62d1142cea7f7f70afcabf888d947c
- 来源：[原始记录](https://github.com/gcc-mirror/gcc/commit/a3f5541bcf62d1142cea7f7f70afcabf888d947c)
- 规则判断：high / vector-crypto-hypervisor；打包候选：是，待人工评估
- 命中规则：functional:add、keyword:vector-crypto-hypervisor:vector、path:gcc/config/riscv/vector.md、token:risc-v、token:riscv
- 涉及文件：gcc/config/riscv/vector.md
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V 向量、密码学或虚拟化相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为高；未验证构建、运行或发布状态。
- 打包建议：建议人工核对上游状态和适用版本，并完成构建及回归测试后再决定打包。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。

### RISC-V: Error out early for unsupported builtins. \[PR127553\]

- 仓库：gcc-mirror/gcc；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-09-28T18:55:41Z
- 作者：Robin Dapp；SHA：2b980c3e11a6b6ef0223d1668672bac877038185
- 来源：[原始记录](https://github.com/gcc-mirror/gcc/commit/2b980c3e11a6b6ef0223d1668672bac877038185)
- 规则判断：high / vector-crypto-hypervisor；打包候选：是，待人工评估
- 命中规则：functional:add、keyword:vector-crypto-hypervisor:vector、path:gcc/config/riscv/riscv-vector-builtins.cc、path:gcc/testsuite/gcc.target/riscv/pr127553.c、path:gcc/testsuite/gcc.target/riscv/rvv/base/bug-9.c、path:gcc/testsuite/gcc.target/riscv/rvv/base/intrinsic\_required\_ext-1.c、path:gcc/testsuite/gcc.target/riscv/rvv/base/intrinsic\_required\_ext-10.c、path:gcc/testsuite/gcc.target/riscv/rvv/base/intrinsic\_required\_ext-2.c、path:gcc/testsuite/gcc.target/riscv/rvv/base/intrinsic\_required\_ext-3.c、path:gcc/testsuite/gcc.target/riscv/rvv/base/intrinsic\_required\_ext-4.c、path:gcc/testsuite/gcc.target/riscv/rvv/base/intrinsic\_required\_ext-5.c、path:gcc/testsuite/gcc.target/riscv/rvv/base/intrinsic\_required\_ext-6.c、path:gcc/testsuite/gcc.target/riscv/rvv/base/intrinsic\_required\_ext-7.c、path:gcc/testsuite/gcc.target/riscv/rvv/base/intrinsic\_required\_ext-8.c、path:gcc/testsuite/gcc.target/riscv/rvv/base/intrinsic\_required\_ext-9.c、path:gcc/testsuite/gcc.target/riscv/rvv/base/pr114988-1.c、path:gcc/testsuite/gcc.target/riscv/rvv/base/pr114988-2.c、path:gcc/testsuite/gcc.target/riscv/rvv/base/pr120436.c、path:gcc/testsuite/gcc.target/riscv/rvv/base/target\_attribute\_v\_with\_intrinsic-17.c、path:gcc/testsuite/gcc.target/riscv/rvv/base/target\_attribute\_v\_with\_intrinsic-18.c、path:gcc/testsuite/gcc.target/riscv/rvv/base/target\_attribute\_v\_with\_intrinsic-19.c、path:gcc/testsuite/gcc.target/riscv/rvv/base/target\_attribute\_v\_with\_intrinsic-20.c、path:gcc/testsuite/gcc.target/riscv/rvv/base/target\_attribute\_v\_with\_intrinsic-21.c、path:gcc/testsuite/gcc.target/riscv/rvv/base/target\_attribute\_v\_with\_intrinsic-22.c、path:gcc/testsuite/gcc.target/riscv/rvv/base/target\_attribute\_v\_with\_intrinsic-23.c、path:gcc/testsuite/gcc.target/riscv/rvv/base/target\_attribute\_v\_with\_intrinsic-24.c、path:gcc/testsuite/gcc.target/riscv/rvv/base/target\_attribute\_v\_with\_intrinsic-25.c、path:gcc/testsuite/gcc.target/riscv/rvv/base/target\_attribute\_v\_with\_intrinsic-26.c、path:gcc/testsuite/gcc.target/riscv/rvv/base/target\_attribute\_v\_with\_intrinsic-27.c、path:gcc/testsuite/gcc.target/riscv/rvv/base/target\_attribute\_v\_with\_intrinsic-28.c、path:gcc/testsuite/gcc.target/riscv/rvv/base/target\_attribute\_v\_with\_intrinsic-29.c、path:gcc/testsuite/gcc.target/riscv/rvv/base/target\_attribute\_v\_with\_intrinsic-3.c、path:gcc/testsuite/gcc.target/riscv/rvv/base/target\_attribute\_v\_with\_intrinsic-7.c、path:gcc/testsuite/gcc.target/riscv/rvv/base/target\_attribute\_v\_with\_intrinsic-8.c、token:risc-v、token:riscv
- 涉及文件：gcc/config/riscv/riscv-vector-builtins.cc、gcc/testsuite/gcc.target/riscv/pr127553.c、gcc/testsuite/gcc.target/riscv/rvv/base/bug-9.c、gcc/testsuite/gcc.target/riscv/rvv/base/intrinsic\_required\_ext-1.c、gcc/testsuite/gcc.target/riscv/rvv/base/intrinsic\_required\_ext-10.c、gcc/testsuite/gcc.target/riscv/rvv/base/intrinsic\_required\_ext-2.c、gcc/testsuite/gcc.target/riscv/rvv/base/intrinsic\_required\_ext-3.c、gcc/testsuite/gcc.target/riscv/rvv/base/intrinsic\_required\_ext-4.c、gcc/testsuite/gcc.target/riscv/rvv/base/intrinsic\_required\_ext-5.c、gcc/testsuite/gcc.target/riscv/rvv/base/intrinsic\_required\_ext-6.c、gcc/testsuite/gcc.target/riscv/rvv/base/intrinsic\_required\_ext-7.c、gcc/testsuite/gcc.target/riscv/rvv/base/intrinsic\_required\_ext-8.c、gcc/testsuite/gcc.target/riscv/rvv/base/intrinsic\_required\_ext-9.c、gcc/testsuite/gcc.target/riscv/rvv/base/pr114988-1.c、gcc/testsuite/gcc.target/riscv/rvv/base/pr114988-2.c、gcc/testsuite/gcc.target/riscv/rvv/base/pr120436.c、gcc/testsuite/gcc.target/riscv/rvv/base/target\_attribute\_v\_with\_intrinsic-17.c、gcc/testsuite/gcc.target/riscv/rvv/base/target\_attribute\_v\_with\_intrinsic-18.c、gcc/testsuite/gcc.target/riscv/rvv/base/target\_attribute\_v\_with\_intrinsic-19.c、gcc/testsuite/gcc.target/riscv/rvv/base/target\_attribute\_v\_with\_intrinsic-20.c、gcc/testsuite/gcc.target/riscv/rvv/base/target\_attribute\_v\_with\_intrinsic-21.c、gcc/testsuite/gcc.target/riscv/rvv/base/target\_attribute\_v\_with\_intrinsic-22.c、gcc/testsuite/gcc.target/riscv/rvv/base/target\_attribute\_v\_with\_intrinsic-23.c、gcc/testsuite/gcc.target/riscv/rvv/base/target\_attribute\_v\_with\_intrinsic-24.c、gcc/testsuite/gcc.target/riscv/rvv/base/target\_attribute\_v\_with\_intrinsic-25.c、gcc/testsuite/gcc.target/riscv/rvv/base/target\_attribute\_v\_with\_intrinsic-26.c、gcc/testsuite/gcc.target/riscv/rvv/base/target\_attribute\_v\_with\_intrinsic-27.c、gcc/testsuite/gcc.target/riscv/rvv/base/target\_attribute\_v\_with\_intrinsic-28.c、gcc/testsuite/gcc.target/riscv/rvv/base/target\_attribute\_v\_with\_intrinsic-29.c、gcc/testsuite/gcc.target/riscv/rvv/base/target\_attribute\_v\_with\_intrinsic-3.c、gcc/testsuite/gcc.target/riscv/rvv/base/target\_attribute\_v\_with\_intrinsic-7.c、gcc/testsuite/gcc.target/riscv/rvv/base/target\_attribute\_v\_with\_intrinsic-8.c
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V 向量、密码学或虚拟化相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为高；未验证构建、运行或发布状态。
- 打包建议：建议人工核对上游状态和适用版本，并完成构建及回归测试后再决定打包。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。

### RISC-V: Consider spills in conv-dynamic LMUL \[PR127075\].

- 仓库：gcc-mirror/gcc；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-09-28T18:55:41Z
- 作者：Robin Dapp；SHA：a924d879f01d00d6c29e870c51bebcbf5e5a96eb
- 来源：[原始记录](https://github.com/gcc-mirror/gcc/commit/a924d879f01d00d6c29e870c51bebcbf5e5a96eb)
- 规则判断：high / vector-crypto-hypervisor；打包候选：是，待人工评估
- 命中规则：functional:add、keyword:vector-crypto-hypervisor:vector、path:gcc/config/riscv/riscv-vector-costs.cc、path:gcc/config/riscv/riscv-vector-costs.h、path:gcc/testsuite/gcc.dg/vect/costmodel/riscv/rvv/pr127075.c、token:risc-v、token:riscv
- 涉及文件：gcc/config/riscv/riscv-vector-costs.cc、gcc/config/riscv/riscv-vector-costs.h、gcc/testsuite/gcc.dg/vect/costmodel/riscv/rvv/pr127075.c
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V 向量、密码学或虚拟化相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为高；未验证构建、运行或发布状态。
- 打包建议：建议人工核对上游状态和适用版本，并完成构建及回归测试后再决定打包。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。

### posix: Add POSIX posix\_spawn\_file\_actions\_add{,f}chdir

- 仓库：sailfishos-mirror/glibc；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-09-28T15:57:36Z
- 作者：zatrazz；SHA：371d58d11bf7aacd4bf471bcb22bc7278330f349
- 来源：[原始记录](https://github.com/sailfishos-mirror/glibc/commit/371d58d11bf7aacd4bf471bcb22bc7278330f349)
- 规则判断：high / compiler-option；打包候选：是，待人工评估
- 命中规则：functional:add、keyword:compiler-option:option、path:sysdeps/unix/sysv/linux/riscv/rv32/libc.abilist、path:sysdeps/unix/sysv/linux/riscv/rv64/libc.abilist
- 涉及文件：NEWS、conform/data/spawn.h-data、posix/Makefile、posix/Versions、posix/spawn.h、posix/spawn\_faction\_addchdir.c、posix/spawn\_faction\_addfchdir.c、posix/tst-spawn-chdir-posix.c、posix/tst-spawn-chdir.c、sysdeps/mach/hurd/i386/libc.abilist、sysdeps/mach/hurd/x86\_64/libc.abilist、sysdeps/unix/sysv/linux/aarch64/libc.abilist、sysdeps/unix/sysv/linux/alpha/libc.abilist、sysdeps/unix/sysv/linux/arc/libc.abilist、sysdeps/unix/sysv/linux/arm/be/libc.abilist、sysdeps/unix/sysv/linux/arm/le/libc.abilist、sysdeps/unix/sysv/linux/csky/libc.abilist、sysdeps/unix/sysv/linux/hppa/libc.abilist、sysdeps/unix/sysv/linux/i386/libc.abilist、sysdeps/unix/sysv/linux/loongarch/ilp32/libc.abilist、sysdeps/unix/sysv/linux/loongarch/lp64/libc.abilist、sysdeps/unix/sysv/linux/m68k/coldfire/libc.abilist、sysdeps/unix/sysv/linux/m68k/m680x0/libc.abilist、sysdeps/unix/sysv/linux/microblaze/be/libc.abilist、sysdeps/unix/sysv/linux/microblaze/le/libc.abilist、sysdeps/unix/sysv/linux/mips/mips32/fpu/libc.abilist、sysdeps/unix/sysv/linux/mips/mips32/nofpu/libc.abilist、sysdeps/unix/sysv/linux/mips/mips64/n32/libc.abilist、sysdeps/unix/sysv/linux/mips/mips64/n64/libc.abilist、sysdeps/unix/sysv/linux/or1k/libc.abilist、sysdeps/unix/sysv/linux/powerpc/powerpc32/fpu/libc.abilist、sysdeps/unix/sysv/linux/powerpc/powerpc32/nofpu/libc.abilist、sysdeps/unix/sysv/linux/powerpc/powerpc64/be/libc.abilist、sysdeps/unix/sysv/linux/powerpc/powerpc64/le/libc.abilist、sysdeps/unix/sysv/linux/riscv/rv32/libc.abilist、sysdeps/unix/sysv/linux/riscv/rv64/libc.abilist、sysdeps/unix/sysv/linux/s390/libc.abilist、sysdeps/unix/sysv/linux/sh/be/libc.abilist、sysdeps/unix/sysv/linux/sh/le/libc.abilist、sysdeps/unix/sysv/linux/sparc/sparc32/libc.abilist、sysdeps/unix/sysv/linux/sparc/sparc64/libc.abilist、sysdeps/unix/sysv/linux/x86\_64/64/libc.abilist、sysdeps/unix/sysv/linux/x86\_64/x32/libc.abilist
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V 编译选项相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为高；未验证构建、运行或发布状态。
- 打包建议：建议人工核对上游状态和适用版本，并完成构建及回归测试后再决定打包。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。


## 中优先级

### vect: Fix scalar iteration bounds when doing alignment peeling with partial vectors \[PR127677\]

- 仓库：gcc-mirror/gcc；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-10-02T12:20:24Z
- 作者：TamarChristinaArm；SHA：d7bd302654fab2ddd8d7e8539f163db63a2f07e5
- 来源：[原始记录](https://github.com/gcc-mirror/gcc/commit/d7bd302654fab2ddd8d7e8539f163db63a2f07e5)
- 规则判断：medium / bugfix；打包候选：是，待人工评估
- 命中规则：keyword:bugfix:fix、keyword:compiler-option:-mabi、keyword:compiler-option:-march、keyword:isa-extension:zvl、keyword:vector-crypto-hypervisor:vector、keyword:vector-crypto-hypervisor:vectorization、token:risc-v、token:rv64
- 涉及文件：gcc/testsuite/gcc.dg/vect/vect-early-break\_146-pr127677.c、gcc/tree-vect-loop-manip.cc
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V 问题修复相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为中；未验证构建、运行或发布状态。
- 打包建议：建议人工核对上游状态和适用版本，并完成构建及回归测试后再决定打包。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。

### RISC-V: Fix h-&gt;got union phase confusion for DT\_RELR

- 仓库：RTEMS/sourceware-mirror-binutils-gdb；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-10-02T09:49:33Z
- 作者：Jens Remus；SHA：e522ebecf7381e1e03548a7d0816b8ce3c038984
- 来源：[原始记录](https://github.com/RTEMS/sourceware-mirror-binutils-gdb/commit/e522ebecf7381e1e03548a7d0816b8ce3c038984)
- 规则判断：medium / bugfix；打包候选：是，待人工评估
- 命中规则：keyword:bugfix:fix、path:bfd/elfnn-riscv.c、token:risc-v、token:riscv
- 涉及文件：bfd/elfnn-riscv.c
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V 问题修复相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为中；未验证构建、运行或发布状态。
- 打包建议：建议人工核对上游状态和适用版本，并完成构建及回归测试后再决定打包。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。

### RISC-V: Add Zcmt table-jump relocation definitions

- 仓库：RTEMS/sourceware-mirror-binutils-gdb；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-10-01T09:35:04Z
- 作者：pz9115；SHA：4b013df1822f977e2d9ceeeabc0eb2f827f66c03
- 来源：[原始记录](https://github.com/RTEMS/sourceware-mirror-binutils-gdb/commit/4b013df1822f977e2d9ceeeabc0eb2f827f66c03)
- 规则判断：medium / other；打包候选：否
- 命中规则：path:include/elf/riscv.h、path:include/opcode/riscv.h、token:risc-v、token:riscv
- 涉及文件：include/elf/riscv.h、include/opcode/riscv.h
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V 其他变更相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为中；未验证构建、运行或发布状态。
- 打包建议：保留跟踪，暂不列为优先打包候选；需结合实际版本和测试结果人工评估。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。

### RISC-V: PR30237, don't add PT\_RISCV\_ATTRIBUTES in objcopy/strip

- 仓库：RTEMS/sourceware-mirror-binutils-gdb；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-10-01T08:49:22Z
- 作者：OctopusET；SHA：97e4144904779d0c986670ed977d7c3fa61806b2
- 来源：[原始记录](https://github.com/RTEMS/sourceware-mirror-binutils-gdb/commit/97e4144904779d0c986670ed977d7c3fa61806b2)
- 规则判断：medium / other；打包候选：否
- 命中规则：path:bfd/elfnn-riscv.c、token:risc-v、token:riscv
- 涉及文件：bfd/elfnn-riscv.c
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V 其他变更相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为中；未验证构建、运行或发布状态。
- 打包建议：保留跟踪，暂不列为优先打包候选；需结合实际版本和测试结果人工评估。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。

### RISC-V: Added DT\_RELR support

- 仓库：RTEMS/sourceware-mirror-binutils-gdb；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-10-01T08:23:17Z
- 作者：Nelson Chu；SHA：b0c84e4cd5dae13d186b6099c080137d250a986a
- 来源：[原始记录](https://github.com/RTEMS/sourceware-mirror-binutils-gdb/commit/b0c84e4cd5dae13d186b6099c080137d250a986a)
- 规则判断：medium / bugfix；打包候选：是，待人工评估
- 命中规则：keyword:bugfix:fix、path:bfd/elfnn-riscv.c、path:ld/emulparams/elf32lriscv-defs.sh、path:ld/testsuite/ld-riscv-elf/discard-pic.d、path:ld/testsuite/ld-riscv-elf/discard.ld、path:ld/testsuite/ld-riscv-elf/discard.s、path:ld/testsuite/ld-riscv-elf/ld-riscv-elf.exp、path:ld/testsuite/ld-riscv-elf/relr-addend.d、path:ld/testsuite/ld-riscv-elf/relr-addend.s、path:ld/testsuite/ld-riscv-elf/relr-align-rv32-pic.d、path:ld/testsuite/ld-riscv-elf/relr-align-rv32-pic.rd、path:ld/testsuite/ld-riscv-elf/relr-align-rv64-pic.d、path:ld/testsuite/ld-riscv-elf/relr-align-rv64-pic.rd、path:ld/testsuite/ld-riscv-elf/relr-align.s、path:ld/testsuite/ld-riscv-elf/relr-data-rv32-pic.d、path:ld/testsuite/ld-riscv-elf/relr-data-rv32-pic.rd、path:ld/testsuite/ld-riscv-elf/relr-data-rv32-pie.d、path:ld/testsuite/ld-riscv-elf/relr-data-rv32-pie.rd、path:ld/testsuite/ld-riscv-elf/relr-data-rv64-pic.d、path:ld/testsuite/ld-riscv-elf/relr-data-rv64-pic.rd、path:ld/testsuite/ld-riscv-elf/relr-data-rv64-pie.d、path:ld/testsuite/ld-riscv-elf/relr-data-rv64-pie.rd、path:ld/testsuite/ld-riscv-elf/relr-data.s、path:ld/testsuite/ld-riscv-elf/relr-discard-pic.d、path:ld/testsuite/ld-riscv-elf/relr-discard-pie.d、path:ld/testsuite/ld-riscv-elf/relr-got-rv32-pic.d、path:ld/testsuite/ld-riscv-elf/relr-got-rv32-pic.rd、path:ld/testsuite/ld-riscv-elf/relr-got-rv32-pie.d、path:ld/testsuite/ld-riscv-elf/relr-got-rv32-pie.rd、path:ld/testsuite/ld-riscv-elf/relr-got-rv64-pic.d、path:ld/testsuite/ld-riscv-elf/relr-got-rv64-pic.rd、path:ld/testsuite/ld-riscv-elf/relr-got-rv64-pie.d、path:ld/testsuite/ld-riscv-elf/relr-got-rv64-pie.rd、path:ld/testsuite/ld-riscv-elf/relr-got-start.d、path:ld/testsuite/ld-riscv-elf/relr-got-start.s、path:ld/testsuite/ld-riscv-elf/relr-got.s、path:ld/testsuite/ld-riscv-elf/relr-relax.d、path:ld/testsuite/ld-riscv-elf/relr-relax.s、path:ld/testsuite/ld-riscv-elf/relr-relocs.ld、path:ld/testsuite/ld-riscv-elf/relr-textrel-pic.d、path:ld/testsuite/ld-riscv-elf/relr-textrel-pie.d、path:ld/testsuite/ld-riscv-elf/relr-textrel.s、token:risc-v、token:riscv
- 涉及文件：bfd/elfnn-riscv.c、binutils/readelf.c、binutils/testsuite/lib/binutils-common.exp、ld/NEWS、ld/emulparams/elf32lriscv-defs.sh、ld/ld.texi、ld/testsuite/ld-riscv-elf/discard-pic.d、ld/testsuite/ld-riscv-elf/discard.ld、ld/testsuite/ld-riscv-elf/discard.s、ld/testsuite/ld-riscv-elf/ld-riscv-elf.exp、ld/testsuite/ld-riscv-elf/relr-addend.d、ld/testsuite/ld-riscv-elf/relr-addend.s、ld/testsuite/ld-riscv-elf/relr-align-rv32-pic.d、ld/testsuite/ld-riscv-elf/relr-align-rv32-pic.rd、ld/testsuite/ld-riscv-elf/relr-align-rv64-pic.d、ld/testsuite/ld-riscv-elf/relr-align-rv64-pic.rd、ld/testsuite/ld-riscv-elf/relr-align.s、ld/testsuite/ld-riscv-elf/relr-data-rv32-pic.d、ld/testsuite/ld-riscv-elf/relr-data-rv32-pic.rd、ld/testsuite/ld-riscv-elf/relr-data-rv32-pie.d、ld/testsuite/ld-riscv-elf/relr-data-rv32-pie.rd、ld/testsuite/ld-riscv-elf/relr-data-rv64-pic.d、ld/testsuite/ld-riscv-elf/relr-data-rv64-pic.rd、ld/testsuite/ld-riscv-elf/relr-data-rv64-pie.d、ld/testsuite/ld-riscv-elf/relr-data-rv64-pie.rd、ld/testsuite/ld-riscv-elf/relr-data.s、ld/testsuite/ld-riscv-elf/relr-discard-pic.d、ld/testsuite/ld-riscv-elf/relr-discard-pie.d、ld/testsuite/ld-riscv-elf/relr-got-rv32-pic.d、ld/testsuite/ld-riscv-elf/relr-got-rv32-pic.rd、ld/testsuite/ld-riscv-elf/relr-got-rv32-pie.d、ld/testsuite/ld-riscv-elf/relr-got-rv32-pie.rd、ld/testsuite/ld-riscv-elf/relr-got-rv64-pic.d、ld/testsuite/ld-riscv-elf/relr-got-rv64-pic.rd、ld/testsuite/ld-riscv-elf/relr-got-rv64-pie.d、ld/testsuite/ld-riscv-elf/relr-got-rv64-pie.rd、ld/testsuite/ld-riscv-elf/relr-got-start.d、ld/testsuite/ld-riscv-elf/relr-got-start.s、ld/testsuite/ld-riscv-elf/relr-got.s、ld/testsuite/ld-riscv-elf/relr-relax.d、ld/testsuite/ld-riscv-elf/relr-relax.s、ld/testsuite/ld-riscv-elf/relr-relocs.ld、ld/testsuite/ld-riscv-elf/relr-textrel-pic.d、ld/testsuite/ld-riscv-elf/relr-textrel-pie.d、ld/testsuite/ld-riscv-elf/relr-textrel.s
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V 问题修复相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为中；未验证构建、运行或发布状态。
- 打包建议：建议人工核对上游状态和适用版本，并完成构建及回归测试后再决定打包。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。

### RISC-V: Spill more unsplittable moves \[PR127484\].

- 仓库：gcc-mirror/gcc；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-09-28T18:55:40Z
- 作者：Robin Dapp；SHA：3d79c978b53474d2b613fe3e28037393c8d037b0
- 来源：[原始记录](https://github.com/gcc-mirror/gcc/commit/3d79c978b53474d2b613fe3e28037393c8d037b0)
- 规则判断：medium / other；打包候选：否
- 命中规则：path:gcc/config/riscv/riscv.cc、path:gcc/config/riscv/riscv.md、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/pr127484.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/pr127547.c、token:risc-v、token:riscv
- 涉及文件：gcc/config/riscv/riscv.cc、gcc/config/riscv/riscv.md、gcc/testsuite/gcc.target/riscv/rvv/autovec/pr127484.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/pr127547.c
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V 其他变更相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为中；未验证构建、运行或发布状态。
- 打包建议：保留跟踪，暂不列为优先打包候选；需结合实际版本和测试结果人工评估。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。

### RISC-V: Compute live ranges for pattern results

- 仓库：gcc-mirror/gcc；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-09-28T15:19:37Z
- 作者：garthlei；SHA：b0434879418053061782e825ea0bf2eadb654b2b
- 来源：[原始记录](https://github.com/gcc-mirror/gcc/commit/b0434879418053061782e825ea0bf2eadb654b2b)
- 规则判断：medium / bugfix；打包候选：是，待人工评估
- 命中规则：keyword:bugfix:regression、keyword:vector-crypto-hypervisor:vector、keyword:vector-crypto-hypervisor:vectorization、path:gcc/config/riscv/riscv-vector-costs.cc、path:gcc/testsuite/gcc.dg/vect/costmodel/riscv/rvv/dynamic-lmul4-5.c、path:gcc/testsuite/gcc.dg/vect/costmodel/riscv/rvv/dynamic-lmul4-7.c、path:gcc/testsuite/gcc.dg/vect/costmodel/riscv/rvv/dynamic-lmul8-16.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/pr121910.c、token:risc-v、token:riscv、token:rv32、token:rv64
- 涉及文件：gcc/config/riscv/riscv-vector-costs.cc、gcc/testsuite/gcc.dg/vect/costmodel/riscv/rvv/dynamic-lmul4-5.c、gcc/testsuite/gcc.dg/vect/costmodel/riscv/rvv/dynamic-lmul4-7.c、gcc/testsuite/gcc.dg/vect/costmodel/riscv/rvv/dynamic-lmul8-16.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/pr121910.c
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V 问题修复相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为中；未验证构建、运行或发布状态。
- 打包建议：建议人工核对上游状态和适用版本，并完成构建及回归测试后再决定打包。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。


## 低优先级

### RISC-V: Add test cases for vfwadd.vf reg overlap

- 仓库：gcc-mirror/gcc；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-09-29T01:45:31Z
- 作者：Incarnation-p-lee；SHA：3d5f011ffec35d928577f5cfd24c101c5950ae93
- 来源：[原始记录](https://github.com/gcc-mirror/gcc/commit/3d5f011ffec35d928577f5cfd24c101c5950ae93)
- 规则判断：low / other；打包候选：否
- 命中规则：low-value:test、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwadd\_vf-f16-m1.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwadd\_vf-f16-m2.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwadd\_vf-f16-m4.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwadd\_vf-f16-mf2.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwadd\_vf-f16-mf4.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwadd\_vf-f32-m1.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwadd\_vf-f32-m2.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwadd\_vf-f32-m4.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwadd\_vf-f32-mf2.c、test-only、token:risc-v、token:riscv
- 涉及文件：gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwadd\_vf-f16-m1.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwadd\_vf-f16-m2.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwadd\_vf-f16-m4.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwadd\_vf-f16-mf2.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwadd\_vf-f16-mf4.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwadd\_vf-f32-m1.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwadd\_vf-f32-m2.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwadd\_vf-f32-m4.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwadd\_vf-f32-mf2.c
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V 其他变更相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为低；未验证构建、运行或发布状态。
- 打包建议：保留跟踪，暂不列为优先打包候选；需结合实际版本和测试结果人工评估。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。

### RISC-V: Remove xfail of the vfwadd.vf reg overlap test case

- 仓库：gcc-mirror/gcc；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-09-29T01:45:31Z
- 作者：Incarnation-p-lee；SHA：5454af039f44aecefbd30fca712e2c5ca0714c5b
- 来源：[原始记录](https://github.com/gcc-mirror/gcc/commit/5454af039f44aecefbd30fca712e2c5ca0714c5b)
- 规则判断：low / other；打包候选：否
- 命中规则：low-value:test、path:gcc/testsuite/gcc.target/riscv/rvv/base/pr112431-25.c、path:gcc/testsuite/gcc.target/riscv/rvv/base/pr112431-26.c、path:gcc/testsuite/gcc.target/riscv/rvv/base/pr112431-27.c、test-only、token:risc-v、token:riscv
- 涉及文件：gcc/testsuite/gcc.target/riscv/rvv/base/pr112431-25.c、gcc/testsuite/gcc.target/riscv/rvv/base/pr112431-26.c、gcc/testsuite/gcc.target/riscv/rvv/base/pr112431-27.c
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V 其他变更相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为低；未验证构建、运行或发布状态。
- 打包建议：保留跟踪，暂不列为优先打包候选；需结合实际版本和测试结果人工评估。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。

### RISC-V: Add test cases for vfwsub.vf reg overlap

- 仓库：gcc-mirror/gcc；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-09-29T01:45:31Z
- 作者：Incarnation-p-lee；SHA：5d2597a0b61da3c48c2f9dd3768c9806c980bbf8
- 来源：[原始记录](https://github.com/gcc-mirror/gcc/commit/5d2597a0b61da3c48c2f9dd3768c9806c980bbf8)
- 规则判断：low / other；打包候选：否
- 命中规则：low-value:test、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwsub\_vf-f16-m1.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwsub\_vf-f16-m2.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwsub\_vf-f16-m4.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwsub\_vf-f16-mf2.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwsub\_vf-f16-mf4.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwsub\_vf-f32-m1.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwsub\_vf-f32-m2.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwsub\_vf-f32-m4.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwsub\_vf-f32-mf2.c、test-only、token:risc-v、token:riscv
- 涉及文件：gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwsub\_vf-f16-m1.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwsub\_vf-f16-m2.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwsub\_vf-f16-m4.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwsub\_vf-f16-mf2.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwsub\_vf-f16-mf4.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwsub\_vf-f32-m1.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwsub\_vf-f32-m2.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwsub\_vf-f32-m4.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwsub\_vf-f32-mf2.c
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V 其他变更相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为低；未验证构建、运行或发布状态。
- 打包建议：保留跟踪，暂不列为优先打包候选；需结合实际版本和测试结果人工评估。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。

### RISC-V: Add test cases for vfwmul.vf reg overlap

- 仓库：gcc-mirror/gcc；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-09-29T01:45:31Z
- 作者：Incarnation-p-lee；SHA：ba20ee9a2cd5791cf571c873dbf331cdfbe6181d
- 来源：[原始记录](https://github.com/gcc-mirror/gcc/commit/ba20ee9a2cd5791cf571c873dbf331cdfbe6181d)
- 规则判断：low / other；打包候选：否
- 命中规则：low-value:test、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwmul\_vf-f16-m1.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwmul\_vf-f16-m2.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwmul\_vf-f16-m4.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwmul\_vf-f16-mf2.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwmul\_vf-f16-mf4.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwmul\_vf-f32-m1.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwmul\_vf-f32-m2.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwmul\_vf-f32-m4.c、path:gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwmul\_vf-f32-mf2.c、test-only、token:risc-v、token:riscv
- 涉及文件：gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwmul\_vf-f16-m1.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwmul\_vf-f16-m2.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwmul\_vf-f16-m4.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwmul\_vf-f16-mf2.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwmul\_vf-f16-mf4.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwmul\_vf-f32-m1.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwmul\_vf-f32-m2.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwmul\_vf-f32-m4.c、gcc/testsuite/gcc.target/riscv/rvv/autovec/group\_overlap/vfwmul\_vf-f32-mf2.c
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V 其他变更相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为低；未验证构建、运行或发布状态。
- 打包建议：保留跟踪，暂不列为优先打包候选；需结合实际版本和测试结果人工评估。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。

### elf: Only build THP tests for ABIs that define THP-PAGE-SIZE

- 仓库：sailfishos-mirror/glibc；类型：commit；状态：已合入
- 提交时间（committer date）（UTC）：2026-09-28T15:57:39Z
- 作者：zatrazz；SHA：60b925c18fe6436e0885b2be9fde5d8db3688cbb
- 来源：[原始记录](https://github.com/sailfishos-mirror/glibc/commit/60b925c18fe6436e0885b2be9fde5d8db3688cbb)
- 规则判断：low / other；打包候选：否
- 命中规则：low-value:tests、token:riscv
- 涉及文件：sysdeps/unix/sysv/linux/Makefile、sysdeps/unix/sysv/linux/aarch64/Makefile、sysdeps/unix/sysv/linux/alpha/Makefile、sysdeps/unix/sysv/linux/arc/Makefile、sysdeps/unix/sysv/linux/csky/Makefile、sysdeps/unix/sysv/linux/hppa/Makefile、sysdeps/unix/sysv/linux/i386/Makefile、sysdeps/unix/sysv/linux/loongarch/Makefile、sysdeps/unix/sysv/linux/m68k/Makefile、sysdeps/unix/sysv/linux/microblaze/Makefile、sysdeps/unix/sysv/linux/mips/Makefile、sysdeps/unix/sysv/linux/or1k/Makefile、sysdeps/unix/sysv/linux/powerpc/Makefile、sysdeps/unix/sysv/linux/s390/Makefile、sysdeps/unix/sysv/linux/sh/Makefile
- 分析方式：仅规则分析
- 中文摘要：检测到 RISC-V 其他变更相关更新，请结合原始标题和链接核对。
- 影响：规则优先级为低；未验证构建、运行或发布状态。
- 打包建议：保留跟踪，暂不列为优先打包候选；需结合实际版本和测试结果人工评估。
- 分析警告：未配置 LLM\_API\_KEY，使用规则结果。
