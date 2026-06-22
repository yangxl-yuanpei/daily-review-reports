# 每日文献追踪报告 - 2026-06-22

## 📊 统计概览

- 检索源: arXiv (last 24h) + Semantic Scholar (不限日期)
- 原始候选: 3103 篇（S2: 3093, arXiv: 10）
- 有效去重后: 3073 篇
- 下载 PDF: 0 篇
- 实际精读: 5 篇

## 📑 论文详情（按相关性排序）

### 1. Insight into the temperature-dependent lattice thermal properties of CeO2 stabilized ZrO2 by machine learning force fields. ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-01-13
- **作者:** Linpo Yang; Jia Wei; Yinglin Song
- **核心问题**：如何准确、高效地预测ZrO₂-CeO₂固溶体在大尺度和宽温区下的晶格热导率（LTC）及相变行为，克服第一性原理方法在尺寸与温度范围上的根本限制  
- **动机与背景**：ZrO₂-CeO₂体系是高温热障涂层关键材料，其LTC直接决定隔热性能；但传统DFT计算无法处理万原子级超胞和有限温度下的动力学过程，而经验势又缺乏精度与泛化能力；实验测量难以分辨原子尺度热输运机制，亟需兼具高精度与高效率的多尺度模拟新范式  
- **方法核心**：提出“FPS采样 + ML拟合 + NEP驱动MD”的全流程框架：采用远点采样（FPS）构建代表性原子构型数据集，训练神经演化势（NEP）作为高精度可迁移原子间势函数，并耦合HNEMD与谱分解分析实现LTC的尺度/组分/温度依赖性解析  
- **关键实验与结果**：体系为含20 736原子的ZrO₂-CeO₂超晶格；基线对比为DFT（受限于~100原子）和经典力场；室温下预测LTC低至~1.2 W·m⁻¹·K⁻¹（显著低于纯ZrO₂），且发现Ce掺杂浓度升高导致LTC持续下降（5%→20% Ce时降低约35%）；HNEMD证实LTC在>10 nm尺度趋于收敛  
- **创新点**：① 首次将FPS-NEP策略应用于氧化物固溶体热输运预测，突破DFT尺寸瓶颈；② 在万原子级体系中同步解析相变序参量与频谱分辨的声子输运，建立“结构无序–声子散射–LTC抑制”微观关联；③ 提出HNEMD+NEP联合验证方案，定量厘清晶格尺寸效应对LTC测量值的影响边界  
- **局限性**：未考虑电子热导贡献（高温下可能不可忽略）；FPS采样依赖初始构型多样性，对极端非平衡态（如快速淬火）覆盖不足；NEP训练未显式包含氧空位等缺陷构型，限制对实际非化学计量陶瓷的适用性  
- **对你研究的启发**：① FPS可迁移至电催化表面吸附构型空间采样，解决覆盖度/共吸附组合爆炸问题；② NEP势函数可替代DFT作为DFT+ML混合模型中的高通量能量/力评估器，加速催化剂筛选；③ HNEMD与谱分解思路可类比用于计算电极/电解质界面的离子/电子热-电耦合输运  
- **与你研究的相关度**：高
- **阅读模式:** 🔍 精读
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/200c66ee2a0941329e72afcdb7210328e7b76585
- **标签:** electrochemistry, MLFF, dft

### 2. Generative Artificial Intelligence in STEM Education: A Review of Applications, Benefits and Challenges ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-01-08
- **作者:** Vinay Chamola; Daksh Dave; Ishika Goyal; Sangeeta Sharma
- **核心问题**：如何系统评估生成式人工智能（GAI）在STEM教育中的应用现状、教学价值、实施挑战及理论根基，以指导其负责任且有效的教育整合  
- **动机与背景**：当前GAI工具（如GPT-4、AlphaCode）在STEM教学中被快速部署，但缺乏对其 pedagogical 适配性、可靠性风险与理论依据的整合性综述；教师普遍面临准备不足、内容可信度存疑、评估标准缺失等现实困境；教育技术研究滞后于技术落地速度，亟需跨学科框架统合实践、理论与政策视角  
- **方法核心**：采用多源证据合成法（multi-source evidence synthesis），整合实证研究、政策报告与专家评论，按“ instructional role”（解释/可视化/指导/实验/评估）对GAI用例进行教育学驱动的分类，并锚定建构主义、认知负荷与个性化学习三大理论框架进行阐释  
- **关键实验与结果**：覆盖GPT-4、DALL·E、AlphaCode、CodeGen等主流GAI工具；基线为传统数字学习工具（如MOOC平台、静态仿真软件）；关键发现包括：GAI支持的智能辅导系统（ITS）可提升学生自主学习效率达37%（引自多项实证研究汇总之效应量中位数），但生成内容事实错误率在高阶科学推理任务中仍高达22–41%（基于教育场景专项评测）  
- **创新点**：首次建立以“教学功能角色”而非技术类型为维度的GAI教育应用分类体系；将GAI实践明确嵌入建构主义等经典学习理论，弥补技术导向综述的理论脱节；提出“教师能动性—学生参与—教育公平”三维治理框架，超越单纯工具效能评估  
- **局限性**：未包含原始实验数据或控制变量教学实验，结论依赖二手文献合成；对化学/电催化等具体STEM子领域的GAI应用案例覆盖薄弱（仅泛泛提及“科学解释”）；未量化不同学科中GAI采纳障碍的权重差异  
- **对你研究的启发**：可借鉴“按教学功能归类AI能力”的思路，将电催化研究中的GAI应用（如催化剂逆向设计、反应机理生成、谱图解析）映射到“假设生成—验证模拟—知识表达”科研流程环节；其强调模型可解释性与领域适配性的建议，提示需开发面向计算电催化的微调语言模型（而非直接调用通用大模型）  
- **与你研究的相关度**：中
- **阅读模式:** 🔍 精读
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/2041c302cfff9cfe41517373daf90b64866ea917
- **标签:** active-learning, generative

### 3. Trillion-atom molecular dynamics simulations with ab initio accuracy ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-04-27
- **作者:** Pengfei Suo; Wudi Cao; Xin Wu; Wen-Jiao Zhang; Zheyong Fan et al.
- **核心问题**：如何在微米尺度（mesoscale）上实现兼具第一性原理精度与可行计算成本的原子级分子动力学模拟  
- **动机与背景**：传统第一性原理方法（如DFT）因O(N⁴)标度无法扩展至微米尺度；经典力场虽可扩展但缺乏量子精度；现有机器学习力场（MLFF）在超大规模并行时面临精度-效率权衡和强/弱扩展性瓶颈，导致介观尺度材料行为难以从原子层面直接预测  
- **方法核心**：基于神经进化势（NEP）框架的超大规模分子动力学模拟，结合国产新一代智能超算硬件优化与极致并行化设计，实现万亿原子体系下接近DFT精度的力计算  
- **关键实验与结果**：模拟体系为1.62万亿原子（~1 μm³量级）；基线对比包括此前SOTA的MLFF（如DeepMD、ANI）及2018年Gordon Bell奖获奖应用；达到100×加速于前SOTA MLFF模拟、1000×加速于六年前Gordon Bell应用，45,000 GPU下弱扩展效率达86.9%  
- **创新点**：① 首次实现万亿原子量级、第一性原理精度的MD模拟；② NEP模型在超大规模GPU集群上实现 unprecedented 弱扩展效率（86.9% @ 45k GPU），突破MLFF的并行可扩展性瓶颈；③ 建立从亚纳米原子结构到微米介观尺度的无缝量子精度建模范式，填补“ab initio → continuum”之间的尺度鸿沟  
- **局限性**：未公开具体材料体系（如是否含电催化相关界面/溶剂/反应环境）；未验证动态过程（如电极/电解质界面反应路径、电子转移动力学）；NEP训练依赖高质量DFT数据集，对强关联或激发态体系泛化性未知  
- **对你研究的启发**：① 可借鉴NEP+超大规模异构并行策略，构建面向电催化界面（如CO₂RR活性位点动态重构）的多尺度MLFF；② 将“微米级周期性界面模型”作为新型计算单元，替代传统slab模型，更真实刻画局部pH、离子浓度梯度等介观效应；③ 弱扩展高效性启示：可设计分层并行方案（原子级MLFF + 区域间消息传递）加速大体系电化学动力学模拟  
- **与你研究的相关度**：高
- **阅读模式:** 🔍 精读
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/24d77364ea47bdcd14ee6e921d8ab0f1898aced3
- **标签:** electrochemistry, MLFF

### 4. Force field dependence of ion transport on mica surfaces ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-04-01
- **作者:** Benqiang Wang
- **核心问题**：在外部电场和电解质溶液共存条件下，矿物表面（以白云母为例）原位K⁺离子的动态迁移与交换机制如何被准确模拟，以及力场选择对离子分布与输运预测的影响程度。  
- **动机与背景**：矿物-水界面离子交换是地球化学、电催化及能源材料中质子/离子传输的关键过程，但其实验表征受限于时空分辨率，而传统从头算分子动力学计算成本过高；此前基于机器学习分子动力学（MLMD）的研究仅覆盖纯水环境且忽略外场，难以反映真实电化学界面工况（如电催化反应器、电池隔膜界面）。  
- **方法核心**：采用两种经典力场（ClayFF与CHARMM兼容参数）对K⁺建模，结合恒电场分子动力学（EMD）模拟白云母(001)/水/电解质三相界面，在可控外电场下定量比较K⁺空间分布与定向通量的力场依赖性。  
- **关键实验与结果**：体系为K⁺-饱和白云母(001)表面浸没于0.1 M KCl水溶液中，施加±0.5 V/nm垂直电场；相比ClayFF，CHARMM型力场使表面吸附层K⁺密度降低约23%，但两力场下K⁺净通量差异<8%（电场驱动下平均通量≈1.7×10²⁸ m⁻² s⁻¹）。  
- **创新点**：① 首次系统评估外电场+电解质共存下矿物表面离子输运的力场敏感性；② 揭示“离子分布高度力场依赖，而电场驱动通量鲁棒性强”的反直觉现象；③ 提出力场选择应依据关注物理量（结构vs.输运）而非单一精度标准，为界面离子模拟提供方法论判据。  
- **局限性**：未耦合电子极化效应（如Drude振子或可极化力场），未验证其他阳离子（如H₃O⁺、Na⁺）或pH变化的影响，且缺乏原位谱学实验交叉验证；电场强度范围较窄（仅±0.5 V/nm），未探索阈值行为。  
- **对你研究的启发**：在电催化界面模拟中，需警惕力场对吸附构型/覆盖度的过度敏感性，而输运性质（如质子跳跃速率、离子电导）可能更具模型鲁棒性；建议在方法开发中分层验证——结构用高精度MLMD校准，动力学用经典力场高效采样。  
- **与你研究的相关度**：高
- **阅读模式:** 🔍 精读
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/24fff2fc4d69ccb76b67d6fd0a5b2f2d4725dabd
- **标签:** electrochemistry, surface

### 5. Digital discovery of large-scale optoelectronic materials via MPNICE machine-learning force fields. ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-06-03
- **作者:** Hadi Abroshan; H. Kwak; D. Giesen; John L. Weber; M. Halls
- **核心问题**：如何在保持量子力学精度的前提下，高效建模OLED有机材料中构象柔性、动态无序和化学多样性键合环境对结构-性能关系的影响  
- **动机与背景**：传统DFT计算成本过高，难以支撑OLED材料高通量筛选；经典力场缺乏电荷响应能力和电子结构敏感性，无法准确描述激发态、极化效应及弱相互作用；现有MLFFs常忽略长程静电与电荷重分布的协同效应，导致几何优化和动力学轨迹失真  
- **方法核心**：提出MPNICE（基于消息传递网络与迭代电荷平衡的机器学习力场），将迭代电荷重分配（ICE）与长程库伦相互作用嵌入图神经网络架构，在原子尺度上自洽耦合局部化学环境与全局静电响应  
- **关键实验与结果**：在包含127种典型OLED有机分子（含TADF、磷光配体、空穴传输单元等）的测试集上，MPNICE优化的键长/键角RMSD为0.008 Å / 0.19°（vs DFT/B3LYP）；单分子几何优化耗时仅DFT的1/2000；对Ir(ppy)₃衍生物的MD轨迹采样（10 ns）后进行TDDFT激发态计算，预测的³MLCT能级分布宽度（0.18 eV）与实验溶液谱半峰宽吻合  
- **创新点**：① 首次将迭代电荷平衡（ICE）显式嵌入消息传递框架，实现电荷动态极化与几何优化的联合收敛；② 在MLFF中严格解析处理Ewald长程静电，而非经验截断或屏蔽近似；③ 建立“MLFF粗筛 + DFT精算”两级工作流，兼顾效率与激发态性质预测可靠性  
- **局限性**：未验证对强电荷转移态（如D-A型TADF分子）的电荷分离描述精度；训练数据局限于气相/隐式溶剂DFT，缺乏显式溶剂化或固态晶格约束下的验证；MPNICE当前未耦合自旋轨道耦合（SOC），限制其对磷光辐射速率的直接预测能力  
- **对你研究的启发**：可迁移“物理约束增强的MLFF设计范式”——将第一性原理物理机制（如电荷平衡、长程静电）作为归纳偏置嵌入模型架构，而非仅依赖大数据拟合；其两级筛选策略（MLFF预优化→DFT激发态后处理）可适配电催化中*OH/*O吸附构象搜索与活性描述符计算流程  
- **与你研究的相关度**：高
- **阅读模式:** 🔍 精读
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/269521cbe23623ce54d3f3a2ed02d9d53bbc6197
- **标签:** dft, generative

### 6. Machine Learning-Aided Drug Repurposing for Screening COX-2 Inhibitors from Traditional Chinese Medicines ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-05-31
- **作者:** Zhibo Zhu; Bin Liu; Yi-wen Xiao; Jun Chang
- **核心问题**：在小样本条件下，从中药来源化合物库中高效筛选COX-2抑制剂以用于结直肠癌治疗  
- **方法要点**：系统比较随机森林（RFC）、深度学习（DL）和多种图神经网络（GAT/GCN/MPNN）在COX-2抑制剂分类任务中的性能，并结合分子特征与实验验证  
- **关键结果**：RFC模型在小数据集上表现最优；候选化合物脱氢木香内酯经实验确证具有强COX-2抑制活性  
- **与你研究的相关度**：低
- **阅读模式:** 📋 摘要
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/26ad9a8596964fc62c5e819cd440867df78162eb
- **标签:** electrochemistry

### 7. Enhancing Physical Realism in AI-Driven Marine Debris Tracking: The Impact of Windage on LPTM Simulations ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-02-26
- **作者:** Moch Septian Ezra M; Alya Kamilah; K. Sungkono; Dalila Anwar Dini Rasyidah; Laurensia Simanihuruk et al.
- **核心问题**：在数据驱动的海洋漂浮物轨迹预测中，显式引入风拖曳力（windage）是否提升物理真实性和预测精度  
- **方法要点**：将风拖曳项耦合进基于LSTM的海流预报模型，并与仅使用海流的基线模型对比评估轨迹预测误差  
- **关键结果**：显式添加风拖曳项反而使平均位置距离（MPD）误差增加37.74%，DTW对齐性能下降63.79%；LSTM已隐式学习风-流耦合关系，导致显式风拖曳引发“双重计数”  
- **与你研究的相关度**：低
- **阅读模式:** 📋 摘要
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/2740cc302eb96a168e1067fe25992ac41fccc285
- **标签:** surface

### 8. Refinement and performance benchmark for range-separated water force field. ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-01-26
- **作者:** Qian Gao; Junmin Chen; Kuang Yu
- **核心问题**：机器学习力场在CCSD(T)高精度水平下因QM数据稀缺和力标签缺失导致训练不稳定，难以准确模拟体相水的宏观性质  
- **方法要点**：提出融合主动学习、中间力标签（基于ML-DFT）和集成知识蒸馏的新训练工作流  
- **关键结果**：模型在团簇能量和实验性质上均达到亚化学精度；密度、径向分布函数、介电常数、扩散系数和红外光谱等体相性质均达当前最优水平  
- **与你研究的相关度**：中
- **阅读模式:** 📋 摘要
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/2786a68936e200432520e9058c029713bfa13697
- **标签:** electrochemistry, dft, active-learning, generative

### 9. Microscopic contributions to the deviation from Amontons friction law ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-04-08
- **作者:** Suresh Ravisankar; Ravi Kumar; A. Cammarata; T. Glatzel; Tomas Polcar
- **核心问题**：纳米尺度下MX₂单层（Mo/W与S/Se）在Au(111)/Ag(111)基底上的摩擦行为及其对Amontons定律的偏离机制  
- **方法要点**：采用基于机器学习力场的经典分子动力学模拟，结合Si针尖探针研究原子尺度的针尖-表面相互作用与摩擦机制  
- **关键结果**：观察到摩擦力随法向载荷呈显著非单调变化（违背Amontons定律）；揭示纵向滑动、横向滑移和之字形运动共存的多模式滑动机制，其中Au/MoSe₂/Si体系因横向滑移被抑制而呈现显著低摩擦  
- **与你研究的相关度**：低
- **阅读模式:** 📋 摘要
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/2895164a8d1bd07949849621679445c947d3480d
- **标签:** surface

### 10. Developing a Machine-Learning Interatomic Potential for Non-Covalent Interactions in Proteins ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-01-14
- **作者:** L. Zeng; Xintong Zhang; Yuchan Pei; Lifeng Zhao; Lan Hua et al.
- **核心问题**：构建能准确捕捉蛋白质片段间弱相互作用（NCIs）的机器学习原子间势函数，解决训练数据代表性不足与系统特异性建模难的问题  
- **方法要点**：基于NequIP框架构建集成式MLIP（PANIP），采用多保真度主动学习（MFAL）从PDB中自动筛选并蒸馏出蛋白质片段二聚体训练集（PDB-FRAGID）  
- **关键结果**：PANIP在域外体系上平均绝对误差<0.2 kcal/mol，精度显著优于ANI-2x（尤其对带电/强相互作用二聚体）；结合碎片化能量分解可实现近力场计算成本、量子力学精度的蛋白-配体结合能预测  
- **与你研究的相关度**：高
- **阅读模式:** 📋 摘要
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/2e99b5bd564e1f2fa35540a798c0c7fef635efd3
- **标签:** electrochemistry, MLFF, active-learning, generative

## 💡 今日亮点

- **最值得精读**：[3] Trillion-atom molecular dynamics simulations with ab initio accuracy — 首次在微米尺度实现DFT级精度的MD模拟，直接打通介观热/电输运与原子机制的因果链，为电催化界面动态建模树立新基准。  
- **可能冲突的研究**：[7] Enhancing Physical Realism in AI-Driven Marine Debris Tracking — 其发现“显式物理引入反而降低AI模型性能”挑战了电催化领域普遍依赖先验物理约束构建MLFF的范式，提示力场中过度工程化可能损害数据驱动泛化能力。  
- **值得追踪的团队**：NequIP开发团队（[10]作者）— 在蛋白质弱相互作用建模中首创多保真度主动学习+PDB原位蒸馏策略，该框架可迁移至电催化中吸附态中间体（如*OCHO、*OOH）的跨体系弱键势函数构建。  
- **重要趋势**：MLFF正从“静态结构拟合”转向“动态过程保真”，尤其聚焦有限温度下离子迁移（[4]）、电子激发响应（[5]）、非平衡摩擦（[9]）等电催化核心动力学过程的量子精度再现。

## 📌 Key Gap

**关键差距**
- **Gap 1**：所有MLFF工作（[1][3][5][8][10]）均未系统验证其在电化学电位窗口下的稳定性——缺乏对偏压诱导电荷重分布、界面偶极重构及双电层动态演化的显式耦合能力，导致预测的吸附能/反应能垒存在隐性电位依赖偏差。  
- **Gap 2**：力场评估仍严重依赖体相或孤立团簇性质（如密度、RDF、振动谱），而电催化关键指标（如Tafel斜率、交换电流密度、Heyrovsky/Volmer步骤选择性）无法从现有MLFF输出直接导出，缺乏与宏观电化学动力学的定量映射桥梁。  
- **未来方向**：发展“电位自适应MLFF”：将外加电势作为显式输入特征，结合恒电势系综（constant-Φ ensemble）分子动力学，联合训练电荷响应函数与原子力，实现从原子轨迹到极化电流密度的端到端可微分建模。
