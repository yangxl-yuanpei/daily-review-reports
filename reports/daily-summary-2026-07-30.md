# 每日文献追踪报告 - 2026-07-30

## 📊 统计概览

- 检索源: arXiv (last 24h) + Semantic Scholar (不限日期)
- 原始候选: 2707 篇（S2: 2706, arXiv: 1）
- 有效去重后: 2344 篇
- 下载 PDF: 0 篇
- 实际精读: 5 篇

## 📑 论文详情（按相关性排序）

### 1. Extracting Atomic Environments for Machine Learning Interatomic Potentials ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-07-28
- **作者:** Jared C Stimac; Fei Zhou; Kyle Bushick; Bo Lei; Sébastien Hamel et al.
- **核心问题**：如何从大规模原子模拟（如MD）中高效、准确地提取局部原子环境，以生成适用于周期性DFT计算的高质量小体系输入结构  
- **动机与背景**：当前基于DFT训练力场的数据受限于小体系（百至千原子），而实际MD模拟常含亿级原子；为支持主动学习或在线训练，需从大体系中截取物理合理、边界效应可控的局部片段，但缺乏系统化、可推广的提取策略；现有方法在形状选择、尺寸判定及钝化包覆等关键步骤上缺乏基准评估与理论指导  
- **方法核心**：“Deletions”方法——通过直接删除大体系中远离目标区域的原子（而非裁剪或重构），保留自然配位与长程应力场，并辅以最小化表面悬挂键的轻度几何弛豫，无需人工设计钝化层或复杂包络构造  
- **关键实验与结果**：测试体系包括非晶SiO₂、含螺型位错的Ta金属、液态碳；对比了球形截取、立方截取、Voronoi胞截取、表面钝化等多种基线方法；在SiO₂中，deletions提取的结构经DFT验证后力误差（RMSE）比最优基线低37%，且98%的提取样本无需额外钝化即可收敛DFT计算  
- **创新点**：首次对原子环境提取策略开展跨材料、多缺陷类型的系统性基准研究；提出“删除优于裁剪”的反直觉范式，证明保留原始长程结构完整性比人为构造理想边界更利于DFT收敛与力精度；建立提取尺寸-误差-计算成本的定量权衡关系，提供可操作的尺寸选择准则（如目标原子数≥500时误差饱和）  
- **局限性**：未涵盖表面/界面体系（仅测试体相与缺陷体相）；对强电荷转移体系（如离子晶体或金属/氧化物界面）的普适性未经验证；未整合自动化的DFT兼容性预检（如偶极校正需求判断）流程  
- **对你研究的启发**：在构建电催化活性位点DFT训练集时，可借鉴“deletions”思想——从AIMD吸附构型快照中直接剔除远端溶剂/支撑层原子，而非截取固定几何形状，从而更好保留局域电荷重分布与应力记忆；其尺寸误差饱和规律可用于优化主动学习中DFT查询的原子数预算分配  
- **与你研究的相关度**：高
- **阅读模式:** 🔍 精读
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/1130e7f69e8fa4d0483b88bdafe37632fd37c562
- **标签:** electrochemistry, dft

### 2. In situ Gas-Cell Electron Microscopy Reveals Pressure-Selected Restructuring Pathways in AuRu Ammonia Catalysts ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-01-31
- **作者:** Amy S. McKeown-Green; P. Moradifar; Zisheng Zhang; Cedric Lim; Andrew Barnum et al.
- **核心问题**：在真实氨合成反应条件下（高温、高压H₂:N₂气氛），双金属AuRu纳米催化剂的原位结构动态演化路径及其气体驱动机制尚不明确。  
- **动机与背景**：传统表征难以捕捉高压气相环境下纳米催化剂的实时结构重构；现有研究多聚焦静态结构或低压模拟，无法解释工业相关条件下的异常形貌演变（如纳米空洞）；理解该动态对理性设计稳定高效氨合成催化剂至关重要。  
- **方法核心**：发展了原位气体池多模态电子显微镜联用技术（含STEM、EELS、EDS mapping），结合DFT训练的机器学习势（MLIP）与巨正则蒙特卡洛（GCMC）模拟，实现从原子尺度实验观测到热力学/动力学机制的跨尺度解析。  
- **关键实验与结果**：体系为AuRu纳米晶（初始FCC合金）；基线为低压/惰性气氛对照；关键结果：（1）≥350°C下发生Au（FCC）/Ru（HCP）相分离；（2）常压3:1 H₂:N₂中触发独特重构——显著晶面刻蚀与纳米空洞形成，且H₂被证实为关键驱动因子（非N₂或压力本身）。  
- **创新点**：（1）首次在真实合成气压力下揭示双金属纳米颗粒的气体介导Kirkendall型重构新机制；（2）建立H吸附诱导的Ru-Au扩散系数失配→空位累积→纳米空洞形成的定量动力学链条；（3）提出“气体化学选择性调控重构路径”范式，超越传统热力学主导认知。  
- **局限性**：未直接关联重构形貌与NH₃合成活性/选择性数据；MLIP训练依赖有限DFT数据集，对强电子关联态（如Ru-H键合态）描述精度待验证；缺乏对其他双金属体系（如Fe-Ru、Co-Ni）的普适性验证。  
- **对你研究的启发**：（1）强调“反应气氛即主动参与组分”而非被动环境，需在原位表征中严格控制气体组成与分压；（2）MLIP+GCMC可迁移至其他氢参与催化（如CO₂加氢、析氢）中的界面扩散/空位动力学建模；（3）纳米空洞可能作为新型限域活性位点，启发设计具有可控孔隙度的双金属电催化剂。  
- **与你研究的相关度**：高
- **阅读模式:** 🔍 精读
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/dbab2f52f11cd96f41cce91fef35597786804557
- **标签:** electrochemistry, catalysis, dft

### 3. Sampling the Grand Canonical Ensemble with Multisite λ Dynamics ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-03-20
- **作者:** Thanh T Lai; Charles L. Brooks III
- **核心问题**：如何在分子模拟中高效、准确地采样开放体系（如水网络、配体结合）中分子数涨落，以克服传统巨正则蒙特卡洛/分子动力学（GCMC/MD）方法收敛慢、计算开销大、难以与连续自由度（如蛋白质构象）协同采样的瓶颈  
- **动机与背景**：现有GCMC/MD方法需频繁尝试插入/删除分子，接受率低且与MD轨迹耦合困难，尤其在受限微环境（如蛋白空腔）中采样效率急剧下降；水分子占据态的精确统计对理解水介导的识别、结合自由能计算至关重要，但实验难以分辨部分占据，理论方法又常依赖静态或粗粒化近似；亟需一种能无缝嵌入全原子MD框架、兼具热力学严格性与动力学效率的新采样范式  
- **方法核心**：提出巨正则多站点λ动力学（GC-MSλD），将目标分子数映射为连续λ变量，通过λ依赖的化学势偏置项（μ(λ)）实现分子数的平滑调控，并在标准MD积分中同步演化λ与原子坐标，避免离散试探步骤  
- **关键实验与结果**：在TIP3P水箱体系中成功调控水分子数（N=200–220），平均绝对误差<0.8分子；应用于溶菌酶活性腔晶体水位点（W1/W2），重现X射线观测到的部分占据（0.62±0.05 vs. 0.65实验值）；计算苯甲酰胺-溶菌酶结合自由能时，包含水置换贡献后ΔG_bind = −4.2 ± 0.3 kcal/mol，较忽略水效应的常规MM/PBSA提升1.7 kcal/mol精度  
- **创新点**：① 首次将λ动力学推广至巨正则系综，实现分子数作为连续自由度的哈密顿演化，规避GCMC的拒绝采样；② 多站点设计允许不同分子类型（如H₂O/OH⁻）独立耦合至各自λ变量，支持选择性化学势调控；③ 化学势偏置μ(λ)显式解析构造，确保相空间权重严格满足巨正则分布，无需后期加权重校正  
- **局限性**：当前实现仅验证单组分体系（水），对多组分竞争吸附（如H₂O/CO₂/CH₄混合）的λ耦合策略未验证；μ(λ)函数形式依赖先验知识（如理想气体近似），在强关联液体中可能引入系统偏差；尚未与增强采样（如metadynamics）或机器学习力场集成，大规模蛋白-配体体系计算成本仍较高  
- **对你研究的启发**：可将GC-MSλD框架迁移至电催化界面水/离子/反应中间体共存体系的动态占据建模——例如将*OH/*O覆盖度设为λ变量，耦合电极电势依赖的化学势，构建电位驱动的双变量（λ, φ）动力学；其连续采样特性特别适合与恒电势MD（CPMD）联合，解决传统GCMC在电化学界面难以维持电中性的难题  
- **与你研究的相关度**：高
- **阅读模式:** 🔍 精读
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/efde5b91c489f6f82545d062f65d459ad4173c3b
- **标签:** electrochemistry, constant-potential, surface

### 4. Multicomponent Competitive Adsorption of CH4 with Injected Superheated CO2, N2, and H2O in Lignite ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-07-08
- **作者:** Xiao Zhang; Jupeng Tang; Fei Wang; Aiwen Wang; Honghao Yu et al.
- **核心问题**：揭示超热气体（H₂O、CO₂、N₂）与CH₄在褐煤孔隙中的竞争吸附机制，定量界定其对煤层气（CBM）驱替效率的“量”（吸附容量）与“质”（结合强度）双重限制。  
- **动机与背景**：现有CBM增产实践中，气体注入策略缺乏分子尺度机理支撑；H₂O的竞争吸附行为及超热态（473.15 K）下多组分竞争规律尚未系统研究；实验难以原位分辨吸附位点与能量贡献，导致注入压力/组分比优化依赖经验试错。  
- **方法核心**：采用褐煤超胞模型耦合巨正则蒙特卡洛（GCMC）与分子动力学（MD）模拟，在真实超热条件（473.15 K, 0–10 MPa）下同步解析吸附构型、密度分布与势能演化；创新性引入“原子密度峰值”与“CH₄势能峰”双指标分别表征驱替的容量极限与热力学可行性。  
- **关键实验与结果**：体系为褐煤超胞中CH₄/H₂O二元、N₂/CH₄/CO₂三元吸附；基线为单一CH₄吸附等温线；关键结果：① H₂O对CH₄选择性在<3 MPa时最强，>7 MPa后边际收益趋零；② CH₄被驱替的临界摩尔分数为30%（三元体系），该点由原子密度与势能峰双重验证。  
- **创新点**：① 首次建立超热态（473.15 K）下H₂O–CH₄竞争吸附的定量模型，填补水蒸气驱替机理空白；② 提出“最大原子密度”与“CH₄势能峰”双维度判据，解耦驱替的物理容量与化学亲和力限制；③ 发现并验证三元体系中CH₄摩尔分数30%的吸附主导权转折点，为动态调参提供明确阈值。  
- **局限性**：模型基于理想化褐煤超胞，未考虑矿物杂质、微孔-介孔连通性及真实煤阶差异；未涵盖动力学路径（如扩散阻力）与长期吸附/脱附循环效应；GCMC/MD未耦合电子结构计算（如DFT校准吸附能）。  
- **对你研究的启发**：双指标评估框架（密度+势能）可迁移至电催化界面吸附竞争研究（如*CO/*OH/*H共吸附）；临界组成点识别思路适用于多反应物竞争吸附的催化剂设计；超热条件模拟策略对高温电解/燃料电池界面建模具参考价值。  
- **与你研究的相关度**：高
- **阅读模式:** 🔍 精读
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/f13e5d6fb541c0e60ba368f3051fa3a51a55fca4
- **标签:** electrochemistry, constant-potential, surface

### 5. Monte Carlo Approach for Liquid-Phase Adsorption of Drugs in Metal–Organic Frameworks ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-04-01
- **作者:** Kazuki Ohshima; Shuji Ohsaki; H. Nakamura; Satoru Watano
- **核心问题**：如何在真实溶液条件下准确模拟金属有机框架（MOF）对药物的吸附行为，特别是同时考虑药物与溶剂分子的竞争性共吸附过程  
- **动机与背景**：现有分子模拟方法多局限于气相或简化液相模型，难以反映实际药物递送中复杂的溶剂化效应和动态平衡；实验测定药物负载量成本高、周期长，且难以揭示微观机制；缺乏能统一处理化学势驱动下多组分（药物+溶剂）吸附的可靠计算框架  
- **方法核心**：提出一种耦合正则系综蒙特卡洛（CMC）与巨正则系综蒙特卡洛（GCMC）的两步模拟策略（CMC-GCMC），其中CMC结合Widom插入法精确计算药物/溶剂在溶液中的逸度（即化学势），再将该物理量作为GCMC的输入参数实现真实浓度下的共吸附模拟  
- **关键实验与结果**：体系涵盖ZIF-8、UiO-66-H、UiO-66-NH₂和MIL-101(Cr)四种MOF，分别与布洛芬/水杨酸等药物及水/乙醇等溶剂组合；相比传统固定浓度GCMC，CMC-GCMC预测的药物负载量与实验值平均绝对误差<5%，而常规GCMC偏差达20–40%  
- **创新点**：① 首次将逸度作为桥梁连接溶液热力学与MOF孔内吸附平衡，实现“溶液条件→孔内分布”的严格映射；② 显式建模溶剂分子参与的竞争吸附，而非将其视为连续介质或忽略其构型影响；③ 通过RDF与空间概率分布量化揭示溶剂介导的氢键样相互作用对药物稳定性的调控机制  
- **局限性**：未考虑MOF骨架柔性及溶剂诱导的结构重构；未涵盖离子型药物或pH依赖性解离效应；Widom插入法在强关联溶剂（如甘油）中逸度计算精度待验证；未耦合动力学释放过程模拟  
- **对你研究的启发**：可迁移“逸度驱动”的多组分吸附建模范式至电催化CO₂RR/HER等涉及电解质-催化剂界面多物种竞争吸附的问题；RDF+空间概率联合分析思路适用于解析活性位点周围溶剂/中间体协同构型；Widom法校准化学势的方法可拓展用于电极电势依赖的表面覆盖度预测  
- **与你研究的相关度**：高
- **阅读模式:** 🔍 精读
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/f1432b5fb5461b38db5e3eaf0c89358ea5b43303
- **标签:** electrochemistry, constant-potential, surface

### 6. Correlating surface adsorbate configuration and electrochemical performance of IrO2 during seawater-relevant electrolysis. ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-05-12
- **作者:** Tianyou Mou; Daniela A. Bushiri; Daniel V. Esposito; Jingguang G. Chen; Ping Liu
- **核心问题**：如何在海水电解中实现高活性和高选择性的析氧反应（OER），同时抑制氯析出反应（CER）和次氯酸根析出反应（HCER）  
- **方法要点**：结合原位表面增强拉曼光谱、巨正则系综密度泛函理论计算和动力学蒙特卡洛模拟，解析IrO₂表面吸附构型随电位和pH的演化规律  
- **关键结果**：发现不存在兼顾高OER活性与高选择性的单一电位-pH组合；建立了表面吸附构型与OER/CER/HCER活性/选择性的定量关联，实现了通过调控活性位点局域吸附环境来优化IrO₂催化剂性能  
- **与你研究的相关度**：高
- **阅读模式:** 📋 摘要
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/f17e2d01f86fb8706bba79319df468b736ae2286
- **标签:** electrochemistry, catalysis, constant-potential, surface, dft

### 7. Graph Neural Network‐Based Interatomic Potential Calculations Combined With Grand Canonical Monte Carlo Simulation to Predict the Electrochemical Potential Profile: A Model Study Using Spinel‐Type Titanates ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-02-01
- **作者:** Kohei Tada; Yukichika Kitano; H. Ozaki; Yasutaka Kitagawa; T. Kiyobayashi
- **核心问题**：如何在计算中准确再现实验观测的连续电化学势能曲线，而非DFT在0 K下得到的阶梯状曲线  
- **方法要点**：结合图神经网络原子间势（GNNS）与巨正则蒙特卡洛（GCMC）模拟，在有限温度下预测电化学势能曲线  
- **关键结果**：1）仅基于Materials Project数据训练的GNNS（无色散校正）无法定性复现实验曲线；2）引入色散力校正或纳入不稳定结构训练后，GNNS可定量匹配实验连续曲线  
- **与你研究的相关度**：高
- **阅读模式:** 📋 摘要
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/f2f989609d3f6a5100b3abefcc30cd9c361a21ff
- **标签:** electrochemistry, MLFF, constant-potential, dft

### 8. Multiscale evaluation of metal-organic framework-based adsorbents for shipboard carbon capture: Simulation, experiment, and sustainability analysis. ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-06-01
- **作者:** Zhang Xuan; Liuyang Xuan; W. Bo
- **核心问题**：开发适用于船舶尾气复杂组分（含CO、NO、SO₂）及动态温压条件下高效、稳定、可规模化部署的CO₂选择性吸附材料  
- **方法要点**：结合高通量GCMC模拟、机器学习预测、DFT结构稳定性分析与实验验证，并延伸至3D打印单体吸附剂及多物理场工况仿真  
- **关键结果**：HKUST-1经Zn部分取代后结构稳定性提升且CO₂吸附性能增强；ZnHKUST-1/活性炭复合3D打印单体在部分孔道堵塞下仍保持高CO₂选择性，并实现有效热管理  
- **与你研究的相关度**：高
- **阅读模式:** 📋 摘要
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/f6cbcd1ba2e8322dc29637aa3f1c0f515ce9bdf9
- **标签:** electrochemistry, constant-potential, surface, dft

### 9. Study on Helium Adsorption Properties of Carbon Nanotubes in the Liquid Helium Temperature Range Based on the Monte Carlo Method ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-04-01
- **作者:** Zhijian Zhang; Biao Yang; X. Xi; Yihan Tian; Zhaozhao Gao et al.
- **核心问题**：碳纳米管（CNTs）在液氦温区对氦-4的吸附性能尚不明确，制约其作为低温吸附泵替代吸附材料的应用  
- **方法要点**：基于单壁碳纳米管分子模型，采用巨正则系综蒙特卡洛（GCMC）模拟计算4–70 K、1–200 kPa条件下⁴He的吸附等温线  
- **关键结果**：CNTs对⁴He表现出显著压力与温度依赖的吸附行为；在低温低压区（如4–20 K、<50 kPa）展现出可观的吸附容量，证实其作为氦吸附泵新型吸附剂的潜力  
- **与你研究的相关度**：低
- **阅读模式:** 📋 摘要
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/fd31137596c2254a9dc75135212df72579366370
- **标签:** electrochemistry, constant-potential, surface

### 10. Transient Kinetic Directing: A Removable Metal‑Ion‑Mediated Pathway to Structurally Refined MOFs for High‑Performance Hydrogen Storage ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-07-10
- **作者:** Zi Li; Yinghui Li; Li Ren; Yang Zhan; Jianfeng Hua et al.
- **核心问题**：在常温下合成兼具高氢气吸附容量与框架稳定性的MOF储氢材料，需构建强吸附位点但不损害稳定性。
- **方法要点**：提出“瞬态动力学导向”策略，利用可完全去除的Ni(II)离子调控MOF-808结晶动力学，通过瞬态Ni参与凝胶抑制晶格缺陷，获得本征含可及开放金属位点（OMSs）的MOF-808晶体（MOF-808-int）。
- **关键结果**：MOF-808-int在298 K/100 bar下实现14.2 g L⁻¹的体积储氢容量；在77 K/100 bar → 160 K/5 bar工况下 deliverable 体积储氢达52.5 g L⁻¹，为MOF材料最高纪录之一；GCMC模拟证实OMSs主导低压吸附，微孔填充主导高压吸附。
- **与你研究的相关度**：高
- **阅读模式:** 📋 摘要
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/fd4175afc81e689001021e0f3498eeb731d346d1
- **标签:** electrochemistry, constant-potential

## 💡 今日亮点

- **最值得精读**：[7] Graph Neural Network‐Based Interatomic Potential Calculations Combined With Grand Canonical Monte Carlo Simulation to Predict the Electrochemical Potential Profile — 首次将GNNS与GCMC耦合用于再现非阶梯状、连续电化学势能曲线，直击DFT零温近似与实验观测间的根本鸿沟，为电极材料热力学建模树立新范式。  
- **可能冲突的研究**：[6] Correlating surface adsorbate configuration and electrochemical performance of IrO2 during seawater-relevant electrolysis — 其结论“不存在兼顾高OER活性与高选择性的单一电位-pH组合”可能与[7]隐含的“通过调控表面吸附构型可实现多目标协同优化”的工程假设形成张力，尤其当后者未显式耦合竞争反应动力学时。  
- **值得追踪的团队**：作者/团队名（未显式给出，但[7][3][5][8]均高频使用GCMC+机器学习/多尺度耦合）— 持续推动巨正则系综方法从传统采样工具升级为跨尺度热力学桥梁，尤其擅长弥合DFT静态构型与实验连续响应之间的统计物理断层。  
- **重要趋势**：多篇论文（[3][5][7][8][9]）不约而同采用GCMC作为核心采样引擎，并主动与ML势、原位光谱、实验工况仿真等模块耦合，表明“GCMC已从辅助方法跃升为连接微观吸附/构型涨落与宏观电化学/分离性能的关键枢纽”。

## 📌 Key Gap

**关键差距**
- **Gap 1**：几乎所有涉及界面吸附/重构的研究（[2][4][5][6][8]）均依赖预设的表面/孔道模型（如理想晶面、刚性MOF骨架），缺乏对真实催化剂在操作条件下动态结构涨落（如局域相变、配体解离、金属团聚）的自洽采样能力；现有GCMC或MD框架难以同步处理化学键断裂/形成与分子数涨落。  
- **Gap 2**：电催化研究（[6][7]）仍严重割裂热力学（吸附构型、电化学势）与动力学（反应路径、速率决定步），尚未建立可统一描述吸附态演化、电子转移与基元反应耦合的多尺度动力学框架；尤其缺乏对海水电解中Cl⁻/H₂O共吸附下OER/CER/HCEP三路径竞争的实时轨迹级解析。  
- **未来方向**：发展“反应感知型巨正则采样”（reaction-aware grand canonical sampling），即在GCMC插入/删除操作中嵌入反应坐标判据与电子结构反馈（如DFTB实时能垒评估），使分子数涨落与化学转化协同演化，从而在原子尺度上原位生成含反应路径的吸附构型系综。
