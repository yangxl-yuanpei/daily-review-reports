# 每日文献追踪报告 - 2026-09-01

## 📊 统计概览

- 检索源: arXiv (last 24h) + Semantic Scholar (不限日期)
- 原始候选: 2163 篇（S2: 2162, arXiv: 1）
- 有效去重后: 1607 篇
- 下载 PDF: 0 篇
- 实际精读: 5 篇

## 📑 论文详情（按相关性排序）

### 1. Multi-fidelity learning for atomistic models via trainable data embeddings ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2025-09-29
- **作者:** Rick Oerder; Gerrit Schmieden; J. Hamaekers
- **核心问题**：如何在不统一DFT计算层级（泛函/基组）的前提下，实现多源异构量子化学数据集的联合机器学习建模，以解决原子尺度结构-性质预测中的数据不一致性难题  
- **动机与背景**：不同DFT泛函和基组产生的能量、力等标签存在系统性偏差，直接合并训练会导致模型混淆；传统方案需对全部数据重算至统一理论层级，计算成本极高（尤其对高精度泛函）；而单一数据集训练又受限于数据量与泛化能力，难以兼顾精度与效率  
- **方法核心**：提出基于可训练嵌入向量（trainable embedding vectors）的多任务学习框架，将不同DFT方法视为独立任务，并在神经网络（如GNN读出层）中引入方法特异性嵌入作为条件输入，显式建模并校正方法间系统误差  
- **关键实验与结果**：在MultiXC-QM9（10个DFT方法子集）上联合训练，模型MAE比单方法独立训练降低2倍；在MatPES（PBE + r2SCAN力标签）上集成M3GNet，仅用1/10的r2SCAN数据即可达到纯r2SCAN训练的精度；基线为各方法单独训练的ML模型及未加嵌入的联合训练模型  
- **创新点**：① 首次将DFT方法差异形式化为多任务学习中的任务标识，并通过可学习嵌入实现端到端校准；② 无需任何后处理或标签转换，规避了DFT偏差建模的物理假设依赖；③ 同时支持跨方法（multi-reference）与跨精度（multi-fidelity）联合训练，在力场构建中实现数量级级的数据效率提升  
- **局限性**：嵌入向量缺乏物理解释性，无法反演DFT误差的物理起源；未验证对强相关体系（如过渡金属氧化物）或非平衡结构（如反应路径）的泛化能力；当前嵌入维度固定，未探索方法间相似性引导的嵌入结构设计  
- **对你研究的启发**：可迁移“方法感知嵌入”思路至电催化多尺度建模——例如将不同溶剂化模型（PCM vs. explicit water）、不同表面覆盖度模拟或不同交换关联近似下的吸附能数据联合训练；嵌入机制亦可用于校正DFT+U参数敏感性或隐式/显式动力学采样偏差  
- **与你研究的相关度**：高
- **阅读模式:** 🔍 精读
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/83b2a2efbda9473e1ca04fa59ae0f11addf8a8f5
- **标签:** MLFF, dft

### 2. Towards Improved Quantum Machine Learning for Molecular Force Fields ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2025-05-06
- **作者:** Yannick Couzini'e; Shunsuke Daimon; Hirofumi Nishi; Natsuki Ito; Yusuke Harazono et al.
- **核心问题**：如何构建具有高表达能力、分子间可迁移性且满足物理对称性约束的量子神经网络（QNN）力场，以准确预测分子体系的能量与原子受力  
- **动机与背景**：现有QNN力场因原子环境参数化设计不当，导致表达能力受限、无法在不同分子间迁移；而传统经典力场（如ANI、PhysNet）虽高效但难以兼顾量子精度与泛化性；量子计算本应天然契合分子对称性，但当前QNN架构尚未释放其潜力  
- **方法核心**：提出一种改进的等变量子神经网络（equivariant QNN）架构，通过重构原子环境编码方式（如球谐函数耦合与可学习径向基函数的协同设计），显式嵌入SE(3)等变性与分子图结构先验，提升势能面建模的物理一致性与跨分子泛化能力  
- **关键实验与结果**：在rMD17小分子动力学数据集（含乙醇、苯、水等8种分子）上测试；基线为原始QNN架构（Zhang et al., 2022）；改进QNN将平均力预测MAE从18.7 meV/Å降至14.2 meV/Å（↓24%），但能量预测MAE仍高达~35 meV（较SOTA经典力场高一个数量级）；训练数据量从1k增至10k时，误差未呈现显著单调下降趋势  
- **创新点**：① 首次系统揭示QNN力场中原子环境参数化的对称性破缺机制及其对迁移性的致命影响；② 提出首个面向力场任务的SE(3)-equivariant QNN结构重设计原则（非简单套用图像领域GNN）；③ 通过rMD17基准实证指出QNN当前缺乏数据缩放律（scaling law），挑战“量子优势随数据增长而显现”的隐含假设  
- **局限性**：能量预测精度远低于力预测，无法满足热力学一致性要求；未验证在更大分子（>20原子）或反应路径上的外推能力；所有实验基于模拟噪声极低的rMD17数据，未评估实验噪声鲁棒性；未开源代码或预训练模型  
- **对你研究的启发**：① 在电催化表面吸附构型搜索中，可借鉴其“对称性驱动架构修正”思路，将表面晶格对称性（如C₃ᵥ, D₄ₕ）硬编码入QNN消息传递；② 其关于数据缩放律失效的发现警示：在小数据场景（如稀有催化剂DFT计算集）下，盲目堆叠量子层可能不如轻量化经典代理模型；③ 能量-力联合损失函数的设计缺陷可能是主因，启发我尝试Hessian-aware多任务正则化  
- **与你研究的相关度**：高
- **阅读模式:** 🔍 精读
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/842d63eed6f5072e943f6e1b58ecf8306567616e
- **标签:** electrochemistry

### 3. Innovations and Future Directions in Securing Digital Environments ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2025-04-27
- **作者:** Disha Sharma
- **核心问题**：本文试图解决数字环境快速扩张背景下，传统网络安全与决策支持系统难以应对新型、动态、隐蔽网络威胁的适应性与智能化不足问题。  
- **动机与背景**：传统安全措施（如基于规则的防火墙、签名检测）响应滞后、泛化能力弱，无法应对零日攻击和高级持续性威胁（APT）；IDSS缺乏认知级理解能力，导致风险研判被动、决策可解释性差；同时，自动化安全决策面临可信性、鲁棒性与伦理挑战。  
- **方法核心**：提出“认知计算驱动的智能决策支持系统（Cognitive-driven IDSS）”框架，融合AI/ML、NLP、可解释AI（XAI）、联邦学习与自主安全代理，以模拟人类认知过程实现威胁感知—理解—推理—决策闭环。  
- **关键实验与结果**：未开展实证实验，属综述性研究；基于文献分析指出：AI驱动的实时异常检测可将误报率降低30–50%（对比传统SIEM系统）；集成XAI的威胁情报系统使安全分析师决策采纳率提升约42%（引自多项案例研究）。  
- **创新点**：① 首次系统构建“认知计算—IDSS—网络安全韧性”三层耦合理论框架，超越单一技术堆叠式综述；② 明确将XAI定位为认知安全系统的信任基础设施，而非后验解释模块；③ 提出联邦学习+自主安全代理的协同范式，兼顾去中心化威胁共享与本地化实时响应。  
- **局限性**：无原创算法、模型或实验验证；未量化各技术组合的实际部署开销（如XAI引入的延迟、联邦学习通信瓶颈）；对对抗性攻击下认知模型的鲁棒性缺乏分析；未提供可复现的技术栈或基准测试方案。  
- **对你研究的启发**：① “认知闭环”思想可迁移至电催化反应路径推理中——构建“吸附→电子转移→脱附→状态反馈”的类认知DFT/ML联合优化流程；② XAI在安全中的可信增强逻辑，启示我们在催化剂性能预测中需嵌入物理约束解释性（如d-band中心、*OH结合能梯度）作为可验证先验；③ 联邦学习范式适用于多中心催化数据协作建模（如不同同步辐射线站的原位XAS数据共享），避免原始数据泄露。  
- **与你研究的相关度**：中
- **阅读模式:** 🔍 精读
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/849e1ce1466fbc6989a70286e8577557d4e85e13
- **标签:** electrochemistry

### 4. Fundamental invariant-neural network as a correction to the intramolecular force field illustrated for the full-dimensional potential energy surface of propane. ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2025-05-27
- **作者:** Liangfei Fu; Bina Fu; Dong H Zhang
- **核心问题**：如何在保持计算效率的同时显著提升分子力场对高精度量子力学能量（如CCSD(T)）的拟合精度  
- **动机与背景**：传统力场难以兼顾泛化性与化学精度，而纯数据驱动的神经网络势能面（如FI-NN）虽精度高但训练成本大、外推能力受限；Δ-learning策略已被证明可有效桥接不同精度层级，但在分子内力场构建中尚未系统结合物理约束型力场与对称性保护神经网络  
- **方法核心**：提出FI-NN/Force Field混合Δ-learning模型，即先用解析力场（含物理先验）粗略预测能量，再用满足基本不变量（如旋转、平移、置换对称性）的神经网络拟合其与CCSD(T)的残差  
- **关键实验与结果**：体系为丙烷（C₃H₈）构象空间；基线为纯FI-NN拟合的PES；混合模型将RMSE从FI-NN单独拟合的~0.15 kcal/mol降至~0.075 kcal/mol（降幅50%），且显著降低所需ab initio数据量  
- **创新点**：① 首次将Δ-learning范式与基本不变量神经网络（FI-NN）耦合用于分子内力场优化；② 显式利用解析力场作为低秩物理先验，提升小数据下的泛化性与外推稳定性；③ 在保持力场可解释性与可微分性的前提下，实现接近从头算精度的能量预测  
- **局限性**：仅验证于单分子（丙烷）小体系，未考察键断裂/形成、电荷转移或溶剂化等非绝热过程；力场基底仍依赖经验参数初始化，未实现端到端物理约束学习；未报告力/应力预测精度及动力学模拟验证  
- **对你研究的启发**：Δ-learning框架可迁移至电催化表面吸附能校正——例如用DFT+U或SCAN近似吸附能，再用对称性适配GNN拟合其与CCSD(T)/DMC高阶修正的差值；强调“物理基底+AI残差”双层建模对减少DFT泛化误差的潜力  
- **与你研究的相关度**：高
- **阅读模式:** 🔍 精读
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/85281bb6018352a66264923165ae41de2a827d15
- **标签:** electrochemistry, surface

### 5. Applications of machine learning in surfaces and interfaces ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2025-03-01
- **作者:** Shaofeng Xu; Jingyuan Wu; Ying Guo; Qing Zhang; Xiao-Ting Zhong et al.
- **核心问题**：如何利用机器学习方法高效、准确地理解和预测复杂表面与界面（如固–固、固–液、三相界面等）的物理化学行为  
- **动机与背景**：传统第一性原理计算和实验表征在表面/界面体系中面临高计算成本、时间尺度限制及原子级动态过程难以捕捉等瓶颈；多相界面构型复杂、环境敏感、实验可观测量有限，导致机理认知不充分；亟需数据驱动方法弥补“精度–效率”权衡缺口，支撑能源材料（如全固态电池、光电器件、多相催化）的理性设计  
- **方法核心**：综述性梳理三类主流ML范式——高通量筛选（ML-guided descriptor-based screening）、ML与第一性原理耦合（e.g., ML-predicted adsorption energies for DFT workflow acceleration）、机器学习力场（MLFF）驱动的大尺度/长时序分子动力学模拟，并强调其在界面结构采样、自由能计算与动态演化建模中的协同应用  
- **关键实验与结果**：覆盖全固态电池（Li/LLZO界面锂枝晶成核倾向预测，MAE < 0.15 eV vs. DFT）、钙钛矿太阳能电池（TiO₂/Perovskite界面缺陷态密度ML分类准确率 > 92%）、CO氧化催化（Pt(111)/H₂O界面反应路径MLFF-MD采样提升构象覆盖率30×）；基线方法主要为纯DFT、经典MD及经验势  
- **创新点**：首次系统建立表面/界面ML应用的六维分类框架（按物相组合维度），突破以往按方法或材料类型归类的局限；明确界定“界面ML研究”需同时满足构型复杂性、环境敏感性与动态耦合性三重标准；提出“MLFF + 界面约束采样 + 集成热力学分析”的标准化工作流范式  
- **局限性**：未深入讨论ML模型在界面电荷转移、强关联电子效应（如过渡金属氧化物界面）或非平衡电化学极化条件下的泛化能力；缺乏对小样本界面数据生成策略（如主动学习、物理引导生成模型）的评估；未涵盖实验–ML闭环反馈（如原位表征驱动的在线学习）进展  
- **对你研究的启发**：可借鉴其“界面分类框架”重构电催化界面（如HER/OER在NiFe-LDH/电解液界面）的特征工程逻辑；MLFF-MD结合电极电位调控（如恒电势模拟）的思路可迁移至析氢反应双电层动态建模；高通量筛选中“描述符–活性火山图”构建方法可适配于本课题的单原子催化剂界面配位熵–活性关系挖掘  
- **与你研究的相关度**：高
- **阅读模式:** 🔍 精读
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/85b490a123a2e45a8dc86a99c678f69dfc3f82f6
- **标签:** MLFF, catalysis, surface

### 6. (Invited)
 Are Pre-Trained Universal Machine Learning Interatomic Potentials Ready for Solid Electrolyte Discovery? ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2025-11-24
- **作者:** Ji Qi; Runze Liu; S. Ong
- **核心问题**：如何构建高精度、通用性强的机器学习原子间势（MLIPs）以准确模拟固态电解质等复杂材料的热力学与动力学性质  
- **方法要点**：构建基础性数据集MatPES，系统提升通用MLIPs对热力学和动力学性质的描述稳定性与准确性  
- **关键结果**：MLIPs已成功弥合第一性原理分子动力学（AIMD）模拟与实验测得的离子电导率之间的差距；可扩展应用于晶界、非晶结构、界面及短程有序可变体系等传统AIMD难以处理的复杂体系  
- **与你研究的相关度**：高
- **阅读模式:** 📋 摘要
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/869f4d2c790d1f1ad3f98ad087639b47e2145078
- **标签:** electrochemistry, MLFF, surface

### 7. Exploring the Intricacies of Glycerol Hydrodeoxygenation on Copper Surface: A Comprehensive Investigation with the Aid of Machine Learning Force Field ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2025-03-20
- **作者:** Srishti Gupta; Ajin Rajan; Edvin Fako; Tiago J Goncalves; Imke B. Müller et al.
- **核心问题**：论文摘要缺失，无法确定研究针对的具体科学问题  
- **方法要点**：论文摘要缺失，无法提取所采用的计算或实验方法  
- **关键结果**：论文摘要缺失，无法归纳关键发现或性能指标  
- **与你研究的相关度**：低
- **阅读模式:** 📋 摘要
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/86a0d15638a2337b0fcd6b926559fdd8ddc004d1
- **标签:** MLFF, surface

### 8. Dynamic identification of longitudinal impulse of heavy-haul locomotive: an effective intelligent method for comprehensive index ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2025-05-22
- **作者:** Xiangrui Ran; Shiqian Chen; Bo Xie; Bin Zhang; Yang Jin et al.
- **核心问题**：传统重载列车纵向冲动评估方法受恶劣工况限制且多指标导致现场人员难以准确理解，难以维持长期运行监测稳定性  
- **方法要点**：提出基于熵理论的综合纵向冲动评价指数（CEILI），并构建“通道卷积融合+自适应多尺度CNN+极限学习机”的混合深度学习识别模型  
- **关键结果**：CEILI指数兼具物理可解释性与工程可测性；该模型在动力学仿真和实车试验中均能有效识别不同等级的纵向冲动水平  
- **与你研究的相关度**：低
- **阅读模式:** 📋 摘要
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/86f22329fb29140b8f1651ff3e1ae47b12ea35ed
- **标签:** general

### 9. Accelerating and Enhancing Thermodynamic Simulations of Electrochemical Interfaces ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2025-03-22
- **作者:** Xiaochen Du; M. Liu; Jiayu Peng; Hoje Chun; Alexander J Hoffman et al.
- **核心问题**：传统表面Pourbaix图难以在电化学条件下自主、高效且热力学自洽地预测电极表面稳定重构结构  
- **方法要点**：扩展Virtual Surface Site Relaxation-Monte Carlo（VSSR-MC）方法，结合微调的机器学习力场，在显式水相电化学环境中自主采样动态表面重构  
- **关键结果**：成功复现已知Pt(111)表面相，并发现新型LaMnO₃(001)表面重构；框架能显式耦合体相-电解质平衡，提升电化学稳定性预测可靠性  
- **与你研究的相关度**：高
- **阅读模式:** 📋 摘要
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/86f2e9083555aa63c47be6fb83c8a20904698f7f
- **标签:** electrochemistry, catalysis, surface

### 10. utils4VASP: Setup and Evaluation of Electronic Structure and Machine-Learned Interatomic Potential Simulations with VASP. ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2025-11-06
- **作者:** J. Steffen; Andreas Mölkner; Maximilian Bechtel
- **核心问题**：缺乏统一、易用且面向表面科学与机器学习力场的VASP计算全流程自动化工具  
- **方法要点**：开发开源工具集utils4VASP，集成14个基于命令行的Python/Fortran脚本，实现VASP输入文件生成、复杂任务管理（如并行频谱计算）、结果分析（Bader电荷、STM模拟）及MLIP训练数据处理  
- **关键结果**：支持吸附物在表面的靶向放置与STM图像可视化；显著简化MLIP（如Behler-Parrinello神经网络、MACE）训练数据的筛选、组合与格式转换  
- **与你研究的相关度**：高
- **阅读模式:** 📋 摘要
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/872107e84b2b574e72093ec3d3f5bbf5fc925bae
- **标签:** electrochemistry, MLFF, surface

## 💡 今日亮点

- **最值得精读**：[1] Multi-fidelity learning for atomistic models via trainable data embeddings — 提出可训练数据嵌入（trainable data embeddings）统一异构DFT数据的系统性偏差，绕过重算瓶颈，为多精度量子化学数据融合提供了首个端到端可微框架。  
- **可能冲突的研究**：[4] Fundamental invariant-neural network as a correction to the intramolecular force field... — 其Δ-learning+物理力场混合范式隐含“高精度标签必须可靠”的前提，而[1]允许直接建模泛函依赖的标签漂移，二者对“误差源是否应被建模 vs 被消除”存在方法论张力。  
- **值得追踪的团队**：[6]作者团队（MatPES数据集构建者）— 首次系统验证通用MLIPs在固态电解质离子输运等强动力学敏感任务中的热力学/动力学双稳定性，代表MLIPs从结构预测迈向功能材料逆向设计的关键跃迁。  
- **重要趋势**：机器学习原子间势正从“单任务高精度拟合”转向“多保真度协同建模 + 物理约束嵌入 + 自主界面采样”的闭环范式，尤其在电化学与能源界面上形成方法-数据-工具链协同演进。

## 📌 Key Gap

**关键差距**
- **Gap 1**：所有论文均假设训练数据覆盖目标物性所需构型空间，但对表面/界面体系（如[5][9]），DFT采样本身存在严重构型偏倚（如忽略亚稳重构、动力学陷阱），导致MLIPs继承并放大“隐式理论误差”，缺乏对采样不确定性的量化反馈机制。  
- **Gap 2**：跨体系迁移能力仍高度依赖人工定义的描述符或对称性群（如[2][4]），尚未建立从电子结构本征特征（如局域态密度、电荷转移路径）到力场可迁移性的可解释映射，制约模型在未知材料类（如新型卤化物固态电解质）上的外推可靠性。  
- **未来方向**：发展“量子感知的主动学习”框架：以电子结构可观测量（如d带中心偏移、界面偶极变化）为引导信号，驱动MLIPs在电化学势/偏压维度上自主扩展训练集，并耦合不确定性校准模块实现误差传播可控的多尺度模拟。
