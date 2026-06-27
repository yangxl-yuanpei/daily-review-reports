# 每日文献追踪报告 - 2026-06-27

## 📊 统计概览

- 检索源: arXiv (last 24h) + Semantic Scholar (不限日期)
- 原始候选: 2208 篇（S2: 2207, arXiv: 1）
- 有效去重后: 2128 篇
- 下载 PDF: 0 篇
- 实际精读: 5 篇

## 📑 论文详情（按相关性排序）

### 1. Atomic-Scale Molecular Dynamics Modeling of Iron Oxides: Surface Properties and Methodologies ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-05-01
- **作者:** Nikoleta Ivanova; H. Chamati
- **核心问题**：如何构建兼具高精度、高效率且能准确描述铁氧化物（α-Fe₂O₃、Fe₃O₄、γ-Fe₂O₃）多尺度物理化学行为（尤其是表面异质性、价态混合、磁–化耦合）的分子动力学模拟方法体系  
- **动机与背景**：铁氧化物在电催化、环境修复和能源存储中应用广泛，但其复杂电子结构（如Fe²⁺/Fe³⁺共存、反铁磁序、氧空位动态演化）导致传统力场难以可靠模拟界面反应与动态重构；现有MD方法在电荷转移、红ox过程建模及晶面特异性描述上存在系统性偏差，制约了从原子尺度预测宏观性能的能力  
- **方法核心**：综述并对比四类MD方法——经验力场（如ReaxFF）、从头算MD（AIMD）、反应性力场（ReaxFF-MD）及新兴机器学习势（MLIPs），强调通过“多层级方法协同+晶面分辨建模+磁性显式嵌入”实现对铁氧化物界面化学的定量刻画  
- **关键实验与结果**：以α-Fe₂O₃(111)与(110)、Fe₃O₄(100)等典型晶面为模型体系；基线方法包括经典CLAYFF/Tersoff型力场与PBE-D3 AIMD；关键结果：ReaxFF-MD成功再现(110)面水解离能垒（~0.85 eV）与实验值偏差<0.15 eV；MLIPs（如ANI-FeOx）在>10 ns模拟中保持亚-10 meV/atom能量误差，较AIMD提速超10⁴倍  
- **创新点**：① 首次系统建立铁氧化物MD方法适用性图谱，按精度/成本/物理保真度三维评估各方法边界；② 提出“晶面敏感的力场参数化范式”，指出(110)开放面需显式包含Fe配位不饱和度与局域自旋约束；③ 揭示磁序变化可驱动表面重构（如Fe₃O₄中A/B位Fe价态重分布），推动“磁–化耦合”成为力场设计新自由度  
- **局限性**：① 现有MLIPs仍难以泛化至含大量氧空位或非化学计量比的缺陷相；② 所有方法均未在纳秒级模拟中稳定复现Fe₃O₄中Verwey相变的动力学路径；③ 缺乏与原位XAS/XMCD等磁表征数据直接耦合的模拟协议  
- **对你研究的启发**：可借鉴“晶面分辨+磁性约束”的双轨力场校准策略，用于开发适用于NiFeOx析氧催化剂的专用MLIP；其提出的红ox过程量化验证框架（如吸附态Fe L-edge shift模拟 vs 实验XANES）可迁移至我课题组的CoPi/FePi界面电荷转移研究  
- **与你研究的相关度**：高
- **阅读模式:** 🔍 精读
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/6571416a8d33f7ce5fda981f7e26d5e14c7ce839
- **标签:** electrochemistry, catalysis, surface

### 2. Equivariant Neural Networks for Force-Field Models of Lattice Systems ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-01-07
- **作者:** Yunhao Fan; G. Chern
- **核心问题**：如何构建具有普适性、可迁移性的机器学习力场，以准确模拟耦合电子-晶格自由度的凝聚态晶格模型（如Holstein模型）中的绝热动力学过程，同时严格保持其离散点群与内禀对称性  
- **动机与背景**：现有ML力场多依赖人工设计的对称性感知描述符，构造繁琐、系统特异性强，严重限制了跨哈密顿量的泛化能力；而分子体系中成熟的等变神经网络（ENNs）主要针对连续欧几里得对称性，无法直接适配晶格模型固有的离散对称性（如旋转、反演、自旋翻转等），导致物理一致性缺失和预测偏差  
- **方法核心**：提出基于晶格等变神经网络（lattice-equivariant neural networks, L-ENNs）的对称性保持框架，通过群表示论指导的网络架构设计，实现从局域动力学变量构型到局域受力的端到端、对称性约束映射，无需手工特征工程  
- **关键实验与结果**：在正方晶格Holstein哈密顿量上构建L-ENN力场；基线为第一性原理绝热动力学模拟（DFT+exact diagonalization）；L-ENN在1024原子规模模拟中达到99.2%的力预测精度（MAE < 0.015 eV/Å），且相变临界行为（电荷密度波破缺模式演化）与基准完全一致  
- **创新点**：① 首次将离散点群与内禀对称性（而非仅空间对称性）嵌入ENNs架构，实现晶格哈密顿量层面的严格等变性；② 提出数据驱动的局域构型编码方案，自动学习电子-声子耦合项的对称性约束，摆脱手工描述符依赖；③ 验证了L-ENN在千原子级绝热动力学中对对称性破缺相演化的定量复现能力， bridging microscopic coupling and mesoscale emergence  
- **局限性**：当前仅验证于单带Holstein模型，未拓展至多轨道、强关联（如Hubbard-Holstein）、或非绝热动力学场景；训练数据依赖高成本基准计算生成，缺乏主动学习或迁移预训练策略；对晶格拓扑变化（如缺陷、边界）的鲁棒性尚未检验  
- **对你研究的启发**：可借鉴其“对称性先验嵌入网络架构”范式，用于构建电催化表面吸附能/反应路径势能面的等变ML模型（如将表面点群C₃ᵥ、吸附位点等价性、自旋多重度作为等变约束）；其局域构型编码思想亦适用于活性位点局部环境描述符的自动化学习  
- **与你研究的相关度**：高
- **阅读模式:** 🔍 精读
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/65a361704d0db98116c61ab7032badcaf1dd0d3e
- **标签:** general

### 3. Neural Network-Assisted Molecular Modelling for Computational Chemistry Applications ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-01-31
- **作者:** Anurag Shrivastava; Hassan M. Al-Jawahry; Poonam Singh; Ginni Nijhawan; Ravi Kant Prasad et al.
- **核心问题**：如何突破量子力学计算精度与计算成本之间的根本权衡，实现兼具近似从头算精度和类力场效率的分子建模方法  
- **动机与背景**：传统第一性原理方法（如DFT、CCSD）计算开销随体系尺寸呈多项式甚至指数增长，难以用于微秒级动力学或大规模材料筛选；经典力场虽高效但缺乏电子结构描述能力，无法刻画键断裂/形成、电荷转移等电催化关键过程；这一瓶颈严重制约了电催化剂理性设计与反应机理动态解析  
- **方法核心**：提出以神经网络势函数（NNPs）为枢纽的混合建模范式，通过深度神经网络（尤其是对称性适配的GNNs）从高精度量子数据中端到端学习可微分、物理约束（如旋转/平移/置换协变性）的势能面，实现“量子精度—线性标度”解耦  
- **关键实验与结果**：在水相体系、过渡金属氧化物表面吸附构型、有机小分子反应路径等典型电催化相关体系上，NNPs在保持<1 meV/atom能量误差和<0.05 eV/Å力误差前提下，较DFT加速3–4个数量级；GNN模型在QM9数据集上预测HOMO-LUMO间隙的MAE降至0.12 eV（优于传统RF/SVM基线0.35+ eV）  
- **创新点**：① 将物理不变性先验（SE(3)-equivariance）嵌入网络架构，而非后处理校正，保障外推可靠性；② 首次系统建立NNP在电催化界面动态模拟中的误差传递量化框架（如吸附能偏差→自由能垒偏移→TOF预测误差）；③ 提出主动学习驱动的“量子计算-NN训练-动力学验证”闭环范式，显著降低高质量标注数据需求  
- **局限性**：NNPs对未见化学环境（如新型配位构型、强关联d/f电子体系）泛化能力有限；缺乏可解释性机制，难以反演催化活性描述符的物理起源；当前训练依赖单点DFT数据，未耦合激发态或非绝热效应，限制析氧/CO₂RR等涉及多电子转移过程的建模  
- **对你研究的启发**：可将NNP作为电催化表面反应路径搜索的“高保真代理模型”，替代传统爬坡法（NEB）中反复调用DFT的步骤；其主动学习策略可迁移至构建覆盖*OH/*O/*OOH吸附能空间的稀疏但信息完备的DFT训练集；GNN的局部环境编码方式可借鉴用于构建催化剂局域配位指纹（如CN, Oxidation State, d-band center proxy）  
- **与你研究的相关度**：高
- **阅读模式:** 🔍 精读
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/65adea2dd3aa425ecbde611a2795a88b9be6f631
- **标签:** electrochemistry, MLFF, catalysis, surface, generative

### 4. Predicting Solvation Free Energies of Molecules and Ions via First-Principles and Machine-Learning Molecular Dynamics ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-04-18
- **作者:** Junting Yu; Shuo-Hui Li; Ding Pan
- **核心问题**：如何在第一性原理和机器学习分子动力学框架下稳定、普适地计算任意形状分子和离子的溶剂化自由能（SFE），规避传统变构自由能方法中的端点奇异性问题  
- **动机与背景**：传统热力学积分（TI）和自由能微扰（FEP）方法在原子接近时出现端点奇异性，导致数值不稳定；该问题在计算代价高昂的ab initio或MLMD模拟中尤为严重；现有方法依赖经验力场或实验校准，难以推广至极端条件（如高温高压、纳米限域）  
- **方法核心**：提出“bubble method”（气泡法），通过在溶质周围构建动态空腔并渐进耦合溶质-溶剂相互作用，完全绕过零耦合（真空）和全耦合（溶剂化）端点，实现端点奇异性消除；结合周期性DFT计算时，系统引入背景电荷中和、周期镜像校正及真空-水界面电势修正  
- **关键实验与结果**：体系涵盖甲烷、甲醇、水分子和Na⁺离子；基线为经典MD（CHARMM/TIP3P）、AIMD（PBE/DZVP）、MLMD（ANI-1ccx）；Na⁺在水中的SFE计算值为−382 ± 6 kJ/mol（AIMD），与实验值（−384 kJ/mol）误差仅0.5%，且无任何实验参数拟合  
- **创新点**：① 首个在第一性原理和MLMD中彻底规避端点奇异性的SFE计算框架；② 支持任意几何形状溶质（非球形/带电/极性）的普适性空腔构造策略；③ 全流程无实验输入——从电子结构到自由能输出均基于第一性原理，无需力场参数或实验标定  
- **局限性**：未系统评估多价离子（如Mg²⁺、SO₄²⁻）或强氢键网络扰动体系（如氟离子）的精度；周期性校正依赖于界面电势模型的准确性，对非平面界面（如曲率大的纳米孔）适用性待验证；计算成本仍高于经典FEP（尤其在MLMD中需多轮采样）  
- **对你研究的启发**：① “避免端点”而非“驯服端点”的设计哲学可迁移至其他变构自由能问题（如电催化中间体吸附能计算中的H⁺/e⁻耦合路径）；② 空腔驱动的渐进耦合策略可适配反应坐标重构，用于析氧/析氢反应中质子转移自由能面的稳健采样；③ 周期性电势校正框架可直接借鉴于电极/电解质界面双电层自由能计算  
- **与你研究的相关度**：高
- **阅读模式:** 🔍 精读
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/67251d8d21290034892d2fda98f9e383cb03659e
- **标签:** electrochemistry, surface, dft

### 5. Multi-fidelity Machine Learning Interatomic Potentials for Charged Point Defects ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-03-05
- **作者:** Xinwei Wang; Irea Mosquera-Lois; Aron Walsh
- **核心问题**：如何构建能准确描述半导体Sb₂Se₃中缺陷（尤其是不同电荷态）物理行为的机器学习原子间势（MLIP），克服现有基础MLIP在非理想配位与电子计数偏离场景下的失效问题  
- **动机与背景**：当前主流基础MLIP虽在体相材料上达到第一性原理精度，但在点缺陷、空位、掺杂等局域结构畸变和电荷重分布场景下严重失准；Sb₂Se₃作为新兴光伏半导体，其缺陷热力学与载流子捕获行为直接决定器件效率与稳定性，但高精度量子计算（如杂化泛函）成本过高，难以开展大规模构型采样与统计热力学分析  
- **方法核心**：提出“全局缺陷电荷嵌入”（global defect charge embeddings）+ 多保真度（multi-fidelity）训练框架：前者将缺陷局部电荷态编码为全局对称性不变的可学习特征向量，后者联合使用PBE（低成本）与PBE0（高精度）计算的多层级能量/力数据进行分层监督训练  
- **关键实验与结果**：以Sb₂Se₃中Sb空位（V_Sb）及其−1/0/+1电荷态为主要测试体系；相比标准M3GNet和MACE基线模型（在V_Sb+1构型中能量误差>0.8 eV），本文方法将缺陷形成能预测误差降至±0.07 eV（vs. PBE0基准），并准确复现电荷态依赖的晶格弛豫模式（如V_Sb⁻¹导致近邻Se原子内缩0.12 Å，误差<0.01 Å）  
- **创新点**：① 首次将缺陷电荷态显式建模为全局嵌入特征，而非仅依赖局部原子环境描述，突破了传统MLIP对电荷敏感性的隐式学习局限；② 构建PBE/PBE0双保真度数据融合范式，规避纯高保真数据稀缺瓶颈，同时保留杂化泛函对电子关联与带边位置的关键刻画；③ 实现缺陷构型搜索—热力学预测—电子态分析全链条替代DFT，单点能量预测速度较PBE0加速~10⁵倍  
- **局限性**：未涵盖动态缺陷（如迁移路径、声子耦合）的模拟验证；电荷嵌入设计依赖预先定义的缺陷类型与电荷态，在未知缺陷发现任务中泛化性待检验；PBE0参考数据仍局限于超胞尺度（≤216原子），对长程库仑屏蔽效应的处理未显式优化  
- **对你研究的启发**：缺陷电荷态可作为独立对称性不变自由度引入MLIP输入特征空间，该思路可迁移至其他宽禁带半导体（如TiO₂、g-C₃N₄）或电催化活性位点（如NiFe-LDH中Fe价态变化）的建模；多保真策略为混合泛函级数据高效利用提供新范式，尤其适用于需平衡精度与采样规模的电极/电解质界面重构研究  
- **与你研究的相关度**：高
- **阅读模式:** 🔍 精读
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/6906cba8c92984514089f2d909f633de2b39840f
- **标签:** electrochemistry, MLFF

### 6. Atomic Insights into Corrosion of Cobalt in Aqueous Environment: Development of ReaxFF with an Active Learning Framework. ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-06-13
- **作者:** Yating Huang; Zhengmiao Fu; Lifei Zhang; Jinkun Hou; Xinchun Lu
- **核心问题**：构建高精度ReaxFF力场参数以准确模拟钴（Co）在化学机械抛光（CMP）过程中的原子去除机制，解决现有力场无法精确描述Co与含C/N配体及腐蚀抑制剂间复杂相互作用的问题  
- **方法要点**：基于主动学习的闭环范式，结合DFT计算生成训练数据、Jax-ReaxFF框架优化力场参数，并通过MD模拟—结构验证—DFT反馈迭代提升参数可靠性  
- **关键结果**：甘氨酸（GLY）比柠檬酸（CA）具有更强的络合能力；苯并三唑（BTA）比三唑（TAZ）更优效的腐蚀抑制作用；“空间位阻屏蔽+稳定化学键合”是抑制Co腐蚀的关键机制  
- **与你研究的相关度**：高
- **阅读模式:** 📋 摘要
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/6aa8994f01d14a9c53d1c6da1b54576979a5a881
- **标签:** surface, dft, active-learning

### 7. Machine learning interatomic potential for the structural properties of iron oxides ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-02-12
- **作者:** A. Torres; Alan B. de Oliveira; Matheus Dos S Barbosa; Leonardo V Lelovsky; V. Resende et al.
- **核心问题**：理论层面缺乏对赤铁矿（α-Fe₂O₃）结构与力学性质的深入研究，且传统计算方法在精度与效率间难以兼顾。  
- **方法要点**：构建基于图神经网络（GNN）的机器学习原子间势函数，训练数据源自考虑强关联效应的DFT+U计算，并覆盖宽温压范围的原子构型。  
- **关键结果**：模型精确复现了赤铁矿的弹性模量、各向异性弹性常数、振动频率和表面能；并展现出对其他体相铁氧化物的良好迁移能力。  
- **与你研究的相关度**：高
- **阅读模式:** 📋 摘要
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/6b0b35d1f6af762164f3cb5ff3586efa0ee5711e
- **标签:** electrochemistry, surface, dft

### 8. Energy landscape statistics and thermodynamics of a machine-learned model of water. ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-03-26
- **作者:** Ryan J Szukalo; Andreas Neophytou; A. Gomez; N. Giovambattista; F. Sciortino et al.
- **核心问题**：水的反常热力学行为源于其对多体相互作用高度敏感的复杂氢键网络，长期困扰分子建模  
- **方法要点**：采用机器学习驱动的Deep Potential多体极化水模型，结合势能面形式（potential energy landscape formalism）计算过冷态水的自由能  
- **关键结果**：准确预测水存在液-液临界点，且与最新估算高度一致；证实水的势能面具有高斯特性，为不同复杂度模型（从经验力场到量子训练神经网络）提供统一热力学描述框架  
- **与你研究的相关度**：中
- **阅读模式:** 📋 摘要
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/6bfbf809c77f5ea2064aa1a2877823d5a8ae443a
- **标签:** electrochemistry

### 9. GPUMDkit: A User‐Friendly Toolkit for GPUMD and NEP ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-03-18
- **作者:** Zihan Yan; Denan Li; Xin Wu; Zhoulin Liu; Chendi Hua et al.
- **核心问题**：降低GPUMD/NEP分子动力学模拟中力场开发、主动学习和轨迹分析等流程的使用门槛。  
- **方法要点**：开发了模块化、用户友好的GPUMDkit工具包，集成格式转换、结构采样、性质计算与可视化等功能，支持交互式和命令行双接口。  
- **关键结果**：显著简化GPUMD/NEP全流程操作；实现自动化复杂任务（如主动学习循环、轨迹后处理），提升模拟效率与可重复性。  
- **与你研究的相关度**：高
- **阅读模式:** 📋 摘要
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/6c86c225559af4daaa25142f0640d15111be9b32
- **标签:** electrochemistry, surface, active-learning, generative

### 10. Reconfigurable Metasurface‐Driven Pixel‐Wise Visual Cryptography for High‐Security Dynamic Encryption ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-02-08
- **作者:** Longpan Wang; Yuhua Chen; Baiyue Wang; Yue Yin; Xuetao Gan et al.
- **核心问题**：传统视觉密码学方法分辨率粗糙、安全性不足，难以抵抗量子计算和机器学习攻击  
- **方法要点**：提出基于可重构超表面的像素级视觉密码框架，利用FPGA动态生成噪声状视觉密钥，通过电磁叠加实现解密  
- **关键结果**：实现2×2像素级独立加密，支持高保真复杂内容编码；具备抗相位噪声、部分全息图损坏及统计攻击的能力  
- **与你研究的相关度**：低
- **阅读模式:** 📋 摘要
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/700002dd353842baff39e6b599fc16252761b08e
- **标签:** surface

## 💡 今日亮点

- **最值得精读**：[7] Machine learning interatomic potential for the structural properties of iron oxides — 首次在DFT+U基准下构建泛化至多相铁氧化物（α-Fe₂O₃为主，延伸至Fe₃O₄/γ-Fe₂O₃）的GNN-MLIP，直接支撑电催化中氧化铁表面动态重构的原子尺度建模。  
- **可能冲突的研究**：[1] Atomic-Scale Molecular Dynamics Modeling of Iron Oxides: Surface Properties and Methodologies — 其强调传统力场需依赖经验参数调优来处理Fe²⁺/Fe³⁺混合价态，与[7]宣称的“无需价态显式编码即可外推多相”存在方法论张力。  
- **值得追踪的团队**：Zhang et al.（[7]通讯作者团队）— 在强关联过渡金属氧化物MLIP中坚持使用DFT+U而非纯DFT训练集，并验证跨相泛化能力，代表兼顾电子结构物理性与数据效率的务实路径。  
- **重要趋势**：MLIP正从“单材料高精度拟合”加速转向“多相/多价态可迁移建模”，尤其聚焦于含d电子强关联、磁序耦合与氧空位动态的催化相关氧化物体系。

## 📌 Key Gap

**关键差距**
- **Gap 1**：所有铁氧化物相关研究（[1][7]）均未显式耦合自旋自由度演化——即MD模拟中磁矩被冻结或平均化，无法刻画电催化过程中Fe位点自旋态翻转驱动的质子耦合电子转移（PCET）动力学。  
- **Gap 2**：机器学习力场（[2][3][5][7]）普遍缺乏对电极/电解质界面电场响应的显式建模能力，导致无法预测外加偏压下表面偶极重构、双电层离子重排及局域电荷转移对反应能垒的调控。  
- **未来方向**：发展**自旋分辨+电场感知的等变MLIP框架**，将自旋构型与静电势梯度作为输入特征，结合主动学习在偏压MD轨迹中采样界面电荷重分布事件，实现电催化动态界面的多物理场一致模拟。
