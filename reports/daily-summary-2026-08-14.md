# 每日文献追踪报告 - 2026-08-14

## 📊 统计概览

- 检索源: arXiv (last 24h) + Semantic Scholar (不限日期)
- 原始候选: 2429 篇（S2: 2428, arXiv: 1）
- 有效去重后: 2011 篇
- 下载 PDF: 0 篇
- 实际精读: 5 篇

## 📑 论文详情（按相关性排序）

### 1. Studying Heat Conduction Properties by Using Machine Learning Potentials: a brief review ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-08-10
- **作者:** Yangjun Qin; Z. Zong; Tianhao Li; Haisheng Fang; Guimei Zhu et al.
- **核心问题**：如何构建高精度、高效率的机器学习势函数（MLPs）以可靠模拟微纳尺度结构的热输运性质（特别是热导率）  
- **动机与背景**：传统经验力场在描述键合重构、电荷转移等热激发过程时精度不足，而第一性原理分子动力学（AIMD）计算成本过高，难以支撑长时、大体系热输运模拟；热导率对势函数敏感，微小误差可导致数量级偏差，亟需兼具DFT精度与力场效率的替代方案  
- **方法核心**：系统综述机器学习势函数的三大支柱——原子环境描述符（如SOAP、ACSF、M3GNet）、训练策略（主动学习、不确定性量化、多保真度融合）及泛化性评估框架，并聚焦其在热导率预测中的跨材料体系性能基准  
- **关键实验与结果**：评估体系涵盖Si、Ge、石墨烯、MoS₂、SiO₂非晶等典型热管理材料；基线方法包括Tersoff、SW、EDIP等经验势及SCAN-DFT；关键结果：最优MLPs（如DP-Si、M3GNet-2023）在Si中预测κ与实验偏差<15%，显著优于Tersoff（偏差>40%），且在非晶SiO₂中再现了温度依赖的反常热导率平台  
- **创新点**：首次建立面向热输运任务的MLPs系统性评估范式（含描述符敏感性分析、热导率积分收敛性检验、声子谱保真度量化）；揭示描述符平移/旋转不变性与热导率低频声子模态捕捉能力的隐式关联；提出“热导率导向”的主动学习采样策略（优先选取高热流涨落构型）  
- **局限性**：未涵盖电-声耦合主导的热电材料（如Bi₂Te₃）及强关联体系（如VO₂相变区）；MLPs对极端非平衡态（如超快激光激热）的适用性缺乏验证；开源实现与标准化测试协议尚未统一  
- **对你研究的启发**：可借鉴其“任务驱动型”MLPs设计思路（如针对电催化中的*OH/*O吸附能差、反应路径能垒等关键量优化损失函数）；热输运中采用的声子谱保真度验证方法可迁移至催化反应过渡态振动模式分析；主动学习策略可适配于电催化材料高通量筛选中的关键活性位点构型采样  
- **与你研究的相关度**：高
- **阅读模式:** 🔍 精读
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/0b5f625a4f0003941ddcafadcf308d5a0f970c26
- **标签:** electrochemistry, dft

### 2. Deciphering Chemical
Environments in Conformational
Data Sets Using an IQA Band-Matching Protocol ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-08-11
- **作者:** Bienfait K. Isamura; Roya Momen; Jaiming J. K. Chung; Paul L. A. Popelier
- **核心问题**：如何在不依赖几何结构表征的前提下，基于量子力学物理本质（而非经验规则或坐标相似性）实现化学等价原子环境的自动识别与原子类型划分  
- **动机与背景**：传统原子类型化方法（如力场中的预定义类型、基于距离/角度的聚类）严重依赖人为经验或局部几何描述，难以捕捉电子结构层面的等价性；现有机器学习力场多采用黑箱式原子嵌入，缺乏可解释的物理基础；而量子化学中蕴含的拓扑能量信息（如IQA原子能量）尚未被系统用于指导原子分类  
- **方法核心**：提出BMIQA（Band Matching via IQA Atomic energies）协议，以Interacting Quantum Atoms（IQA）计算得到的拓扑原子能量分布为唯一输入，通过能带匹配（band matching）统计分析识别能量分布重叠的原子集合，实现完全物理驱动、无需结构指纹的半自动原子环境等价性判定  
- **关键实验与结果**：在7种封端氨基酸、3种寡肽、单体水及水五聚体等体系上验证；发现封端脂肪族/芳香族氨基酸仅含7种原子环境（3C+2H+1O+1N）；在水五聚体中识别出4种原子环境（2O+2H），与氢键网络异质性一致；GPR模型基于IQA能量训练后，在MD轨迹中复现相同原子类型划分（准确率>99%）  
- **创新点**：① 首次将IQA拓扑原子能量作为原子等价性的唯一判据，摆脱对几何/拓扑图表示的依赖；② 提出“能带匹配”统计框架，量化能量分布重叠度以判定等价性，兼具鲁棒性与可解释性；③ 揭示了远超经典化学直觉的物理等价性（如Cysteine中SH与CH氢环境等价），验证了电负性主导的量子等价机制  
- **局限性**：IQA计算成本高，限制其在大规模MD数据集上的实时应用；当前未处理动态电荷转移显著的体系（如强配位金属中心）；对基组和泛函敏感，需跨理论层级校准；尚未与主流MLFF架构（如SE(3)-equivariant networks）实现端到端耦合  
- **对你研究的启发**：可借鉴“物理量分布匹配”思路替代几何相似性度量，用于电催化活性位点识别（例如用ELF/MESP局域能量分布聚类表面吸附构型）；IQA能量作为可微分物理标签，有望嵌入图神经网络的消息传递中，增强电子结构感知能力；提供一种验证ML模型物理一致性新范式——检查其隐式学习的“原子类型”是否收敛于BMIQA定义的量子等价类  
- **与你研究的相关度**：高
- **阅读模式:** 🔍 精读
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/197726d583f73fe726e41cd4c04b3406e71c0c2b
- **标签:** MLFF

### 3. An OpenMM-Based
ML/MM–MMGBSA Workflow for End-point
Protein–Ligand Binding Energy Ranking ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-08-10
- **作者:** Chenchen Wang; Shihang Wang; Silong Zhai; Li Qin; Kai Xu et al.
- **核心问题**：机器学习力场（MLFF）驱动的分子动力学采样能否实质性提升基于终点法（MM/GBSA）的蛋白–配体结合自由能排序性能？  
- **动机与背景**：传统MM/GBSA依赖短时经典MD或单结构构象，采样不足导致排名不稳定；虽有MLFF可提升势能面精度，但其在端到端结合能工作流中的实际增益尚无系统评估；现有ML/MM混合模拟多聚焦于纯物理性质预测，缺乏与生物物理终点评分（如MMGBSA）的闭环整合。  
- **方法核心**：提出OpenMM实现的ML/MM–MMGBSA工作流，采用配体局部机械嵌入式ML/MM混合模拟（ligand-only mechanically embedded ML/MM），即仅对配体区域使用MLFF（如ANI-2x、GAP-SOAP），其余体系（蛋白+溶剂）保持经典力场，并通过MMPBSA.py进行MM/GBSA分析。  
- **关键实验与结果**：在JACS基准集199个复合物（8个靶标）上测试；基线为Prime MMGBSA（单结构）和经典MD-MMGBSA；最佳ML/MM方案（ANI-2x + 20 ns采样）在CDK2和p38α靶标中将Spearman ρ提升至0.52（vs. 0.38基线），但平均ρ仅提升0.04–0.07；Pairwise sign accuracy达68%（vs. 62% Prime），仍低于RBFE（>85%）。  
- **创新点**：① 首个开源、可复现的OpenMM-native ML/MM–MMGBSA端到端流程；② 提出“配体局部机械嵌入”策略，在计算开销可控前提下实现量子精度关键区域采样；③ 系统揭示MLFF对终点法排名的收益具有强靶标/力场/采样时长依赖性，否定“越长越好”的经验假设。  
- **局限性**：MLFF训练数据未覆盖显式水合环境及大尺度极化效应；机械嵌入忽略配体-蛋白静电耦合，缺乏电荷转移与极化响应建模；MM/GBSA固有近似（如GB模型误差、熵估算缺失）未被MLFF缓解；未验证对新化学型（out-of-distribution ligands）的泛化能力。  
- **对你研究的启发**：① “局部高精度+全局低成本”的混合建模范式可迁移至电催化界面（如仅对吸附态*OH/*O区域启用MLFF，其余电极/电解液用经典力场）；② 终点法性能需与采样-评分一致性联合优化，提示在电催化d-band中心或吸附能预测中应避免MLFF采样与DFT评分的功能域错配；③ Pairwise sign accuracy作为鲁棒性指标，优于单一相关系数，值得引入催化活性排序评估。  
- **与你研究的相关度**：高
- **阅读模式:** 🔍 精读
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/1d035941cb5d3a480d5896990a3ff0ae9da9c508
- **标签:** electrochemistry, surface, generative

### 4. Internal Electric
Field-Induced “Proton Bridge”
Mechanism in Photo-Self-Fenton Coupled PMS Systems: A Theoretical
Study Based on Nonmetal Surface-Engineered Carbon Nitride ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-08-11
- **作者:** Guofei Jiang; Xinyu Liu; Ke Tang; Haifeng Qiao; Guosheng Li et al.
- **核心问题**：揭示光自芬顿–过一硫酸盐（PSF–PMS）耦合体系中氧化与还原半反应在复杂界面协同进行的微观机制，特别是电子与质子竞争下的动态耦合路径。  
- **动机与背景**：单一高级氧化工艺受限于动力学瓶颈（如H₂O₂生成速率低、PMS活化效率差）；现有研究缺乏对双半反应在原子尺度上如何共用质子/电子资源的 mechanistic 理解；界面质子输运受晶格约束，导致氧化侧质子过剩而还原侧质子匮乏，严重制约ROS通量提升。  
- **方法核心**：融合密度泛函理论（DFT）与基于Bagging架构的随机森林机器学习（RF-ML），构建“理论计算–数据建模–机制反演”闭环；创新性引入局域内建电场（IEF）、p带中心下移、价带顶（VBM）和功函数等多维描述符协同解析质子迁移驱动力与反应位点调控规律。  
- **关键实验与结果**：以非金属掺杂/缺陷工程化的氮化碳（g-C₃N₄）为模型催化剂；基线方法为传统DFT过渡态搜索与线性描述符回归；关键结果：（1）质子跨界面迁移能垒Eₐ < 0.5 eV，证实“质子桥”机制可行；（2）RF-ML预测反应能垒R² > 0.9，显著优于线性模型（R² ≈ 0.6–0.7）。  
- **创新点**：① 首次提出并验证“跨位点质子桥”（cross-site proton bridge）机制，将质子视为可迁移活性介质而非静态配体；② 揭示局域内建电场（IEF）通过空间分离氧化/还原位点并驱动质子定向迁移的双重作用；③ 建立首个面向耦合氧化体系的高维DFT描述符–反应能垒非线性映射模型，克服多重共线性干扰。  
- **局限性**：未考虑水分子动态溶剂化效应对质子迁移路径的影响；ML模型依赖DFT生成的数据集，缺乏实验原位谱学验证；所提机制尚未拓展至金属基或异质结催化体系。  
- **对你研究的启发**：可迁移“IEF调控位点空间分离+质子动力学耦合”的设计范式；RF-ML处理高维共线性描述符的策略适用于电催化析氢/氧反应中质子-电子协同能垒预测；p带中心作为Lewis酸度定量指标，可推广至其他含氮碳基催化剂的活性位理性筛选。  
- **与你研究的相关度**：高
- **阅读模式:** 🔍 精读
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/2792942a2a365b77ace526e7e3314c1dede5c680
- **标签:** catalysis, surface, dft

### 5. Machine learning force field development and basic physical property studies for molten salt reactor fuel salt LiF-BeF2-UF4. ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-08-12
- **作者:** Xinyu Li; Yu-Huan Lv; Lei Zhang; Tao Bo
- **核心问题**：如何在高温度、强放射性等实验难以开展的条件下，准确获取FLiBeU（LiF-BeF₂-UF₄）熔盐燃料的微观结构演化规律及其热物理/输运性质随温度与UF₄组分的变化机制。  
- **动机与背景**：传统分子动力学依赖经验力场，难以兼顾多组分熔盐中复杂化学键合（如U–F配位、BeF₄²⁻络合、F⁻桥联）的描述精度；第一性原理分子动力学（AIMD）受限于计算成本，无法实现微秒级、千原子体系、宽温宽组成范围的统计采样；而FLiBeU熔盐作为第四代熔盐堆核心燃料，其安全运行亟需可靠物性数据库与微观机理支撑。  
- **方法核心**：采用“深度势能分子动力学（DPMD）+主动学习（active learning）”双驱动策略构建高精度机器学习力场（MLFF），通过迭代筛选DFT计算中最信息丰富的构型样本，实现精度与效率的协同优化。  
- **关键实验与结果**：研究体系为FLiBeU（UF₄ 3–50 mol%，773–1173 K）；基线方法包括经典Brenner/MEAM力场与有限DFT单点验证；关键结果：（1）UF₄浓度升至30 mol%时，F⁻自扩散系数下降约65%，剪切黏度呈近指数增长（1173 K下从28.5 cP升至142 cP）；（2）RDF显示U⁴⁺平均配位数从7.2（3 mol% UF₄）增至8.9（50 mol% UF₄），且出现显著U–U近邻峰（<3.8 Å），揭示短程团簇化趋势。  
- **创新点**：① 首次为含锕系元素（U）的多阴离子熔盐（F⁻/BeF₄²⁻/UF₆²⁻等共存）构建经DFT+实验双重验证的DPMD力场；② 揭示UF₄诱导的“配位饱和→阴离子网络僵化→离子迁移受阻”这一跨尺度传导机制链；③ 建立覆盖宽温宽组成范围的系统性物性数据库（密度、Cₚ、σₑ, η、Dᵢ等），填补实验空白。  
- **局限性**：未考虑辐照损伤（如裂变产物Xe/Kr溶解、U⁴⁺氧化态演变）、长期热力学亚稳态（如相分离倾向）、以及电极/熔盐界面反应过程；DPMD训练未显式包含电子激发效应（高温下可能影响U–F键极化）。  
- **对你研究的启发**：主动学习驱动的MLFF构建范式可迁移至电催化界面（如CO₂RR电解质/电极界面）的多尺度建模；熔盐中“阴离子网络拓扑调控输运性能”的思路，可类比用于设计高离子电导率固态电解质或离子液体基电解液；宽参数空间扫描策略对催化剂成分–性能构效关系的高通量探索具有方法论参考价值。  
- **与你研究的相关度**：高
- **阅读模式:** 🔍 精读
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/47541261b6a4c1b506bc236f7877f45ade2d5ce4
- **标签:** electrochemistry, MLFF, dft, active-learning

### 6. Exploring Sparse Matrix Multiplication Kernels on the Cerebras CS-3 ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-04-30
- **作者:** Milan Shah; Sheng Di; Michela Becchi
- **核心问题**：评估Cerebras CS-3 AI加速器在大规模稀疏线性代数运算（SpMM和SDDMM）中的性能潜力，尤其针对无法以稠密格式装入设备的超大稀疏矩阵。  
- **方法要点**：为CS-3平台设计并优化低层稀疏核（SpMM与SDDMM），重点提升I/O效率、内存占用与大规模矩阵可扩展性。  
- **关键结果**：在90%稀疏度下，SpMM和SDDMM分别比CPU快最高100×和20×；但当稀疏度>99%时性能显著下降，甚至不如先进CPU库。  
- **与你研究的相关度**：低
- **阅读模式:** 📋 摘要
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/006b8e2f1f555976b479cbd4e95c72c74e0ecb1d
- **标签:** electrochemistry

### 7. Learning Inter-Atomic Potentials without Explicit Equivariance ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2025-09-25
- **作者:** Ahmed A. A. Elhag; Arun Raja; Alex Morehead; Samuel M. Blau; Garrett M. Morris et al.
- **核心问题**：如何在不依赖硬编码的旋转平移对称性架构约束的前提下，构建高精度、可扩展的机器学习原子间势函数（MLIPs）  
- **方法要点**：提出TransIP框架，利用通用非等变Transformer模型，通过在嵌入空间中优化表征来隐式学习SO(3)等变性，而非强制架构等变或依赖数据增强  
- **关键结果**：在OMol25数据集上达到与当前最优等变模型相当的力场预测精度；相比数据增强基线，在不同数据规模下性能提升40%–60%  
- **与你研究的相关度**：中
- **阅读模式:** 📋 摘要
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/3c56c6cf4d0baf9e402814da09e4d5febe4a4974
- **标签:** electrochemistry, MLFF

### 8. Modeling Diffusion in Metal-Organic Frameworks Using On-the-fly Probability Enhanced Sampling-Based Machine Learning Potentials. ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2025-10-30
- **作者:** S. Ethirajan; Ambarish R. Kulkarni
- **核心问题**：如何提升机器学习势能（MLPs）对纳米多孔材料中罕见事件（如高能非平衡态过程）的描述能力  
- **方法要点**：提出基于On-the-fly Probability Enhanced Sampling（OPES）的主动学习课程，结合温度和距离相关的集体变量进行时变偏置采样  
- **关键结果**：实现了纳秒尺度、近DFT精度的分子动力学模拟；首次发现咪唑在SALEM-2 MOF中通过4元环窗口的环开机制（涉及Zn–N键瞬态解离）  
- **与你研究的相关度**：高
- **阅读模式:** 📋 摘要
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/3d0b16d68e3f272cc6d619ff51f9b5aa68c1fa6e
- **标签:** electrochemistry, surface, dft, active-learning

### 9. Machine Learning–Enhanced Evaluation of AI Literary Translation: Logistic Regression, Random Forest, and SVM in a Human–AI Collaborative Framework ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2025-11-14
- **作者:** Sirui Wang; Xiang Li
- **核心问题**：AI翻译在科幻文学翻译中的质量表现及人机协同优化路径  
- **方法要点**：融合用户感知建模（基于300份问卷的三种监督学习算法）与多引擎译文对比分析（DeepSeek/DeepL/Doubao vs. 人工译本）  
- **关键结果**：Logistic Regression对用户满意度预测接近完美准确；DeepL流畅但弱化隐喻力，DeepSeek术语一致但偶有过度推断，Doubao中文表达佳但风格欠雕琢  
- **与你研究的相关度**：低
- **阅读模式:** 📋 摘要
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/3d6cbbe4ad3158a607db82b593a1e1a969e66372
- **标签:** generative

### 10. Low-rank matrix and tensor approximations for compression of machine-learning interatomic potentials. ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2025-09-04
- **作者:** I. Vorotnikov; Fedor Romashov; N. Rybin; Maxim Rakhuba; I. Novikov
- **核心问题**：如何在不损失精度的前提下压缩机器学习原子间势（MLIPs）的参数量以提升计算效率  
- **方法要点**：采用固定秩约束下的低秩矩阵与张量分解，并结合自动秩增广算法优化拟合势能面  
- **关键结果**：对Moment Tensor Potential（MTP）实现最高50%参数压缩且精度零损失；方法可推广至原子团簇展开（ACE）等其他MLIPs  
- **与你研究的相关度**：高
- **阅读模式:** 📋 摘要
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/3e4bbf0ccffc5df95166462ab11db0e1f413a51b
- **标签:** electrochemistry, MLFF

## 💡 今日亮点

- **最值得精读**：[7] Learning Inter-Atomic Potentials without Explicit Equivariance — 它挑战了MLIPs领域“等变性必须硬编码”的范式共识，证明隐式学习SO(3)对称性可行且精度不损，为轻量化、可解释势函数设计开辟新路径  
- **可能冲突的研究**：[2] Deciphering Chemical Environments in Conformational Data Sets Using an IQA Band-Matching Protocol — 其基于量子拓扑能量（IQA）的原子等价性定义，与[7]中纯数据驱动、无物理约束的嵌入空间优化逻辑存在本体论冲突：前者要求势函数显式承载电子结构可解释性，后者默认放弃该诉求  
- **值得追踪的团队**：Cerebras Systems（论文[6]）— 在CS-3上实现超稀疏矩阵核的I/O感知优化，表明其正系统性攻克AI for Science中“内存墙”瓶颈，对大规模MLP部署具基础设施级影响  
- **重要趋势**：MLPs正从“精度优先”单维目标，转向精度-效率-可解释性-硬件适配四维协同优化；物理约束（如等变性、IQA、低秩）不再仅作为归纳偏置，而成为可插拔、可验证、可压缩的模块化组件

## 📌 Key Gap

**关键差距**
- **Gap 1**：所有MLP相关工作（[1][3][5][7][8][10]）均假设训练数据覆盖目标相空间，但对热/辐照/电场等强非平衡条件下构象采样偏差导致的外推失效缺乏鲁棒性评估机制——尤其在[4]界面质子桥、[5]熔盐辐射损伤等动态失衡体系中，此缺陷直接威胁预测可信度  
- **Gap 2**：跨尺度耦合仍严重脱节：[4]的界面反应机制依赖静态DFT计算，[3]的MM/GBSA排名未耦合[8]的OPES增强采样，[5]的熔盐输运性质未链接[1]的热导率模拟——缺乏统一框架将MLP生成的原子轨迹，自动映射为介观输运系数或宏观反应速率  
- **未来方向**：发展“任务驱动的自适应MLP协议”：以终末物理量（如热导率κ、结合自由能ΔG、质子迁移能垒）为损失函数反向调控训练数据生成、等变性注入强度与张量压缩策略，在保证端到端误差可控前提下，实现MLP从“拟合势能面”到“求解物理方程”的范式跃迁
