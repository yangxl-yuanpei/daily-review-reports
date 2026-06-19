# 每日文献追踪报告 - 2026-06-16

## 📊 统计概览
- 检索源: arXiv (last 24h) + Semantic Scholar (不限日期，若命中)
- 原始候选: 18 篇 (arXiv 18, S2: 0)
- 有效去重后: 3 篇
- 过滤已读论文: 5 篇（arXiv: 2606.06848, 2605.27229 + GCMC 类论文）
- 下载 PDF: 1 篇
- 实际精读: 3 篇（1 篇全文，2 篇摘要）

## 📑 论文详情（按相关性排序）

### 1. Hydrogen Chemisorption and Current-Induced Spin Polarization on NbP — 拓扑表面态与化学吸附的动量分辨分析
- **来源:** arXiv 2606.16994
- **期刊/出处:** arXiv: physics.chem-ph, cond-mat.mtrl-sci (preprint)
- **发布日期:** 2026-06-15
- **作者:** Luis Martinez-Gomez, Raphael F. Ribeiro
- **核心问题:** Weyl 半金属 NbP 的 Fermi arcs 表面态在 H 化学吸附中扮演什么角色？
- **方法创新:** DFT + Wannier TBM + pCOHP + 电流诱导自旋极化 (Edelstein 效应)，SOC on/off 对照
- **关键结果:** ΔG_H* SOC ≈ -0.60 eV（vs -0.62 eV 非SOC）；H 投影电流诱导磁矩 ~7×10⁻⁶ μB
- **与你研究的相关性:** **中** — 拓扑材料表面化学分析范式可迁移，但未涉及电化学恒电位
- **原文链接:** https://arxiv.org/pdf/2606.16994v1
- **PDF 状态:** ✅ 已下载全文

### 2. Transferable machine learning of excited-state dynamics with extremal pooling — 激发态 ML 框架
- **来源:** arXiv 2606.16859
- **期刊/出处:** arXiv: physics.chem-ph (preprint)
- **发布日期:** 2026-06-15
- **作者:** Cesare Malosso, Wei Bin How, Gonzalo Díaz Mirón, Ali Hassanali, Michele Ceriotti
- **核心问题:** 如何将 MLIP 从基态推广到激发态，解决能量非广延性问题？
- **方法创新:** Extremal pooling of atomic HOMO/LUMO contributions；可解释原子级激发能贡献
- **关键结果:** 在液态光激发溶剂化电子上验证，定量匹配 ROKS，实现周期性体系长时间尺度模拟
- **与你研究的相关性:** **高** — Extremal pooling 概念可直接迁移到恒电位电荷转移模拟（电荷非广延性）；Ceriotti 组同时深耕 MLIP + NQE + 激发态
- **原文链接:** https://arxiv.org/abs/2606.16859
- **PDF 状态:** ⚠️ 仅摘要

### 3. Evolution of Nonlinear Ion Transport in Nanopore Arrays — 纳米孔阵列的跨尺度离子输运
- **来源:** arXiv 2606.17012
- **期刊/出处:** arXiv: cond-mat.mtrl-sci, cond-mat.mes-hall (preprint)
- **发布日期:** 2026-06-15
- **作者:** Chih-Yuan Lin, Marija Drndić
- **核心问题:** 从单孔到 N~10000 孔阵列，离子输运的标度行为如何变化？
- **方法创新:** 实验制造 sub-3nm/sub-20nm 纳米孔阵列 + 3D 有限元建模；系统测量电导/整流/渗透能
- **关键结果:** 功率密度随阵列扩展下降三个数量级；表面电荷效应在 N~10000 时消失
- **与你研究的相关性:** **低** — 物理机制不同（纯离子输运 vs 电化学反应），但跨尺度非线性行为概念有参考价值
- **原文链接:** https://arxiv.org/abs/2606.17012
- **PDF 状态:** ⚠️ 仅摘要

## 💡 今日亮点
- **最值得精读的一篇:** 2606.16994 (Martinez-Gomez) — 拓扑表面态与化学吸附的关联是前沿交叉方向，pCOHP + 电流诱导自旋极化的方法论完整
- **可能与你研究论点冲突的一篇:** 2606.16859 (Malosso/Ceriotti) — 如果 extremal pooling 方案被证明有效，可能挑战恒电位 MLFF 中对电荷非广延性的处理方式（当前做法通常保留求和架构 + 电荷补偿）
- **值得追踪的作者或团队:** **Michele Ceriotti 组** (EPFL) — 连续在 MLIP (so3krates)、NQE (PIMD)、和最新的激发态 ML 三个方向上均有突破

## 📌 Key Gap
- 这三篇论文分别覆盖了（a）拓扑材料的表面化学成键分析、（b）激发态 ML 的非广延性架构、和（c）纳米孔阵列的跨尺度离子输运，但**未涉及**恒电位条件下的电化学界面 MLFF 模拟，也未涉及 NQE 对表面催化的定量影响
- **待填补空白**: Ceriotti 组的 extremal pooling 概念 + NQE (PIMD) + 恒电位 MLFF 三者的结合 — 即如何在恒电位框架中处理电子的非广延性（如可变的界面电荷）同时纳入核量子效应
