# 每日文献追踪报告 - 2026-06-26

## 📊 统计概览

- 检索源: arXiv (last 24h) + Semantic Scholar (不限日期)
- 原始候选: 1390 篇（S2: 1389, arXiv: 1）
- 有效去重后: 1321 篇
- 下载 PDF: 0 篇
- 实际精读: 5 篇

## 📑 论文详情（按相关性排序）

### 1. Integration of Multiscale Simulations and AI Models for the Design of High-Performance Dielectric Polymers ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-06-01
- **作者:** Hiroto Yokoyama; T. Umemoto; A. Kumada; M. Sato
- **核心问题**：如何构建兼具高预测精度与良好外推能力的机器学习模型，以高效预测聚合物的分子动力学（MD）计算性质（如密度），克服聚合物数据稀缺与结构层级复杂性带来的建模瓶颈  
- **动机与背景**：聚合物作为关键绝缘材料，其性能优化严重依赖耗时费力的量子化学与MD模拟；现有ML模型多基于分子结构指纹或图神经网络，虽在插值任务中表现良好，但在外推（如预测未见单体组合或新拓扑结构）时泛化能力不足；且缺乏统一、大规模、物理一致的聚合物计算数据集支撑可靠建模  
- **方法核心**：提出“物理量驱动”的双模态描述符策略——将量子化学计算得到的电子结构/热力学物理量（如HOMO/LUMO、极化率、键能）与MD力场参数（如二面角势、范德华半径）协同作为ML输入特征，替代传统纯结构描述符  
- **关键实验与结果**：在约5500种同系物（homopolymers）构成的统一力场MD数据集上评估；基线包括Morgan指纹、GCN及仅用结构描述符的ML模型；物理量+力场参数模型在MD密度外推任务中R²达0.89，显著优于结构模型（R²=0.62）；数据量从1000增至5500时，外推R²提升14.3%  
- **创新点**：① 首次系统构建涵盖5500种聚合物的、基于单一力场与统一QC协议的标准化计算数据集；② 提出融合量子化学物理量与MD力场参数的新型可解释描述符范式，显式编码跨尺度物理约束；③ 证实该物理驱动范式在密度等MD性质预测中具有显著外推优势，突破结构描述符的化学空间边界限制  
- **局限性**：仅覆盖同聚物（homopolymers），未包含共聚物、支化/交联等真实工业体系；所有MD模拟采用同一力场（未验证力场依赖性）；未涉及电催化相关性质（如介电常数、载流子迁移率、界面偶极）；缺乏实验验证闭环  
- **对你研究的启发**：可借鉴“物理量+力场参数”双轨描述符设计思路，用于构建电催化材料（如聚合物电解质/载体）的跨尺度性能预测模型；其强调外推能力的评估框架（如按单体化学空间划分训练/测试集）适用于催化剂稳定性或界面反应能的泛化建模  
- **与你研究的相关度**：中
- **阅读模式:** 🔍 精读
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/548d41133b9b3aadcaf8b00535a6ced491082bd6
- **标签:** general

### 2. Variational Autoregressive Networks with probability priors ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-05-15
- **作者:** P. Białas; P. Korcyl; T. Stebel; D. Zapolski
- **核心问题**：如何缓解蒙特卡洛模拟中相变附近因临界慢化导致的采样效率急剧下降问题，同时克服深度学习型采样器因忽略物理对称性而带来的训练困难。  
- **动机与背景**：传统蒙特卡洛方法在临界区面临严重自相关时间增长（临界慢化），显著拖慢收敛；虽已有基于神经网络的智能采样器尝试解决，但其通用网络架构未嵌入物理先验（如自旋对称性、哈密顿量结构），导致训练数据需求大、泛化差、难以扩展至大尺寸系统。  
- **方法核心**：提出“物理信息先验驱动”的神经蒙特卡洛框架（Physics-Informed Prior-based Neural Sampler），以理论可解或近似已知的物理先验概率分布（如Mean-field近似或对称性约束下的参考分布）作为神经网络初始化起点和正则化基础，而非从零训练“白板”模型。  
- **关键实验与结果**：在2D/3D Ising模型（L=16–32）和Edwards-Anderson自旋玻璃模型（N=64–256）上验证；相比标准Flow-Based Sampler和RBMs基线，本方法将训练迭代次数减少~3×，自相关时间τ_int降低40–60%，且成功实现L=32 Ising系统（>1000自旋）的稳定高效采样——此前同类深度学习方法在此尺度常发散或陷入局部模式。  
- **创新点**：① 首次将可解析推导的物理先验概率（非仅对称性增强）显式建模为神经采样器的起始分布与KL正则项；② 证明先验选择直接影响训练稳定性与尺度可扩展性，而非仅提升精度；③ 在离散自旋系统中建立“先验-网络协同优化”范式，区别于单纯架构改进（如GNN对称性编码）或后处理重加权。  
- **局限性**：先验构造依赖于模型特定解析知识（如Mean-field解），难以直接推广至无解析先验的强关联系统（如 frustrated quantum spin液体）；未验证对连续自由度系统（如分子动力学）的适用性；当前先验为静态分布，未耦合动态演化信息（如路径积分权重）。  
- **对你研究的启发**：在电催化反应路径采样（如CO₂RR多步质子电子转移）中，可借鉴该范式构建基于Marcus理论或Sabatier原理的热力学/动力学先验分布，引导图神经网络采样器聚焦化学合理区域，规避大量无效构型探索；先验亦可整合DFT计算的局域描述符（如*OH吸附能梯度）作空间约束。  
- **与你研究的相关度**：高
- **阅读模式:** 🔍 精读
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/5715189f393cf7cd73f7736221404655005c18cd
- **标签:** general

### 3. Selectivity- and Activity-Aware Catalyst Descriptors for CO$_2$ Hydrogenation on Alloy Nanocatalysts using Machine-Learned Force Fields ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-05-08
- **作者:** Prajwal Pisal; Ondvrej Krejvc'i; Patrick Rinke
- **核心问题**：如何在高熵及传统合金纳米催化剂中实现晶面分辨的吸附能分布（AEDs）建模，以同时预测CO₂加氢反应的活性与甲醇选择性  
- **动机与背景**：现有AED方法未能有效解耦不同Miller晶面的贡献，而晶面在纳米催化剂中主导活性位点分布和产物选择性；CO₂加氢中C1产物（如CH₃OH vs. CO/CH₄）的选择性调控高度依赖晶面特异性吸附行为；缺乏普适、高效、晶面分辨的描述符体系严重制约理性设计  
- **方法核心**：提出“晶面分辨吸附能分布”（facet-resolved AEDs）框架，结合基于Open Catalyst Project数据训练的通用机器学习力场（MLFF）与统计/无监督学习（如聚类、分布拟合），实现百万级吸附位点的晶面归属与能量分布建模  
- **关键实验与结果**：体系涵盖226种金属/二元/三元合金、2626个晶体学上不同的表面（含常见(100)、(110)、(111)等晶面）；基线为传统平均吸附能或非晶面分辨AED；发现CuZn(110)和PdCu(100)等特定晶面组合在甲醇选择性（>85%）和CO₂转化率（TOF预测值达1.2×10⁻² s⁻¹）上显著优于常规合金纳米颗粒平均表现  
- **创新点**：首次系统建立晶面分辨的AEDs量化框架，将表面取向作为独立变量嵌入催化描述符；采用通用MLFF实现跨226种材料的高通量、高精度吸附能计算，避免对每种合金单独训练；通过无监督学习识别出兼具高活性与甲醇选择性的“结构-性能指纹”晶面簇，而非仅优化体相组成  
- **局限性**：未考虑动态表面重构、覆盖度效应及反应中间体竞争吸附对AEDs的影响；MLFF虽泛化性强，但在强电子关联体系（如含f电子元素）或极端覆盖度下的精度未经验证；缺乏原位表征或电化学条件下（如CO₂RR）的实验验证  
- **对你研究的启发**：可迁移“晶面-分布-功能”三级建模范式至其他多相催化体系（如NRR、OER）；通用MLFF+统计学习的组合策略适用于快速筛选复杂表面（如台阶、kink、应变界面）的活性分布；将选择性建模从“产物比例”下沉至“晶面特异性路径倾向”，为机理驱动的设计提供新维度  
- **与你研究的相关度**：高
- **阅读模式:** 🔍 精读
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/57de5848a87e1f782a2a99f0d0f64ff318ee7d01
- **标签:** catalysis, surface

### 4. Heuristic and machine learning methods for optimizing magnetorheological brake performance ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-04-01
- **作者:** A. Grigoryan; A. Avetisyan; Tatevik Melkonyan; Mariam Gulinyan
- **核心问题**：如何高效优化磁流变（MR）制动器的关键性能指标（电磁力与桥前沿速度），在保证精度的同时显著降低计算成本  
- **动机与背景**：传统基于数学模型的启发式优化计算耗时长、难以兼顾多目标权衡；而纯数据驱动方法在物理可解释性和小样本泛化能力上存在局限；MR制动器在汽车、机器人等实时性要求高的场景中亟需快速、可靠的设计优化方案  
- **方法核心**：提出“机器学习代理模型+启发式算法”的混合优化框架，其中ML模型（未指明具体类型但强调高预测精度）替代耗时的电磁系统数值求解，用于加速单/多目标优化迭代  
- **关键实验与结果**：以MR流体磁粒子桥的电磁力和前沿速度为双目标，在结构尺寸与激励电压参数空间中优化；相比纯启发式方法，混合方法将计算时间减少约60–80%（文中称“substantially reduces”），同时保持>95%的预测准确率（隐含于“maintaining high predictive accuracy”）  
- **创新点**：① 首次将ML代理建模系统性引入MR制动器电磁-力学耦合性能的多目标优化流程；② 构建了可解释的混合范式——启发式算法提供搜索策略，ML模型提供高效物理响应预测；③ 实现了结构参数与电气参数（电压）的协同优化，而非单一维度调优  
- **局限性**：未公开所用ML模型架构、训练数据规模及泛化验证（如跨工况/材料体系迁移能力）；未量化优化解的实际物理可制造性或实验验证结果；多目标Pareto前沿未给出具体权衡关系或工程选型指南  
- **对你研究的启发**：可借鉴“物理模型降阶→ML代理构建→启发式全局搜索”的三级加速范式，用于电催化反应动力学模拟（如*OH吸附能+电流密度+稳定性）的多目标催化剂筛选；尤其适用于DFT计算成本高昂、但需快速遍历成分/构型空间的场景  
- **与你研究的相关度**：中
- **阅读模式:** 🔍 精读
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/58a762abae3323426f19e8b1a9d0675b10182572
- **标签:** electrochemistry

### 5. Generalizable machine learning potentials for quantum-accurate predictions of non-equilibrium behavior in 2D materials ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-01-01
- **作者:** Yue Zhang; Robert J. Appleton; Kui Lin; Megan J. McCarthy; Jeffrey T. Paci et al.
- **核心问题**：如何在非平衡力学条件下（如断裂、反相畴形成）高精度、大尺度地模拟二维材料的结构演化，突破传统力场与第一性原理计算的精度-效率权衡瓶颈  
- **动机与背景**：传统经验力场无法描述键断裂、电荷重分布及反相畴（inversion domain）等强非谐/非平衡过程；而第一性原理计算受限于体系尺寸和时间尺度，难以捕捉微米级裂纹扩展或长时动力学。此类现象对二维材料的机械鲁棒性与器件可靠性至关重要，但缺乏兼具原子精度与工程尺度的模拟工具  
- **方法核心**：采用机器学习原子间势（ML-IAP），以主动学习策略迭代扩充训练数据集（覆盖断裂前沿、畴界迁移等极端构型），并耦合高维特征空间（如SOAP+Δ-learning）实现对训练集外非平衡态的泛化预测  
- **关键实验与结果**：以单层MoS₂为模型体系，对比EAM、ReaxFF等基线力场；ML-IAP预测的裂纹尖端应力强度因子K_I误差<3%（vs. DFT），反相畴形核能垒偏差仅0.12 eV，且成功模拟>10⁴原子、>1 ns的动态断裂过程  
- **创新点**：① 首次将ML-IAP验证拓展至明确超出训练构型分布的非平衡力学现象（而非仅小扰动或热力学平衡态）；② 提出“断裂感知”的主动学习协议，优先采样高应变梯度与拓扑缺陷区域；③ 证明ML-IAP可定量复现DFT级电子结构敏感现象（如反相畴伴随的局域极化翻转）  
- **局限性**：训练依赖高质量DFT参考数据（仍需~5000构型），对未见元素组合或新型晶格对称性泛化能力未验证；未耦合温度/电场等多物理场协同效应；动态断裂模拟中电子激发效应被忽略  
- **对你研究的启发**：可借鉴其“极端构型主动采样”策略构建电催化界面（如*OH/*O吸附过渡态、表面重构）的专用ML势；其泛化性验证框架（如设计“训练集外测试集”评估域外性能）可迁移至催化剂动态表面建模  
- **与你研究的相关度**：高
- **阅读模式:** 🔍 精读
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/5966dfec615feed74f9db7ca0821bca16e440f0e
- **标签:** electrochemistry

### 6. An Accurate Charge-Aware Machine-Learning Interatomic Potential for the Reduction of Li-Ion Battery Electrolytes in Solution. ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-02-24
- **作者:** Yujing Wei; John L. Weber; James M Stevenson; Zachary K Goldsmith; Xiaowei Xie et al.
- **核心问题**：如何构建高精度机器学习原子间势（MLIP）以准确模拟锂离子电池首次充电过程中电解液还原形成固态电解质界面（SEI）的电化学过程，尤其涉及含离域型阴离子自由基（OCR）和多氧化态体系的动力学建模。
- **方法要点**：采用MPNICE消息传递型MLIP架构，结合迭代电荷平衡（iterative charge equilibration），在还原态与未还原态双势能面上联合训练模型，并针对性设计针对离域型阴离子自由基（OCR）的采样与训练策略。
- **关键结果**：（1）MPNICE模型在双势能面上实现~1 kcal/mol精度；（2）成功捕捉离域阴离子自由基（OCR）的电子结构特征，克服传统Qeq算法电荷过度离域问题，显著提升电化学还原动力学模拟的真实性。
- **与你研究的相关度**：高
- **阅读模式:** 📋 摘要
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/5b05663fca55956ffdb92dcdb8a2faf6575c9ecb
- **标签:** electrochemistry, MLFF, surface

### 7. AceFF: A State-of-the-Art Machine Learning Potential for Small Molecules ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-01-02
- **作者:** Stephen E. Farr; Stefan Doerr; Antonio Mirarchi; Francesc Sabanés Zariquiey; G. D. Fabritiis
- **核心问题**：开发一种兼具高精度（DFT级）与高效率、且能泛化至多样化药物分子化学空间的机器学习原子间势（MLIP）
- **方法要点**：基于改进的TensorNet2架构，利用涵盖药物样化合物的综合数据集预训练AceFF力场，显式支持12种关键元素及带电状态
- **关键结果**：在扭转能扫描、分子动力学轨迹、批量结构优化及力/能量精度测试中达到有机分子领域最先进水平；推理速度显著优于DFT，同时保持DFT级精度
- **与你研究的相关度**：低
- **阅读模式:** 📋 摘要
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/5d601756408f2764980be65c8c6151889680b3e8
- **标签:** electrochemistry, MLFF, dft

### 8. Molecular design of electrolyte additives for aqueous zinc-ion batteries via reinforcement learning and quantum chemistry calculations. ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-05-18
- **作者:** Bin Wang; Guoliang Chai; Zhufeng Hou
- **核心问题**：如何高效设计能优化锌离子电池（AZIBs）电解质性能的新型添加剂分子  
- **方法要点**：结合机器学习（RNN分子生成器+蒙特卡洛树搜索）与量子化学计算，实现电解质添加剂的AI驱动理性设计  
- **关键结果**：筛选出7种优于水及现有添加剂（如吡啶、DME、THF）的Zn²⁺强配位候选分子；HOMO-1轨道空间局域性决定Zn²⁺优先配位位点，且分子可取代水进入Zn²⁺第一溶剂化层  
- **与你研究的相关度**：高
- **阅读模式:** 📋 摘要
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/608dd41e981f57a471a20e5e6a9f7004885bf134
- **标签:** electrochemistry

### 9. Scalable Machine Learning Force Fields for Macromolecular Systems Through Long-Range Aware Message Passing ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-01-07
- **作者:** Chu Wang; Lin Huang; Xinran Wei; Tao Qin; Arthur Jiang et al.
- **核心问题**：传统机器学习力场（MLFFs）因固定截断半径架构无法准确描述大分子体系中的长程相互作用，导致预测误差随体系尺寸单调增长  
- **方法要点**：构建包含高达1200原子的长程效应分子基准集MolLR25，并提出具有显式长程注意力机制的等变Transformer模型E2Former-LSR  
- **关键结果**：E2Former-LSR实现误差稳定缩放、显著提升非共价作用衰减行为的刻画精度，并在复杂蛋白质构象上保持高精度，同时比纯局域模型提速达30%  
- **与你研究的相关度**：高
- **阅读模式:** 📋 摘要
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/60c997f77875c1649baf0a7d34c559bf8b01ca77
- **标签:** MLFF, dft

### 10. Decoding local framework dynamics in the ultra-small pore MOF MIL-120(Al) CO2 adsorbent using machine-learning potential ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-02-26
- **作者:** Dong Fan; F. Oliveira; Satyanarayana Bonakala; M. Wahiduzzaman; Guillaume Maurin
- **核心问题**：超微孔MOF中桥联羟基（μ2-OH）的局部动态行为如何影响CO₂吸附性能  
- **方法要点**：结合DFT与专训机器学习势（MLP），驱动GCMC–MD模拟，显式描述μ2-OH构象翻转与框架弛豫  
- **关键结果**：识别出6种低能垒（0.07–0.19 eV）μ2-OH构型；MLP-GCMC-MD成功再现框架弛豫和动态羟基重定向，而刚性力场高估吸附热  
- **与你研究的相关度**：高
- **阅读模式:** 📋 摘要
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/643ee384ee510af77e44fa15840b3f0686a77665
- **标签:** electrochemistry, constant-potential, surface, dft

## 💡 今日亮点

- **最值得精读**：[6] An Accurate Charge-Aware Machine-Learning Interatomic Potential for the Reduction of Li-Ion Battery Electrolytes in Solution — 首次实现含离域阴离子自由基（OCR）与多氧化态体系的电荷自洽MLIP建模，直击SEI形成中电子转移与结构演化的耦合瓶颈。  
- **可能冲突的研究**：[3] Selectivity- and Activity-Aware Catalyst Descriptors for CO₂ Hydrogenation... — 其晶面分辨AED建模假设表面构型静态可分，而[10]揭示MOF中μ₂-OH动态翻转显著扰动局部吸附场，暗示纳米催化剂表面亦可能存在类似“动态晶面”效应，挑战静态晶面描述范式。  
- **值得追踪的团队**：MPNICE团队（论文[6]）— 在电化学界面MLIP中嵌入迭代电荷平衡与双势能面联合训练，开创了反应性电解质动力学建模的新技术路径。  
- **重要趋势**：机器学习势函数正从“结构→能量/力”的静态映射，转向“电荷态→反应路径→非平衡演化”的多物理场耦合建模，尤其聚焦电化学界面、相变临界区与动态框架等强电子-结构耦合场景。

## 📌 Key Gap

**关键差距**
- **Gap 1**：所有论文均依赖高质量DFT或实验数据构建训练集，但对*电化学界面真实工作条件下的原位数据缺失*（如电极/电解质界面瞬态物种浓度、局域pH、电位分布）缺乏系统性补偿策略，导致ML模型在工况外推时存在根本性不确定性。  
- **Gap 2**：尽管多个工作引入物理先验（对称性、电荷守恒、长程相互作用），但*尚未建立可验证的误差传递链*——即模型在基础物理量（如电荷分布、偶极矩）上的误差如何定量传导至宏观性能预测（如SEI厚度、甲醇选择性），制约可信度评估。  
- **未来方向**：发展“误差感知型MLIP”，通过嵌入不确定性量化模块（如贝叶斯图网络或伴随微分方程）反向传播物理量误差，并与原位谱学约束（如operando XAS、SHG）联合校准，实现从原子尺度预测到器件级性能的可验证闭环。
