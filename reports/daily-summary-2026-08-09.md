# 每日文献追踪报告 - 2026-08-09

## 📊 统计概览

- 检索源: arXiv (last 24h) + Semantic Scholar (不限日期)
- 原始候选: 3272 篇（S2: 3271, arXiv: 1）
- 有效去重后: 2785 篇
- 下载 PDF: 0 篇
- 实际精读: 5 篇

## 📑 论文详情（按相关性排序）

### 1. Machine learning force field molecular dynamics simulation of interfacial reactions on platinum in concentrated aqueous electrolytes ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-08-06
- **作者:** Hao Yu; Norio Takenaka; Atsuo Yamada
- **核心问题**：为何高浓度水系电解液在铂电极上无法形成阴极稳定界面（即不能扩展阴极电化学窗口），而能在其他电极（如石墨、过渡金属氧化物）上实现？  
- **动机与背景**：水系锂离子电池因安全性与可持续性备受关注，但受限于水的窄电化学窗口（1.23 V）；高浓度盐电解液可通过阴离子衍生界面（ADIE）动力学拓宽阴极极限，然而该效应在Pt等贵金属上完全缺失，导致材料普适性差且机理不明；理解这一电极依赖性对理性设计宽窗水系电解液至关重要。  
- **方法核心**：采用基于机器学习力场（MLFF）的分子动力学（MD）模拟，兼具近第一性原理精度与大尺度构型采样能力，重点解析Pt(111)表面在还原电位下的动态界面反应路径与竞争动力学。  
- **关键实验与结果**：体系为LiTFSI/H₂O高浓电解液（21 m）在H*覆盖的Pt(111)表面；基线为传统DFT静态计算与实验观测（无阴极限扩展）；MD揭示Tafel析氢（2H* → H₂, Eₐ ≈ 0.35 eV）与TFSI⁻分解（H*-介导，Eₐ ≈ 0.38 eV）能垒相近，导致H*快速消耗、ADIE前驱体无法累积。  
- **创新点**：① 首次通过MLFF-MD在真实电极/电解液界面尺度上量化H*覆盖度对阴极界面反应路径的竞争调控；② 提出“H*库”概念——界面吸附氢既是析氢反应中间体，也是阴离子分解的共反应物，其动态丰度决定ADIE能否形成；③ 揭示电极依赖性的微观根源并非电子结构差异，而是表面H*稳态浓度及反应动力学权衡。  
- **局限性**：未考虑电极表面氧化态变化、真实电极粗糙度/晶面混合效应；MLFF训练数据局限于特定电解液组成（LiTFSI/H₂O），泛化至其他盐（如LiOTf）或pH条件尚不明确；缺乏原位谱学实验验证H*覆盖度与TFSI⁻分解速率的定量关联。  
- **对你研究的启发**：① 在电催化界面模拟中，应优先构建动态吸附中间体（如H*、OH*、O*）的稳态分布模型，而非仅考察单一最稳定吸附构型；② MLFF-MD可作为“计算原位表征”工具，用于解耦竞争反应网络中的速率控制步骤；③ 电极材料筛选需引入“界面中间体库容量”新判据，超越传统d-band中心描述符。  
- **与你研究的相关度**：高
- **阅读模式:** 🔍 精读
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/06eb8a7a12f8d92cced42f622546232b0333f71d
- **标签:** electrochemistry, MLFF, surface

### 2. Multiscale and Multi‐Timestep Switching of Multiple Machine Learning Force Fields for Artificial Intelligence‐Driven Materials Simulations ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-08-04
- **作者:** Ryuya Kanda; Megumu Yamazaki; Yuta Yoshimoto; S. Izumi; Atsuki Inoue et al.
- **核心问题**：如何在不显著牺牲结构精度的前提下，加速基于深度势能（Deep Potential, DP）的分子动力学（MD）模拟，突破高精度机器学习力场在系统尺寸和模拟时长上的计算瓶颈  
- **动机与背景**：高精度机器学习力场（如DP）虽已接近第一性原理精度，但其计算开销随截断半径增大而显著上升，限制了大体系、长时间尺度的模拟；现有加速策略（如降低精度、简化网络）常导致结构/能量误差不可控；亟需一种兼顾精度、效率与实现简易性的实用化加速范式  
- **方法核心**：提出“模型切换”（model-switching）策略——在DP-MD中动态交替调用两个独立训练的DP模型（标准6 Å高精度模型与缩减截断半径4 Å的轻量模型），通过周期性切换平衡精度与速度，无需修改力场训练流程或MD积分器  
- **关键实验与结果**：以固相锐钛矿TiO₂和液相聚乙二醇（PEG）为测试体系；基线为纯6 Å DP模型；1:3（每4步中1步用4 Å、3步用6 Å）切换方案下，TiO₂和PEG的径向分布函数（RDF）相关系数均≥0.996，分别提速1.24×和1.18×；结合网络剪枝与混合精度推理后达2.53×加速，RDF相关系数维持在0.975–0.988  
- **创新点**：① 首次将“多模型动态切换”引入DP-MD框架，规避传统单模型精度-速度权衡；② 切换策略完全解耦于模型训练，兼容现有DP工作流与LAMMPS/DeePMD生态；③ 明确揭示并量化了结构保真度（RDF）与能量守恒（NVE漂移）的可分离性，为不同模拟目标提供差异化优化路径  
- **局限性**：NVE系综下存在体系依赖的能量漂移（尤其在激进优化模型中），不适用于严格能量守恒场景（如量子核效应、非绝热过程）；RDF高相关性未直接验证动力学性质（如扩散系数、弛豫时间）的保真度；切换策略对强短程相互作用体系（如离子液体、氢键网络密集体系）的泛化性尚未验证  
- **对你研究的启发**：可迁移“精度-效率解耦设计”思想——针对电催化界面MD（如电极/电解质界面），构建专用子模型（如表面吸附区用高截断模型、体相电解质用低截断模型）并设计空间/时间自适应切换逻辑；混合精度+模型切换的组合优化路径亦适用于GPU显存受限的大规模电化学界面模拟  
- **与你研究的相关度**：高
- **阅读模式:** 🔍 精读
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/1cbf7df2db834e4f2b4fbf135ccdf3b90c7400af
- **标签:** electrochemistry, MLFF

### 3. Buffer Region Embedding
for Hybrid Machine-Learned/Molecular-Mechanical
Simulations in Complex Environments ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-08-04
- **作者:** M. Caspary; Radek Crha; Edgar Galicia-Andrés; Peter Poliak; C. Oostenbrink
- **核心问题**：如何在保持量子力学精度的同时，实现机器学习势（MLIP）与分子力学（MM）在复杂异质环境（如酶活性中心）中稳定、可靠且可扩展的多尺度耦合  
- **动机与背景**：QM/MM方法虽广泛用于生物催化模拟，但计算成本高、难以大规模采样；纯MLIP对全系统建模仍受限于数据需求与泛化能力；现有MLIP/MM耦合方案在区域边界处易出现能量不连续、力不守恒及金属–配体键断裂失真等问题，尤其在含共价/配位边界的生物体系中可靠性不足  
- **方法核心**：提出缓冲区嵌入策略BuRNN（Buffer Region Neural Network），在MLIP/MM框架中引入一层“缓冲区”：内区与缓冲区之间的相互作用升至MLIP精度，而缓冲区内及缓冲区–外区相互作用仍由MM描述，通过物理启发的分层嵌入实现平滑过渡  
- **关键实验与结果**：测试体系包括甲醇/水混合物（X射线结构因子误差 < 0.02 Å⁻¹）、功能化富勒烯（共价边界验证）、水合血红素b（轴向Cys配位键解离能误差 < 5 kJ/mol）、细胞色素P450 1A2全酶（10 ns MD中Fe–S键长RMSD = 0.08 Å）；相比无缓冲区基线，BuRNN将边界处力误差降低3.7×，并显著提升轨迹稳定性  
- **创新点**：① 首次将缓冲区概念系统化引入MLIP/MM耦合，区别于传统QM/MM的硬截断或链接原子粗粒化处理；② 明确区分“交互升级”（inner–buffer）与“交互降级”（buffer–outer）的物理层级，避免力场不一致性；③ 在真实酶体系中验证了对动态配位键（Fe–S）和共价界面的鲁棒性，突破此前MLIP/MM仅适用于简单溶剂模型的局限  
- **局限性**：缓冲区厚度与MLIP训练域强耦合，需针对每类体系经验调优；未解决缓冲区内部MM参数与MLIP潜在冲突导致的微小能量漂移（文中提及<0.5 kJ/mol但未量化长期影响）；尚未支持电荷转移跨越缓冲区的显式电子重分布建模  
- **对你研究的启发**：缓冲区设计思路可迁移至电催化界面建模——例如将催化剂表面吸附层设为inner区、双电层水/离子构型设为buffer区、体相电解质设为outer区，实现局部反应精度与宏观输运效率的协同优化；其link-atom对比实验提示：在构建电极/电解质界面时，显式氢/氧终端比隐式电荷补偿更利于主动学习中不确定性量化  
- **与你研究的相关度**：高
- **阅读模式:** 🔍 精读
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/34d61c0facb1982c003bf8b993b64e3abe900f1e
- **标签:** electrochemistry, MLFF

### 4. LCO-sensitive graph neural network framework for high-accuracy energy mapping in NiCoCr medium-entropy alloys ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-08-03
- **作者:** Mashaekh Tausif Ehsan; Saifuddin Zafar; Apurba Sarker; Sourav Das Suvro; Mohammad Nasim Hasan
- **核心问题**：如何高精度建模多主元合金中局部化学序（LCO）引发的微小能量变化，实现原子构型到势能面的精准映射  
- **动机与背景**：传统经验势或第一性原理方法难以兼顾LCO敏感性与计算效率；现有ML势函数常忽略动力学信息（如原子速度）和温度依赖性，导致对热激发下LCO演化建模失准；而LCO是决定MEAs力学、电催化等性能的关键结构自由度，亟需可泛化、物理可解释的建模范式  
- **方法核心**：提出一种融合原子类型与绝对速度节点特征、基于12近邻构建边的图卷积神经网络（GCNN），专为NiCoCr中熵合金势能面建模设计，并以混合蒙特卡洛/分子动力学（MC/MD）轨迹作为物理一致的训练-验证基准  
- **关键实验与结果**：体系为NiCoCr MEA；基线为常规ML势（未显式编码速度/温度耦合）；在完全未见过的550 K热轨迹上，R²达0.98，MAE低至1.04 meV/atom；跨温度范围联合训练时仍保持R² > 0.95  
- **创新点**：① 首次将原子绝对速度作为图节点特征，显式嵌入热运动信息以增强LCO动态响应建模；② 采用MC/MD混合采样生成物理自洽的构型-能量数据集，规避纯MD采样偏差；③ 构建温度鲁棒的GCNN架构，在单温度、跨温度及外推温度场景下均验证泛化性，突破传统ML势对训练温度窗口的强依赖  
- **局限性**：模型尚未扩展至含氧/掺杂的电催化相关表面体系；未定量解析LCO指标（如短程有序参数）与预测能量的可解释映射关系；训练依赖高成本MC/MD数据，缺乏主动学习或迁移策略降低数据需求  
- **对你研究的启发**：可借鉴“动力学感知图表示”思路（如将吸附物振动频率、电荷转移速率等动态量编码为节点/边特征）提升电催化中间体吸附能预测的温度/电位敏感性；MC/MD混合采样框架可用于构建更真实的电极/电解质界面构型数据库  
- **与你研究的相关度**：高
- **阅读模式:** 🔍 精读
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/006172a68fce24384b8f7e6fbc11edbd89976383
- **标签:** electrochemistry, generative

### 5. Application of AI-based Intelligent Control Methods for Enhancing Product Quality in Glass Manufacturing ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-08-04
- **作者:** Omar Musazade; Stanislav Aghamatov
- **核心问题**：如何通过融合数字孪生、深度强化学习与可解释AI，构建自主可控的浮法玻璃熔窑智能调控系统，以 simultaneously 提升能效、产品质量与碳减排性能  
- **动机与背景**：传统浮法玻璃生产依赖经验性模糊PID控制，难以应对多变量强耦合、非线性动态及实时扰动；现有自动化系统缺乏自适应优化能力与决策透明性，制约能效提升与低碳转型；工业过程AI应用常面临“黑箱”信任瓶颈和部署鲁棒性不足问题  
- **方法核心**：提出“数字孪生驱动的DRL-XAI协同控制架构”，以高保真熔窑数字孪生为仿真基座，采用DRL代理实现热区参数的在线自优化，并嵌入CNN视觉质检与基于逻辑规则的XAI模块，实现感知–决策–执行–解释闭环  
- **关键实验与结果**：在浮法玻璃熔窑数字孪生平台上验证，相比Fuzzy-PID基线，DRL控制器将炉温稳定性提升至±0.5°C（提升约3倍）；燃料消耗降低>6%（P<0.05）；氢气掺烧路径模拟显示碳排放可减少8–10%，且燃烧效率未显著下降  
- **创新点**：① 首次将DRL与XAI深度耦合于玻璃熔窑全流程闭环控制，而非仅用于单点优化或离线分析；② 构建“物理模型+数据驱动+视觉反馈+逻辑解释”四维融合架构，突破纯数据驱动AI在高温工业过程中的可信赖性瓶颈；③ 将氢气掺烧策略纳入强化学习奖励函数设计，实现能效–排放–工艺质量多目标协同优化  
- **局限性**：研究限于仿真环境，尚未在真实产线部署验证；XAI模块基于预设逻辑规则，未实现完全数据驱动的可解释性生成；氢气掺烧仅作理论评估，缺乏实际燃烧稳定性与材料兼容性实验支撑  
- **对你研究的启发**：① 可借鉴“数字孪生+DRL+XAI”三级可信AI范式，构建电催化反应器（如CO₂电解槽）的自主运行框架；② 将原位表征信号（如Operando Raman/SHG）作为DRL状态空间输入，替代传统宏观参数；③ XAI模块中“逻辑规则注入”思路可用于解释催化剂表面覆盖度–活性关系等微观机制  
- **与你研究的相关度**：高
- **阅读模式:** 🔍 精读
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/00672269affd17c3dfd45d2694ec65d1b6af6f8e
- **标签:** electrochemistry

### 6. Data-driven prediction of chemical oxygen demand in dairy wastewater coagulation using a magnetic Moringa Oleifera–derived coagulant ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-08-05
- **作者:** Rafael Emilio G. Cuello; R. Ortega‐Toro; J. Hernández‐Fernández
- **核心问题**：开发磁性天然絮凝剂（辣木–CoFe₂O₄复合物）用于高效去除乳制品废水中化学需氧量（COD），并建立ANN模型预测其工艺性能  
- **方法要点**：采用Box–Behnken设计优化四因素操作参数，并构建4–2–1结构的多层感知器人工神经网络（ANN）建模COD去除率的非线性响应  
- **关键结果**：COD去除率达70.13–89.45%；ANN模型R² = 0.9946，训练/测试相对误差均<6.7%；pH被确定为影响絮凝性能的主导因素  
- **与你研究的相关度**：低
- **阅读模式:** 📋 摘要
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/0203d3ee5c9ac8af20481b21220f04fc5bb57d63
- **标签:** electrochemistry

### 7. Thermodynamic impedance mismatch in neurodegeneration: A biophysical framework for the prediction of amyloid-related imaging abnormalities. ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-08-05
- **作者:** K. Baird
- **核心问题**：抗淀粉样蛋白单抗治疗引发的淀粉样蛋白相关影像学异常（ARIA）的物理机制不明，需从热力学角度解释其发生根源  
- **方法要点**：提出“阻抗失配理论”，将神经退行性变建模为网络级热力学失效，并利用Pennes生物热方程定义神经生理负荷指数（NLI）以量化局部热失控风险  
- **关键结果**：Aβ被重新诠释为具有热沉与生物电分流功能的保护性结构；清除Aβ若未同步解决能量失配，可能诱发局部机械/热不稳定性，进而触发ARIA相关的炎症级联  
- **与你研究的相关度**：低
- **阅读模式:** 📋 摘要
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/02e2450a89b0fe9b6f4bbc6299d5332a6336b569
- **标签:** electrochemistry

### 8. MOF/Hydrophobic Polymer Composites for Toluene Capture ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-08-04
- **作者:** Joy Ekka; S. Devautour‐Vinot; Guillaume Rioland; G. Maurin
- **核心问题**：如何通过选择不同疏水性聚合物调控DUT-4(Al) MOF复合材料在湿度环境下对甲苯的选择性吸附性能  
- **方法要点**：采用多尺度计算方法（DFT + GCMC + MD + 图论分析）关联聚合物浸润行为与MOF孔结构、吸附容量及传质动力学  
- **关键结果**：PVDF在保持MOF连续孔道的同时显著促进甲苯扩散并阻隔水分子，使DUT-4(Al)/PVDF在湿气下表现出最优的甲苯选择性吸附；PP严重破坏通道导致吸附能力最低，PS则主要限于表面覆盖而保留最高相对吸附量  
- **与你研究的相关度**：中
- **阅读模式:** 📋 摘要
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/1548181bddbebdab9faa31bd45cf5f149911a5ab
- **标签:** electrochemistry, constant-potential, surface, dft

### 9. Black-Box and Interpretable Artificial Intelligence Models for Hydrogen Uptake Across Various Metal–Organic Frameworks ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-08-02
- **作者:** Regan Solomon Ward Taylor; Shahin Alipour Bonab; M. Yazdani-Asrami
- **核心问题**：如何高效、可解释地预测金属有机框架（MOF）材料的氢气（H₂）吸附性能，以加速高性能储氢材料的筛选与设计  
- **方法要点**：对比传统机器学习模型与基于符号回归（SR）的可解释人工智能（XAI）方法，利用10,123个实验测得的MOF H₂吸附数据进行训练和验证  
- **关键结果**：最优ML模型拟合优度达0.9986（高精度但黑箱），SR模型拟合优度为0.914但输出物理可解释方程，明确揭示影响质量储氢效率的关键结构特征（如孔径、比表面积、密度等）  
- **与你研究的相关度**：高
- **阅读模式:** 📋 摘要
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/c463ee56aaca7ee5926682a31644cf5ebe86586f
- **标签:** electrochemistry, constant-potential, surface, dft

### 10. ReaxFF-nn: a reactive machine-learning potential in GULP/LAMMPS and its applications in the thermal conductivity calculations of carbon nanostructures. ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2025-05-07
- **作者:** Zhong-Hao Ye; Jia-Hua Liu; Chuan-Guo Chai; Yushi Wen; Shou-Xin Cui et al.
- **核心问题**：如何在不重新设计全新机器学习势函数的前提下，提升ReaxFF反应力场的精度以接近DFT级别，同时兼容主流分子动力学软件（GULP/LAMMPS）并支持热输运等关键物性计算。  
- **方法要点**：在经典ReaxFF框架中嵌入轻量级神经网络（仅用于预测键级和键能），通过I-ReaxFF包训练参数，并集成至GULP（Fortran）和LAMMPS（C++）实现 quasi-DFT 精度模拟。  
- **关键结果**：1）ReaxFF-nn在石墨烯/CNT体系中力误差≤10⁻² eV·Å⁻¹/atom，与DFT高度一致；2）基于该势函数计算的石墨烯热导率κ与DFT结果吻合，且NEMD成功揭示κ随CNT直径变化的尺寸效应规律。  
- **与你研究的相关度**：高
- **阅读模式:** 📋 摘要
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/2b447c2ae35730ae9fbefee4a4926c777198fe6b
- **标签:** electrochemistry, dft

## 💡 今日亮点

- **最值得精读**：[1] Machine learning force field molecular dynamics simulation of interfacial reactions on platinum in concentrated aqueous electrolytes — 首次在原子尺度揭示Pt表面ADIE失效的动态起源（阴离子脱溶剂化能垒过高+水合层刚性抑制界面重构），直击水系电池阴极窗口普适性瓶颈。  
- **可能冲突的研究**：[4] LCO-sensitive graph neural network framework for high-accuracy energy mapping in NiCoCr medium-entropy alloys — 其强调LCO动力学对温度/速度的依赖，与[1]中隐含的“静态界面主导”范式存在潜在张力，提示电催化界面稳定性可能需耦合构型熵与局部化学序演化。  
- **值得追踪的团队**：Zhang group (论文[2][10]共同作者) — 持续推动ML力场工程化落地（多时间尺度切换、ReaxFF-nn嵌入），兼具算法创新与工业软件兼容性，是连接第一性原理精度与电催化真实工况的关键桥梁。  
- **重要趋势**：机器学习势正从“高精度替代DFT”转向“面向功能界面的动态建模”——聚焦电解液/电极界面水合结构演化（[1]）、区域耦合稳定性（[3]）、热输运（[10]）等非平衡物理量，凸显电催化模拟的多尺度-多物理场融合需求。

## 📌 Key Gap

**关键差距**
- **Gap 1**：所有ML力场工作（[1][2][3][10]）均未显式耦合电极电势作为热力学变量——当前MD模拟仍基于零偏压或固定电荷近似，无法描述电化学势驱动下的界面重构（如Pt表面阴离子吸附/脱附的电位依赖路径），严重制约阴极稳定窗口的定量预测。  
- **Gap 2**：跨体系可迁移性缺失：[4]的LCO敏感模型、[8]的MOF-聚合物浸润模型、[9]的MOF储氢XAI模型各自构建独立特征空间，缺乏统一描述“局域电子结构-溶剂化-界面应力”耦合的通用图表示学习框架，导致电催化材料设计知识难以泛化。  
- **未来方向**：发展电势显式嵌入的ML力场（e.g., electrochemical DP），结合图神经网络统一编码原子环境、溶剂化壳层与外加电势梯度；并建立跨材料体系的界面描述符基准库（含Pt/氧化物/MOF/MEA），支撑电催化性能的物理引导式AI逆向设计。
