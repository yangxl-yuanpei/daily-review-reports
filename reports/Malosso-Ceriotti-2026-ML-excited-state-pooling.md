### 1. 论文元信息
- **标题**: Transferable machine learning of excited-state dynamics with extremal pooling
- **作者**: Cesare Malosso, Wei Bin How, Gonzalo Díaz Mirón, Ali Hassanali, Michele Ceriotti (EPFL / ICTP)
- **期刊/出处**: arXiv: physics.chem-ph (preprint)
- **发布日期**: 2026-06-15
- **arXiv ID**: 2606.16859
- **PDF 状态**: ⚠️ 仅摘要（arXiv PDF 转换失败，仅基于摘要分析）

### 2. 核心问题
如何将机器学习原子间势（MLIP）从基态推广到激发态，使其能够以可负担的计算成本模拟光化学过程的激发态动力学？

### 3. 动机与背景
- MLIP 在基态模拟中取得了革命性成功，但标准架构假设能量的广延性（extensivity），这在激发态中不成立
- 激发态势能面模拟对光化学、太阳能转换、大气化学至关重要，但传统的 ab initio 方法对长时间尺度和扩展体系计算成本太高
- 缺乏通用的、可迁移的激发态 ML 框架

### 4. 方法核心
1. **Extremal pooling 机制**: 预测每个原子的 HOMO 和 LUMO 贡献，通过取极值（而非求和）得到体系总的激发能
2. **仅训练激发态能量和力**，不依赖基态信息
3. 架构学习了可解释的原子级贡献，编码了电子局域化的物理信息

### 5. 关键实验与结果
- 展示在**液态水的光激发溶剂化电子**上的应用
- 再现了激发过程中的关键反应链：氢原子解离 + 质子耦合电子转移（PCET）
- 与 Restricted Open-Shell Kohn-Sham (ROKS) 计算结果定量一致
- 实现了周期性体系在参考电子结构方法无法触及的长度和时间尺度上的激发态模拟

### 6. 创新点
1. **首次提出面向激发态的 extensivity-free ML 架构** — extremal pooling 从根本上绕过了传统 MLIP 对总能广延性的依赖
2. **可解释的原子级激发态贡献** — 每个原子对激发能的贡献编码了电子局域化程度的物理信息
3. **从 Ceriotti 组此前基态 ML 研究到激发态的自然延伸**，展示了同一框架的通用性

### 7. 局限性
- 目前仅展示在溶剂化电子这一单一体系上，泛化性尚需更多验证
- 需要参考激发态数据（ROKS/TDDFT），对更大体系的数据生成成本仍高
- Extremal pooling 可能不适用于激发态具有多中心离域特征的情况

### 8. 对你研究的启发
- **核心方法启发**: Extremal pooling 的概念可能适用于恒电位 MLFF 中处理电荷转移 — 电荷变化也是非广延的（电荷集中在界面），类似激发态
- **PCET 模拟**: 如果研究方向涉及界面 PCET（如 NQE 对 PCET 的影响），本文的激发态动力学方法提供了端到端的 ML 替代方案
- **与 Ceriotti 组的关系**: 该组同时在做 MLIP、NQE (PIMD)、激发态，值得关注他们将三者结合的交叉工作
