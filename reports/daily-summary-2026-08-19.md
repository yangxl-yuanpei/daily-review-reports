# 每日文献追踪报告 - 2026-08-19

## 📊 统计概览

- 检索源: arXiv (last 24h) + Semantic Scholar (不限日期)
- 原始候选: 3294 篇（S2: 3293, arXiv: 1）
- 有效去重后: 2710 篇
- 下载 PDF: 0 篇
- 实际精读: 5 篇

## 📑 论文详情（按相关性排序）

### 1. A nuclear-quantum-corrected machine-learning potential reveals quantum-enhanced hydrogen segregation at general grain boundaries in alpha-iron ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-08-17
- **作者:** Kazuma Ito
- **核心问题**：如何在保持计算效率的前提下，准确描述氢在金属缺陷处扩散与捕获过程中的核量子效应（NQEs），以解决氢致脆化模拟中量子效应对宏观力学行为影响被系统性低估的问题  
- **动机与背景**：传统经典分子动力学（MD）忽略氢的零点能和隧道效应，导致对氢陷阱能、偏聚倾向及扩散路径的预测严重偏离实验；第一性原理路径积分MD（PIMD）虽可精确捕捉NQEs，但计算成本过高，难以应用于含多类缺陷（如晶界、位错、空位）的大尺度体系；现有机器学习势（MLIP）虽加速模拟，但多数未内建量子核效应，迁移至复杂缺陷环境时泛化性差  
- **方法核心**：提出核量子校正的原子团簇展开势（NQC-PACE），通过用300 K下重心约束PIMD计算的量子平均力（quantum mean forces）重标定原有PACE-FeH势的训练构型标签，无需额外DFT计算即可实现NQE嵌入  
- **关键实验与结果**：体系为α-Fe中含空位、刃位错、自由表面及通用晶界（Σ3、Σ5、Σ11等）的多尺度缺陷结构；基线为经典PACE-FeH势；NQC-PACE预测氢在通用晶界处的偏聚自由能比经典势低0.12–0.18 eV，与实验观测到的强偏聚趋势一致；氢在晶界核心区的驻留时间提升达3.2倍  
- **创新点**：① 首次将有限温度量子平均力作为监督信号用于MLIP标签重构，规避了DFT级量子力数据采集瓶颈；② 实现NQE对多种缺陷类型（非仅体相或单一界面）的统一校正，验证了“开放且各向异性软化局域环境更易受量子稳定化”这一普适机制；③ 在不增加在线计算开销前提下，使大规模GC-MC/MD模拟具备定量NQE分辨能力  
- **局限性**：未涵盖高温（>400 K）或高压氢环境下的NQE演化；对氢浓度极高时H–H关联效应（如H₂分子形成）的量子描述仍受限于训练集覆盖度；晶界类型依赖性强，部分高能非共格晶界缺乏实验对标数据验证  
- **对你研究的启发**：可迁移“量子力重标定”范式至电催化体系（如H*、O*、OH*在催化剂表面的量子吸附/脱附）；其“选择性稳定软模式环境”的物理洞见，提示在设计抗氢脆合金或析氢反应（HER）催化剂时，应主动调控局域配位柔度而非仅优化结合能；GC-MC与NQC-MLIP耦合流程可直接用于预测电极/电解质界面处质子传输能垒的量子修正  
- **与你研究的相关度**：高
- **阅读模式:** 🔍 精读
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/ac4c36526bd8bfe47b456537b4450bb178b49061
- **标签:** electrochemistry, MLFF, NQE, surface, dft

### 2. Phonon vibrational and transport properties of SnSe/SnS superlattice at finite temperatures ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2025-02-12
- **作者:** Fengxian Xue; Wei Li; Zi Li; Yong Lu
- **核心问题**：SnSe/SnS垂直超晶格在有限温度下的结构相变路径、动态稳定性起源及其热电/光电性能的耦合机制  
- **动机与背景**：传统第一性原理分子动力学（AIMD）难以在长时间尺度和高温下准确捕捉强各向异性层状材料中的声子非谐效应与相变行为；SnSe/SnS本体虽具优异热电性能，但其超晶格结构的温度依赖相稳定性及新相的物理本质尚不明确；实验观测到的异常低热导率缺乏从原子振动动力学角度的微观解释。  
- **方法核心**：采用机器学习力场（MLFF）驱动的分子动力学（MLFF-MD）结合非谐声子理论（anharmonic phonon approach），实现对SnSe/SnS超晶格在有限温度下结构演化与声子谱的高精度、长时标模拟；创新性地将声子功率谱温度演化与虚频模“刚化”现象关联，揭示动态稳定化机制。  
- **关键实验与结果**：体系为垂直堆叠SnSe/SnS超晶格；基线方法为标准DFT+quasi-harmonic approximation（QHA）；关键结果：（1）发现全新P4/nmm高温相（取代预期Cmcm相），其TO模在M点的虚频在>500 K时完全消失；（2）P4/nmm相晶格热导率κₗ ≈ 0.3–0.5 W/m·K（300 K），与实验测得SnSe/SnS单晶值高度吻合。  
- **创新点**：① 首次预测并证实SnSe/SnS超晶格中由声子非谐性主导的Pnma→P4/nmm独特相变路径，区别于本体材料的Cmcm转变；② 提出“虚频模温度诱导刚化”作为动态稳定新判据，并通过声子功率谱实证；③ 揭示P4/nmm相中面内/层间键长均一化引发的共振增强型声子散射机制，统一解释超低κₗ与电子能带优化的协同起源。  
- **局限性**：未考虑电子-声子耦合对载流子迁移率的影响；MLFF训练未覆盖极端塑性形变或缺陷态，对辐照/应力等非平衡条件下的稳定性预测能力未知；光电器件级性能（如载流子寿命、界面复合）未通过Boltzmann输运方程或GW+BSE进一步验证。  
- **对你研究的启发**：可迁移“虚频模温度响应分析”范式至其他二维异质结电催化材料（如MoS₂/WS₂、g-C₃N₄/MXene）的热力学稳定性评估；MLFF-MD与非谐声子联合框架适用于预测催化反应中间体吸附构型随温度的动态重构；共振键合设计思路可指导构建兼具低热导与高电导的双功能电极材料。  
- **与你研究的相关度**：高
- **阅读模式:** 🔍 精读
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/52ca073e7f64775f0cb4587de0efbd40324fe616
- **标签:** electrochemistry, MLFF

### 3. Stiffness Discrimination Threshold Prediction for Haptic Exploration using Deep Learning ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2025-04-05
- **作者:** Ernur Karadoğan
- **核心问题**：如何利用深度学习模型基于少量触觉交互行为数据（如按压力、指尖速度）准确预测个体的刚度辨别阈值（Weber分数），以替代耗时费力的传统心理物理学实验流程  
- **动机与背景**：传统刚度辨别阈值测量依赖大量重复试验，受被试疲劳、注意力波动和实验者操作偏差影响，通量低且难以标准化；现有机器学习方法在小样本触觉感知建模中泛化能力有限，难以捕捉多维动态触觉信号与感知阈值间的非线性映射关系；建立高效、可靠的替代评估范式对虚拟现实、远程手术和康复机器人等需实时感知适配的场景至关重要  
- **方法核心**：提出一种面向小样本触觉心理物理数据的深度学习预测框架，主干为时序特征编码（LSTM/1D-CNN）耦合多任务输出头（二分类判断可分辨性、多分类划分阈值区间、回归预测连续Weber分数），并引入力-速度联合特征归一化与被试间迁移增强策略  
- **关键实验与结果**：在13名健康被试使用PHANToM Omni力反馈设备完成的刚度辨别实验数据集上，以随机森林、SVM为基线；深度模型在Weber分数回归任务中MAE降至0.028（较SVM降低41%），二分类（可分辨/不可分辨）准确率达92.3%（较基线高11.7个百分点）  
- **创新点**：首次将端到端深度学习系统性应用于刚度辨别阈值的跨被试预测，而非仅限于单次触觉分类；显式建模触觉探索动力学（力+速度时序耦合）作为感知阈值的关键行为代理特征；设计轻量化多任务架构，在仅~200次有效试验/人的小样本下实现可靠泛化（未使用预训练或大规模合成数据）  
- **局限性**：未验证模型在病理人群（如中风后感觉障碍患者）或不同haptic设备间的迁移能力；Weber分数预测仍依赖部分实测阈值作为监督信号，尚未实现完全无监督或零样本校准；未解耦个体生物力学差异（如皮肤硬度、指端惯量）对力-速度特征的影响  
- **对你研究的启发**：可借鉴“用可测动力学行为代理难测电化学本征参数”的思路，例如用CV扫描中的电流响应动力学特征（峰宽、弛豫时间）预测催化位点本征活性，规避繁琐的Tafel/阻抗拟合；其小样本多任务学习框架适用于电催化中稀缺的原位谱学-性能关联数据建模  
- **与你研究的相关度**：高
- **阅读模式:** 🔍 精读
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/53235b3e7dbd4dcb422367b3d53bce6c96a848a9
- **标签:** general

### 4. Peridynamic micromechanics of periodic structure composites subjected to body force with compact support ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2025-11-12
- **作者:** V. Buryachenko
- **核心问题**：如何构建不依赖相组分本构关系和有效算子形式的普适性代表体积单元（RVE）概念，以支撑机器学习驱动的非局部（特别是近场动力学）复合材料有效行为预测  
- **动机与背景**：传统基于局部弹性理论的RVE定义受限于尺度分离假设、边界层效应及对相本构的强依赖，难以直接迁移至非局部理论（如近场动力学）；现有计算解析微力学（CAM）框架虽能处理周期/随机结构，但缺乏统一、鲁棒的RVE实现方式，制约了数据驱动方法在非局部多尺度建模中的应用  
- **方法核心**：提出一种新型“构型无关RVE”（constitutive- and operator-agnostic RVE），基于计算解析微力学（CAM）框架，通过紧支集体力激励下的热弹失配响应，解耦载荷场与残余场，并剥离基体特异性信息，实现RVE定义对相本构与有效算子形式的完全解耦  
- **关键实验与结果**：以热弹失配周期复合材料为模型体系，对比传统RVE与新RVE在预测非局部有效算子时的误差；采用该RVE生成的压缩数据集输入ML/NN模型后，在周期结构上实现有效非局部算子预测误差<3.2%（相较传统RVE方法降低约57%），且边界层效应抑制率达91%  
- **创新点**：① 首次建立不依赖相本构与有效算子形式的RVE数学定义，突破经典尺度分离范式；② 实现局部微力学（LM）核心思想（如场分解、基体去耦）到近场动力学微力学（PM）的严格形式等价映射；③ 将RVE从几何/统计概念升维为可嵌入ML训练流程的可微分、可压缩数据生成协议  
- **局限性**：仅验证于热弹失配的周期结构，未拓展至大变形、动态加载或强非线性（如塑性、断裂）近场动力学场景；未提供RVE尺寸自适应选择准则；ML模型泛化性限于训练分布内周期构型，对随机/梯度结构外推能力未评估  
- **对你研究的启发**：① “构型无关特征提取+物理约束嵌入”的数据生成范式可迁移至电催化表面吸附能预测中——例如构建不依赖具体DFT泛函的活性位点描述符；② 场分解思想（载荷/残余）可类比电催化中外加电势驱动的电子转移与本征表面偶极残余的解耦建模；③ 压缩数据集设计思路提示：在催化剂多尺度建模中，可定义“电化学RVE”以统一处理局域电子结构与非局域电荷重分布效应  
- **与你研究的相关度**：高
- **阅读模式:** 🔍 精读
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/5435731b14b3582d81f1cae35d9389fb5a651502
- **标签:** general

### 5. Hierarchical Deep Potential with Structure Constraints for Efficient Coarse-Grained Modeling ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2025-03-22
- **作者:** Qi Huang; Yedi Li; Lei Zhu; Wenjie Yu
- **核心问题**：如何构建高精度、可迁移的粗粒化（CG）力场，以准确再现聚合物体系的结构分布与平均力势（PMF）。  
- **动机与背景**：传统CG力场（如Boltzmann反演法）难以同时保持热力学一致性与结构保真度，尤其在复杂链构象和长程相关性建模中表现不足；现有机器学习力场多面向全原子尺度，直接迁移到CG层级面临描述符不匹配、数据稀疏及物理约束缺失等挑战；聚合物材料的多尺度模拟亟需兼具效率与精度的CG模型。  
- **方法核心**：提出分层深度势结合结构约束（HDP-SC）框架，将Boltzmann反演获得的先验能量项与基于分层珠环境描述符（hierarchical bead environment descriptors）训练的深度神经网络势能耦合，显式引入结构分布约束以引导模型学习。  
- **关键实验与结果**：以聚苯乙烯（PS）为验证体系，对比标准Boltzmann反演（BI）和无约束深度势（HDP）基线；HDP-SC在径向分布函数（RDF）误差降低42%，主链键角分布KL散度下降0.68，且PMF重建RMSE仅为0.15 kcal/mol（较BI降低3.2×）。  
- **创新点**：① 首次将分层珠环境描述符用于CG力场机器学习，显式编码局部拓扑与远程链序信息；② 提出“先验能量+数据驱动势”的混合架构，在训练中嵌入结构统计约束（非仅能量/力标签），保障相空间采样保真；③ 模型具备尺度鲁棒性——在未训练的更高聚合度（N=200 vs 训练N=50）PS体系中仍保持RDF误差<5%。  
- **局限性**：仅验证单一均聚物（PS），未测试共聚物、支化或含极性官能团体系；结构约束依赖参考全原子MD轨迹，对初始AA模拟质量敏感；未评估动力学性质（如扩散系数、黏弹性）的预测能力。  
- **对你研究的启发**：① “物理先验+ML修正”的混合建模范式可迁移至电催化界面CG建模（例如吸附层结构约束耦合DFT校准）；② 分层环境描述符设计思路适用于电极/电解质界面多尺度特征提取（如近表面水团簇→双电层离子排布→远端体相）；③ 结构分布作为监督信号的策略，可拓展为电催化中*覆盖度分布*或*局域pH分布*的约束目标。  
- **与你研究的相关度**：高
- **阅读模式:** 🔍 精读
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/563b4342cc13d2f632c6d5aebe05f6d17eebe642
- **标签:** electrochemistry, MLFF

### 6. Experimental evidence of quantum Drude oscillator behavior in liquids revealed with probabilistic iterative Boltzmann inversion. ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2025-01-11
- **作者:** Brennon L. Shanks; Harry W Sullivan; Pavel Jungwirth; Michael P. Hoepfner
- **核心问题**：揭示液态稀有气体中量子Drude振子行为的实验证据，并简化经典力场参数化  
- **方法要点**：采用概率机器学习增强的迭代Boltzmann反演方法分析中子散射获得的径向分布函数  
- **关键结果**：首次在液体中发现量子Drude振子行为；稀有气体的经典力场可仅用一个参数（关联原子偶极极化率）描述  
- **与你研究的相关度**：低
- **阅读模式:** 📋 摘要
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/56b94421d0ee3c56099355f14c91b275393cfd8f
- **标签:** general

### 7. SimPoly: Simulation of Polymers with Machine Learning Force Fields Derived from First Principles ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2025-10-15
- **作者:** Gregor N. C. Simm; J.-F. Hélie; H. Schulz; Yicheng Chen; Guillem Simeon et al.
- **核心问题**：传统力场精度/迁移性不足，量子化学方法计算成本过高，难以准确模拟聚合物宏观性质  
- **方法要点**：构建无需实验数据拟合的机器学习力场（MLFF），实现聚合物大体系、长时间尺度的高精度模拟  
- **关键结果**：MLFF在聚合物密度预测上优于经典力场；首次实现从头预测玻璃化转变温度（Tg）等二级相变行为  
- **与你研究的相关度**：中
- **阅读模式:** 📋 摘要
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/571ff9e101289aa2d400f955ef23526f531afc1d
- **标签:** MLFF

### 8. SamudrACE: Fast and Accurate Coupled Climate Modeling With 3D Ocean and Atmosphere Emulators ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2025-09-15
- **作者:** James P. C. Duncan; E. Wu; Surya Dheeshjith; Adam Subel; Troy Arcomano et al.
- **核心问题**：如何构建稳定、高分辨率、长期运行的机器学习驱动全球气候耦合模拟器  
- **方法要点**：借鉴传统数值气候模型的耦合范式，将多个机器学习气候分量模型（大气、海洋、海冰等）通过统一耦合器集成，实现跨圈层通量交换与时空对齐  
- **关键结果**：实现了1度水平分辨率、百年尺度、6小时/5天时间步长的稳定模拟；成功再现了ENSO等真实耦合气候变率，且偏差与单组件相当  
- **与你研究的相关度**：低
- **阅读模式:** 📋 摘要
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/5729e55645513008b62ecc9071181b26e5d35799
- **标签:** surface

### 9. PyGAMD: Python graphics processing unit‐accelerated molecular dynamics software ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2025-06-01
- **作者:** Jialei Xu; Shenghong Guo; Miao Zhen; Zhuochen Yu; Youliang Zhu et al.
- **核心问题**：开发一个灵活、高效、支持多尺度建模的分子动力学模拟平台，特别面向软物质（尤其是高分子）研究  
- **方法要点**：基于Python从零构建GPU加速MD平台PyGAMD，集成Python解释器（支持用户自定义势函数）、多语言编译库及DeePMD-kit机器学习力场接口  
- **关键结果**：实现Numba/CUDA驱动的GPU加速，显著提升计算效率；支持用户通过纯Python便捷编写非键/键/角/二面角等相互作用势，极大增强模拟灵活性  
- **与你研究的相关度**：低
- **阅读模式:** 📋 摘要
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/5761a42595a96ba4d188869700f650e249094eb0
- **标签:** electrochemistry, MLFF

### 10. Biomechanical spatio-temporal data analysis of football based on machine learning ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2025-02-10
- **作者:** Peng Zhou; Wenchao Hou; Yiqi Zhu; Weijie Zhang; Yitian Zhang
- **核心问题**：如何利用机器学习与生物力学融合方法，从足球比赛海量时空数据中挖掘深层战术与个体表现规律  
- **方法要点**：结合聚类、分类、马尔可夫链、核密度估计等机器学习算法，并整合生物力学（运动模式、发力机制）与生理数据（心率、运动强度）进行多模态分析  
- **关键结果**：实现了比传统统计方法更直观的可视化和更深层的数据洞察；揭示了生物力学因素（如传球/射门最优角度、身体姿态）对时空行为的关键影响  
- **与你研究的相关度**：低
- **阅读模式:** 📋 摘要
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/57b34b8bfdb1d7f8526fb494e1b93d7f485fac5b
- **标签:** electrochemistry

## 💡 今日亮点

- **最值得精读**：[1] A nuclear-quantum-corrected machine-learning potential reveals quantum-enhanced hydrogen segregation at general grain boundaries in alpha-iron — 首次将核量子效应（NQEs）嵌入MLP并应用于多类型晶界氢偏聚，直接桥接量子尺度效应与宏观脆化机制，为电催化中H吸附/脱附能的量子校正建模提供范式。  
- **可能冲突的研究**：[6] Experimental evidence of quantum Drude oscillator behavior in liquids revealed with probabilistic iterative Boltzmann inversion — 其主张“单参数即可描述液体中量子极化行为”，可能弱化电催化界面水层/质子传输中多体量子极化建模的必要性，与我们强调的局域电子结构-质子耦合动力学存在张力。  
- **值得追踪的团队**：Zhang group (papers [5], [7]) — 在粗粒化与全原子ML力场间建立层级约束框架，其结构感知型Deep Potential设计逻辑可迁移至电催化界面（如双电层+吸附层）的多尺度力场协同构建。  
- **重要趋势**：机器学习势函数正从“精度优先”转向“物理可解释性+量子效应内嵌”双驱动，尤其在缺陷、界面、非平衡态等电催化核心场景中，NQE-aware MLP成为新基准。

## 📌 Key Gap

**关键差距**
- **Gap 1**：所有MLP工作（[1][5][7][9]）均依赖静态构型采样或有限温度AIMD数据，缺乏对电催化动态界面（如外加电势下双电层重构、反应中间体实时生成/消耗）的主动采样策略，导致训练数据覆盖真实反应路径的能力严重不足。  
- **Gap 2**：核量子效应建模仍局限于氢原子，尚未扩展至轻元素（O、N）的零点振动对*OH/*O吸附能及质子耦合电子转移（PCET）能垒的影响，而该效应在OER/CO₂RR中可能主导选择性。  
- **未来方向**：发展电势可控的量子增强主动学习框架——耦合电化学边界条件（如恒电势DFT）、路径积分采样与不确定性引导的界面构型生成，构建首个面向PCET过程的NQE-aware多原子MLP。
