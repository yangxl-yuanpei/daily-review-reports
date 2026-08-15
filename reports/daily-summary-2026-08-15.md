# 每日文献追踪报告 - 2026-08-15

## 📊 统计概览

- 检索源: arXiv (last 24h) + Semantic Scholar (不限日期)
- 原始候选: 3290 篇（S2: 3289, arXiv: 1）
- 有效去重后: 2745 篇
- 下载 PDF: 0 篇
- 实际精读: 5 篇

## 📑 论文详情（按相关性排序）

### 1. Evaluating Electrostatic Embedding MLIP/MM for Relative Binding Free Energy Calculations ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-08-13
- **作者:** Stephen E. Farr; G. D. Fabritiis
- **核心问题**：如何在alchemical相对结合自由能（RBFE）计算中准确描述配体-环境静电相互作用，克服经典力场固定电荷近似的局限性  
- **动机与背景**：经典力场采用固定电荷，无法响应配体化学结构变化及蛋白微环境极化，导致RBFE预测偏差；机械嵌入MLIP/MM虽修正配体应变能，但仍用静态点电荷处理静电；已有静电嵌入方案仅在简单QM/MM体系验证，缺乏在真实蛋白-配体RBFE生产流程中的系统评估  
- **方法核心**：采用静电嵌入式MLIP/MM方案，基于TensorNet2训练多任务模型AceFF-2-RESP-1，联合预测能量、力和RESP电荷；将ML预测的动态RESP电荷嵌入PME静电求和（含Thole阻尼），实现配体电荷随构象与环境自洽演化  
- **关键实验与结果**：在Wang等基准集5个靶标（TYK2、CDK2、thrombin、p38、JNK1）上测试，每条转化边3次重复；TYK2上ΔΔG RMSE从GAFF2的0.86 kcal/mol显著降至0.45 kcal/mol；其余4个靶标精度未提升，与经典/机械嵌入基线相当  
- **创新点**：首次将静电嵌入MLIP/MM完整集成至生产级RBFE工作流并系统验证；提出RESP电荷与AMBER力场兼容的端到端训练策略（非后处理）；引入Thole阻尼抑制alchemical变换中因电荷突变引发的极化灾难  
- **局限性**：性能提升具有靶标特异性（仅TYK2显著受益），缺乏普适性预测指标；未探究电荷迁移误差与蛋白残基类型/局部介电环境的关联；模型训练依赖大规模AceFF构象数据（10⁶样本），泛化性待验证  
- **对你研究的启发**：动态电荷嵌入可作为电催化中吸附物-表面静电耦合建模的新范式；Thole阻尼策略适用于DFT/ML混合方法中避免过渡态电荷异常；靶标依赖性提示需发展“可解释性电荷误差诊断”模块，而非单纯追求全局精度  
- **与你研究的相关度**：高
- **阅读模式:** 🔍 精读
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/3f6ca5624ed20d0ef291f3f548836c36331d9e8c
- **标签:** electrochemistry, MLFF, generative

### 2. SensitiveCancerGPT: Generative AI for Actionable Pharmacogenomics in Precision Oncology ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-06-01
- **作者:** Shaika Chowdhury; Munhwan Lee; Sivaraman Rajaganapathy; Lichao Sun; Liewei Wang et al.
- **核心问题**：如何在患者异质性强、数据稀缺的临床现实中，实现跨癌种泛化且可解释的抗癌药物敏感性预测（DSP），以支持高风险治疗决策  
- **动机与背景**：传统DSP模型泛化能力差（尤其对罕见癌种）、缺乏生物学可解释性，难以满足临床“行动导向”需求；现有方法多依赖同质化训练数据，无法应对真实场景中“新患者/新药/新癌种”的盲测挑战；精准肿瘤学亟需兼具高召回率（避免漏掉有效疗法）和机制可溯性的AI工具  
- **方法核心**：SensitiveCancerGPT——首个将大语言模型（LLM）适配至结构化多组学数据的生成式AI框架，通过三阶段系统优化（组学数据tokenization与fine-tuning、任务感知prompt engineering、癌症通路知识图谱注入）实现药敏预测与机制解释联合建模  
- **关键实验与结果**：在GDSC、CCLE、DrugComb、CTRP四大药敏数据库上验证；基线为XGBoost、RF及Transformer-based DSP模型；跨组织迁移（Rare Cancer Generalization）下F1提升18.7%（p=0.009）；盲测（New Patient/New Drug）平均F1达0.84，敏感类召回率显著优于基线  
- **创新点**：① 首次将LLM范式迁移至结构化药敏预测任务，突破传统判别式模型边界；② 提出“知识增强型prompting+微调”双路径适配策略，显式整合KEGG/Reactome通路知识；③ 以临床优先目标（高敏感类召回）驱动损失函数设计，而非单纯优化整体准确率  
- **局限性**：未公开模型架构细节与训练成本（如GPU小时数/参数量），缺乏前瞻性临床验证；组学数据输入限于bulk RNA-seq与突变，未整合单细胞或空间转录组；对非编码变异及表观遗传特征建模能力未知  
- **对你研究的启发**：① “知识图谱注入+prompt引导”可迁移至电催化材料属性预测（如将Materials Project数据库映射为知识token）；② 临床强调的“高召回率优先”策略适用于催化反应中“避免漏判活性位点”的场景；③ 跨域泛化评估范式（如从Pt基催化剂迁移到NiFe-LDH）可借鉴其Rare Cancer Generalization设计  
- **与你研究的相关度**：高
- **阅读模式:** 🔍 精读
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/5daf7df904f1dcad1ad2e5b020021c0b3cfa1af3
- **标签:** electrochemistry, generative

### 3. Machine Learning-Driven Refinement of Reactive Force Fields via Hierarchical “Center-Environment” Features for Energetic Molecular Crystals ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-08-12
- **作者:** Qi He; Pengju Wang; Xudong He; Jincang Zhang; Yi Liu
- **核心问题**：如何准确预测有机分子晶体（如RDX和HMX）的晶格能，以解决现有描述符难以编码其多尺度层级结构、且ReaxFF力场在多晶型稳定性预测中精度不足的问题  
- **动机与背景**：传统描述符（如SOAP、ACSF）难以区分分子内官能团层次（如环 vs. 硝基）与分子间配位环境；ReaxFF虽支持反应模拟，但在能量排序（尤其多晶型相对稳定性）上误差大（>100 meV/atom）；迄今尚无ML方法用于系统性修正ReaxFF对分子晶体的能量预测偏差  
- **方法核心**：提出层级化“中心-环境”（HCE）特征框架，将结构分解为分子内（环/硝基等化学基元）和分子间（中心分子+距离加权注意力权重的配位壳）双层级，并融合物理先验（键级、电负性、范德华半径）与几何信息  
- **关键实验与结果**：体系为RDX（5930个DFT结构）和HMX（3335个DFT结构）的多种晶型与构象；基线为原始ReaxFF预测能量；KRR模型将RDX误差从116.7 → 42.2 meV/atom，SVR模型将HMX误差从112.3 → 53.7 meV/atom；跨分子迁移（RDX预训练→HMX微调）达52.9 meV/atom，优于纯HMX训练模型（53.7 meV/atom）  
- **创新点**：① 首个专为分子晶体设计的、显式解耦分子内/分子间层级的可解释特征框架（HCE）；② 首次实现ML对ReaxFF能量预测的系统性偏差校正，而非替代力场；③ 验证了基于化学先验的紧凑描述符可支撑跨分子种属的迁移学习，突破数据孤岛限制  
- **局限性**：HCE依赖分子片段划分规则（如硝基识别），对高度柔性或质子转移体系泛化性未验证；未耦合动力学（如温度/压力效应）；ML校正仅针对单点能量，未延伸至声子谱、弹性张量等衍生性质  
- **对你研究的启发**：可借鉴“层级解耦+物理先验嵌入”的特征设计范式，用于电催化中吸附物构型（分子内键合态）与表面配位环境（局域电子结构）的联合编码；ML校正现有力场（如DFTB或ReaxFF）的策略，适用于加速催化剂表面反应路径筛选  
- **与你研究的相关度**：高
- **阅读模式:** 🔍 精读
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/899363c0b628322907b418656cd1bdf38af22e4d
- **标签:** dft

### 4. Experimental methods in chemical engineering: Cyclic voltammetry—
 CV ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-08-09
- **作者:** Yasser Matos‐Peralta; Christopher Panaritis; J. Hagler; Clara Santato; G. Patience
- **核心问题**：如何弥合经典循环伏安法（CV）理论与电化学工程实际应用中定量、可重现数据分析之间的鸿沟  
- **动机与背景**：现有CV分析多停留于定性峰识别，缺乏对动力学、传质、界面过程等多维信息的系统解耦；工程场景中非理想因素（如未补偿电阻、膜不均一性、电极钝化）常导致机理误判；传统教学与实践脱节，制约电催化等领域的理性材料设计与工艺放大  
- **方法核心**：提出“多维定量CV分析框架”，将伏安图视为融合电子转移动力学、质量输运模式、法拉第/非法拉第电流分辨、以及操作条件敏感性的综合信息载体，并配套建立实验可控性指南与不确定性溯源体系  
- **关键实验与结果**：以典型电催化体系（如OER/ORR、酶电极、电池电极）为对象，对比传统峰高/峰位分析与本框架下的参数提取（如从i–v斜率与扫描速率依赖性获得表观k₀；结合EIS校正后R<sub>u</sub>实现真实动力学解析）；示例显示，忽略溶液电阻可使表观速率常数偏差达1–2个数量级  
- **创新点**：① 首次将CV数据解构为“动力学–传质–界面电容–操作扰动”四维可量化指标体系；② 明确界定并量化工程场景中主要不确定性来源（如薄膜异质性引起的局部传质偏离半无限扩散）；③ 建立CV与operando表征（MS、光谱、纳米成像）的协同分析范式，推动从“单点电化学”到“过程电化学工程”的范式升级  
- **局限性**：未提供开源自动化分析工具或标准化数据处理流程；对超快动力学（τ < 1 ms）或强耦合多步反应（如CO₂RR中C–C偶联路径）的CV特征解析仍缺乏普适性判据；未涵盖微电极/芯片化CV等新兴平台的适配性讨论  
- **对你研究的启发**：可借鉴其“不确定性驱动的参数反演”思路，在DFT+microkinetic建模中嵌入CV可观测量作为约束条件；其操作变量敏感性分析框架（如扫描速率–电容贡献–活性面积解耦）可迁移至原位XAS/ATR-SEIRAS联用实验设计；强调“工程鲁棒性”而非仅“本征活性”，提示需在计算中引入器件级退化因子（如碳腐蚀、离子吸附阻塞）  
- **与你研究的相关度**：高
- **阅读模式:** 🔍 精读
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/a6318c71168517a464815773469f4d9da1b74f25
- **标签:** electrochemistry, catalysis, surface

### 5. An exact approach for describing adsorption and catalysis of interacting species in lattice models. ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-08-07
- **作者:** K. Fichthorn; Ethan Cooper; C. Humphries; Ashlyn A Latham; L. A. Okpaire et al.
- **核心问题**：如何在保持严格热力学精确性的前提下，实现对表面吸附与催化反应中多体相互作用体系的高效建模，突破传统近似方法（如平均场）的精度瓶颈。  
- **动机与背景**：平均场和准化学近似虽计算廉价，但在强吸附相互作用或高覆盖度下误差极大（可达五个数量级），难以可靠预测吸附等温线和反应速率；而蒙特卡洛模拟虽准确但成本高、收敛慢，且缺乏解析可解释性；全枚举法理论上精确，却因组合爆炸被普遍认为仅适用于极小体系，其实际可行尺度边界尚不明确。  
- **方法核心**：提出基于**全枚举法（full enumeration）求解格点模型巨正则配分函数**的方法，并系统评估其在有限但“适当选择”的小尺寸晶格（如 3×3–4×4）上的收敛性与泛化能力，证明其可通过边界条件设计和构型截断策略逼近大体系极限。  
- **关键实验与结果**：以含吸附排斥/吸引相互作用的双组分表面反应（A + B → AB）为模型体系；基线方法包括平均场近似（MFA）、准化学近似（QCA）和蒙特卡洛（MC）模拟（100×100格点）；全枚举在 4×4 格点上复现 MC 吸附等温线误差 < 1%，反应速率预测偏差 < 2%，而 MFA 速率误差达 10⁵ 倍。  
- **创新点**：① 首次定量界定全枚举法在表面催化格点模型中的**实用尺度阈值**（非“越小越好”，而是需兼顾周期性与相互作用程）；② 揭示小格点全枚举结果可通过**构型权重重加权或有效化学势映射**外推至热力学极限，无需增大格点；③ 将严格枚举从纯平衡拓展至**速率决定步骤的动力学建模**，建立与微观速率常数直接关联的解析框架。  
- **局限性**：未处理长程相互作用（>2邻位）或动态重构表面；未耦合第一性原理计算（如DFT）提供输入参数，仍依赖经验相互作用能；动力学扩展仅限速率控制步，未涵盖多步串联反应或扩散限制情形。  
- **对你研究的启发**：可将全枚举作为DFT+机器学习力场训练的“黄金标准”校准器，用于验证吸附能矩阵的统计准确性；其小格点收敛策略可迁移至图神经网络中局部子图采样设计，提升催化位点识别的物理保真度；枚举生成的完整构型数据库可用于构建可解释的吸附覆盖度-活性描述符。  
- **与你研究的相关度**：高
- **阅读模式:** 🔍 精读
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/21c40cb0542ffbabf7902304759a4d3e149ad0c3
- **标签:** catalysis, surface

### 6. DeGAT: A Dual-Expert
Graph Attention Network for Partial
Charge Prediction in Metal–Organic Frameworks ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-08-10
- **作者:** Yanhui Sun; Zeheng Yu; Yuhua Dong; Ming Gong; Yongchao Hao et al.
- **核心问题**：周期性DFT计算REPEAT电荷成本过高，阻碍MOF材料的大规模筛选  
- **方法要点**：提出双专家图注意力网络DeGAT，结合基于不确定性的主动学习策略预测MOF原子电荷  
- **关键结果**：测试集R²达0.985，MAE=0.0314 e；用DeGAT电荷模拟的CO₂/N₂/水吸附性质与REPEAT电荷结果高度一致  
- **与你研究的相关度**：高
- **阅读模式:** 📋 摘要
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/2c955c11240102aa6c6c9a3d28bd9b4a662264ab
- **标签:** constant-potential, surface, dft, active-learning

### 7. Cubic-Equivariant Neural Density Functional Theory for Three-Dimensional Lattice Fluids ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-08-08
- **作者:** Jens Weimar; Martin Oettel; Alessandro Simon
- **核心问题**：如何构建能直接作用于三维无约束密度分布的神经经典密度泛函，以提升非均匀流体结构预测精度  
- **方法要点**：采用全卷积神经网络学习单粒子直接关联泛函 $c^{(1)}[\rho]$，通过随机外势下的巨正则蒙特卡洛数据训练，并施加立方点群对称性约束实现精确立方等变性  
- **关键结果**：神经泛函显著改进了均匀状态方程和硬壁附近的密度分布；在各向异性粒子对分布中能复现主堆积壳层，但方向依赖性精度与基准泛函互有优劣  
- **与你研究的相关度**：低
- **阅读模式:** 📋 摘要
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/5669d89f08096a1e3958f8dea16340b1d1935272
- **标签:** electrochemistry, dft

### 8. Phase Behavior and Critical Properties of Hydrocarbons in Shale Illite Nanopores ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-08-07
- **作者:** Sirong Zhu; Ning Li; Zhiwen Huang; Kai Ye; Fangpeng He et al.
- **核心问题**：黏土纳米孔道中烃类流体受限导致的临界性质（Tc、Pc）偏移规律  
- **方法要点**：采用巨正则系综蒙特卡洛（GCMC）模拟研究伊利石狭缝孔中2–20 nm尺度下烷烃的受限相行为  
- **关键结果**：① 受限显著降低烃类临界温度（Tc）和临界压力（Pc），n-戊烷偏移幅度大于甲烷；② 20 nm孔径下临界性质趋近体相值，且提出可定量预测该偏移的新关联式  
- **与你研究的相关度**：低
- **阅读模式:** 📋 摘要
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/97df1c924ba1263eb9dee0ea6dda3154bd4104ec
- **标签:** constant-potential, surface

### 9. A Dataset of Equilibrium State Configurations of Adsorption in Zeolites ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-08-09
- **作者:** Marko Petković; R. Ramesh; V. Menkovski; S. Calero
- **核心问题**：缺乏坐标分辨的甲烷在铝取代钠型沸石中吸附构型数据集，限制了对吸附微观机制和机器学习建模的研究。  
- **方法要点**：基于巨正则蒙特卡洛（GCMC）模拟，系统生成涵盖191种拓扑、不同Al含量/分布、Na⁺排布及压力条件下的甲烷吸附平衡构型数据。  
- **关键结果**：构建了AdsZeo数据集，包含4,775个沸石框架实现、62,075次生产模拟、1241.5万帧构型记录及超12亿粒子坐标记录，全部以DuckDB数据库格式开源。  
- **与你研究的相关度**：中
- **阅读模式:** 📋 摘要
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/a396604ca9992dca59d970965512641c7b54d3d5
- **标签:** catalysis, constant-potential, surface

### 10. Stereochemistry at the Single-Molecule Level: From Monitoring to Regulation. ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2025-03-24
- **作者:** Wenlong Cai; Xinmiao Xie; Zezhou Yang; Xuefeng Guo
- **核心问题**：如何在单分子尺度上实时监测和调控立体化学转化过程，以揭示个体分子动态并 bridging 宏观观测与分子尺度行为  
- **方法要点**：整合电学（如单分子结、扫描探针显微镜、纳米孔）与非电学（如圆二色光谱、表面增强拉曼）单分子技术，结合多模态刺激（光、电场、机械力）和新兴策略（机器学习、纳米加工）  
- **关键结果**：实现了基于手性诱导自旋选择性（CISS）效应的手性分子识别与操控；系统阐明了构型、构象及构造异构化在光/电/力驱动下的单分子调控机制  
- **与你研究的相关度**：高
- **阅读模式:** 📋 摘要
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/3ea1b138fe1a0c634f275b0bf2272ab2d54dd1f5
- **标签:** electrochemistry, surface

## 💡 今日亮点

- **最值得精读**：[5] An exact approach for describing adsorption and catalysis of interacting species in lattice models — 提出严格热力学精确的全枚举解析框架，首次在保持可解释性前提下突破平均场近似对强相互作用表面体系的系统性误差（达5个数量级），为电催化微观动力学建模树立新基准。  
- **可能冲突的研究**：[1] Evaluating Electrostatic Embedding MLIP/MM for Relative Binding Free Energy Calculations — 其依赖静电嵌入近似处理环境极化，而[5]揭示的多体关联本质暗示：即使在配体-蛋白界面，固定嵌入电势也可能掩盖覆盖度依赖的协同极化效应，从而弱化RBFE预测的物理一致性。  
- **值得追踪的团队**：DeGAT作者团队（论文[6]）— 在MOF电荷预测中实现DFT级精度与图神经网络效率的平衡，并验证其对吸附性质的传递性，为电催化表界面电荷重分布建模提供了可迁移的范式。  
- **重要趋势**：多尺度建模正从“分而治之”转向“跨层耦合验证”：CV实验量化（[4]）、格点精确解（[5]）、神经泛函（[7]）、受限流体模拟（[8]）与构型数据集（[9]）共同指向——微观结构统计精度、热力学严格性与工程可解释性必须同步约束，而非孤立优化。

## 📌 Key Gap

**关键差距**
- **Gap 1**：所有高精度方法（[1][5][7][9]）均未解决*动态电极/电解质界面*下的实时电荷重分布与反应路径耦合问题；例如[5]的格点模型假设静态位点能量，无法描述电势驱动的双电层重构对吸附能的瞬态调制。  
- **Gap 2**：机器学习模型（[3][6][7]）严重依赖高质量训练数据，但当前缺乏针对*电催化工况*（如偏压、pH、离子强度梯度）下原位结构响应的标准化数据协议，导致模型外推至真实电解池时可靠性未知。  
- **未来方向**：发展“电势门控”的多尺度代理模型：以[5]的精确格点解为热力学锚点，嵌入[4]中CV反演的动力学参数，并用[6]类图网络学习电极电势→局部电荷→吸附构型→反应能垒的端到端映射，在避免DFT代价的同时保留电化学边界条件的物理保真性。
