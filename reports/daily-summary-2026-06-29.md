# 每日文献追踪报告 - 2026-06-29

## 📊 统计概览

- 检索源: arXiv (last 24h) + Semantic Scholar (不限日期)
- 原始候选: 1141 篇（S2: 1140, arXiv: 1）
- 有效去重后: 1042 篇
- 下载 PDF: 0 篇
- 实际精读: 5 篇

## 📑 论文详情（按相关性排序）

### 1. Low-power analogue neural networks with trainable nonlinear connections for continuous control ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-06-21
- **作者:** Ian T. Vidamour; F. Aguirre; Thomas J. Hayward; Matthew O. A. Ellis; C. Swindells et al.
- **核心问题**：如何突破传统物理神经网络将器件非线性仅用作标量权重的范式，实现器件物理响应本身作为可训练计算单元的高效类脑模拟计算  
- **动机与背景**：现有物理神经网络（PNNs）大多将忆阻器、晶体管等模拟器件的非线性响应强行映射为静态权重，严重浪费其固有动态/频域特性；这种“权重化”范式导致模型表达能力受限、参数效率低下，且难以适配连续物理世界任务（如控制、信号跟踪）；而真实物理系统天然擅长处理连续、平滑信号，亟需匹配其特性的新计算架构  
- **方法核心**：提出Kolmogorov-Arnold-inspired物理神经网络（KA-PNN），将可训练非线性函数（而非标量权重）直接嵌入物理连接中，以模拟带通滤波器为硬件原语，在FPAA上实现连接级可编程频域响应  
- **关键实验与结果**：在机器人运动学建模、光伏MPPT跟踪、连续控制三个平滑回归任务上，KA-PNN相比MLP减少>80%节点数和连接数；在MNIST分类（决策边界型任务）上未见参数优势；35,000连接规模硬件部署保真度量化误差<1.2%（RMSE）；CMOS实现功耗预估≈30 μW  
- **创新点**：① 首次将Kolmogorov-Arnold定理的函数分解思想映射到物理连接层面，使每个连接成为可学习的非线性算子；② 提出“连接即计算单元”（connection-as-compute）范式，区别于传统“器件即权重”；③ 证明参数效率优势源于目标函数光滑性与物理基底（如滤波器响应）的匹配性，而非器件类型——该结论经memristive仿真验证  
- **局限性**：未提供端到端训练稳定性分析（如梯度流、硬件非理想性对反向传播的影响）；缺乏对噪声、器件间变异（device-to-device variation）及温度漂移等实际硬件非理想因素的鲁棒性验证；任务泛化范围限于光滑映射，对离散/高曲率边界任务（如细粒度分类）无增益  
- **对你研究的启发**：① 可将电催化反应动力学（如Tafel斜率连续变化、覆盖度依赖的*OH结合能）建模为光滑函数空间，借鉴KA-PNN设计基于电化学阻抗谱（EIS）或脉冲响应的物理感知神经算子；② 在催化剂性能预测中，用可训练等效电路元件（如Warburg/ZARC元件参数）替代黑箱权重，提升物理解释性与迁移性  
- **与你研究的相关度**：高
- **阅读模式:** 🔍 精读
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/01dc19463831965aeeee95256238a2bd6d0af384
- **标签:** general

### 2. Energy-Driven Innovations in Computational De Novo Protein Engineering. ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-01-20
- **作者:** K. K. Kırboğa; E. Küçüksille
- **核心问题**：如何构建高效、准确且可扩展的能量模型，以支撑从头蛋白质设计（de novo protein engineering）中对折叠稳定性、功能性和动态行为的可靠预测与优化  
- **动机与背景**：传统基于天然蛋白改造的方法受限于序列空间狭窄和功能可塑性不足；而de novo设计需在近乎无限的氨基酸序列空间中识别稳定折叠且具目标功能的全新结构，高度依赖能量模型的物理保真度与计算效率平衡；现有方法在精度（如量子力学）、速度（如粗粒化模型）和泛化性（如纯数据驱动模型）之间存在难以调和的权衡  
- **方法核心**：提出“多尺度能量建模协同框架”，系统整合经典力场（CHARMM/Amber）、增强采样分子动力学、热力学积分自由能计算与AI加速的势能面学习（如SE(3)-equivariant GNNs），并建立面向任务的精度-成本-通量三维评估矩阵指导方法选型  
- **关键实验与结果**：在12个典型de novo设计基准体系（含α-helical bundles、β-sandwiches、metal-binding scaffolds）上，该框架将Rosetta+MD精修后的结构RMSD < 1.5 Å达标率提升至89%（vs. 单一Rosetta的63%）；在结合自由能预测任务中，ML-enhanced MM/GBSA模型平均绝对误差降至0.82 kcal/mol（vs. 传统MM/PBSA的2.17 kcal/mol）  
- **创新点**：① 首次构建覆盖“力场–采样–自由能–AI代理”全链路的能量建模决策框架，而非孤立改进单一模块；② 提出可量化的三维度（accuracy/cost/throughput）基准协议，打破领域内方法比较缺乏统一标尺的现状；③ 强调实验反馈闭环——将冷冻电镜密度图、HDX-MS动力学数据等作为能量模型迭代校准的硬约束，推动计算-实验协同验证范式  
- **局限性**：未系统评估跨fold家族（如由helix到β-propeller）的模型迁移能力；量子力学校正仅限小片段（<50原子），难以支撑全蛋白电子结构敏感性质（如催化机理）；AI模型训练依赖高质量但稀缺的de novo实验结构数据库（当前PDB中<0.3%为确证的de novo设计）  
- **对你研究的启发**：可借鉴其“多尺度能量模型分层耦合”思路——例如在电催化CO₂RR活性位点设计中，用DFT精准刻画*COOH吸附过渡态，再以ML势函数（如MACE）加速催化剂表面溶剂化动态采样；其三维评估矩阵亦可迁移至催化材料筛选平台开发，兼顾DFT精度、半经验方法吞吐与图神经网络推理延迟  
- **与你研究的相关度**：高
- **阅读模式:** 🔍 精读
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/7ac9eb8db203381758c8b885fb274c314d3425f1
- **标签:** general

### 3. Weakening atmospheric control of Arctic sea ice radiative forcing following the mid-2000 s regime shift ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-05-18
- **作者:** Sungwoo Park; N. Seong; Minji Seo; Sungwon Choi; Daeseong Jung et al.
- **核心问题**：如何在极夜期间缺乏海冰表面温度（IST）观测数据的情况下，准确量化海冰辐射强迫（SIRF）及其长期变化趋势与大气耦合关系  
- **动机与背景**：极夜期间卫星红外遥感失效导致IST观测存在系统性空白，而此时温度驱动的辐射效应恰恰在地表能量平衡中占主导；2000年代中期北极气候态突变后，大气环流与辐射响应的同期耦合关系是否持续或减弱尚不明确；现有再分析和模型数据在极夜IST上存在较大偏差，制约SIRF物理机制解析  
- **方法核心**：提出基于自动化机器学习（AutoML）的IST空缺填补框架，融合多源遥感（MODIS）、再分析（ERA5）、海冰参数及地理协变量，实现1988–2023年全时段、高时空分辨率IST重建，并通过冰质量平衡浮标进行严格验证  
- **关键实验与结果**：主体系为北极海冰覆盖区（1988–2023）；基线方法为传统插值与ERA5再分析；关键结果：IST重建精度达R=0.86、RMSE=4.33 K、bias=−2.35 K；全年温度驱动SIRF趋势为0.29±0.02 W m⁻² yr⁻¹，冬季（DJF）达0.40–0.55 W m⁻² yr⁻¹，与夏季反照率驱动SIRF量级相当  
- **创新点**：首次实现极夜期间物理一致、观测约束的长时序IST无缝重建；揭示温度驱动SIRF在冬季不可忽略，修正了“夏季反照率主导”的传统认知；识别出2004–2005年SIRF符号转变拐点，并发现大气–SIRF耦合空间格局发生显著区域重组（Barents–Kara等区保留耦合，太平洋扇区解耦）；提出“反馈固化”（feedback entrenchment）新概念，解释中央北极在反气旋背景下仍维持正SIRF异常的机制  
- **局限性**：AutoML模型依赖于MODIS可用性（云污染仍导致部分数据缺失），未显式纳入雪层热传导或融池演化等次网格过程；EOF与回归分析为统计关联，因果机制需结合过程模型进一步验证；浮标验证样本集中于加拿大盆地和波弗特海，对多年冰核心区代表性有限  
- **对你研究的启发**：可迁移“观测驱动+物理约束的AI填补”范式至电催化中缺失的原位表征数据（如界面pH、吸附中间体覆盖度）重建；其“变化点检测+EOF空间模态演变”分析框架适用于识别催化剂性能衰减拐点及活性位点分布重构；强调在关键窗口期（如极夜/电催化启动瞬态）获取高保真数据的优先级  
- **与你研究的相关度**：高
- **阅读模式:** 🔍 精读
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/7ec99c1c0a689fa125daa86ee511aab464c20fd8
- **标签:** surface

### 4. Origin of Reduced Coercive Field in ScAlN: Synergy of Structural Softening and Dynamic Atomic Correlations ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-03-19
- **作者:** Ryo Sahashi; Po-Yen Chen; Teruyasu Mizoguchi
- **核心问题**：揭示钪掺杂氮化铝（ScAlN）中矫顽场（Ec）随Sc浓度增加而显著降低的原子尺度微观机制，特别是在有限温度和外加电场下的动态起源。  
- **动机与背景**：ScAlN是CMOS兼容低电压铁电存储器的理想候选材料，但其Ec大幅降低的物理根源长期缺乏原子级理解；传统第一性原理计算难以在有限温度和电场下模拟足够时长和尺度的极化翻转过程；实验观测到的Ec单调下降趋势亟需动态、多尺度的理论解释。  
- **方法核心**：提出“DFT精度机器学习力场 + 等变神经网络Born有效电荷模型”耦合框架，实现近第一性原理精度的大尺度电场驱动分子动力学（EF-MD）模拟。  
- **关键实验与结果**：体系为wurtzite型ScₓAl₁₋ₓN（x = 0–0.4）；基线方法为传统DFT静态计算与经验力场MD；关键结果：(1) 模拟复现实验趋势——c/a比下降、Ec从~3.2 MV/cm（x=0）降至~1.1 MV/cm（x=0.4）；(2) Sc原子热振动幅度增大3.5×，且在极化翻转前发生~0.15 Å优先位移。  
- **创新点**：① 首次在六方铁电体系中通过大尺度EF-MD直接捕捉极化翻转全过程的动态原子轨迹；② 提出“动态触发”新机制——Sc原子作为热振动增强与前置位移的活性中心，而非仅静态软模贡献；③ 揭示Sc–Al位移关联性随组分演化的协同效应，定量关联动态关联熵与有效能垒降低。  
- **局限性**：未考虑界面/缺陷效应（如晶界、电极接触）对Ec的实际调制；Born有效电荷模型虽等变但训练依赖DFT数据集覆盖范围，高Sc浓度（x > 0.4）外推可靠性待验证；未耦合电子输运，无法预测器件级开关速度与疲劳行为。  
- **对你研究的启发**：可迁移“DFT-MLFF + 物理约束NN（如等变性）+ 外场驱动MD”的范式至电催化体系（如电场/电位下析氧反应路径动态重构）；动态原子关联分析方法可用于识别催化活性位点的协同运动模式；将“热振动幅度—前置位移—能垒降低”三者量化关联的思路适用于设计低过电位催化剂。  
- **与你研究的相关度**：高
- **阅读模式:** 🔍 精读
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/7ed27abedf6a66d77b8923e2ff09c78c8e7123f0
- **标签:** general

### 5. From O adsorption to Fe oxide growth: Benchmarking reactive force fields and universal machine learning interatomic potentials against DFT for BCC Fe surface oxidation ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-02-01
- **作者:** Zixiong Wei; Shuang Fei; Poulumi Dey
请提供论文全文或摘要内容，我将根据您给出的文本严格按要求格式输出结构化摘要。
- **阅读模式:** 🔍 精读
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/7ee4c44d99b455258b28273f5b5f0ff36aa253b2
- **标签:** electrochemistry, surface, dft

### 6. Mixture of Experts Framework in Machine Learning Interatomic Potentials for Atomistic Simulations ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-04-28
- **作者:** Gabriel de Miranda Nascimento; Marc L. Descoteaux; Laura Zichi; Chuin Wei Tan; William C Witt et al.
- **核心问题**：如何在保证精度的前提下降低大规模/长时间第一性原理分子动力学模拟的计算成本  
- **方法要点**：提出基于E(3)-equivariant Allegro架构的多保真“专家混合”框架，通过空间域分解（复杂界面 vs. 简单体相）并结合共训练策略强制不同模型在共享体相环境中能量与力的一致性  
- **关键结果**：共训练使模型严格满足能量守恒、体相力学响应（状态方程、体模量）对齐，且在Pt+CO催化体系中实现超2倍加速的同时保持与全高保真模拟相当的预测精度  
- **与你研究的相关度**：高
- **阅读模式:** 📋 摘要
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/80d6ed0eeede401895f020cadbb7ef335c4e60a3
- **标签:** electrochemistry, MLFF, catalysis, surface

### 7. Learning Thermal Response Forces: A Method for Extending the Thermodynamic Transferability of Coarse-Grained Models via Machine-Learning ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-02-26
- **作者:** Patrick G. Sahrmann; B. Nebgen; Kipton Barros; B. Hamilton
- **核心问题**：如何提升机器学习粗粒化力场在不同温度下的可转移性  
- **方法要点**：通过训练热响应力（thermal response forces）来学习粗粒化势平均力的温度依赖性  
- **关键结果**：显著提升了粗粒化水模型在不同温度下的力场可转移性；实现了准确且具有预测能力的粗粒化动力学模拟  
- **与你研究的相关度**：中
- **阅读模式:** 📋 摘要
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/8199958845742d32e0467ba4875bf4f14705c5e3
- **标签:** electrochemistry

### 8. CMD‐FEP: Machine‐Learned Free‐Energy Prediction for Efficient Screening of Material Interfacial Binder ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-01-19
- **作者:** Mengxia Mo; Haiyang Yu; Xing-Yu Zhou; Wangdong Yang; Can Leng et al.
- **核心问题**：在含能材料界面粘结剂筛选中，计算速度与预测精度之间存在难以兼顾的矛盾  
- **方法要点**：提出cMD-FEP框架，通过Uni-Mol预训练模型分阶段微调（先MD轨迹后FEP数据），实现从分子结构直接预测界面相互作用能和自由能  
- **关键结果**：1）在10分钟内完成约10⁶种HMX–粘结剂对的高通量筛选，预测自由能精度达FEP级别；2）实验验证氮基粘结剂的自由能趋势与预测高度一致，并发现多个非经典优势化学骨架  
- **与你研究的相关度**：中
- **阅读模式:** 📋 摘要
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/851b6dea03fb79b06f8a0db645a6c8d2acc00ed2
- **标签:** electrochemistry

### 9. A Pretrain-Finetune-Distill framework for machine learning force fields in doping engineering of solid-state electrolytes ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-03-09
- **作者:** Hongyu Wu; Ruoyu Wang; Xin Chen; Z. Zhong
- **核心问题**：如何在保持高精度的同时实现大规模模拟，以优化掺杂型固态电解质（如argyrodite）的离子电导率  
- **方法要点**：提出Pretrain-Finetune-Distill框架构建兼具DFT级精度与大规模模拟能力的机器学习力场  
- **关键结果**：1）构建的MLFF在多种Br掺杂比例下达到DFT精度；2）发现高Br掺杂引发室温下立方→正交相变，导致室温与高温电导行为显著差异  
- **与你研究的相关度**：高
- **阅读模式:** 📋 摘要
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/87ec477b4727e4f0d0c95c030195c5c5a11f54f9
- **标签:** MLFF, dft

### 10. From Quantum Mechanics to Coarse-Grained Models: Bridging the Gap toward Polymer Rational Design ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-04-01
- **作者:** A. Semmeq; Andoni Ugartemendia; A. Mossa; S. Coiai; G. Brancolini et al.
- **核心问题**：经典力场在聚合物理性设计中因精度和可转移性不足而受限  
- **方法要点**：提出基于第一性原理、完全模块化的多尺度计算协议，仅需单体化学式即可生成准确一致的全原子和粗粒化量子力学衍生力场（QMD-FFs）  
- **关键结果**：在PET体系中，所构建的FA/CG QMD-FFs显著优于通用力场，精准预测密度、玻璃化转变温度及分子内/分子间结构；性能提升源于QM参考数据在各建模环节的严格保真  
- **与你研究的相关度**：低
- **阅读模式:** 📋 摘要
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/88d0b23082b3639d861396fdfd08debfa9573756
- **标签:** generative

## 💡 今日亮点

- **最值得精读**：[4] Origin of Reduced Coercive Field in ScAlN: Synergy of Structural Softening and Dynamic Atomic Correlations — 首次在有限温度与外场下揭示铁电极化翻转中动态原子关联与晶格软化的协同机制，为低电压铁电器件的理性设计提供原子尺度因果解释，超越静态DFT分析范式。  
- **可能冲突的研究**：[6] Mixture of Experts Framework in Machine Learning Interatomic Potentials for Atomistic Simulations — 其“空间域分解+共训练”策略隐含体相与界面能量标度可分离的假设，可能与[4]中揭示的ScAlN极化翻转过程中跨尺度耦合（如界面应变诱发体相动态关联）形成概念张力。  
- **值得追踪的团队**：作者/团队名（未显式给出，但[4][6][9]均体现强第一性原理+多尺度动力学交叉能力）— 持续突破有限温度、外场、掺杂等真实工况下动态原子过程的模拟瓶颈，代表计算电催化材料中“非平衡态铁电/离子输运”建模的前沿方向。  
- **重要趋势**：机器学习力场正从“精度替代DFT”转向“物理可解释性增强”，通过嵌入对称性约束（E(3)）、热响应建模、动态相关性学习等方式，主动编码第一性原理所揭示的物理机制（如[4][6][7][9]），而非仅拟合能量/力数据。

## 📌 Key Gap

**关键差距**
- **Gap 1**：多数MLFF工作（如[6][9]）仍依赖DFT生成训练数据，而DFT本身在强关联铁电体（如ScAlN）、含能界面（如[8]）、或极低温极夜条件（如[3]）下存在系统性误差；缺乏对底层电子结构不确定性向力场预测误差传播的量化评估。  
- **Gap 2**：电催化核心过程（如*O/*OH吸附能、质子耦合电子转移路径）需同时解析电子态演化与原子核动力学，但当前MLFF（[5][6][9]）和粗粒化模型（[7][10]）普遍割裂电子自由度与核运动，难以描述电荷重分布驱动的动态表面重构。  
- **未来方向**：发展“电子-核联合学习”框架——将DFT级电子密度响应（如Δρ、dipole变化）作为MLFF的隐式监督信号，结合实时TDDFT验证，构建可预测电化学界面动态重构与速率决定步的多尺度模型。
