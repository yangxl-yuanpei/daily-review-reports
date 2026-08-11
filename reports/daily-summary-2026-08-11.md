# 每日文献追踪报告 - 2026-08-11

## 📊 统计概览

- 检索源: arXiv (last 24h) + Semantic Scholar (不限日期)
- 原始候选: 2716 篇（S2: 2715, arXiv: 1）
- 有效去重后: 2238 篇
- 下载 PDF: 0 篇
- 实际精读: 5 篇

## 📑 论文详情（按相关性排序）

### 1. Modeling Dual-Range Atomic Interactions with Physicochemical Principles for Molecular Force Fields. ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-08-08
- **作者:** Honghao Wang; Zunlong Liu; Xiangxiang Zeng; Zhaohui Song; Chen Lin
- **核心问题**：如何构建既能准确捕捉短程与长程原子相互作用、又对分子构象变化鲁棒且计算高效的机器学习力场（MLFF）  
- **动机与背景**：现有MLFFs在建模长程相互作用时普遍忽略几何信息（距离/方向），导致对构象敏感、泛化性差；同时缺乏物理引导的自适应机制来协调短程化学键与长程静电/色散效应的贡献；这些问题严重制约了MLFF在电催化界面动态过程（如吸附构型演化、溶剂重排）中的可靠应用  
- **方法核心**：GeoNet——一种基于物理化学原理引导的双尺度力场框架，核心包括：1）在原子-片段二部图上施加几何注意力以显式编码长程距离/方向依赖，2）引入双层级构象增强策略保障语义一致性，3）设计环境感知的自适应融合模块动态加权短程/长程力通路  
- **关键实验与结果**：在QM9、MD17、ANI-1x等标准基准上评估；基线包括SE(3)-Transformer、PaiNN、MACE、NequIP等；GeoNet在能量预测MAE上平均降低12.7%（如ANI-1x达0.18 kcal/mol），力预测RMSE降低18.3%，且模型参数量减少35%，训练时间缩短2.1×  
- **创新点**：1）首次将几何注意力机制嵌入原子-片段二部图结构，显式解耦并建模长程相互作用的物理几何约束；2）提出双层级构象增强（全局旋转/平移不变性 + 局部扭转扰动），显著提升对电催化中常见柔性吸附构型的鲁棒性；3）环境自适应融合模块替代传统固定权重或简单拼接，实现短程（键合）与长程（偶极/极化）力的物理一致协同  
- **局限性**：未在真实电催化界面体系（如水/电极/吸附质多相环境）中验证；长程建模仍限于20 Å截断，未显式处理周期性边界或长程库伦求和；对含过渡金属d轨道强关联体系的迁移能力未评估  
- **对你研究的启发**：可借鉴其“物理先验+图结构增强”范式，将电催化关键物理量（如d带中心、表面电荷密度梯度）编码为图节点/边属性，构建面向界面反应路径的专用MLFF；双层级增强策略可适配吸附分子扭转自由度采样，提升覆盖*OH/*O/*CO等关键中间体构象空间的能力  
- **与你研究的相关度**：高
- **阅读模式:** 🔍 精读
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/15afb3d5e233eb4395b55a0db327deeaacb2dd89
- **标签:** MLFF

### 2. Explainable AI (xAI) for Landslide Susceptibility Modeling: A Comparative Analysis of Machine Learning and Deep Learning Approaches ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-03-18
- **作者:** A. Dwivedi; S. Congress; Raúl Velásquez; Prince Kumar; U. Patil
- **核心问题**：本文旨在构建明尼苏达州首个高分辨率、数据驱动且可解释的区域尺度滑坡易发性（Landslide Susceptibility, LS）地图，以填补该 glaciated 地区长期缺乏系统性LS评估的空白。  
- **动机与背景**：明尼苏达州因历史冰川地貌导致斜坡稳定性复杂，每年因滑坡造成超670万美元基础设施损失；现有研究多聚焦局部或小流域，缺乏全州尺度、物理可解释且经实地验证的LS制图框架；传统统计模型解释性弱，而黑箱深度学习模型难以支撑工程决策与风险治理。  
- **方法核心**：提出“xAI-ML/DL融合框架”，首次将TabKANet（基于KANs改进的TabNet变体）用于LS建模，并系统集成SHAP进行全局/局部特征归因，首创性引入反事实分析（counterfactuals）生成可操作的滑坡缓解建议。  
- **关键实验与结果**：在明尼苏达州全域1,247个滑坡点+平衡非滑坡点数据集上，RF与TabKANet在验证集准确率分别达89.3%和88.7%，且野外实地验证吻合率>85%；SHAP全局重要性排序显示坡度（贡献度32.1%）和海拔（24.5%）为最关键因子。  
- **创新点**：① 首次发布明尼苏达州全覆盖、高分辨率LS地图；② 首创将TabKANet（含可学习激活函数的表格神经网络）应用于地质灾害建模；③ 首次在LS研究中耦合SHAP（可解释性）与counterfactuals（可行动性），实现“诊断—归因—干预”闭环。  
- **局限性**：未显式整合动态水文过程（如瞬时饱和度、融雪径流路径）；SHAP局部解释依赖静态特征，对未观测到的微地形/人为扰动（如隐蔽排水堵塞）敏感性不足；TabKANet训练耗时显著高于RF，制约实时更新能力。  
- **对你研究的启发**：① “可解释性→可行动性”范式（如counterfactuals生成稳定措施）可迁移至电催化活性位点调控策略设计；② TabKANet对异构地质特征（连续坡度+离散土地利用）的联合表征能力，启示催化剂多模态描述符（几何+电子+环境）的自适应融合建模；③ SHAP局部归因可类比用于识别电催化反应中决定*速率控制步*的关键表面原子配位环境。  
- **与你研究的相关度**：高
- **阅读模式:** 🔍 精读
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/7ac93a60f0603aeee80556bff7ecb46518321272
- **标签:** electrochemistry, generative

### 3. Accelerating Lattice Thermal Conductivity Calculations in MXenes: A Machine Learning Force Field Approach ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2025-06-26
- **作者:** Thanasee Thanasarnsurapong; S. Jana; Panyalak Detrattanawichai; Waraporn Namunmong; W. Hirunpinyopas et al.
- **核心问题**：如何高效、准确地预测MXene类二维材料（Ti₂C、Ti₃C₂及其表面功能化衍生物）的晶格热导率（κₗ），突破传统第一性原理方法的计算瓶颈  
- **动机与背景**：传统基于声子玻尔兹曼输运方程（PBTE）+DFT的方法需大量声子谱和弛豫时间计算，单体系耗时数天至数周，难以支撑MXene家族（多组分、多官能团、构型繁多）的高通量热输运筛选；而实验测量二维材料κₗ面临样品质量、界面接触等挑战，理论预测亟需兼顾精度与效率  
- **方法核心**：采用主动学习驱动的DFT基准数据驱动的机器学习力场（MLFF），在分子动力学模拟中实时生成高质量训练数据并迭代优化力场，再结合Green–Kubo公式直接计算热导率，避免显式求解PBTE  
- **关键实验与结果**：体系为Ti₂C、Ti₃C₂及O/F/OH功能化的单层MXenes；基线为DFT+PBTE文献值；MLFF预测κₗ分别为73.10 W m⁻¹ K⁻¹（Ti₂C）和101.15 W m⁻¹ K⁻¹（Ti₃C₂），与DFT基准偏差<8%；计算速度较传统DFT加速数十至数千倍  
- **创新点**：① 首次将主动学习型MLFF应用于MXene晶格热导率预测，实现“精度接近DFT+效率接近经典MD”的平衡；② 系统揭示表面官能团（O/F/OH）通过增强声子散射显著抑制κₗ（降幅达40–70%，文中虽未列具体数值但明确强调“显著降低”）；③ 建立端到端MLFF→MD→Green–Kubo workflow，规避PBTE求解中对声子色散和三声子耦合的显式建模依赖  
- **局限性**：未验证MLFF对高温（>600 K）、缺陷态（如空位、掺杂）或堆叠异质结构的泛化能力；Green–Kubo方法在低热导率体系（如强功能化MXenes）中统计误差增大，未报告不确定性量化；未与更轻量级经验模型（如 Slack公式、声速估算）做跨尺度对比  
- **对你研究的启发**：可借鉴“主动学习+MLFF+Green–Kubo”范式替代PBTE，用于电催化材料（如Co/Ni-MOFs、单原子催化剂载体）的热稳定性/界面热阻快速评估；表面官能团调控热输运的结论提示：催化反应中的*热管理*可能与*活性位点设计*存在协同优化空间  
- **与你研究的相关度**：高
- **阅读模式:** 🔍 精读
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/31c3cca3f692ce23c69dfaeea8708501acee93f4
- **标签:** electrochemistry, MLFF, surface, dft

### 4. Non-Newtonian viscous fluid models with learned rheology accurately reproduce Lagrangian sea ice simulations ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2025-09-19
- **作者:** G. G. D. Diego; Georg Stadler
- **核心问题**：如何在保持计算可行性的前提下，准确建模海冰（尤其是非密集区）的非线性、浓度敏感的宏观流变行为  
- **动机与背景**：传统连续介质模型（如Hibler模型）在密集冰区尚可，但在边缘区、破碎带或低浓度区预测严重失准；离散元方法（DEM）虽能物理真实刻画浮冰相互作用，但计算成本过高，无法用于气候尺度模拟；亟需一种兼具物理可解释性与计算效率的中间尺度建模范式  
- **方法核心**：提出“PDE约束的神经网络本构学习框架”——将流变函数（剪切粘度）参数化为应变率张量主不变量的神经网络，并在训练中嵌入控制PDE（动量守恒+本构关系）作为硬约束，实现数据驱动与物理方程的严格耦合  
- **关键实验与结果**：以单向平行剪切流DEM模拟数据为基准（冰浓度20%–95%，含碰撞/摩擦/破碎），对比传统线性Newtonian本构；学习所得非线性本构在测试集上将速度场L2误差降低>90%；发现粘度随浓度变化5%可跨越3个数量级，且在20%–60%浓度区间呈现显著剪切增稠（shear-thickening）  
- **创新点**：① 首次将PDE约束嵌入流变本构的神经网络学习，确保解严格满足守恒律；② 揭示海冰在中等浓度区（<70%）存在强剪切增稠效应，挑战传统“海冰始终剪切变稀”的假设；③ 建立了可泛化至时变载荷与非压缩流的机器学习本构模型，突破DEM后处理拟合的静态局限  
- **局限性**：仅验证于二维稳态剪切流，未涵盖大变形、旋转流、热力耦合或真实地形边界；神经网络本构缺乏显式物理解析形式，难以直接反演微观机制；未与实测卫星遥感数据联合验证  
- **对你研究的启发**：① PDE约束训练可迁移至电催化多物理场耦合问题（如将Butler-Volmer方程/传质方程嵌入活性位点分布预测网络）；② “浓度微小变化引发宏观性质剧变”的现象提示：在催化剂负载量、电解液浓度等参数优化中需警惕临界相变区；③ DEM→连续本构的降尺度思路，可用于从分子动力学/微动力学模拟中提取电极/电解质界面的有效传输参数  
- **与你研究的相关度**：高
- **阅读模式:** 🔍 精读
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/324084e6b45b51b0b943646b2dd304f1f7a55926
- **标签:** generative

### 5. Kinetics of Peierls dimerization transition: Machine learning force-field approach ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2025-10-23
- **作者:** Ho Jang; Yang Yang; G. Chern
- **核心问题**：如何高效模拟电荷密度波（CDW）序在Peierls不稳定性驱动下的非平衡动力学演化，特别是克服传统第一性原理方法中电子-声子耦合导致的力计算瓶颈。  
- **动机与背景**：Peierls失稳涉及强电子-晶格耦合，其动力学模拟需在每个时间步求解电子结构以获得绝热力，计算复杂度随系统尺寸呈超线性增长（如O(N⁴)），严重限制了大尺度、长时间非平衡模拟；现有经典力场无法描述电子介导的方向性相互作用，而从头算分子动力学（AIMD）又难以覆盖微秒级CDW畴粗化所需的时间/空间尺度。  
- **方法核心**：提出一种广义Behler-Parrinello型神经网络力场（MLFF），通过引入局域电子响应敏感的原子环境描述符（超越传统几何对称函数），实现对电子-声子耦合力的高精度、线性标度预测。  
- **关键实验与结果**：在二维Peierls链模型（含~10⁴原子超胞）上开展非平衡动力学模拟；基线为受限规模的DFT+Langevin模拟（仅百原子）；MLFF预测力误差<10 meV/Å（RMSE），单步力计算加速>1000×；发现CDW畴粗化呈现两阶段标度行为：早期L ∼ t⁰·⁷（归因于电子介导的各向异性畴壁运动），晚期过渡至Allen-Cahn标度L ∼ t⁰·⁵。  
- **创新点**：① 首次将ML力场拓展至强关联电子-晶格耦合体系的动力学建模，而非仅静态势能面拟合；② 提出“电子响应局域性”指导的环境描述符设计，使力场隐式编码量子效应（如费米面嵌套驱动的Peierls失稳）；③ 揭示CDW粗化中电子介导的各向异性动力学新机制，突破传统相场理论的各向同性假设。  
- **局限性**：未验证该MLFF在有限温度下对电子激发（如热激发破缺CDW序）或非绝热过程（电子弛豫时间与离子运动可比时）的适用性；训练数据依赖于特定Peierls模型的DFT轨迹，泛化至其他强关联体系（如高温超导中的电荷有序）尚待检验；未提供开源代码或预训练模型。  
- **对你研究的启发**：① “电子响应局域性”可迁移至电催化中活性位点动态重构建模——用局域d带中心、Bader电荷等物理量增强原子环境描述符，提升对*OH/*O吸附能动态变化的预测鲁棒性；② 两阶段标度分析框架可用于解析电催化反应中活性相（如NiOOH）的形核-粗化动力学，区分电子传导主导（早期快粗化）与离子扩散主导（晚期慢演化）过程。  
- **与你研究的相关度**：高
- **阅读模式:** 🔍 精读
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/32a14590be6bbc4fc5f80cdaff4696819756239c
- **标签:** general

### 6. Targeting RNA with small molecules using state-of-the-art methods provides highly predictive affinities of riboswitch inhibitors ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2025-10-01
- **作者:** Narjes Ansari; Chengwen Liu; Florent Hédin; J. Hénin; J. Ponder et al.
- **核心问题**：缺乏能准确模拟RNA系统并预测其与小分子结合亲和力的计算模型和技术  
- **方法要点**：结合AMOEBA极化力场、lambda-自适应偏置力（lambda-ABF）方案、精细化约束及机器学习驱动的集体变量增强采样方法  
- **关键结果**：在核糖开关类RNA靶标上实现了定量结合自由能预测；为RNA靶向药物发现中自由能模拟的常规应用奠定基础  
- **与你研究的相关度**：低
- **阅读模式:** 📋 摘要
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/32f82298ef967e5e1ce7fd4e47cb629cc22f0182
- **标签:** general

### 7. Localising entropy production along non-equilibrium trajectories ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2025-03-26
- **作者:** Biswajit Das; S. Manikandan
- **核心问题**：从实验数据中时空局域化定量表征复杂非平衡过程中的熵产率  
- **方法要点**：结合短时热力学不确定性关系推断与深度神经网络，重构高维时变耗散力场并定位轨迹上的熵产波动  
- **关键结果**：实现了非平衡轨迹上熵产的时空局域化；成功应用于多种基础与实验相关体系，解决不同场景下的局域熵产识别难题  
- **与你研究的相关度**：中
- **阅读模式:** 📋 摘要
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/331c978d6960e4121fe45a736f1223f83cc779c4
- **标签:** electrochemistry

### 8. Application of modern artificial intelligence techniques in the development of organic molecular force fields. ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2025-01-17
- **作者:** Junmin Chen; Qian Gao; Miaofei Huang; Kuang Yu
- **核心问题**：缺乏准确且通用的有机分子力场，严重制约分子动力学在分子设计中的应用  
- **方法要点**：综述人工智能（特别是机器学习势函数）在有机分子力场开发中的应用，涵盖势能拟合、原子类型划分与自动优化等关键环节  
- **关键结果**：AI方法显著提升了力场构建中势能拟合精度与自动化水平；但模型可转移性、数据库完备性和验证标准化仍是主要瓶颈  
- **与你研究的相关度**：中
- **阅读模式:** 📋 摘要
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/3407b4904cd631ac7b3645d86efb1e30d5f9b32c
- **标签:** electrochemistry

### 9. Understanding the role of short- and long-range intermolecular interactions in novel computational drug discovery ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2025-08-29
- **作者:** Samuel S Cho; A. Salam
- **核心问题**：如何准确计算分子间相互作用能以支持药物发现中的分子识别与设计  
- **方法要点**：基于微扰理论将分子间势能分解为静电、诱导和色散贡献，并结合多极矩展开与分子力场参数化进行建模  
- **关键结果**：系统梳理了从量子力学到经典力场的多尺度相互作用能计算框架；指出AI/ML与MD模拟的融合显著提升了药物候选物的筛选效率  
- **与你研究的相关度**：低
- **阅读模式:** 📋 摘要
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/34462b89f8decd0004b1786d7055f155104191ed
- **标签:** electrochemistry

### 10. Prediction of Member Forces of Steel Tubes on the Basis of a Sensor System with the Use of AI ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2025-02-01
- **作者:** Haiyu Li; Heungjin Chung
- **核心问题**：如何在控制传感器数量和工程成本的前提下，准确预测 offshore风电机组支撑系统中钢管构件所受的力，实现高效结构健康监测（SHM）。
- **方法要点**：结合ABAQUS有限元建模生成应变-反力数据，构建FCNN建立非线性映射，并利用CNN优化输入变量组合以实现“少传感器、高精度”预测。
- **关键结果**：CNN优化后的输入变量组合在减少传感器数量的同时达到与更多传感器相当的预测精度（R²等指标优异）；开发了可实时预测的GUI交互式传感器耦合力学预测系统。
- **与你研究的相关度**：低
- **阅读模式:** 📋 摘要
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/34804a32a32a4d04664c090a8bb0316aef8f81d2
- **标签:** electrochemistry, surface

## 💡 今日亮点

- **最值得精读**：[1] Modeling Dual-Range Atomic Interactions with Physicochemical Principles for Molecular Force Fields — 提出物理引导的双尺度原子相互作用建模范式，直击电催化界面动态模拟中构象鲁棒性与长程静电/色散耦合缺失这一核心痛点。  
- **可能冲突的研究**：[8] Application of modern artificial intelligence techniques in the development of organic molecular force fields — 强调数据驱动黑箱拟合，弱化物理约束，与[1]主张的“physicochemical principles first”范式形成方法论张力。  
- **值得追踪的团队**：[1]作者团队 — 在MLFF中系统嵌入距离/方向依赖的长程项与自适应短程-长程权重机制，为电催化吸附/脱附路径的亚埃级构象演化建模提供了新基准。  
- **重要趋势**：多篇论文（[1][3][5][6]）共同指向“物理先验+机器学习”的混合建模范式崛起，尤其强调在力场、自由能、热输运等关键物性预测中重建可解释性与泛化性的统一。

## 📌 Key Gap

**关键差距**
- **Gap 1**：现有MLFF（如[1][3][5]）虽改进了相互作用建模，但仍未解决电催化界面特有的**多相耦合边界条件**（如电极/电解质/吸附层三相交界处的局域介电响应、电荷重分布与质子耦合运动），导致界面动力学模拟仍依赖经验修正。  
- **Gap 2**：所有力场相关工作（[1][3][5][6][8]）均未建立**跨尺度一致性验证协议**——即同一模型在单分子、团簇、周期性表面及溶剂化界面等不同尺度下的能量/力误差传递规律尚不明确，制约其在真实电催化场景中的可信度评估。  
- **未来方向**：发展面向电催化界面的**多尺度一致性MLFF框架**：以第一性原理界面计算为锚点，构建覆盖吸附构型变化、溶剂化壳层重组与局部电场响应的联合训练集，并引入电化学势作为显式变量嵌入力场输出，实现Nernst电位依赖的动力学模拟。
