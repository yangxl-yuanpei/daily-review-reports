# 精读报告

## 1. 论文元信息
- **标题**: The Intricacies of Computational Electrochemistry
- **作者**: Nitish Govindarajan, Georg Kastlunger, Joseph A. Gauthier, Jun Cheng, I. Filot, Arthur Hagopian, H. Hansen, Jun Huang, Piotr M. Kowalski, Jinwen Liu, Juan M Lombardi, Mikael Maraschin, Andrew A. Peterson, Hemanth S. Pillai, Hector Prats, Conor J. Price, R. van Roij, Jan Rossmeisl, R. R. Seemakurthi, Seung-Jae Shin, Audrey Smith, Jia-Xin Zhu, K. Doblhoff-Dier (et al.)
- **出处**: 2025, Perspective (⚠️ 仅摘要 — S2 closed access)
- **Tags**: electrochemistry, perspective, CP, benchmarking

## 2. 核心问题
计算电化学为何如此困难，以及当前领域面临哪些未解决的争论和方法论挑战？

## 3. 动机与背景
- 计算电化学的复杂性不仅来自电化学过程的多尺度性质，也来自方法的快速发展和缺乏统一指南
- 基于 Lorentz Center 研讨会的讨论，总结社区共识和开放问题
- 多位领域内顶级研究者联合撰写

## 4. 方法核心
- 恒电位 vs 恒电荷模拟的选择并非 trivial（需考虑界面电容和绝对电位对齐）
- 电化学反应自由能图的解释存在挑战（计算氢电极 CHE 的局限）
- Poisson–Nernst–Planck 方程并非万能（忽略某些关键效应）
- 该领域急需更多基准测试 (benchmarking)

## 5. 关键实验与结果
- 恒电位方法在可解释性和尺寸收敛上优于恒电荷方法
- 恒电荷方法对界面电容偏差和绝对电位对齐误差更具有鲁棒性
- 明确呼吁建立基准测试标准

## 6. 创新点
- 社区共识性综述，总结了 20+ 位专家的观点
- 清晰指出了恒电位 vs 恒电荷 debate 的核心权衡
- 提出了计算电化学的方法论路线图

## 7. 局限性
- 属观点/展望类文章，无新数据或新方法
- 某些观点可能具有主观性
- 缺少对 ML 势和 NQE 的深入讨论

## 8. 对你研究的启发
- 恒电位 MLMD 需要在恒电位和恒电荷之间做出明智选择
- 明确指出了需要基准测试，你的 CP-MLMD 工作可作为 benchmark 案例
- 界面电容对齐仍是主要挑战，含 NQE 的模拟中电容对同位素取代的响应值得探索
