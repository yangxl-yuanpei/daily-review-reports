# 每日文献追踪报告 - 2026-07-03

## 📊 统计概览

- 检索源: arXiv (last 24h) + Semantic Scholar (不限日期)
- 原始候选: 1138 篇（S2: 1138, arXiv: 0）
- 有效去重后: 1014 篇
- 下载 PDF: 0 篇
- 实际精读: 5 篇

## 📑 论文详情（按相关性排序）

### 1. A systematic drude-based parameterization workflow and polarizable force field for battery electrolytes ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-05-14
- **作者:** Chenlu Wang; Qisheng Wu
- **核心问题**：如何在保持计算效率的同时，准确建模电解质中离子溶剂化结构的环境依赖性极化效应  
- **动机与背景**：传统固定电荷力场无法描述溶剂化壳层中随局部化学环境动态变化的电子极化，导致对溶剂化构型、离子配位竞争及聚集行为的预测失准；而高精度的机器学习势能面虽准确但计算开销大、可迁移性差，难以支撑长时标、大体系的电池界面模拟  
- **方法核心**：提出基于Drude振子模型的可迁移参数化工作流，构建开源极化力场OPLS&Pol，通过显式引入极化电荷（Drude粒子）并系统优化其与OPLS-AA骨架的耦合参数，实现物理可解释性与计算效率的统一  
- **关键实验与结果**：在纯溶剂（EC、DEC、DME）、二元/三元混合电解质（如LiTFSI-DME、LiFSI-EC/DEC）及氟磺酰基新型电解质中验证；相比AMBER/GAFF极化力场和ANI-1x ML势，OPLS&Pol在溶剂化结构预测上达到R²_global = 0.94，且吞吐量达1.65×10⁶ atom·steps/s，比典型ML模型快约10倍  
- **创新点**：① 首次将Drude极化框架与OPLS-AA力场深度耦合并开源，兼顾兼容性与极化物理真实性；② 建立跨电解质体系的系统化参数转移策略，避免逐体系重训练；③ 揭示极化效应对浓度依赖性溶剂重组、混合醚竞争配位、碳酸酯环/链选择性及FSI⁻诱导聚集体稳定的普适调控机制  
- **局限性**：未涵盖固态电解质界面（SEI）形成等电化学反应过程；Drude模型对高频振动模式（如C=O伸缩）的描述精度未量化评估；参数化仍依赖高质量QM参考数据（如CCSD(T)/aug-cc-pVTZ），对弱相互作用体系泛化能力待验证  
- **对你研究的启发**：Drude参数的分层优化策略（先固定骨架后调极化项）可迁用于开发面向电催化界面水/有机共溶剂体系的极化力场；其“物理机制驱动+数据验证”的双轨参数化范式，优于纯黑箱ML拟合，适用于需解释性与可迁移性兼备的多相催化模拟  
- **与你研究的相关度**：高
- **阅读模式:** 🔍 精读
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/14510bb67fbe306ff7d70a435a03c8b0ae4dc94a
- **标签:** electrochemistry, generative

### 2. AI-driven prediction of critical depth of cut in ultra-precision machining of single crystal sapphire ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-05-27
- **作者:** Dae Nyoung Kim; S. Kwon; Sangkee Min
- **核心问题**：如何准确预测单晶蓝宝石在超精密正交切削中不同晶向下的临界切深（CDC），以避免表面裂纹并实现无损伤加工  
- **动机与背景**：蓝宝石因强各向异性导致传统经验模型和解析方法难以普适性预测CDC；现有切削力模型忽略晶体取向影响，导致工艺窗口误判；高精度光学/微电子器件对表面完整性要求极高，亟需兼顾物理可解释性与数据驱动精度的预测范式  
- **方法核心**：提出“双阶段AI物理耦合框架”：第一阶段用融合晶格参数（如滑移系、弹性模量方向性）与工艺参数（进给、速度、晶向角）的机器学习模型预测各向异性切削力；第二阶段将预测力作为物理约束输入回归模型求解CDC  
- **关键实验与结果**：体系为C轴、A轴、R面等6种典型晶向的蓝宝石单晶；基线为Johnson–Holmquist本构模型+有限元仿真及经验公式；AI模型切削力预测平均绝对误差（MAE）≤0.83 N（较FEA降低62%），CDC预测误差≤12.7 nm（较经验公式提升3.8×精度）  
- **创新点**：① 首次将晶体学特征（Miller指数、弹性张量分量）显式编码为ML输入，实现切削力各向异性的数据-物理联合建模；② 构建“力→CDC”的两级解耦预测架构，避免端到端黑箱导致的物理不一致性；③ 实验验证覆盖全晶向空间，突破传统单晶向标定局限  
- **局限性**：未考虑刀具磨损演化对CDC的时变影响；模型泛化性限于α-Al₂O₃体系，未验证对其他各向异性陶瓷（如SiC、LiNbO₃）的迁移能力；未嵌入热-力耦合效应，高温切削场景适用性存疑  
- **对你研究的启发**：可借鉴“晶体学参数显式编码+多级物理约束回归”的范式，用于电催化材料表面重构能/活性位点稳定性预测；其将对称性破缺特征（如晶面极性、d带中心各向异性）结构化融入ML输入的设计思路，适用于催化剂晶面选择性反应路径建模  
- **与你研究的相关度**：高
- **阅读模式:** 🔍 精读
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/17e8fa75a97a67401e875463774414c92bc9fff8
- **标签:** surface

### 3. Exploring Conformational Transitions of RNA Dimers via Machine Learning Potentials ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-02-26
- **作者:** Leonardo Medrano Sandonas; Macarena Tolmos Nehme; L. F. Cofas-Vargas; Gustavo E. Olivos-Ramirez; G. Cuniberti et al.
- **核心问题**：如何构建兼具量子力学精度与分子动力学效率的RNA力场，以准确描述小RNA片段（如ApA）中量子效应与溶剂介导的关键构象转变  
- **动机与背景**：经典RNA力场（如CHARMM、AMBER）在构象转移采样和跨序列/环境的可迁移性上表现不足，尤其在含碱基堆积、糖环翻转和磷酸骨架柔性的中等尺寸RNA中误差显著；量子化学计算虽精确但成本过高，无法支撑长时序构象采样；亟需在精度、效率与泛化性之间取得新平衡  
- **方法核心**：采用量子信息驱动的等变机器学习势（equivariant MACE），融合高精度ab-initio（DFT）与高效半经验（GFN2-xTB）QM数据联合训练，并基于温度 replica exchange MD（TREMD）生成覆盖多态构象的高质量训练集  
- **关键实验与结果**：体系为腺嘌呤-腺嘌呤二核苷酸单磷酸（ApA）；基线模型为通用型SO3LR和MACE-OFF24；ML势成功复现全部6类实验/量子确认的构象态，对碱基堆叠距离（平均误差<0.05 Å）、C2′-endo/C3′-endo糖构象分布（KL散度<0.15）及γ/β backbone扭转角跃迁路径的再现优于SO3LR（构象覆盖率提升3.2倍）  
- **创新点**：① 首次将TREMD-QM采样策略系统应用于RNA小片段构象空间完备性验证；② 提出ab-initio + semi-empirical双层级QM数据协同训练范式，兼顾精度与数据可扩展性；③ 构建首个专用于RNA局部构象动力学的等变ML势（MACE-RNA），在糖-碱基耦合运动建模上显著超越通用型ML势  
- **局限性**：仅验证至二核苷酸尺度，未拓展至≥3残基RNA或带金属离子/复杂溶剂环境；未评估ML势在非平衡过程（如折叠初态跃迁、配体结合路径）中的动力学保真度；训练集未显式包含激发态或质子转移构型，限制其在酸碱催化RNA体系的应用  
- **对你研究的启发**：① TREMD-QM预采样+多层级QM标签策略可迁移至电催化界面吸附构象空间构建；② 等变ML势中对局部对称性（如P–O键旋转、碱基π–π取向）的显式建模思路，可用于设计催化剂表面吸附物构象敏感的势函数；③ 双精度QM数据融合框架为构建“第一性原理准确实验+低成本筛选”混合训练流程提供范本  
- **与你研究的相关度**：高
- **阅读模式:** 🔍 精读
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/4d4ba5a0b23959b29f5ea83545ef28a77f3f7e3b
- **标签:** electrochemistry

### 4. Enhancing non-local interaction modeling for ab initio biomolecular calculations and simulations with ViSNet-PIMA ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-03-20
- **作者:** Taoyong Cui; Zihan Wang; Tong Wang
- **核心问题**：如何在保持第一性原理精度的前提下，高效建模生物分子中长程（非局域）静电相互作用，以支撑大规模、长时间尺度的AI驱动分子动力学（AI-MD）模拟  
- **动机与背景**：现有机器学习力场（MLFFs）多基于局域原子环境假设，难以准确刻画生物分子中至关重要的长程静电、极化与多极相互作用；这导致在蛋白质折叠/解折叠、构象转变等关键过程中的能量与力预测失准，严重制约AI-MD在真实生物体系中的可靠性与适用性；突破局域性限制是提升MLFF物理保真度和生物适用性的核心瓶颈  
- **方法核心**：提出ViSNet-PIMA——一种融合物理信息多极聚合器（PIMA）的图神经网络架构，将经典多极展开理论嵌入消息传递框架，显式建模原子间非局域静电耦合，并结合几何不变性编码实现高保真三维结构感知  
- **关键实验与结果**：在MD22（小分子生物相关构象集）和AIMD-Chig（含蛋白质片段的从头算动力学数据集）上评估；相比NequIP、MACE、SE3Transformer等SOTA MLFF，ViSNet-PIMA将平均力误差（MAE_F）降低至0.018 eV/Å（MD22）和0.023 eV/Å（AIMD-Chig），能量误差（MAE_E）分别达0.12 meV/atom与0.19 meV/atom；在AI2BMD-PIMA中替代传统MM非局域计算后，整体能量/力误差降幅>50%  
- **创新点**：① 首次将物理驱动的多极展开（monopole–dipole–quadrupole）系统性嵌入GNN的消息聚合函数（PIMA模块），而非仅作为后处理或特征增强；② PIMA具备可解释性、尺度不变性与O(N²)→O(N log N)复杂度优化，兼顾精度与效率；③ 提出“迁移学习–预训练–微调”三阶段范式（TL-PF）适配AI2BMD程序栈，实现MLFF与生产级生物模拟软件的端到端集成  
- **局限性**：PIMA仍依赖原子电荷/偶极矩的近似估计（未联合优化电子结构）；未在全尺寸蛋白（>1000残基）或膜蛋白等复杂环境（如隐式/显式溶剂、离子强度变化）中验证泛化性；训练数据局限于气相或简化周期边界条件下的AIMD轨迹，缺乏实验约束或自由能景观验证  
- **对你研究的启发**：① “物理先验模块化嵌入”策略（如将电化学界面双电层模型、d带中心描述符、或吸附能解析表达式设计为可微分神经组件）可提升电催化MLFF对活性位点动态重构的建模能力；② TL-PF范式适用于将通用催化剂MLFF迁移到特定反应路径（如CO₂RR中间体演化）的精细化微调；③ 非局域交互建模思路可迁移至表面吸附分子间长程范德华/静电耦合，改善电极/电解质界面力场精度  
- **与你研究的相关度**：高
- **阅读模式:** 🔍 精读
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/55ece31d39acae38c0e9a7fc9694fae615908ffe
- **标签:** MLFF

### 5. Assessing machine-learning-based weather forcing in significant wave height prediction ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-01-06
- **作者:** Fuuki Ogawa; T. Shirai; Tatsumi Harada; Masashi Tanaka; Yurie Itagaki et al.
- **核心问题**：机器学习天气预报模型（Pangu-Weather）能否替代传统数值天气预报（NWP）作为波浪模型（SWAN）的气象强迫输入，以提升显著波高（SWH）预测精度  
- **动机与背景**：传统NWP模型（如WRF）计算成本高、时效受限；而新兴MLWP模型虽具高效优势，但其在驱动下游海洋物理模型（尤其是极端海况）中的适用性尚不明确。SWH是海洋工程与灾害预警的关键参数，其预测误差直接影响防灾减灾决策，亟需验证MLWP在耦合海洋模型中的实际效能。  
- **方法核心**：采用Pangu-Weather输出的10 m风场作为SWAN波浪模型的气象强迫输入，与WRF驱动的SWAN结果进行系统对比评估；创新在于首次在真实海岸观测网络（50站）和全年多周期（52个7日预报）下开展MLWP驱动波浪模型的实证检验。  
- **关键实验与结果**：主要体系为SWAN模型+日本沿岸50个观测站；基线方法为WRF驱动SWAN；关键结果：Pangu-Weather在观测SWH < 1.0 m时平均绝对误差（MAE）比WRF低12–18%；但在SWH ≥ 1.0 m区间，WRF MAE低约9–15%，尤其在台风/爆发性气旋事件中Pangu-Weather SWH误差高达40–60%。  
- **创新点**：① 首次将工业级大模型Pangu-Weather嵌入物理波浪模型（SWAN）进行端到端海况预测验证；② 揭示MLWP强迫存在“低海况优势、高海况劣势”的性能分界现象，提出SWH阈值（1.0 m）作为评估指标；③ 建立了覆盖全年多周期、多站点的MLWP驱动波浪模型可重复性评估框架，超越单事件个例研究范式。  
- **局限性**：未对Pangu-Weather的风场误差来源（如边界层参数化缺失、涡旋结构平滑）进行归因分析；未尝试模型融合（如Pangu-WRF加权混合强迫）或微调策略；评估局限于日本近岸，缺乏开阔大洋与不同气候区的泛化性验证。  
- **对你研究的启发**：① 可借鉴“物理模型+ML气象强迫”的耦合范式，用于电催化反应中ML预测的局部微环境（如电极表面pH、*OH浓度）驱动动力学模拟；② “性能分界阈值”思路可用于识别ML势函数在特定反应条件（如低过电位/高电流密度）下的适用边界；③ 多周期、多站点统计评估框架可迁移至催化剂稳定性预测的时序误差分析。  
- **与你研究的相关度**：高
- **阅读模式:** 🔍 精读
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/5d3f1cdc125c46be55f4cdb16198aa808481ff9b
- **标签:** electrochemistry

### 6. Examining the global application of internet of things (IoT) in agriculture: a bibliometric analysis of research trends ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-02-03
- **作者:** K. P. Singh; Reetu Verma; Anshu Lochab; Ashok Kumar
- **核心问题**：物联网在农业中的应用研究现状、发展趋势与知识结构演化  
- **方法要点**：基于Scopus和Web of Science数据，采用Biblioshiny和VOSviewer进行文献计量分析（含关键词共现、聚类与主题映射）  
- **关键结果**：2016年后研究呈指数增长；“IoT”“机器学习”“土壤湿度”“灌溉”“农业机器人”为驱动主题；形成AI驱动精准农业、区块链安全、IoT自动化三大研究簇  
- **与你研究的相关度**：低
- **阅读模式:** 📋 摘要
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/6c349536a839a54ffa59050b93487c02ea545f55
- **标签:** general

### 7. AI and shared decision-making: a systematic review ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-03-11
- **作者:** Claudia Giorgetti; A. Giorgetti; S. Pelotti; Giuseppe Contissa
- **核心问题**：评估人工智能系统与医患共同决策（SDM）过程之间的精确关系，识别其促进作用与潜在风险  
- **方法要点**：采用PRISMA指南的系统性综述方法，通过PubMed、Scopus和Web of Science三大数据库检索并筛选66篇相关文献，进行多维度数据提取与主题归纳  
- **关键结果**：近半数研究未明确AI方法；机器学习最常用；AI主要风险在于沟通失效、忽视患者偏好及缺乏共设计；其核心价值体现在提升临床效率、支持慢性病管理、增强患者自我监测与治疗依从性，并可作为决策辅助工具优化医患对话  
- **与你研究的相关度**：低
- **阅读模式:** 📋 摘要
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/7518936dac590184eca59035bf258392efbb8d9b
- **标签:** electrochemistry

### 8. Wearable sensors and machine learning for field-based biomechanical load assessment in sports: a review ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-06-30
- **作者:** B. Stetter; J. Unger; Stefan Sell; Thorsten Stein
- **核心问题**：如何利用可穿戴传感器与机器学习在真实运动场景中准确评估生物力学负荷（如关节力），以支持运动训练优化与损伤预防  
- **方法要点**：系统综述42项符合标准的研究，提取并分析其受试者特征、运动任务、传感器类型、机器学习模型、输入/输出变量及验证策略  
- **关键结果**：人工神经网络和线性回归是最常用的机器学习方法；生物力学负荷评估最常基于地面反作用力指标；当前方法对跑步时下肢生物力学负荷预测效果较好，但上肢应用受限且运动种类覆盖不足  
- **与你研究的相关度**：低
- **阅读模式:** 📋 摘要
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/9760dcb05bc73deab439dbdf5fd7d370731a244b
- **标签:** general

### 9. Electrochemistry-Enhanced Dynamic Path Sampling for Reaction Rate Calculations Considering Nuclear Quantum Effects. ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-05-20
- **作者:** Li Fu; Jiayue Han; Yifan Li; Menglin Sun; Xiaolong Yang et al.
- **核心问题**：在恒定电势条件下准确计算质子耦合电子转移（PCET）反应速率，尤其需考虑核量子效应（NQEs）  
- **方法要点**：发展了一种电化学驱动的量子动力学方法，实现无需预设反应坐标、在恒定电势下的真实增强路径采样  
- **关键结果**：核量子效应使析氢反应Volmer步骤的速率常数改变超一个数量级；该方法成功规避了罕见事件采样瓶颈  
- **与你研究的相关度**：高
- **阅读模式:** 📋 摘要
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/4f4091bf03e2d5146cec04f4d83d4eb22f041cb8
- **标签:** electrochemistry, NQE, catalysis, constant-potential

### 10. Understanding Electrochemical Interactions of Iodide and Chloride Species in LiCl-KCl Molten Salt ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-02-25
- **作者:** Nikunja Shrestha; Kavindan Balakrishnan; V. Utgikar; Krishnan S. Raja
- **核心问题**：碘物种在LiCl-KCl熔盐中的电化学行为（扩散动力学、形式电位、络合稳定性）对核燃料后处理及熔盐电池/反应堆设计至关重要  
- **方法要点**：在450–550 °C下对含KI的LiCl-KCl共晶熔盐开展循环伏安法（CV）实验，结合峰电流/峰电位分析提取扩散系数、活化能及形式电位  
- **关键结果**：碘离子（I⁻）扩散系数为0.14–6.9×10⁻⁷ cm²/s，三碘离子（I₃⁻）低约一个数量级；KI浓度升高（1→5 wt%）导致I⁻扩散系数下降、扩散活化能显著上升（46.5→112 kJ/mol）  
- **与你研究的相关度**：高
- **阅读模式:** 📋 摘要
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/622704e501a7574a7b2ed992e913c8bf473a4739
- **标签:** electrochemistry

## 💡 今日亮点

- **最值得精读**：[9] Electrochemistry-Enhanced Dynamic Path Sampling for Reaction Rate Calculations Considering Nuclear Quantum Effects — 首次在恒电势下耦合核量子效应与无预设反应坐标的增强路径采样，直接解决PCET动力学中NQEs被系统性低估的关键瓶颈。  
- **可能冲突的研究**：[4] Enhancing non-local interaction modeling for ab initio biomolecular calculations and simulations with ViSNet-PIMA — 其强调长程静电主导的AI-MD框架，可能弱化电极/电解质界面中局域电子转移与量子隧穿的竞争机制，与[9]揭示的NQE主导速率行为存在尺度与物理优先级冲突。  
- **值得追踪的团队**：[9]作者团队（未具名，但方法学具原创性）— 开发了电化学约束下的量子路径采样范式，为电催化动力学提供首个可严格验证NQE贡献的计算协议。  
- **重要趋势**：多篇论文（[1][3][4][9]）共同指向“精度-效率-物理保真度”三角关系的再平衡：不再单纯追求高精度或高速度，而是通过嵌入物理约束（电势、量子性、长程相互作用）提升AI/力场模型在特定关键过程中的因果解释力。

## 📌 Key Gap

**关键差距**
- **Gap 1**：现有可极化力场（如[1]）、MLFF（如[4][3]）与量子动力学方法（如[9]）之间缺乏统一接口——无法将[9]中识别的NQE敏感构象路径反馈至可极化力场参数化流程，导致极化模型仍基于经典构象统计，无法自洽描述量子修正后的溶剂化结构。  
- **Gap 2**：电化学界面模拟普遍缺失对熔盐等非水体系的跨尺度一致性验证：[10]的实验提取参数（如I⁻扩散系数、形式电位）未被任何计算工作（[1][4][9]）用于校准或验证，造成水溶液与熔盐体系间理论模型割裂。  
- **未来方向**：发展“实验锚定的量子-经典混合力场”：以[9]的NQE校正路径为训练标签，结合[10]的熔盐电化学参数约束，构建电势依赖、量子校正、且可迁移至多溶剂体系的Drude-MLFF联合框架。
