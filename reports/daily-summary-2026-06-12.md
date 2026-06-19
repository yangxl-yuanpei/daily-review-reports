# 每日文献追踪报告 - 2026-06-12

## 📊 统计概览
- 检索源: arXiv (last 24h) + Semantic Scholar (不限日期)
- 原始候选: 20篇（S2）+ 15篇（arXiv）
- 有效去重后: 7篇
- 下载 PDF: 7篇（2篇 arXiv 直链 + 2篇 RSC/MPG 直链 + 2篇 ACS 手动 + 1篇 PMC）
- 实际精读: 7篇

## 📑 论文详情（按相关性排序）

### 1. Sun2024 — GC-HMC + PIMC + DP-Ne for NQEs in PCET
- **来源:** arXiv:2407.12458
- **作者:** Menglin Sun, Bin Jin, Xiaolong Yang, Shenzhen Xu
- **核心问题:** 如何在严格恒电位（GC 系综）条件下同时考虑质子 NQE 和界面充分采样？
- **方法创新:** GC-HMC + PIMC + DP-Ne MLFF（Ne 为额外输入，输出包括 ∂E/∂Ne）统一框架
- **关键结果:** Volmer ΔEa↓0.13 eV @ -0.9V（50-100× 速率增强）；Heyrovsky ΔEa↓0.09 eV
- **与你研究的相关性:** **高** — NQE + GC 系综 + MLFF 三大要素齐聚
- **原文链接:** https://arxiv.org/abs/2407.12458
- **PDF 状态:** ✅ 已下载

### 2. Bunting2025 — NQEs of C-H Activation at Pt/Au with ML Potentials
- **来源:** PCCP (10.1039/D5CP01527H)
- **作者:** Rhiannon J. Bunting, María del Carmen Marín, et al.
- **核心问题:** ML 势能面结合 CMD 能否揭示 C-H 活化中 NQEs 的金属依赖性？
- **方法创新:** Allegro MLIP + CMD，对比 Pt(111) vs Au(111) 的 NQE 差异
- **关键结果:** Pt 上 NQE 加速 ~20×（ZPE 主导），Au 上无 NQE；谐振近似在 Au 上失效
- **与你研究的相关性:** **高** — NQE + MLIP 方法直接相关；金属依赖性值得关注
- **原文链接:** https://doi.org/10.1039/D5CP01527H
- **PDF 状态:** ✅ 已下载

### 3. Wang2025 — Constant-Potential MLFF for Electrochemical Interfaces
- **来源:** JCTC (10.1021/acs.jctc.5c00784)
- **作者:** Zeyu Wang, Junhan Chang, Jincheng Li, Qi Zhu, Feng Hao
- **核心问题:** 如何在恒电位分子动力学中同时保持 MLFF 精度和效率？
- **方法创新:** MACE 架构 + CP-MLFF（Ne → (F, EF) 映射），主动学习集成
- **关键结果:** Ea 从 0.894 eV 逐步收敛到 0.460 eV（Ni-N-C CO2RR）; Si(100)-H 测试通过
- **与你研究的相关性:** **高** — 恒电位 MLFF 方法论（与 Sun2024 互补）
- **原文链接:** https://doi.org/10.1021/acs.jctc.5c00784
- **PDF 状态:** ✅ 已下载

### 4. Bi2023 — EF-RPMD for Nonadiabatic Dynamics + NQEs
- **来源:** arXiv:2311.08779
- **作者:** Rui-Hao Bi, Wenjie Dou
- **核心问题:** 如何在电子摩擦模型中纳入 NQE（零点能 + 隧穿）？
- **方法创新:** 将平均电子摩擦作用于 RPMD 质心模式（EF-RPMD）+ Ehrenfest 修正
- **关键结果:** 对称 PES 下与 QME 几乎精确一致；非对称 PES 低温有偏差；仅 Γ > ħω 时有效
- **与你研究的相关性:** **高** — 非绝热 + NQE 的简洁方案，可直接嵌入 GC 框架
- **原文链接:** https://arxiv.org/abs/2311.08779
- **PDF 状态:** ✅ 已下载

### 5. Zhang2025 — RPMD Rate Theory for H2 Desorption from Pt(111)
- **来源:** Precis. Chem. (10.1021/prechem.4c00099)
- **作者:** Yaolong Zhang, Bin Jiang (USTC)
- **核心问题:** RPMD 能否定量预测 H2 在 Pt(111) 上的解离和重组？
- **方法创新:** RPMD 反应速率理论 + 高维 PES（神经网络势）
- **关键结果:** 解离速率因子 2 以内与实验吻合；ZPE 主导 NQE，隧穿贡献小
- **与你研究的相关性:** **中-高** — RPMD 在表面反应的应用基准案例
- **原文链接:** https://doi.org/10.1021/prechem.4c00099
- **PDF 状态:** ✅ 已下载

### 6. Zhou2024 — EEP-MLFF for Constant Potential Cu/MoS2
- **来源:** JPCC (10.1021/acs.jpcc.4c08188)
- **作者:** Guozhi Zhou, Feng Hao (HIT)
- **核心问题:** 恒电位 MLFF 能否避免传统 ESM 的电荷泄漏问题？
- **方法创新:** EEP-MLFF（U 为显式输入 + SO3 Power Spectrum 描述符）
- **关键结果:** Cu 团簇在 V < -0.1V 时形成；平躺→倾斜二聚体转变；pCOHP 揭示强 Cu-Cu 键
- **与你研究的相关性:** **中** — 恒电位 MLFF（Cu/MoS2 体系），方法有价值
- **原文链接:** https://doi.org/10.1021/acs.jpcc.4c08188
- **PDF 状态:** ✅ 已下载

### 7. Joll2025 — Fe(II)/Hematite Reactive Neural Network Potential
- **来源:** JPCL (10.1021/acs.jpclett.4c03252) / PMC11789133
- **作者:** Simon T. Joll, et al.
- **核心问题:** 反应性 NNP 能否准确描述 Fe(II)/Hematite 水界面动力学？
- **方法创新:** c-NNP 对比经典 FF，不预设反应坐标
- **关键结果:** DFT 级精度（能量 RMSE < 5 meV/atom）; 水交换 k = 1.8×10⁸ s⁻¹; Fe²⁺ 无氧化
- **与你研究的相关性:** **中** — MLFF 界面应用案例，但缺乏 CPM 和 NQE 成分
- **原文链接:** https://doi.org/10.1021/acs.jpclett.4c03252
- **PDF 状态:** ✅ 已下载

## 💡 今日亮点
- **最值得精读的一篇:** Sun2024 — 首个同时实现 GC 系综 + NQE + 充分采样的电化学模拟框架，DP-Ne MLFF 设计具有直接复用价值
- **可能与你研究论点冲突的一篇:** Bi2023 指出 EF-RPMD 仅在 Γ > ħω 时有效，Sun2024 的 GC-HMC + PIMC 框架目前完全忽略非绝热效应——两者结合需要仔细处理适用边界
- **值得追踪的作者或团队:** Shenzhen Xu (PKU) — GC-HMC 方法有望拓展到恒 pH 条件; Wenjie Dou (Westlake) — 非绝热动力学+NQE 方法论; Bin Jiang (USTC) — RPMD 在表面反应的系统应用; Feng Hao (HIT) — 恒电位 MLFF

## 📌 Key Gap
目前尚无方法同时处理 GC 系综 + NQE + 非绝热效应。Sun2024 覆盖 GC + NQE 但缺非绝热；Bi2023 覆盖 NQE + 非绝热但缺 GC 系综。将 EF-RPMD 嵌入 GC-HMC 框架是自然的下一步。此外 Bunting2025 发现 NQE 金属依赖性（Pt 有、Au 无），提示 NQE 贡献大小与金属电子结构相关，这是 GC-NQE 框架需纳入的维度。
