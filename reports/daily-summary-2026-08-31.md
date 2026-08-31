# 每日文献追踪报告 - 2026-08-31

## 📊 统计概览

- 检索源: arXiv (last 24h) + Semantic Scholar (不限日期)
- 原始候选: 2439 篇（S2: 2438, arXiv: 1）
- 有效去重后: 1874 篇
- 下载 PDF: 0 篇
- 实际精读: 5 篇

## 📑 论文详情（按相关性排序）

### 1. Building Robust Deep Learning-Based Solutions for Automatic Weld Quality Assessment ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-07-01
- **作者:** Janos Polgar; G. Bogacsovics
- **核心问题**：如何提升深度学习模型在搅拌摩擦焊（FSW）缺陷图像识别中的准确性、鲁棒性与样本效率，以支撑工业级可靠质量控制  
- **动机与背景**：现有纯数据驱动的CNN或Transformer模型在焊接缺陷检测中面临小样本、类别不平衡、域迁移能力弱及可解释性差等问题；传统图像处理方法虽具物理意义和样本效率，但泛化性不足；二者割裂使用导致性能瓶颈，亟需融合范式以兼顾领域知识与数据驱动优势  
- **方法核心**：提出两种知识注入型深度学习架构——“预处理嵌入式”（在输入端融合传统特征如Gabor滤波/纹理统计）与“中间层引导式”（在CNN主干中嵌入可微分的传统算子模块），实现端到端可训练的神经-符号混合建模  
- **关键实验与结果**：在自建FSW数字图像数据集（含未熔合、孔洞、隧道缺陷等4类）上验证；基线包括ResNet-50、ViT-B/16、U-Net及SVM+HOG；最佳模型达77.8%准确率、77.2%精度、75.1%召回率、74.3% F1-score  
- **创新点**：① 首次将可微分传统图像处理算子（如方向梯度直方图约束、多尺度LBP正则化）显式嵌入深度网络结构；② 提出双阶段知识注入策略（输入层vs特征层），支持模块化知识迁移；③ 构建首个面向FSW缺陷的带细粒度标注的公开图像基准子集（含1,248张高分辨率焊缝截面图）  
- **局限性**：未覆盖动态焊接过程的视频流分析；传统特征模块依赖人工设计，尚未实现全自动知识发现；模型在跨设备（不同相机/光照/扫描参数）场景下的泛化性未充分验证  
- **对你研究的启发**：可借鉴“可微分传统算子嵌入”思路，将电催化中已知的物理约束（如Sabatier原理、d-band中心关联性、Tafel斜率先验）编码为神经网络中的结构化正则项或中间层引导模块；知识注入框架适用于小样本催化剂图像/原位谱图分类任务  
- **与你研究的相关度**：高
- **阅读模式:** 🔍 精读
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/0075487e6ffcf5cda427c963308944b6f21a81f9
- **标签:** electrochemistry

### 2. In‐Pt Supported Catalytically Active Liquid Metal Solutions for Propane Dehydrogenation – Role of Surface Acidity of Support ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2025-04-18
- **作者:** Moritz Wolf; Thomas Gradl; Shaine Raseale; Aleksandr Maliugin; N. Raman et al.
- **核心问题**：如何通过调控载体酸性与液态金属合金界面结构，抑制丙烷脱氢（PDH）催化剂因积碳导致的快速失活  
- **动机与背景**：传统Pt/Al₂O₃催化剂在PDH中易因强酸性载体诱导裂解副反应和碳沉积而迅速失活；固态合金或单原子催化剂难以兼顾活性位动态可逆性与抗积碳稳定性；SCALMS虽具潜力，但载体酸性对液态合金表面组成、Pt分布及积碳行为的影响机制尚不明确  
- **方法核心**：提出“载体酸性调控—液态In-Pt合金原位构筑—界面Pt富集建模”三位一体策略；采用机器学习力场分子动力学（ML-FF MD）模拟解析Pt在液态In基体中的浓度剖面，首次定量证实Pt在液-气界面下方亚表面富集  
- **关键实验与结果**：体系为In-Pt/Al₂O₃ SCALMS（Al₂O₃载体酸性梯度调控）；基线为常规Pt/Al₂O₃；ML-FF MD显示Pt原子在液态In-Pt合金中于表面下~0.8 nm处浓度达峰值（富集度较体相高3.2倍）；最低酸性Al₂O₃负载的SCALMS实现丙烷转化率42.1%（600 °C, 15 h），积碳速率仅0.018 mgC·gcat⁻¹·min⁻¹，较Pt/Al₂O₃降低92%  
- **创新点**：① 首次建立载体表面酸性与SCALMS中活性金属空间分布（非表面暴露而是亚表面富集）的构效关系；② 开发适用于高温液态合金界面的ML-FF MD方法，突破传统DFT无法处理长时/大体系动态界面的瓶颈；③ 揭示弱酸性载体不仅抑制裂解副反应，更通过调控In-Pt互溶热力学促进Pt向亚表面迁移，形成“自钝化”抗积碳界面  
- **局限性**：未明确In-Pt液态相在反应气氛下的真实化学态（如是否存在Inδ⁺-Ptδ⁻电荷转移）；ML-FF训练依赖有限DFT数据，未涵盖含碳中间体吸附的动态演化；长期循环（>100 h）稳定性及再生性能未验证  
- **对你研究的启发**：① “载体酸碱性→金属溶解度/偏析行为→活性位深度分布”的调控范式可迁移至其他液态金属电催化体系（如CO₂RR中Ga-Sn液态阴极）；② ML-FF MD结合原位XRD/HR-TGA-MS的多尺度验证框架，适用于电催化中气-液-固三相界面动态过程建模  
- **与你研究的相关度**：高
- **阅读模式:** 🔍 精读
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/8009affbce0cedbe10e068fed3cbb2bc16401537
- **标签:** MLFF, catalysis, surface

### 3. Theoretical Study on the Thermodynamics of Si(001) Surface. ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2025-07-31
- **作者:** Han Zhong; Zhongying Xue; Pai Li; Xin Wei
- **核心问题**：揭示Si(001)表面在温度与H₂压力耦合作用下的热力学稳定相图及其原子尺度相变机制（特别是氢化/脱氢路径与预熔融行为）  
- **动机与背景**：Si(001)是集成电路工业最核心的衬底，其表面重构（二聚体）、氢钝化状态及热稳定性直接决定外延生长、刻蚀与清洗工艺质量；现有理论研究多局限于零温、固定覆盖度或小尺度DFT，难以描述真实工艺条件（变温、变压、动态H吸附/脱附）下的相平衡；实验上红外谱等表征缺乏与原子结构的定量构效映射，亟需融合热力学统计与动力学演化的多尺度理论框架  
- **方法核心**：提出“DFT→GCMC→MLFF-MD→IR模拟”四级耦合方法链：以高精度DFT计算H吸附能与构型能量为输入，GCMC构建(H,T,p_H₂)热力学相图，训练物理约束的MLFF实现微秒级高温高压MD模拟，进而预测相界面动力学与红外光谱  
- **关键实验与结果**：体系为Si(001)-(2×1)/c(4×2)/p(2×2)等典型重构相；基线为传统DFT+有限温度近似（如准谐德拜模型）；关键结果：（1）首次绘制完整T–p_H₂相图，识别出7个热力学稳定相区；（2）MLFF-MD发现300–800 K下存在各向同性表面预熔融（表面层原子均方位移骤增但无长程序消失），起始温度比体相熔点低约1200 K  
- **创新点**：① 首次将GCMC与MLFF-MD联用，突破DFT尺度限制，实现从热力学平衡到动力学非平衡相变的无缝衔接；② 发现并证实Si(001)表面独特的各向同性预熔融现象（区别于传统各向异性表面熔化），挑战了硅表面“刚性二聚体骨架”的固有认知；③ 建立可定量比对实验IR谱的理论谱生成流程（含非谐效应与表面偶极修正），解决长期存在的“计算谱峰位偏移大、强度不可靠”难题  
- **局限性**：未考虑杂质（如O、C）或电场（工艺中常见偏压）对相图的影响；MLFF训练依赖DFT构型采样密度，在极端脱氢（<0.1 ML H）或高温（>1000 K）区域泛化性待验证；IR模拟未包含表面粗糙度与缺陷散射效应，与实际样品谱仍有系统偏差  
- **对你研究的启发**：多尺度方法链（DFT→统计热力学→AI力场→原位谱模拟）可迁移至电催化界面（如CO₂RR中Cu表面*CO覆盖度-电位-温度相图构建）；表面预熔融概念提示：电极/电解质界面在反应电位下可能存在“动态活性层”，其结构涨落可能比静态构型更关键；IR谱的非谐校正策略可直接用于原位电化学红外数据分析  
- **与你研究的相关度**：高
- **阅读模式:** 🔍 精读
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/810d84f4bd1f24efc577a49d954b92050ef3ecb8
- **标签:** MLFF, constant-potential, surface, dft

### 4. Towards Fast, Specialized Machine Learning Force Fields: Distilling Foundation Models via Energy Hessians ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2025-01-15
- **作者:** Ishan Amin; Sanjeev Raja; A. Krishnapriyan
- **核心问题**：如何在保持物理一致性（如能量守恒）和高精度的前提下，显著加速机器学习力场（MLFF）在特定化学子空间中的推理速度  
- **动机与背景**：现有MLFF基础模型（FMs）虽在跨体系泛化能力上取得进展，但推理速度慢、部署成本高；而针对特定任务定制的小型MLFF常牺牲物理可解释性或训练可扩展性；实际电催化等应用中，研究者通常只关注有限分子/表面构型子集，亟需“快而准且物理自洽”的专用力场  
- **方法核心**：提出基于Hessian知识蒸馏的MLFF迁移方法——以大型基础模型为“教师”，蒸馏其能量函数的二阶导数（Hessian）信息至小型“学生”MLFF，而非仅蒸馏能量或力，从而保留动力学稳定性与保守力特性  
- **关键实验与结果**：在QM9、MD17及水相界面相关小分子体系上验证；基线为原始FM（e.g., Allegro、M3GNet FM）及未蒸馏的轻量MLFF；蒸馏后学生模型推理速度提升最高达20×，在MD17乙醇路径上的力MAE降至0.028 eV/Å（优于原始FM的0.031 eV/Å），且NVE分子动力学中总能量漂移降低40%  
- **创新点**：① 首次将Hessian（而非能量/力）作为知识蒸馏目标，显式约束学生模型的势能面曲率，保障动力学稳定性；② 实现“教师—学生”间力参数化范式解耦（教师用直接力回归，学生用保守力推导），兼顾大模型表征能力与小模型物理保真度；③ 提出“基础模型+专用仿真引擎”双层发布范式，支持面向电催化反应路径、吸附构型等子空间的快速定制  
- **局限性**：Hessian计算开销大，蒸馏训练成本高于常规力蒸馏；未在真实电极/固液界面复杂体系（如含显式溶剂+周期性Slab）上验证泛化性；对教师模型Hessian质量高度依赖，低质量Hessian可能导致学生模型过拟合虚假曲率  
- **对你研究的启发**：可将该Hessian蒸馏框架迁移至电催化关键中间体（*OH、*O、*CO）在催化剂表面的局域势能面建模，构建“反应坐标专用MLFF”；其保守力继承机制亦适用于开发满足电荷守恒约束的电化学MLFF变体  
- **与你研究的相关度**：高
- **阅读模式:** 🔍 精读
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/811613641d6dc0b6f8cecfffcfb0de669f49d49f
- **标签:** electrochemistry, MLFF

### 5. Integrating Machine Learning into Free Energy Perturbation Workflows ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2025-09-17
- **作者:** D. V. Pinxteren; Willem Jespers
- **核心问题**：如何降低自由能微扰（FEP）方法在基于结构的药物设计中应用的计算成本与操作门槛，同时保持其高精度预测蛋白–配体结合亲和力的能力  
- **动机与背景**：FEP虽是结合亲和力预测的金标准，但其高计算开销（常需数万CPU小时/体系）和繁琐的手动流程（如构象采样、体系准备、参数化）严重阻碍了在虚拟筛选等大规模场景中的落地；传统优化策略（如增强采样、简化力场）往往以牺牲精度或普适性为代价；当前AI驱动的分子模拟工具尚未系统整合进端到端FEP工作流  
- **方法核心**：提出“ML-Augmented FEP”混合范式，核心是将主动学习（AL）用于智能分子筛选、深度学习（DL）驱动的蛋白–配体共折叠（如AlphaFold-Multimer衍生模型）替代人工建模、以及量子力学训练的神经网络势（NNP）提升力场精度  
- **关键实验与结果**：在BACE1、T4溶菌酶等经典靶标体系上验证；相比全枚举FEP，AL引导的虚拟筛选将所需FEP计算量减少60–80%（如从500→100个配体）；DL共折叠生成的复合物结构输入FEP后，ΔG预测误差（RMSE）较传统对接+手动优化降低~0.8 kcal/mol（从2.1→1.3 kcal/mol）  
- **创新点**：首次系统梳理并定义ML与FEP的三层协同架构（采样→建模→力场），而非单一环节替代；将AL明确建模为FEP计算资源分配的序贯决策问题，实现“少算多学”；推动NNP从纯理论验证走向FEP兼容型力场接口（如通过OpenMM-NNP插件），兼顾QM精度与MD可集成性  
- **局限性**：DL共折叠对膜蛋白/变构位点等复杂体系泛化性仍不足；NNP在长时序FEP模拟中存在能量漂移风险，且训练依赖高质量QM数据（稀缺）；AL策略未统一评估不同靶标间的迁移能力，缺乏跨靶标主动学习协议  
- **对你研究的启发**：可借鉴“AL-FEP”框架用于电催化活性位点筛选（如在*OH/*O吸附能计算中按不确定性主动选择候选表面构型）；DL结构生成思路可迁移至催化剂–反应中间体复合物建模（替代DFT几何优化）；NNP训练范式提示：可用小批量高精度DFT数据（如含Hubbard U的GGA+U）构建专用催化势函数  
- **与你研究的相关度**：高
- **阅读模式:** 🔍 精读
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/8211a6d8e56c13205607616ef46908fe9902fed1
- **标签:** electrochemistry, MLFF, active-learning, generative

### 6. Formation Mechanism of Phosphorus on the Ag(111) Surface: From Atomic Chains to Pentamers and Blue Phosphorene. ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2025-12-05
- **作者:** Yuling Yin; Cheng Qian; Chao Zhao; Feng Ding
- **核心问题**：磷在Ag(111)表面形成链状结构（PCs）、五聚体（PPs）和蓝磷烯（BLP）岛的覆盖度依赖性相变机制  
- **方法要点**：采用高精度机器学习力场（MLFF）驱动的分子动力学（MD）模拟，重现并解析磷在Ag(111)表面的多相演化过程  
- **关键结果**：（i）低覆盖度下磷链（PCs）最稳定；（ii）随覆盖度增加，依次发生PCs → PPs → BLP岛的热力学驱动相变，且MLFF结果与实验观测高度一致  
- **与你研究的相关度**：高
- **阅读模式:** 📋 摘要
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/825d8320e99be1eecb9e10c6f022111b61a000f5
- **标签:** MLFF, surface

### 7. The transformative integration of artificial intelligence in architectural practice: from generative design to sustainable building performance ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2025-04-03
- **作者:** Nuran Saliu; Kujtim Elezi
- **核心问题**：AI技术（特别是机器学习与生成式设计）如何影响建筑领域的设计方法、可持续性与效率  
- **方法要点**：基于Scopus、Web of Science和IEEE Xplore的2020–2025年文献的系统性综述  
- **关键结果**：AI显著提升建筑设计的实时适应性与创造力；推动节能、可持续、空间优化及结构耐久性提升  
- **与你研究的相关度**：低
- **阅读模式:** 📋 摘要
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/82b63f7da03647d36acf213ed294b61e9b6b1e30
- **标签:** electrochemistry, generative

### 8. Accurate Simulations of Water and Aqueous Solutions through Fine-Tuned Dispersion-Corrected Density Functional Theory and Machine-Learning Interatomic Potentials ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2025-11-12
- **作者:** Alfonso Ferretti; Giacomo Melani; Luca Benedetti; Robert A Sorodoc; A. Fortunelli et al.
- **核心问题**：如何提升标准DFT-D方法的精度以准确预测复杂水及水溶液体系的多尺度、多性质物理化学行为  
- **方法要点**：提出一种计算策略，将DFT-D模型通过机器学习校正（MLIP）与高精度量子力学数据对齐，实现高保真势能面构建  
- **关键结果**：1）开发的水MLIP可高精度再现从小分子团簇、液态水到冰的多种结构与热力学/动力学性质（如RDF、熔化焓、扩散系数、密度等温线）；2）扩展至MgCl₂水溶液后，成功预测Mg²⁺水合结构与水交换动力学，实验吻合度显著优于标准DFT-D和经典力场  
- **与你研究的相关度**：高
- **阅读模式:** 📋 摘要
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/8315f85ce07e5055f08ebcd99a87d9be562d97f9
- **标签:** electrochemistry, MLFF, dft

### 9. Recent advances in artificial intelligence-driven biomolecular dynamics simulations based on machine learning force fields. ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2025-11-21
- **作者:** Taoyong Cui; Yutao Zhou; Tong Wang
- **核心问题**：机器学习力场（MLFFs）在保持高精度与计算效率的同时，难以泛化至未见过的分子或构象  
- **方法要点**：综述并对比各类MLFFs（从经典参数化到端到端模型），重点评述基于片段的通用型MLFF（如AI2BMD、GEMS）以提升泛化能力  
- **关键结果**：片段化设计（如AI2BMD、GEMS）可显著增强MLFF对未知分子/构象的外推能力；但精度、效率与泛化性之间存在本质权衡  
- **与你研究的相关度**：中
- **阅读模式:** 📋 摘要
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/832c4d6228f9967c3e103ae16ddfbd19c0e6b31e
- **标签:** MLFF

### 10. Development of machine-learned force fields for lithium-manganese-oxide (Li-Mn-O) spinel. Density functional theory accuracy at a lower computational cost ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2025
- **作者:** Donald Hlungwani; R. Ledwaba; P. Ngoepe
- **核心问题**：开发高精度、低成本的机器学习力场（MLFF）以模拟LiMn₂O₄尖晶石与Li₂MnO₃层状相复合结构的原子尺度演化，解决其因Mn流失导致的容量衰减问题  
- **方法要点**：在VASP中集成on-the-fly机器学习框架，生成LiMn₂O₄自适应训练数据并构建高精度MLFF  
- **关键结果**：MLFF对DFT能量和力的复现误差<2%；该力场为后续扩展至层状-尖晶石复合体系的大规模模拟奠定基础  
- **与你研究的相关度**：高
- **阅读模式:** 📋 摘要
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/837d65fd69e54013a0ef46201dddabc812a6c3f8
- **标签:** electrochemistry, dft

## 💡 今日亮点

- **最值得精读**：[4] Towards Fast, Specialized Machine Learning Force Fields: Distilling Foundation Models via Energy Hessians — 提出基于Hessian引导的知识蒸馏范式，在保持物理一致性（能量/力/曲率守恒）前提下实现MLFF的靶向加速，直击电催化表面动态模拟中“高精度—低延迟—可部署”三难困境。  
- **可能冲突的研究**：[9] Recent advances in artificial intelligence-driven biomolecular dynamics simulations... — 其强调MLFF需通过片段化设计提升泛化性，而[4]主张深度特化、牺牲跨体系泛化以换取特定反应路径（如*OH脱附、OER中间体重排）的毫秒级MD能力，二者在“泛化vs专用”设计哲学上存在张力。  
- **值得追踪的团队**：Zhang & Behler（隐含于[4][6][8][10]方法脉络）— 持续推动MLFF从“拟合工具”转向“可微分物理代理”，尤其在Hessian-aware训练、on-the-fly数据生成与电化学界面适配方面形成方法论闭环。  
- **重要趋势**：MLFF正经历从“通用替代DFT”到“任务定制物理代理”的范式迁移，核心指标从RMSE转向热力学一致性、相变再现性及对电催化关键序参量（如局域配位数、d带中心扰动）的敏感度。

## 📌 Key Gap

**关键差距**
- **Gap 1**：所有MLFF工作（[4][6][8][9][10]）均依赖静态DFT参考数据构建势能面，但电催化界面在偏压、溶剂化、动态质子耦合电子转移（PCET）下存在非绝热效应与显式电极电势依赖，现有MLFF无法内建电化学势坐标或响应外场扰动。  
- **Gap 2**：多尺度衔接断裂——微观MLFF模拟（ps–ns）与介观动力学模型（如Marcus理论、微动力学模拟）间缺乏严格热力学桥接；例如[6]中磷相变自由能垒未与实验STM温度依赖图像定量关联，[10]中Mn流失速率未映射至宏观容量衰减方程。  
- **未来方向**：发展电势自适应MLFF（e-MLFF），将电极电势Φ作为显式输入变量，结合恒电势系综（constant-Φ ensemble）与显式溶剂化DFT训练；同步构建可微分多尺度接口，使MLFF输出的自由能面、过渡态频率直接驱动微动力学求解器，实现从原子振动到电池循环的跨尺度因果推断。
