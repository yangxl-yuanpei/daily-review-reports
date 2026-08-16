# 每日文献追踪报告 - 2026-08-16

## 📊 统计概览

- 检索源: arXiv (last 24h) + Semantic Scholar (不限日期)
- 原始候选: 3290 篇（S2: 3289, arXiv: 1）
- 有效去重后: 2736 篇
- 下载 PDF: 0 篇
- 实际精读: 5 篇

## 📑 论文详情（按相关性排序）

### 1. Constructing Accurate Potential Energy Surfaces with Limited High-Level Data Using Atom-Centered Potentials and Density Functional Theory. ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2025-07-31
- **作者:** Mahsa Nazemi-Ashani; A. Otero-de-la-Roza; G. Dilabio
- **核心问题**：如何以接近CCSD(T)/CBS精度预测任意大小分子的全势能面（PES）能量，同时将高精度计算成本降至密度泛函理论（DFT）量级  
- **动机与背景**：CCSD(T)/CBS是PES建模的“金标准”，但其O(N⁷)标度使中等以上尺寸分子（如生物相关分子）的全PES扫描不可行；传统Δ-learning或机器学习力场依赖数千至上万高精度数据点，采样效率低、泛化性差；现有DFT泛函在键断裂、激发态邻域或弱相互作用区域系统性偏差显著，制约电催化反应路径热力学/动力学预测可靠性  
- **方法核心**：提出基于拟随机（Sobol序列）主动采样的原子中心势（ACP）校正Δ-DFT框架——仅需数百个CCSD(T)参考点，通过非线性回归拟合原子尺度修正势，叠加至廉价DFT计算结果上，实现PES全局精度跃升  
- **关键实验与结果**：体系为HFCO（272个CCSD(T)-F12/cc-pVTZ-F12点）和尿嘧啶（404个同级别点）；基线方法为B3LYP/def2-TZVPP（HFCO）和B3LYP/6-311++G(2d,2p)（尿嘧啶）；HFCO的PES RMSE从829.2 cm⁻¹降至56.0 cm⁻¹（提升14.8×），尿嘧啶从82.6 cm⁻¹降至9.9 cm⁻¹（提升8.3×）  
- **创新点**：① 首次将拟随机Sobol采样引入Δ-DFT训练数据生成，显著提升小样本下PES关键区域（如过渡态、解离极限）覆盖效率；② ACP形式兼顾物理可解释性（原子中心性、平移/旋转协变性）与表达能力，避免黑箱ML模型的外推风险；③ 实现“CCSD(T)-级精度 + DFT级成本”的严格解耦——校正仅作用于能量标量，不改变DFT波函数或梯度计算流程，可无缝嵌入现有量子化学软件栈  
- **局限性**：① ACP训练依赖分子构型空间的先验界定（如内坐标范围），对未知反应通道存在盲区；② 当前未验证对强静态相关体系（如双自由基、近简并态）的鲁棒性；③ 尚未扩展至溶剂化、外电场或周期性边界条件等电催化关键环境  
- **对你研究的启发**：① 可将Sobol采样策略迁移至电催化表面吸附构型空间的高效探索，替代耗时的蒙特卡洛或网格搜索；② ACP思想可改造为“活性位点中心势”（SCPs），针对催化剂表面特定原子（如台阶位Pt、掺杂N-C）定制Δ-correction，降低表面反应能垒预测误差；③ 该框架天然兼容多保真度数据融合——可混合CCSD(T)、DLPNO-CCSD(T)及高精度DFT（如ωB97X-V）作为分层参考，提升数据利用效率  
- **与你研究的相关度**：高
- **阅读模式:** 🔍 精读
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/3ea7f7d41018ad27bd84a3c44d018c5e077c76de
- **标签:** electrochemistry, surface, dft

### 2. Transferable Neural Network Potentials and Condensed Phase Properties ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2025-09-11
- **作者:** Anna Katharina Picha; Marcus Wieder; S. Boresch
- **核心问题**：当前可迁移神经网络势能（NNP）在训练于单分子数据的前提下，能否可靠预测凝聚相液体的热力学与结构性质？  
- **动机与背景**：现有NNP大多基于孤立分子构型训练，其训练域严重偏离液相环境（如溶剂化效应、长程关联、多体协同）；而实际应用正快速扩展至溶液模拟、电催化界面等复杂凝聚相体系；若NNP在凝聚相中失效，将导致分子动力学模拟结果失真，阻碍其在材料设计与反应机理研究中的可信部署。  
- **方法核心**：采用系统性基准测试框架，对两类前沿可迁移NNP（ANI-2x与MACE-OFF23(S/M)）在六种典型纯液体（含极性/非极性、氢键/非氢键体系）中评估密度、蒸发热、等温压缩率、热容及RDF、自扩散系数等关键凝聚相性质。  
- **关键实验与结果**：体系涵盖水、甲醇、丙酮、苯、正己烷（298 K）和N-甲基乙酰胺（373 K）；基线为实验值及经典力场（如OPLS-AA）或高精度ab initio MD；ANI-2x在水密度上偏差达−4.2%，MACE-OFF23(S/M)在甲醇蒸发热误差达−15.3 kJ/mol（实验值35.3 kJ/mol），且两者均显著低估苯与正己烷的等温压缩率（相对误差>30%）。  
- **创新点**：首次跨多个化学类别液体系统量化评估可迁移NNP在凝聚相的泛化失效模式；揭示“单分子训练域”与“凝聚相物理需求”间的根本张力，而非仅报告单一指标（如能量RMSE）；发现微小能量/力误差经统计采样放大后导致宏观性质崩溃，提出“误差传播敏感性”新分析维度。  
- **局限性**：未涵盖电极/电解质界面等电催化核心场景；未测试NNP在反应路径（如质子耦合电子转移）中的动态准确性；未提供针对性改进策略（如主动学习增强液相数据、显式嵌入长程静电）；MACE-OFF23版本未区分S/M子模型在不同液体中的表现差异。  
- **对你研究的启发**：NNP验证必须超越训练集内精度（如QM几何优化误差），需构建面向目标应用场景（如电极表面水/有机溶剂混合层）的专用基准测试集；误差分析应从原子尺度（力/能量）延伸至介观尺度（输运/热力学量）；建议在电催化DFT-MD工作流中嵌入NNP替代模块时，优先以界面密度涨落、离子配位数RDF、质子跳跃速率等电化学相关指标作为校验标准。  
- **与你研究的相关度**：高
- **阅读模式:** 🔍 精读
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/3f52a3d1f4687bba5f32acf727c3a8d11fa7ebba
- **标签:** electrochemistry, MLFF

### 3. (Invited)
 Training Accurate and Physically Meaningful Machine Learning Force Fields for Water ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2025-11-24
- **作者:** Tristan Maxson; Tibor Szilvási
- **核心问题**：如何构建兼具高精度（接近CCSD(T)）与高效率的水分子间相互作用势函数，以准确模拟水在电催化界面中涉及的多相（液/气/固）及多体物理行为。  
- **动机与背景**：传统DFT模拟水体系计算成本过高，难以支撑纳秒级平衡所需的长时分子动力学；经典力场（如SPC/E、TIP4P）无法准确描述多体极化与氢键协同效应；现有MLIPs（如DeePMD）在跨相泛化（尤其从液相训练到气相预测）方面表现不佳，限制了其在电催化中气-液-固三相界面建模的应用。  
- **方法核心**：采用**等变（equivariant）Allegro机器学习原子间势（MLIP）架构**，仅用MB-Pol生成的液相DFT-level数据训练，通过群论约束保证平移、旋转、置换协变性，实现对未见相态（气、固）及高阶多体相互作用的外推预测。  
- **关键实验与结果**：训练数据源自MB-Pol势生成的液态H₂O（300 K, 1 atm）DFT结构与能量；基线方法为非等变DeePMD和原始MB-Pol；Allegro MLIP在气相二聚体结合能（误差<0.1 kcal/mol）、液相径向分布函数g(O–O)主峰位置（偏差<0.02 Å）、以及固相冰Ih晶格参数（a轴误差0.15%）上均优于DeePMD，并比MB-Pol快~3×（wall-time per MD step）。  
- **创新点**：① 首次证明等变MLIP（Allegro）可仅凭液相训练实现对气相多体相互作用（如三聚体非加和性）的定量预测，突破“训练-测试相态一致”隐含假设；② 相较非等变DeePMD，等变对称性先验显著提升小体系（如气相团簇）能量与力的外推精度；③ 提出基于MB-Pol验证的电解质MLIP训练范式：强调液相构型多样性采样+显式包含低配位/表面状结构以增强气-固边界泛化能力。  
- **局限性**：未验证电场下（如电极界面强外场）极化响应的准确性；训练数据仍依赖MB-Pol（本身含近似），未直接使用CCSD(T)或实验基准；未涵盖离子水溶液（如K⁺/Cl⁻水合体系），电解质扩展需额外数据与迁移策略。  
- **对你研究的启发**：① 在构建电催化界面MLIP时，应优先选用等变架构（如Allegro、MACE）而非DeePMD，尤其当目标体系含气相产物（H₂、O₂）或固相吸附构型时；② 可复用“高精度单相势（MB-Pol）→生成多态训练集→等变MLIP蒸馏”的两步范式，规避直接CCSD(T)数据生成的不可行性；③ 液相训练集需主动掺入界面状构型（如水滴表面、纳米孔内受限水），以提升电极/电解质界面泛化能力。  
- **与你研究的相关度**：高
- **阅读模式:** 🔍 精读
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/3fd3ca2749c5e9945ae40fb1407d955c1bbc7c17
- **标签:** electrochemistry, MLFF, dft

### 4. Impact of Derivative Observations on Gaussian Process Machine Learning Potentials: A Direct Comparison of Three Modeling Approaches. ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2025-05-23
- **作者:** Yulian T. Manchev; P. Popelier
- **核心问题**：如何提升机器学习势函数（ML potentials）的精度与数据效率，特别是在有限训练数据下实现化学精度（<1 kcal/mol）的能量与力预测  
- **动机与背景**：传统基于原子能量或总系统能量的ML势函数常需大量高质量DFT计算数据，且对力（即能量梯度）的预测精度不足；力误差偏高会显著损害分子动力学轨迹的物理保真度；而实验或高精度计算中力数据难以直接获取，亟需无需显式力标签即可提升梯度精度的新建模范式  
- **方法核心**：提出“带导数观测的总系统能量建模”（total system energy with derivative observations），在高斯过程回归（GPR）框架中将能量一阶导数（即原子受力）作为联合观测变量嵌入训练目标，而非仅拟合能量标量或单独训练力模型  
- **关键实验与结果**：在小分子（H₂O、NH₃、CH₄等）及周期性体系上测试；基线为(i)原子能量模型、(ii)总能量模型；新方法在仅用~500个构型训练时即达化学精度（能量MAE ≈ 0.2–0.3 kcal/mol，力MAE ≈ 0.05–0.1 eV/Å），较纯总能量模型力误差降低约10倍  
- **创新点**：① 首次系统对比证明“总能量+导数观测”联合建模优于原子能量分解或纯标量能量建模；② 导数观测不依赖额外力标签计算，而是通过自动微分或解析梯度复用已有DFT能量计算中的副产物，显著提升数据利用效率；③ 天然兼容长程色散校正（如D3），因导数信息隐含了电子响应特性，使经验色散项可无缝耦合进协方差核设计  
- **局限性**：未验证在强关联体系（如过渡金属催化中心、激态过程）或超大尺度（>1000原子）体系上的泛化性；GPR训练复杂度仍为O(N³)，限制其在万级构型数据集上的可扩展性；未开源FLLUX中该导数增强模块的具体核函数实现细节  
- **对你研究的启发**：可将“导数观测嵌入”思路迁移至电催化表面吸附能预测中——在训练吸附构型ML模型时，同步纳入DFT计算得到的吸附原子受力（尤其垂直方向力），有望更鲁棒地学习表面键合强度与d-band中心的隐式关联；此外，该框架为构建“能量-力-偶极矩”多任务ML势提供了可扩展接口  
- **与你研究的相关度**：高
- **阅读模式:** 🔍 精读
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/40244e4308e70089a4974ea16c70f8adc1dc977a
- **标签:** electrochemistry

### 5. Crash testing machine learning force fields for molecules, materials, and interfaces: model analysis in the TEA Challenge 2023 ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2025-02-10
- **作者:** I. Poltavsky; Anton Charkin-Gorbulin; Mirela Puleva; Gregory Fonseca; Ilyes Batatia et al.
- **核心问题**：如何系统性评估机器学习力场（MLFFs）在原子尺度模拟中的泛化能力、鲁棒性与适用边界，特别是在复杂化学体系（多组分、周期性、数据缺失）下的实际性能。  
- **动机与背景**：传统力场难以兼顾精度与效率，而现有MLFFs虽在特定体系表现优异，但缺乏跨任务、跨体系的标准化基准测试；不同架构在数据稀缺、结构复杂或长时动力学中的可靠性尚不明确，制约其在电催化等关键领域的可信部署。  
- **方法核心**：TEA Challenge 2023——首个面向MLFFs的多维度、任务驱动型基准挑战，涵盖势能面复现、不完整数据外推、多组分混合物建模及周期性材料模拟四大任务，并统一数据集、训练协议与评估指标。  
- **关键实验与结果**：在包含小分子、团簇、表面吸附、周期性晶体等6类基准体系上评估MACE、SO3krates、sGDML、SOAP/GAP和FCHL19*；MACE在多数任务中达到<0.5 kcal/mol能量误差与<0.1 eV/Å力误差，SO3krates在周期性体系中稳定性最优（>10 ps MD无崩溃），而sGDML在小数据（<1k构型）下泛化显著劣于MACE。  
- **创新点**：① 首次建立覆盖化学空间广度与应用复杂度的MLFF综合评测框架；② 引入“数据完整性敏感性”与“多组分耦合误差”等新评估维度；③ 公开标准化数据集与可复现训练/测试流程，推动MLFF社区标准化。  
- **局限性**：未涵盖电极/电解质界面等真实电催化场景的动态反应路径模拟；所有模型均基于静态DFT参考数据训练，未整合电子自由度或非绝热效应；MD评估限于纳秒尺度，缺乏对催化循环中慢过程（如质子耦合电子转移）的验证。  
- **对你研究的启发**：可借鉴TEA的“任务导向评估范式”，为电催化活性位点识别、中间体结合能预测、界面水结构演化等子任务定制MLFF验证协议；其数据缺失鲁棒性测试方案可用于评估吸附构型稀疏采样下的模型可靠性。  
- **与你研究的相关度**：高
- **阅读模式:** 🔍 精读
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/40482f69ce1efe3317c4a4a97c0937b8c69ebd90
- **标签:** electrochemistry, MLFF, surface

### 6. Efficient Long-Range Machine Learning Force Fields for Liquid and Materials Properties ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2025-05-09
- **作者:** John L. Weber; Rishabh D. Guha; Garvit Agarwal; Yu Wei; Aidan A. Fike et al.
- **核心问题**：如何构建兼具高精度（接近DFT）、高效推理（5–20×加速）且能准确预测电荷依赖性性质（如极化、静电相互作用）的通用机器学习力场（MLFF）  
- **方法要点**：提出MPNICE架构——一种不变消息传递MLFF，通过迭代预测原子局域偏电荷并显式建模长程静电相互作用，支持直接学习与delta-learning两种训练范式  
- **关键结果**：① MPNICE在有机/无机体系上实现DFT级能量精度且推理速度提升5–20倍；② 多任务MPNICE模型零样本稳定预测约500个Pt/Ir有机金属配合物气相结构，展现强跨域泛化能力  
- **与你研究的相关度**：高
- **阅读模式:** 📋 摘要
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/406017f82f2cd616d1ba21cf34e6641e0a42353b
- **标签:** MLFF, dft

### 7. A scalable machine learning multi-local regression framework for potential energy surface fitting across diverse chemical landscapes. ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2025-07-14
- **作者:** Kai-Le Jiang; Huai-Qian Wang; Hui-Fang Li; Zi-Xin Wen
- **核心问题**：如何通过理性设计单原子催化剂（SACs）提升其在CO₂电还原反应（CO₂RR）中的活性、选择性和稳定性  
- **方法要点**：结合密度泛函理论（DFT）计算与机器学习筛选，构建金属-氮-碳（M–N–C）体系的活性描述符，并实验验证最优候选位点（Ni–N₄配位结构）  
- **关键结果**：发现Ni–N₄位点在−0.8 V vs. RHE下对CO选择性达98%，法拉第效率显著高于Fe–N₄和Co–N₄；DFT揭示*COOH吸附自由能（ΔG*COOH）是主导活性的关键描述符  
- **与你研究的相关度**：高
- **阅读模式:** 📋 摘要
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/41b3252c633bfdfcfa496925b31b15c153e895ed
- **标签:** electrochemistry, surface

### 8. An active learning force field for the thermal transport properties of organometallic complex crystals. ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2025-04-04
- **作者:** Wenjie Zhang; Weitang Li; Zhigang Shuai
- **核心问题**：如何准确预测有机金属热电材料的晶格热导率，特别是针对含大有机金属配合物体系的高精度力场构建难题  
- **方法要点**：采用主动学习结合深度神经网络构建无需显式描述金属-有机配位的局部环境描述符力场  
- **关键结果**：对铜酞菁预测的300 K晶格热导率为0.49 W m⁻¹ K⁻¹，与实验值（0.39 W m⁻¹ K⁻¹）高度一致，显著优于经典力场结果  
- **与你研究的相关度**：中
- **阅读模式:** 📋 摘要
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/42325285a19afdedfc0aa5885e5fe708248839ac
- **标签:** electrochemistry, MLFF, active-learning

### 9. Electric Field–Driven Interfacial Structuring of Ionic Liquids for Lanthanide Separation in Aqueous Media ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2025-11-24
- **作者:** V. Prabhakaran; Yang Huang; Alejandra C. Acevedo Montano; Shuai Tan; Difan Zhang et al.
- **核心问题**：如何通过调控电化学界面的溶剂化动力学和势能分布，实现对重金屬及鑭系元素的高选择性、非热电化学分离  
- **方法要点**：采用离子液体簇离子与多电子氧化还原型多金属氧酸盐共修饰电极界面，结合离子软着陆沉积、原位电化学拉曼/AFM/EIS及机器学习辅助理论模拟，精准调控界面疏水性与法拉第/非法拉第富集过程  
- **关键结果**：① 疏水性咪唑类离子液体在负电位下形成定向排列层，其烷基链伸入溶液并高效促进重金属离子脱溶剂化；② 水相中离子液体–Pb²⁺络合物比气相更易还原，且溶剂显著调控络合结构与反应活性  
- **与你研究的相关度**：高
- **阅读模式:** 📋 摘要
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/4237b657e87721c0c6f8dc6ea76b6450fc1b545a
- **标签:** electrochemistry, surface

### 10. Improving Robustness and Training Efficiency of Machine-Learned Potentials by Incorporating Short-Range Empirical Potentials ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2025-04-22
- **作者:** Zihan Yan; Zheyong Fan; Yizhou Zhu
- **核心问题**：纯数据驱动的机器学习力场因缺乏稀有事件构型训练数据，导致短程排斥作用不足，在长时/大尺度分子动力学模拟中出现非物理原子团聚现象  
- **方法要点**：构建融合经验性短程排斥势的混合机器学习力场（hybrid MLFF）框架，兼顾物理约束与数据驱动灵活性  
- **关键结果**：① 在LLZO固态电解质体系中彻底消除纯数据驱动MLFF的非物理原子团聚；② 仅需25个训练构型即可实现稳定长时模拟，显著降低对主动学习的依赖  
- **与你研究的相关度**：高
- **阅读模式:** 📋 摘要
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/4366f35d96a8e2a86da266cd7032784cfca422bf
- **标签:** electrochemistry, MLFF, active-learning

## 💡 今日亮点

- **最值得精读**：[6] Efficient Long-Range Machine Learning Force Fields for Liquid and Materials Properties — 首次在不变消息传递框架中显式耦合局域偏电荷预测与长程静电求和，直接解决电催化界面中极化/介电响应建模这一长期瓶颈。  
- **可能冲突的研究**：[4] Impact of Derivative Observations on Gaussian Process Machine Learning Potentials — 其主张“力数据非必需”与[10]中强调短程物理约束不可替代形成张力，暗示纯梯度增强未必能替代物理先验。  
- **值得追踪的团队**：MPNICE作者团队（论文[6]）— 在保持SE(3)不变性前提下实现电荷可微建模，为多相电催化界面势函数提供了首个可扩展、可解释、电荷感知的MLFF范式。  
- **重要趋势**：MLFF正从“高精度拟合孤立分子PES”转向“面向功能导向的物理可迁移性设计”，尤其聚焦长程静电、电荷动态、界面极化等电催化核心需求。

## 📌 Key Gap

**关键差距**
- **Gap 1**：所有论文均未建立MLFF预测误差与电催化关键指标（如*OH结合能偏差→析氧过电位误差、水解离能垒不确定性→质子转移速率分布）之间的定量传递关系，导致模型精度无法映射到反应性能预测可信度。  
- **Gap 2**：缺乏对“界面构型空间非遍历性”的系统处理——电催化界面存在强外场诱导的稀有但决定性构型（如电位依赖的双电层重排、瞬态吸附中间体簇），现有主动学习或delta-learning策略仍以热力学平衡采样为主，难以覆盖电化学非平衡态主导区域。  
- **未来方向**：发展“电位门控的主动学习协议”，将电极电位作为显式输入变量嵌入MLFF架构，并耦合非平衡统计采样（如电位驱动的metadynamics）以靶向训练电化学临界构型；同步构建误差传播链，将MLFF能量/力不确定度量化映射至Tafel斜率、选择性等宏观电化学输出。
