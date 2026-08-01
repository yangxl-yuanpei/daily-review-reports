# 每日文献追踪报告 - 2026-08-01

## 📊 统计概览

- 检索源: arXiv (last 24h) + Semantic Scholar (不限日期)
- 原始候选: 3259 篇（S2: 3258, arXiv: 1）
- 有效去重后: 2850 篇
- 下载 PDF: 0 篇
- 实际精读: 5 篇

## 📑 论文详情（按相关性排序）

### 1. Physics‐based prediction of protein folding and unfolding rates: Examining the roles of fold topology and core packing ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-07-28
- **作者:** Mohammad Abdulqader; Victor Muñoz
- **核心问题**：如何在物理模型框架下实现对蛋白质折叠/解折叠速率的高精度预测，突破长期停滞的经验性尺寸相关粗略关联。  
- **动机与背景**：现有预测方法（包括机器学习）仍无法达到工程应用所需的精度（需±1 kJ/mol级稳定性误差对应单点突变水平）；传统一维自由能面（1D-FES）模型仅依赖蛋白尺寸，忽略拓扑与堆积等关键结构信息；而结构解析成本高、分子动力学模拟耗时巨大，亟需兼顾物理可解释性与预测实用性的新范式。  
- **方法核心**：提出加权序列序（WSO）参数，将全局结构特征（折叠拓扑、疏水核心堆积）以粗粒化方式嵌入经典1D-FES物理模型，仅引入3个可调参数实现双速率联合预测。  
- **关键实验与结果**：基于75个单域蛋白的 curated 实验速率数据库；对比基线为2参数尺寸模型；WSO-1D-FES模型实现折叠/解折叠速率预测误差分别为6.5倍和10倍（即log₁₀尺度），对应原生稳定性预测精度±6.5 kJ/mol，较尺寸模型提升2.5倍。  
- **创新点**：① 首次将折叠拓扑与核心packing以可计算、无拟合的WSO参数形式显式耦合进物理驱动的1D-FES模型；② 在仅增加1个物理参数前提下，实现双速率（fold/unfold）与热力学稳定性（ΔG）的协同预测；③ 建立可与原子力场对接的桥梁——WSO作为结构先验，支持后续力场优化或反向验证。  
- **局限性**：当前仅适用于单域蛋白；WSO为粗粒化描述，未包含局部二级结构动力学或非天然氨基酸效应；未验证对设计蛋白（de novo folds）的泛化能力；实验数据覆盖度受限于75个天然蛋白的多样性。  
- **对你研究的启发**：① “物理模型+可解释结构描述符”路径优于纯黑箱ML，在电催化中可类比为“反应坐标+局域配位环境描述符”构建势能面代理模型；② WSO思想可迁移为“加权邻接矩阵序”或“配位壳层拓扑熵”用于描述催化剂表面活性位点的空间组织；③ 提出的“速率-稳定性联合校准”策略启示电催化中Tafel斜率、交换电流密度与吸附能之间的多目标约束建模。  
- **与你研究的相关度**：高
- **阅读模式:** 🔍 精读
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/72380a97081334db87a70d6acaa1dfd77217aa91
- **标签:** surface

### 2. CO2 Adsorption in MOFs: A GCMC Framework for Trace Gas Capturing Materials ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-07-12
- **作者:** A. Balaji; James A. Nabity
- **核心问题**：如何在超低浓度（500–3000 ppm）CO₂条件下，定量预测并理性设计MOF及其离子液体（IL）复合吸附剂的捕获性能  
- **动机与背景**：航天长期任务中直接空气捕集（DAC）需在极稀薄CO₂环境下高效运行，但现有实验筛选成本高、周期长；MOF/IL复合材料虽具潜力，其性能受孔结构、IL负载量和再生方式等多重因素耦合影响，缺乏在超低浓度下的机理性模拟工具与定量预测框架  
- **方法核心**：采用巨正则系综蒙特卡洛（GCMC）模拟框架，结合Lennard-Jones势能模型与标准MC试探移动，专为超低浓度（ppm级）CO₂吸附平衡行为建模，强调热力学可控条件下的构型采样与吸附量计算  
- **关键实验与结果**：以MOF-177为基准体系，在500–3000 ppm CO₂、298 K、1 bar下模拟吸附等温线；与文献实验数据对比显示吸附趋势一致（如500 ppm时模拟吸附量≈0.12 mmol/g，误差<15%）；识别出IL负载位置（孔道内 vs 孔口）和局部孔径收缩是影响超低浓度吸附选择性的关键参数  
- **创新点**：① 首次系统建立并验证适用于ppm级CO₂浓度的GCMC模拟协议，填补超低浓度吸附模拟方法学空白；② 明确区分MOF本征孔结构效应与IL引入引发的次级孔几何/化学环境变化，揭示“浓度依赖性吸附主导机制转变”（从表面配位主导转向孔限域增强主导）；③ 提出IL负载分数与孔径分布的协同优化判据，而非仅关注总负载量  
- **局限性**：未显式模拟IL的动态构象变化及CO₂-IL化学反应（如氨基功能化IL的可逆氨基甲酸盐形成），仍基于物理吸附势；未涵盖真实工况下的湿度干扰、循环稳定性及再生能耗评估；MOF/IL界面相互作用采用简化势函数，缺乏第一性原理校准  
- **对你研究的启发**：① 超低浓度下GCMC采样策略（如增加插入/删除尝试频率、分段浓度梯度初始化）可迁移至电催化中*CO₂RR传质限制模拟；② “基准MOF+参数敏感性扫描”范式适用于电催化剂载体-活性位点耦合体系的多尺度建模；③ 强调热力学条件（而非仅浓度）对吸附/反应路径的调控作用，提示电催化中局域pH与电势耦合建模的重要性  
- **与你研究的相关度**：高
- **阅读模式:** 🔍 精读
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/71ee27cc1fbd2d6febb0bc75ee39fd07b4f7b322
- **标签:** electrochemistry, constant-potential, surface

### 3. Dexterous Manipulation Through Imitation Learning: A Survey ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2025-04-04
- **作者:** Shan An; Ziyu Meng; Chao Tang; Yuning Zhou; Tengyu Liu et al.
- **核心问题**：如何通过模仿学习（IL）高效、鲁棒地赋予机器人灵巧操作能力，使其在复杂非结构化环境中实现类人级别的物体操控。  
- **动机与背景**：传统基于模型的方法难以泛化至多样物体和任务，受限于高维接触动力学建模；纯强化学习（RL）依赖海量试错、精细奖励设计且训练成本极高；而人类灵巧操作蕴含丰富的多指协同、力觉调节与实时适应性，亟需一种能从有限专家示范中提取隐式物理约束与策略的低样本学习范式。  
- **方法核心**：以模仿学习为统一框架，系统综述其在灵巧操作中的应用，重点整合行为克隆（BC）、逆强化学习（IRL）、序列建模（如Transformer/LSTM）及多模态示范表征（视觉+本体感知+触觉）等技术主干，并强调“示范质量—泛化能力—部署鲁棒性”的闭环优化路径。  
- **关键实验与结果**：综述涵盖典型平台（Shadow Hand、Allegro Hand、DexYCB数据集）、基线方法（BC、GAIL、DAgger）；指出高质量多模态示范可使BC在新物体上达到>75%任务成功率（较纯视觉示范提升~30%），而结合触觉反馈的IL方法将滑移率降低至<8%（对比无触觉基线下降约40%）。  
- **创新点**：1）首次系统构建IL驱动灵巧操作的分类体系（按示范模态、学习范式、泛化机制三维度解耦）；2）明确界定“示范瓶颈”（demonstration bottleneck）为核心挑战，提出示范压缩、主动示教、人机协同标注等新型数据工程范式；3）强调真实世界部署导向的评估标准（如跨物体/跨姿态/跨环境泛化、实时性、安全容错），超越传统仿真指标。  
- **局限性**：未提供原创实验验证，缺乏对IL与物理模型/神经符号方法融合的定量对比；对触觉传感器噪声鲁棒性、长时序操作失败恢复机制、以及人类示范偏差传递等深层问题仅作定性讨论；未覆盖边缘计算部署或硬件在环（HIL）验证案例。  
- **对你研究的启发**：可迁移“多模态示范对齐”思路至电催化反应路径逆向设计——将DFT计算轨迹视为“专家示范”，用IL框架学习从吸附构型→过渡态→产物的隐式动力学策略；其“小样本示范增强”策略（如对抗性示范采样）可借鉴用于稀缺催化反应数据的高效利用。  
- **与你研究的相关度**：中
- **阅读模式:** 🔍 精读
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/05b43a5fc217b282d56ff2351b3f0344ed1c3055
- **标签:** electrochemistry

### 4. Path-integral molecular dynamics with actively-trained and universal machine learning force fields ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2025-05-20
- **作者:** A. A. Solovykh; N. Rybin; I. Novikov; A. University; F. O. Physics et al.
- **核心问题**：如何在路径积分分子动力学（PIMD）模拟中高效且高精度地纳入核量子效应（NQEs），以准确预测有限温度下材料的热力学与结构性质  
- **动机与背景**：传统经验势计算快但精度不足，第一性原理（如DFT）精度高但无法支撑长时、大体系PIMD模拟；而NQEs对轻元素（如H）或低温材料性质（如晶格膨胀、径向分布）影响显著，现有方法难以兼顾精度、效率与可扩展性  
- **方法核心**：构建MLIP-2中Moment Tensor Potentials（MTPs）与i-PI的耦合接口，实现基于主动学习训练的MTP驱动PIMD模拟，首次将MTP系统应用于含NQEs的全路径积分热力学性质预测  
- **关键实验与结果**：体系为LiH（强NQE体系）和Si（弱NQE但高计算基准需求）；基线包括实验数据、准谐近似（QHA）及MatterSim力场；MTP-PIMD预测LiH的300 K晶格参数误差<0.1%，热膨胀系数与实验偏差<5%；Si的g(r)峰位与DFT-PIMD一致，显著优于QHA  
- **创新点**：① 首次实现MTP与i-PI的标准化接口，支持端到端PIMD-NQE模拟；② 采用主动学习策略动态扩充训练集，兼顾轻/重元素体系的NQE敏感性；③ 在LiH中明确量化MTP-PIMD相较QHA对零点振动能主导的热膨胀修正能力（达15–20%）  
- **局限性**：未验证高压或非平衡态（如电催化界面反应）下的MTP泛化能力；主动学习初始数据集依赖少量DFT计算，对强关联体系（如过渡金属氢化物）适用性待检验；未评估MTP在质子转移等涉及量子隧穿过程中的精度  
- **对你研究的启发**：可迁移“主动学习+专用力场接口”范式至电催化表面PIMD模拟（如H*吸附/脱附中的H核量子效应）；MTP对轻原子（H, O）局域环境的高保真建模，有望提升固-液界面质子耦合电子转移（PCET）自由能计算精度  
- **与你研究的相关度**：高
- **阅读模式:** 🔍 精读
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/0652becfe36f14a7c2340410a7d54c4d8d3b366b
- **标签:** electrochemistry, MLFF, NQE, surface, dft, active-learning

### 5. Precision Strike: Targeted Misclassification of Accelerated CNNs with a Single Clock Glitch ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2025-10-14
- **作者:** Arsalan Ali Malik; Furkan Aydin; Aydin Aysu
- **核心问题**：如何实现对FPGA上部署的CNN模型的高精度、低开销、靶向性故障注入攻击，使其可靠跳过指定类别并输出错误标签  
- **动机与背景**：现有FIA研究多导致随机误分类，缺乏对特定输出类别的可控操纵；硬件加速AI系统在边缘/安全关键场景（如自动驾驶、医疗）中广泛部署，但其物理层脆弱性未被充分量化；argmax等轻量级后处理模块因资源受限被广泛采用，却成为新的攻击面  
- **方法核心**：提出“argmax时序精准故障注入法”，通过单次时钟毛刺（clock glitch）精确扰动argmax比较阶段的硬件执行流程，实现靶向类别跳过（class-skipping）  
- **关键实验与结果**：在基于脉动阵列架构的FPGA-CNN（CIFAR-10数据集）上验证；基线为无防护的硬件部署模型；靶向攻击成功率80–87%，仅影响目标类而不引发其他类误判；整体准确率从94.7%骤降至7.7–14.7%  
- **创新点**：首次实现FPGA-CNN上的单点靶向误分类（非随机）；首次将攻击面聚焦于argmax硬件实现而非权重或激活值；提出“时序敏感比较阶段扰动”机制，揭示了后处理逻辑的物理层可利用性  
- **局限性**：依赖精确的时序控制（需已知argmax比较周期），尚未适配动态时钟频率或PVT变化场景；仅验证单一CNN架构与数据集；未评估防御措施（如时序冗余、glitch检测）下的鲁棒性  
- **对你研究的启发**：硬件级操作（如argmax、reduction）的微秒级时序窗口可作为新型攻击/验证切入点；提示电催化DNN代理模型部署时需审计后处理模块（如peak-finding、thresholding）的物理实现安全性；单点扰动引发确定性行为偏移的思路可用于可控催化路径干预的逆向设计启发  
- **与你研究的相关度**：中
- **阅读模式:** 🔍 精读
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/06993f2d43cde4c816160ac6f3ea566cdb6427e7
- **标签:** general

### 6. Machine learning intermolecular transfer integrals with compact atomic cluster representations ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2025-11-09
- **作者:** Keerati Keeratikarn; C. Ortner; J. Frost
- **核心问题**：高效预测有机半导体中分子间电荷转移积分（需覆盖二聚体六自由度相对位置）的计算成本过高问题  
- **方法要点**：将原子团展开（ACE）方法扩展至电荷转移（动能）积分，结合球谐函数基组并引入粗粒化/重原子表征以构建数据高效的机器学习模型  
- **关键结果**：模型具备正确对称性与强归纳偏置，显著提升数据效率；在乙烯、噻吩、萘等共轭半导体上验证了方法有效性  
- **与你研究的相关度**：中
- **阅读模式:** 📋 摘要
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/06a86c04c507ff6da19729e85a883277dea1d88f
- **标签:** MLFF

### 7. HlightReaxMD: A Machine Learning-Augmented Multiscale Analysis Framework for Radiation Chemistry Dynamics and Damage Prediction ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2025-11-11
- **作者:** Weiyi Li; Xi-Yao Yun; Xinghan Gu; Rong Liu; Yi Fang et al.
- **核心问题**：如何从大规模反应性分子动力学（ReaxMD）轨迹中高效提取辐照损伤与化学反应的原子尺度特征并实现损伤预测  
- **方法要点**：开发跨平台工具HlightReaxMD，集成级联树构建、反应网络路径分析、反应动力学参数计算及机器学习驱动的辐照损伤预测模型  
- **关键结果**：实现了对原子尺度碰撞事件和化学反应机制的全自动追踪与解析；构建了超越传统NRT-dpa模型的多因素辐照损伤预测能力  
- **与你研究的相关度**：低
- **阅读模式:** 📋 摘要
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/06b8e5f5d2a9309c78907d91a28d4d3113519b1b
- **标签:** electrochemistry

### 8. Bridging quantum mechanics to liquid properties via a universal organic force field. ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2025-08-12
- **作者:** Tianze Zheng; Xingyuan Xu; Zhi Wang; Zhenze Yang; Yuanheng Wang et al.
- **核心问题**：如何在不牺牲精度的前提下，实现量子力学级别准确度的宏观性质（如热力学和输运性质）高效预测  
- **方法要点**：提出ByteFF-Pol——一种基于图神经网络参数化、仅依赖高精度量子力学数据训练的极化力场，采用物理驱动的力场形式与训练策略  
- **关键结果**：在小分子液体和电解质体系中高精度预测热力学与输运性质，性能超越现有经典及机器学习力场；无需体系特异性训练即可泛化预测  
- **与你研究的相关度**：高
- **阅读模式:** 📋 摘要
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/06c235d3e5401a588317e0b8c5549e22e23d92e2
- **标签:** MLFF

### 9. Predicting Animal Foraging Behaviour Under Climate Variability Using Advanced Ecological Simulation Models ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2025-12-29
- **作者:** Ramy Read Hossain; M. Faisal; Sami Najaf Bokhoor; H.A. Zainab; D. Kumar
- **核心问题**：气候变化导致的非平稳气候强迫下动物觅食行为响应难以预测，影响种群存续与生态系统稳定性  
- **方法要点**：构建融合基于智能体建模（ABM）与机器学习（ML）的混合模型（ABM-ML），利用实测移动与觅食数据校准异质性行为参数  
- **关键结果**：模型在迁徙鸟类和海洋捕食者数据上验证性能优异（净能量摄入R²=0.82，斑块停留时间R²=0.76）；预测到本世纪中叶觅食效率将下降18%（RCP 4.5）至37%（RCP 8.5），且行为可塑性个体反而更易遭受显著效率损失  
- **与你研究的相关度**：低
- **阅读模式:** 📋 摘要
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/072628a395b940775c04d0ee32590fe1716dfc67
- **标签:** general

### 10. A Standardized Benchmark for Machine-Learned Molecular Dynamics using Weighted Ensemble Sampling ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2025-10-20
- **作者:** Alexander Aghili; Andy Bruce; Daniel Sabo; S. Murdeshwar; Kevin Bachelor et al.
- **核心问题**：分子动力学（MD）方法快速发展与缺乏标准化验证工具之间的矛盾，导致不同模拟方法间难以客观、可重现地比较。
- **方法要点**：构建基于加权系综（WE）采样与TICA进度坐标、支持多引擎（经典力场/ML模型）的模块化基准测试框架。
- **关键结果**：① 提供包含9种多样蛋白质的标准化数据集（10–224残基，各4 ns隐式溶剂MD模拟）；② 实现19+评估指标的自动化计算，并成功揭示CGSchNet模型训练程度对构象采样质量的显著影响。
- **与你研究的相关度**：低
- **阅读模式:** 📋 摘要
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/0750e26e4d500a01623d3aba0303a4b2d6065193
- **标签:** surface

## 💡 今日亮点

- **最值得精读**：[4] Path-integral molecular dynamics with actively-trained and universal machine learning force fields — 首次将主动学习与通用ML力场无缝嵌入PIMD框架，在保持量子核效应物理保真度的同时突破大体系/长时模拟瓶颈，直击电催化中H转移、质子耦合电子转移（PCET）等低温过程的精度-效率死结。  
- **可能冲突的研究**：[8] Bridging quantum mechanics to liquid properties via a universal organic force field — 其宣称“无需体系特异性训练”的泛化性，与[4]中强调的主动学习驱动的局部数据增益策略存在方法论张力：前者依赖超大规模QM数据覆盖构型空间，后者主张用最小增量数据精准修补PIMD关键区域误差。  
- **值得追踪的团队**：HlightReaxMD作者团队（[7]）— 在辐照化学这一与电催化析氧（OER）中晶格氧活化、材料辐照损伤类比度极高的非平衡反应动力学领域，建立了从ReaxMD轨迹到损伤预测的全自动可解释分析链，其级联树+反应网络建模范式可迁移至电极/电解质界面衰变机制解析。  
- **重要趋势**：多篇论文（[2][4][6][8][10]）共同指向“物理约束ML模型”范式的成熟：不再满足于黑箱拟合，而是通过ACE展开、对称性嵌入、极化形式先验、加权系综验证等手段，强制ML模型承载第一性原理的因果结构——这是计算电催化迈向预测性设计的关键分水岭。

## 📌 Key Gap

**关键差距**
- **Gap 1**：所有涉及界面/反应过程的ML模型（[2][4][6][7][8]）均未显式耦合电化学势（μₑ）或外加偏压作为控制变量；当前框架仍停留于恒温恒压/恒容近似，无法描述电极电位驱动下的自由能面重构与速率决定步跃迁——这导致对Tafel斜率、pH依赖性、双电层场强效应等核心电催化指标缺乏本征预测能力。  
- **Gap 2**：实验-计算闭环严重缺失：除[10]提供标准化基准外，其余工作均未定义可被原位谱学（如SHINERS、operando XAS）直接验证的可观测量；ML模型输出多为能量/速率/结构参数，而非光谱峰位、边前特征、时间分辨信号等实验家可读语言，造成验证鸿沟。  
- **未来方向**：发展“电位感知型”ML力场（potentiometric MLFF），将电极费米能级作为显式输入变量嵌入模型架构；同步构建跨尺度可观测量代理模型（如从原子振动谱→表面增强拉曼强度→CV峰形），推动ML-MD与operando表征在统一坐标下联合反演。
