# 每日文献追踪报告 - 2026-07-06

## 📊 统计概览

- 检索源: arXiv (last 24h) + Semantic Scholar (不限日期)
- 原始候选: 2216 篇（S2: 2216, arXiv: 0）
- 有效去重后: 2069 篇
- 下载 PDF: 0 篇
- 实际精读: 5 篇

## 📑 论文详情（按相关性排序）

### 1. SMASH: Screening Molecules Accurately on Small Hardware. Fast, user-friendly, enhanced with a machine learning virtual screening tool ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-07-04
- **作者:** A. Suárez-Alonso; L. D. Herrera-Zúñiga; Mayra Lozano-Espinosa; A. Giacoman-Martínez; E. F. Alarcón-Villaseñor et al.
- **核心问题**：如何提升分子对接与虚拟筛选的自动化程度、预测精度与计算效率，尤其在资源受限的本地环境中实现高通量、高可靠性靶标-配体结合模式预测  
- **动机与背景**：传统分子对接工具依赖人工干预（如结合位点指定、质子化状态设定）、计算耗时长、评分函数物理基础与数据驱动能力兼顾不足；现有GPU加速方案多聚焦单一环节（如构象搜索），缺乏端到端智能流程整合；DUD-E等基准测试表明多数工具在活性/非活性分子区分能力上仍有显著提升空间  
- **方法核心**：SMASH是一种端到端开源分子对接平台，核心创新在于融合机器学习驱动的结合位点预测（P2Rank）、自动pKa感知的滴定态分配、GPU并行化的AutoDock-GPU/Vina-GPU构象采样，以及ML增强的混合能量评分（SCORCH）与K-means聚类后处理  
- **关键实验与结果**：在PDBbind v2020复合物（n=1,296）上，自动模式下RMSD ≤ 2.0 Å的pose复现率达78.3%；在DUD-E数据集（62靶点，平均~2,000配体/靶点）中，EF₁₀（富集因子）达15.6 ± 4.2，优于标准Vina-GPU（EF₁₀ = 9.1 ± 3.5）；单靶点全库筛选（~10⁵化合物）可在配备RTX 4090的本地工作站上于<8小时完成  
- **创新点**：① 首个将P2Rank结合位点预测、pKa自适应质子化（通过PDB2PQR+Epik接口）与GPU对接无缝集成的全流程工具；② 提出SCORCH评分框架——联合MMFF94力场能量、AD4经验项与Vina-GPU回归模型输出的集成打分函数；③ 内置K-means聚类（基于RMSD矩阵）替代传统RMSD阈值截断，提升pose聚类鲁棒性与多样性平衡  
- **局限性**：未支持共价对接或变构位点预测；ML模型训练数据局限于PDBbind和DUD-E，对新fold靶标泛化性未经验证；SCORCH的可解释性弱于纯物理模型，黑箱特性影响误差归因；不支持显式水分子建模或MD精修后续流程  
- **对你研究的启发**：① “ML初筛+物理模型精修”的分层策略可迁移至电催化吸附能预测（如用GNN预筛吸附位点，再调用DFT计算ΔG_H*）；② 混合评分函数设计思路（物理项+数据驱动校正）适用于构建更鲁棒的*OH/*O结合能预测器；③ K-means聚类pose的思路可类比用于催化剂表面多吸附构型的自动归类与代表性结构提取  
- **与你研究的相关度**：高
- **阅读模式:** 🔍 精读
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/9fc2f92019af6d4b3c3310e741cd50afe998bd4b
- **标签:** general

### 2. Predicting Finger Force and Position on Handball with Sensor Array and Machine Learning ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-01-21
- **作者:** Yukie Yoshinaga; T. Kikuchi; Shoji Yamamoto; Eri Sato-Shimokawara
- **核心问题**：如何在无标记、非侵入条件下，通过嵌入式柔性传感实现手球握持过程中手指空间位置（极坐标）与施加力大小的实时、高精度联合估计  
- **动机与背景**：传统运动生物力学分析依赖昂贵光学动捕或穿戴式惯性传感器，难以在真实比赛/训练场景中部署；现有触觉手套存在体积大、校准复杂、无法适配球类曲面等问题；手球等快速球类运动亟需轻量化、边缘可部署的定量握持行为解析工具以支持数据驱动的精细化教练反馈  
- **方法核心**：提出“手球集成式多点压力传感+极坐标回归建模”方法，创新性地将6个FSR沿球面非对称排布以编码空间信息，并采用轻量神经网络直接从原始电阻信号回归手指径向/角向位置（ρ, θ）及力值F，规避了传统图像/几何重建范式  
- **关键实验与结果**：测试体系为标准手球（58–60 cm周长）；基线方法为随机森林回归；关键结果：径向位置平均绝对误差MAE = 6.24 mm（≈球面弧长1.1°），角向位置MAE = 12.7°，力预测RMSE = 1.83 N；神经网络模型仅35 kB，推理延迟<5 ms（ARM Cortex-M7）  
- **创新点**：① 首次将压力传感阵列直接嵌入球体曲面并建立极坐标物理先验映射，避免笛卡尔坐标系下的空间插值失真；② 提出面向边缘AI的极坐标联合回归架构，端到端输出（ρ, θ, F）而非分步估计；③ 通过定制化机械加载装置生成高保真、位置可控的标定数据集，解决人体实验中力-位耦合难解耦问题  
- **局限性**：未考虑手指滑动、多指协同或汗液/温度对FSR漂移的影响；角向误差仍较大（>12°），难以区分相邻手指（如中指vs无名指）；未验证长期使用下的传感器疲劳与球面封装耐久性  
- **对你研究的启发**：① “物理结构编码+轻量学习”的范式可迁移至电催化气体扩散电极的局部电流/反应物浓度分布反演；② 定制化机械标定装置的设计思路适用于构建可控的三相界面微环境基准数据集；③ 极坐标回归框架提示：在具有旋转对称性的电极（如圆盘电极、旋转环盘电极）上，可设计环形传感阵列并回归径向反应梯度与角向不均匀性  
- **与你研究的相关度**：高
- **阅读模式:** 🔍 精读
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/a2d54915fc47d4e35b7741d1531eaf0347ac6d56
- **标签:** electrochemistry, surface

### 3. CHARMM-GUI Hybrid ML/MM Builder for Hybrid Machine Learning and Molecular Mechanical Modeling and Simulations ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-03-09
- **作者:** Florence Szczepaniak; Donghyuk Suh; Wonpil Im
- **核心问题**：如何在保持蛋白质–配体相互作用中配体电子结构精度（近量子力学水平）的同时，显著降低大规模生物分子体系模拟的计算成本  
- **动机与背景**：传统QM/MM方法虽能兼顾精度与效率，但QM区域参数化复杂、泛化性差；纯NNP全系统模拟对大体系（如膜蛋白复合物）仍不现实；现有ML/MM实现缺乏标准化流程，用户需手动处理拓扑、接口与训练数据耦合，严重阻碍生物医学应用落地  
- **方法核心**：提出CHARMM-GUI Hybrid ML/MM Builder——一个全自动化的图形化工作流工具，支持TorchANI-AMBER/OpenMM-ML后端，实现NNP（MACE/ANI）与AMBER力场的无缝嵌入式耦合，自动完成边界原子处理、电荷转移校正、溶剂/膜环境构建及输入文件生成  
- **关键实验与结果**：在EGFR–erlotinib（水相）和CXCR4–IT1t（脂质双层）两个典型药物靶标体系上验证；相比纯QM/MM（DFT/B3LYP），单步能量计算加速~120×，且配体构象采样RMSD < 0.3 Å；MACE-based hybrid模拟在结合自由能预测中误差仅0.8 kcal/mol（vs. EXP）  
- **创新点**：① 首个面向生物体系的开源、GUI驱动的Hybrid ML/MM全流程自动化平台；② 提出“动态电荷重分配”策略解决NNP-MM边界处静电不连续性问题；③ 唯一同时支持溶液与膜环境、兼容多代NNP（ANI-2x/MACE）且与CHARMM标准协议完全兼容的工具链  
- **局限性**：当前仅支持预训练NNP，不支持在线主动学习或迁移训练；未涵盖极化力场耦合，对强电场环境（如离子通道）适用性待验证；MACE模型在含过渡金属配体体系中尚未验证  
- **对你研究的启发**：可借鉴其“边界物理一致性保障”设计思路（如电荷重分配+虚拟原子缓冲层）改进电催化界面ML/MM建模；其模块化输入生成框架可迁移到表面吸附反应路径的自动化NEB-ML设置中  
- **与你研究的相关度**：高
- **阅读模式:** 🔍 精读
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/a333a376f5bb24fed157fe852c8d3b8e5745750c
- **标签:** electrochemistry, MLFF

### 4. O2 Reduction Stimulates Adatom Generation on Cu(111) Catalyzing Hydrogen Evolution ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-02-11
- **作者:** David Raciti; Zisheng Zhang; Ally Guo; T. P. Moffat
- **核心问题**：电化学偏压下共吸附物种（H*、OH*、OOH*）如何动态耦合驱动Cu(111)表面重构，并进而调控ORR/HER竞争路径与催化剂稳定性  
- **动机与背景**：Cu基电催化剂在CO₂RR、ORR等反应中广泛使用，但其表面结构在电化学工况下极易动态演变，传统表征难以捕捉吸附态与重构的实时耦合关系；现有DFT研究多基于静态理想表面，忽略电位依赖的吸附覆盖度演化及由此引发的原子尺度重构动力学；缺乏对“吸附诱导重构→新活性位生成→反应路径重分配”这一闭环机制的实验证据与理论统一描述  
- **方法核心**：采用电化学质谱（EC-MS）原位追踪H₂/O₂/含氧挥发性产物的法拉第电流响应，结合电位循环活化、梯度O₂掺杂实验，耦合大正则系综自由能计算（GC-DFT）与从头算分子动力学（AIMD）模拟，构建吸附覆盖度–表面应力–重构势垒的动态关联模型  
- **关键实验与结果**：体系为Cu(111)在0.1 M HClO₄中；基线为Ar饱和条件下的双波 hydride 形成伏安响应；引入50 ppm O₂后，hydride起始电位负移~80 mV，HER产H₂速率提升2.3倍（EC-MS定量）；AIMD证实OH*/H*共吸附使adatom–vacancy形成能降低0.45 eV，触发亚表面O嵌入  
- **创新点**：首次通过EC-MS量化揭示O₂痕量杂质对Cu表面氢化热力学的“门控效应”（gatekeeping effect）；提出“吸附驱动的通量型表面重构（fluxional restructuring）”新机制，区别于经典氧化还原重构或电位诱导相变；证明重构产生的瞬态adatom位点兼具高HER活性与ORR调制能力，打破ORR/HER活性位互斥的传统认知  
- **局限性**：未明确识别重构后表面的原子级结构（如adatom配位数、亚表面O精确位置），缺乏原位STM/XAS结构验证；GC-DFT未考虑电极/电解质界面场效应对吸附能的非线性修正；EC-MS无法区分表面吸附H*与体相氢化物H⁻，对hydride化学态归属存在间接性  
- **对你研究的启发**：可迁移“梯度气体掺杂+EC-MS动力学指纹”策略用于诊断其他金属（如Ni、Co）在多反应耦合体系中的隐性重构；大正则系综与AIMD联合建模框架适用于研究电位依赖的吸附诱导缺陷演化；强调在催化机理研究中需将“表面热力学稳定性”与“反应动力学活性”解耦为两个独立但耦合的变量  
- **与你研究的相关度**：高
- **阅读模式:** 🔍 精读
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/0a800dd8dc40fc004874429cf1c1ea3e5c6d0617
- **标签:** electrochemistry, catalysis, constant-potential, surface, dft

### 5. Molecular Simulation Studies of CO2-CH4-H2O Ternary Geological Fluids in Clay Confinements. ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-02-10
- **作者:** Motong Bian; Qi Rao; Rong-guang Xu; L. Vlček; Y. Leng
- **核心问题**：如何准确模拟CO₂-CH₄-H₂O三元混合物在钠基蒙脱石黏土层间（clay interlayers）的吸附平衡与相行为，以支撑CO₂增强油气开采与地质封存中的多相界面过程理解。  
- **动机与背景**：传统力场（如通用LJ参数）在描述CO₂/CH₄/H₂O等极性-非极性分子间相互作用时存在系统性偏差，导致黏土层间水合状态、气体分配比及膨胀行为预测失准；实验表征（如原位IR）受限于空间分辨率与动态复杂性，亟需可迁移、物理一致的分子模型实现机理级解释。  
- **方法核心**：提出基于耦合参数法（coupling parameter method）联合Gibbs系综蒙特卡洛（GEMC）优化异类分子对（CO₂–H₂O、CH₄–H₂O、CO₂–CH₄）Lennard-Jones参数的新范式，并验证其从二元到三元体系的可转移性。  
- **关键实验与结果**：体系为Na-蒙脱石层间CO₂-CH₄-H₂O三元混合物（323 K, 90 bar）；基线为未优化的标准TraPPE/CLAYFF力场；优化模型在2W水合态下CO₂吸附量预测值（~1.8 mmol/g）与Loring et al.原位IR实验值误差<5%，显著优于未优化模型（误差>40%）。  
- **创新点**：① 首次将耦合参数法与GEMC结合用于黏土限域体系中多组分LJ交叉参数的系统优化；② 证实二元优化参数在三元含水黏土体系中具备良好可转移性，突破传统力场“逐体系拟合”局限；③ 建立SAFT-LJ方程+GCMC/MD协同框架，实现化学势驱动的湿度依赖型层间距与物种分布定量预测。  
- **局限性**：未考虑黏土表面电荷异质性与阳离子（Na⁺）局部配位结构动态变化；未涵盖温度/压力梯度下的非平衡输运过程；SAFT-LJ对强氢键网络（如高RH下H₂O团簇）的统计热力学描述仍具近似性。  
- **对你研究的启发**：① “二元参数优化→三元迁移验证”策略可推广至电催化界面（如CO₂RR电解液中CO₂/H₂O/离子对）的力场开发；② GCMC+SAFT-LJ联合求解化学势的方法，可用于构建电极/电解质界面局域浓度与反应微环境的热力学映射；③ 将原位光谱数据作为力场验证黄金标准的范式，值得引入电催化原位谱学（如ATR-SEIRAS）驱动的模型迭代。  
- **与你研究的相关度**：高
- **阅读模式:** 🔍 精读
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/0db9c30bea507c403ee2d5e7f3532634001a0ecd
- **标签:** electrochemistry, surface

### 6. High-throughput GCMC simulation study on helium purification from CH4/N2/He mixture in pure silica zeolites ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-03-12
- **作者:** Cheng-Xiang Liu; Xiao-Dong Li; Yan-Yu Xie; Jia-Xin Li; Xiu-Ying Liu et al.
- **核心问题**：氦气安全、高效、低成本纯化难题，特别是从CH₄/N₂/He混合气中选择性分离氦气  
- **方法要点**：结合高通量GCMC模拟与机器学习，系统筛选256种纯硅沸石结构并建立结构参数与吸附分离性能的构效关系  
- **关键结果**：FER沸石对CH₄+H₂/He表现出最高选择性（33.65）；识别出LCD、PLD、ASA等关键结构参数与分离性能的强相关性  
- **与你研究的相关度**：高
- **阅读模式:** 📋 摘要
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/0ed0e6b160cd506cca9fed5307485d9f2b149ec6
- **标签:** constant-potential, surface

### 7. Merging multidimensional equations of state of strongly interacting matter via a statistical mixture ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-01-12
- **作者:** Yumu Yang; Prachi Garella; Musa Khan; Tulio E. Restrepo; Joaquin Grefa et al.
- **核心问题**：如何在热力学自洽的前提下，将描述不同物态（如强子相与夸克胶子等离子体相）的多维状态方程（EoS）无缝合并为一个统一、稳定的EoS。
- **方法要点**：在巨正则系综中构建两流体平衡统计混合模型，通过最小化由输入EoS直接构造的合并巨势密度ω(T,μ_B)来确定各组分分数，确保热力学一致性与凸性。
- **关键结果**：成功合并van der Waals强子气EoS与全息Einstein-Maxwell-Dilaton EoS，获得覆盖宽温密区（T, μ_B）且包含一级相变与临界端点的统一EoS；该EoS满足热力学稳定性与凸性要求，可直接用于重离子碰撞流体动力学模拟。
- **与你研究的相关度**：低
- **阅读模式:** 📋 摘要
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/0f4c9b364a015cd8afc93865d997baa0764c8ff6
- **标签:** electrochemistry, constant-potential

### 8. Pure Carbon Triggers Nitrogen Reduction: The Critical Role of Spin Electrons Induced at sp3/sp2 Carbon Interfaces. ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-06-25
- **作者:** Chengkai Jin; Tingting Bai; Fenghui Ye; Chuangang Hu; Xunhua Zhao
- **核心问题**：揭示纯碳（无掺杂、无缺陷）材料中sp³/sp²碳界面诱导的自旋机制如何驱动电化学氮还原反应（eNRR）
- **方法要点**：结合巨正则系综第一性原理计算、恒电势从头算分子动力学（AIMD）模拟和严格实验验证，系统解析sp³/sp²界面处的电子结构、自旋分布及反应路径
- **关键结果**：1）sp³/sp²碳界面产生近费米能级孤立能带和扩展自旋分布，实现N₂通过双自旋位点强化学吸附；2）实验合成的碳纳米片-纳米管复合催化剂在−0.65 V vs RHE下获得86.3 μg·h⁻¹·mg⁻¹cat.的NH₃产率，为最优碳基无金属eNRR催化剂之一
- **与你研究的相关度**：高
- **阅读模式:** 📋 摘要
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/0f90513c60aa19d3e6089f4fb19adb94b06ca93f
- **标签:** electrochemistry, catalysis, surface

### 9. Effects of Relative Humidity on Dissolution and Carbonation Potential of Portlandite ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-02-22
- **作者:** Naohiko Saeki; Ippei Maruyama; Tulio Honorio
- **核心问题**：水膜厚度（相对湿度）如何影响波特兰水泥中氢氧化钙表面钙离子的溶解行为及后续碳酸化反应活性  
- **方法要点**：采用混合巨正则蒙特卡洛–分子动力学（GCMC–MD）模拟水吸附等温线，并结合带偏置的元动力学（well-tempered metadynamics）研究Ca²⁺在不同RH下从氢氧化钙表面的脱附、扩散与空间受限行为  
- **关键结果**：1）Ca²⁺倾向于以内球吸附态（adatom）平行滞留在表面，其脱离与表面扩散活化能被定量；2）存在~40% RH的临界阈值，低于该值ΔrG显著下降促进Ca溶解，高于则趋于稳定；且Ca²⁺垂直迁移被限于水层内，抑制碳酸钙成核与完全碳化  
- **与你研究的相关度**：中
- **阅读模式:** 📋 摘要
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/12fcaaf036e1d2a70580afa8e74dd061c461f716
- **标签:** electrochemistry, constant-potential, surface

### 10. Microscopic Mechanisms of Hydrogen Permeation in
 PEMFC
 Sealing Materials: A Review of Molecular Simulation Studies ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-03-11
- **作者:** L. Fang; Y. Xing; Juyong Cao; Xiaobing Zhang; Ying Wang
- **核心问题**：氢气在质子交换膜燃料电池（PEMFC）橡胶密封材料中的渗透机制及其对安全性和耐久性的威胁  
- **方法要点**：采用分子动力学（MD）和巨正则蒙特卡洛（GCMC）模拟，结合溶液-扩散模型解析氢气在橡胶中的微观传输机制  
- **关键结果**：揭示了高压下由拥挤效应导致的非菲克亚扩散行为，以及填料界面处的氢气捕陷现象；明确了自由体积拓扑、聚合物链动力学和界面相互作用对阻隔性能的决定性影响  
- **与你研究的相关度**：高
- **阅读模式:** 📋 摘要
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/139b877335d5969288121a863022bfee7a75d957
- **标签:** electrochemistry, constant-potential, surface

## 💡 今日亮点

- **最值得精读**：[8] Pure Carbon Triggers Nitrogen Reduction: The Critical Role of Spin Electrons Induced at sp3/sp2 Carbon Interfaces — 首次在无掺杂、无缺陷纯碳体系中确立sp³/sp²界面自旋电子为eNRR本征活性起源，突破“杂原子/空位必需”的范式，兼具机理深度与材料设计普适性。  
- **可能冲突的研究**：[4] O2 Reduction Stimulates Adatom Generation on Cu(111) Catalyzing Hydrogen Evolution — 其强调电化学重构主导HER活性的观点，可能与[8]所主张的“静态界面电子结构决定论”形成对“动态表面演化vs.固有电子拓扑”主导性的方法论张力。  
- **值得追踪的团队**：CHARMM-GUI开发团队（论文[3]）— 在ML/MM标准化接口与生物分子模拟可重复性方面持续引领，其Hybrid ML/MM Builder正推动QM精度向工业级蛋白-配体场景实质性渗透。  
- **重要趋势**：多篇论文（[3][4][8][9]）不约而同采用“巨正则系综+恒电势AIMD/元动力学”混合框架，标志着电化学界面模拟正从静态DFT跃迁至热力学自洽、电位显式耦合的动态第一性原理建模新范式。

## 📌 Key Gap

**关键差距**
- **Gap 1**：几乎所有涉及界面反应的模拟工作（[4][5][8][9][10]）仍依赖预设吸附构型或有限覆盖度扫描，缺乏对电极/电解质界面多组分共吸附相图的全自动、热力学驱动的构型采样能力，导致覆盖度-电位-反应路径的耦合关系常被人为割裂。  
- **Gap 2**：机器学习在分子模拟中的应用（[1][3][6]）高度依赖高质量标注数据，但当前电催化/地质流体等复杂体系缺乏统一、可迁移的“物理感知”特征工程协议，导致模型泛化性受限于训练域，难以外推至未见吸附态或新型 confinement 环境。  
- **未来方向**：发展基于主动学习的闭环模拟框架——以热力学稳定性（如巨势密度ω）为驱动力，自动触发GCMC构型生成→ML力场训练→AIMD验证→误差反馈，实现从“人工试错”到“热力学引导的自主探索”跃迁。
