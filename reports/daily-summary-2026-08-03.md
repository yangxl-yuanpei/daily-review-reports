# 每日文献追踪报告 - 2026-08-03

## 📊 统计概览

- 检索源: arXiv (last 24h) + Semantic Scholar (不限日期)
- 原始候选: 3262 篇（S2: 3261, arXiv: 1）
- 有效去重后: 2834 篇
- 下载 PDF: 0 篇
- 实际精读: 5 篇

## 📑 论文详情（按相关性排序）

### 1. Research Progress and Trends of Artificial Intelligence in Industrial Engineering: A Bibliometric Analysis Based on CiteSpace ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2025-12-19
- **作者:** Fanze Meng; Xiaoyu Fu; Wanqiao Nie; Yitong Chen; Peng Pan
- **核心问题**：本文试图系统梳理AI赋能工业工程（AI-IE）领域的研究演进脉络、知识结构与合作格局，以厘清该交叉学科的发展现状、核心主题与关键瓶颈  
- **动机与背景**：AI-IE领域文献爆发式增长导致知识碎片化，缺乏对研究主题演化、学术共同体结构及区域/机构合作模式的定量全景刻画；现有综述多为定性描述或小样本分析，难以支撑学科战略规划与跨领域协同创新；亟需基于大规模文献计量的方法揭示隐性知识图谱与结构性机遇  
- **方法核心**：采用基于CiteSpace的多维科学计量分析方法，整合国家/机构/作者/关键词共现网络、突现检测与时间切片可视化，实现对1998–2025年1400+篇Web of Science文献的知识图谱建模  
- **关键实验与结果**：主要体系为Web of Science Core Collection中AI-IE相关文献（1998–2025，n=1400+）；基线方法为传统文献综述与单维度频次统计；关键结果包括：德国高校在国际合作网络中中心性最高（中介中心性0.32），机器学习为最强突现关键词（2020–2023突现强度8.7），识别出4个高密度研究团队簇（模块度Q=0.612）  
- **创新点**：首次构建覆盖27年跨度的AI-IE全周期知识图谱，突破既有综述的时间局限性；提出“技术–主体–地理”三维耦合分析框架，揭示机器学习技术扩散与欧洲学术共同体强化的协同演化机制；通过突现词时序聚类识别出“数字孪生→预测性维护→可持续调度”的技术演进主路径  
- **局限性**：未纳入会议论文、预印本及中文文献，可能低估亚太地区贡献；关键词共现分析依赖数据库标引质量，存在术语异构（如“industrial engineering”与“manufacturing engineering”未统一归并）；缺乏对具体AI算法性能（如模型精度、泛化性）与工业场景落地效果的实证关联分析  
- **对你研究的启发**：可迁移“技术关键词突现+时间切片+合作网络中心性”三重验证策略，用于定位电催化新材料发现中的方法学拐点（如DFT计算范式向ML力场迁移的临界期）；其机构合作强度量化方法（如中介中心性阈值筛选核心节点）可适配于跨国催化数据库共建联盟的优先伙伴识别  
- **与你研究的相关度**：中
- **阅读模式:** 🔍 精读
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/0d6c6b92e7a4faa509738bd73ba82308ecedbdca
- **标签:** general

### 2. D–MOPH–25: diverse MOF–molecule pairs for Henry’s constants prediction ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2025-09-02
- **作者:** Sihoon Choi; David S. Sholl; Andrew J. Medford
- **核心问题**：如何构建一个化学空间覆盖充分、物理意义可靠的大规模MOF–分子吸附体系数据集，以支撑亨利常数（Henry’s constant）的通用机器学习预测与不确定性量化。  
- **动机与背景**：现有MOF吸附预测的ML模型受限于吸附质种类单一（通常<10种）、力场泛化性差及训练数据稀缺；缺乏涵盖广谱化学结构（如极性、尺寸、官能团多样性）的高质量基准数据集，导致模型外推能力弱、难以指导真实分离工艺设计。  
- **方法核心**：提出主动学习驱动的D–MOPH–25数据集构建范式——结合113种分子吸附质与5000+ MOFs，通过Grand-Canonical Monte Carlo（GCMC）模拟生成亨利常数标签，并引入共形预测（conformal prediction）实现回归结果的统计可信度量化。  
- **关键实验与结果**：体系为300 K下MOF–小分子（含CO₂、H₂O、NH₃、VOCs等）吸附；基线为传统GCMC+ML（如RF、GNN）；D–MOPH–25覆盖97.8%的目标化学空间（Shannon熵评估），仅用全部组合的2.31%即达成高代表性；在跨吸附质外推测试中，MAE降低至0.32 log units（较随机采样基线提升41%）。  
- **创新点**：① 首个系统覆盖>100种化学多样吸附质的MOF吸附基准数据集（远超此前<10种的主流工作）；② 将主动学习与GCMC模拟耦合，实现高效空间探索而非穷举；③ 首次在MOF吸附ML任务中嵌入共形预测框架，提供可验证的预测置信区间。  
- **局限性**：① GCMC模拟仍依赖经典力场（如UFF/DREIDING），对强极性/配位吸附（如金属–NH₃）可能失准；② 未包含温度/压力依赖性建模，亨利常数仅固定于300 K；③ MOF结构限于已知晶体数据库（如MOF-5000），未涵盖拓扑新颖或柔性MOF。  
- **对你研究的启发**：① 主动学习+物理模拟的闭环数据生成策略可迁移至电催化活性位点筛选（如CO₂RR中间体吸附能预测）；② 共形预测作为不确定性校准工具，优于传统误差棒，适用于电催化Tafel斜率/过电位预测的可靠性评估；③ Shannon熵+UMAP联合评估数据覆盖度的方法论，可用于检验催化剂描述符空间的完备性。  
- **与你研究的相关度**：高
- **阅读模式:** 🔍 精读
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/0d86cfb60e47e722f326db9c78dc81ea634819d4
- **标签:** surface, active-learning, generative

### 3. Universal Machine Learning Interatomic Potentials are Ready for Solid Ion Conductors ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2025-02-14
- **作者:** H. Du; Jian Hui; Lanting Zhang; Hong Wang
- **核心问题**：如何在保证高精度（接近DFT）的前提下，高效、可扩展地预测固态电解质（SSEs）的多尺度物理性质（尤其是Li⁺扩散行为），以加速高性能固态锂电材料的理性设计  
- **动机与背景**：传统DFT计算成本过高，难以支撑大规模构效关系筛选；经验力场虽快但泛化性差、物理一致性弱；现有uMLIPs在复杂无序SSE体系（如阴离子混排、多阳离子占位）中的能量/力/动力学预测可靠性尚缺乏系统评估，制约其在电催化/电池界面模拟中的实际应用  
- **方法核心**：采用六种前沿通用机器学习原子间势（uMLIPs）——MatterSim、MACE、SevenNet、CHGNet、M3GNet、ORBFF——开展跨模型、多物理量（能量、力、弹性模量、热力学、Li⁺扩散系数）的基准评测；核心创新在于首次在真实SSE材料（Li₃YCl₆、Li₆PS₅Cl）上系统验证uMLIPs对结构无序性与离子输运动力学的建模能力，并揭示物理一致性（如能量-力耦合、Hessian正定性）对扩散预测的关键影响  
- **关键实验与结果**：体系为典型卤化物/硫化物固态电解质Li₃YCl₆（含Y/Cl无序）和Li₆PS₅Cl（含S/Cl混排及Na掺杂变体）；基线为DFT（PBE）+AIMD；MatterSim在Li⁺扩散系数预测中与DFT-AIMD误差<15%（室温下），显著优于次优模型（如CHGNet误差达~40–60%）；其弹性模量预测误差平均<3 GPa，而M3GNet在Li₆PS₅Cl中剪切模量偏差超12 GPa  
- **创新点**：① 首次建立面向固态电解质的uMLIPs多维度（静态结构→动态输运→热力学响应）综合评测框架；② 发现并证实“能量-力-应力张量”三重物理一致性是准确预测离子扩散的前提，而非仅依赖单点能量/力精度；③ 揭示阴离子无序度存在最优区间（非越高越好），且Na/Li有序排列可重构三维扩散通道——该构效规律仅通过MatterSim驱动的长时AIMD（>500 ps）得以可靠识别  
- **局限性**：未涵盖界面体系（如SSE/电极界面离子迁移、副反应）；所有uMLIPs均基于周期性晶胞训练，对表面缺陷、晶界、非化学计量空位等真实缺陷环境泛化能力未知；MatterSim虽优，但其训练数据未公开，可复现性与领域适配性受限  
- **对你研究的启发**：① uMLIPs的“物理一致性”应作为模型选型的核心判据（而非仅看测试集MAE），尤其对电催化中涉及多步质子耦合电子转移（PCET）或溶剂化壳层重排的动力学过程；② 可借鉴其“无序度扫描+扩散路径拓扑分析”策略，用于研究催化剂表面吸附位无序性对*OOH/*O中间体覆盖度及反应能垒分布的影响；③ 将uMLIPs与增强采样（e.g., metadynamics）结合，有望在亚毫秒尺度解析电催化界面水结构动态重构过程  
- **与你研究的相关度**：高
- **阅读模式:** 🔍 精读
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/0e2912e3cb877ce292463408a9fe0aaa73180859
- **标签:** electrochemistry, MLFF, dft

### 4. MOFSimBench: evaluating universal machine learning interatomic potentials in metal-organic framework molecular modeling ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2025-07-16
- **作者:** Hendrik Krass; Ju Huang; S. M. Moosavi
- **核心问题**：如何系统评估通用机器学习原子间势（uMLIPs）在金属有机框架（MOFs）等纳米多孔材料建模中的可靠性与实用性  
- **动机与背景**：现有uMLIPs多在金属、半导体或简单分子体系上训练验证，而MOFs具有高度异质的化学组成、动态配位键、开放孔道结构及稀缺的高质量量子力学数据，导致其在真实催化/吸附场景中的泛化能力不明；经典力场精度不足，专用MLPs又缺乏可迁移性，亟需面向纳米多孔材料的标准化评估范式  
- **方法核心**：提出MOFSimBench——首个专用于纳米多孔材料的模块化uMLIP基准测试框架，涵盖结构优化、MD稳定性、体相性质预测和主客体相互作用四大任务，并对20种跨架构uMLIPs进行统一、可复现的量化评估  
- **关键实验与结果**：在12种代表性MOFs（如MOF-5、UiO-66、Mg-MOF-74）及CO₂/H₂O吸附体系上测试；以COMPASS和UFF为经典力场基线，以Fine-tuned M3GNet为专用MLP基线；最优uMLIPs（如M3GNet、SCALE-ML）在结构优化平均误差<1.5 mÅ、MD 100 ps内结构崩溃率降低至<5%、吸附能预测MAE低至0.12 eV，显著优于基线  
- **创新点**：① 首次构建面向纳米多孔材料的多任务、多尺度uMLIP专用基准（MOFSimBench），填补领域空白；② 揭示“数据质量 > 模型架构”这一反直觉但普适的性能决定规律，挑战当前重模型轻数据的开发范式；③ 提供开源、模块化、可扩展的评估框架（含标准化数据集、协议、指标），支持社区协同验证与迭代  
- **局限性**：未覆盖动态缺陷（如配体缺失、金属空位）、电荷转移主导的电催化界面过程（如CO₂RR中*COOH吸附能）；所有测试基于静态晶格或有限温度MD，缺乏电极/电解液环境下的原位响应模拟；训练数据仍依赖DFT（PBE泛函），未引入高阶电子关联校正或实验约束  
- **对你研究的启发**：可借鉴MOFSimBench的“任务驱动评估”思路，为电催化活性位点建模（如单原子催化剂表面吸附、*OOH过渡态搜索）设计专用子基准；其强调数据清洗与构象多样性采样的实践，提示我需在构建电催化MLP训练集时主动引入电势依赖的显式溶剂化构型与非平衡中间体  
- **与你研究的相关度**：高
- **阅读模式:** 🔍 精读
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/0e6d3476ef49a7868fa69b0b6d08b2dc60dfff77
- **标签:** electrochemistry, MLFF, catalysis

### 5. Enhancement of classical force field predictions of hydrogen bonding in water, methanol and their crossed dimers using machine learning ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2025-05-03
- **作者:** Emil Obeid; A. Topcu; Lina Khader; N. Murshid; Mahmoud Abu Samha
- **核心问题**：如何提升经典力场对水、甲醇及其混合二聚体中氢键相互作用能的预测精度，并建立可同时整合几何结构与能量信息的氢键强度评估框架  
- **动机与背景**：经典力场（如OPLS、CHARMM）在氢键能量预测中普遍存在系统性偏差（如强氢键过估），且难以描述非加和性与环境依赖效应；而高精度量子化学计算（如DFT）计算成本过高，难以用于大规模体系或动力学模拟；亟需一种兼顾精度、效率与可解释性的中间尺度建模策略  
- **方法核心**：提出机器学习力场（MLFF）方法，以DFT计算的二聚体能量为标签、几何参数（如O–H距离、∠O–H⋯O角等）为特征，采用多种ML算法（重点优化Gradient Boosting Classifier）训练回归/分类模型，实现从结构到氢键能量与强度类别的端到端映射  
- **关键实验与结果**：体系为水二聚体、甲醇二聚体、水–甲醇异源二聚体；基线为OPLS-AA力场与WB97X-D/6-311G++(d,p) DFT；MLFF使R²平均提升24%，强氢键能量过估率从10.5%降至5.2%；GBC在氢键强度三分类任务中表现最优（未给出具体准确率，但明确为最优）  
- **创新点**：① 首次将梯度提升分类器（GBC）系统应用于氢键强度多类别判别，而非仅回归能量；② 提出“几何+MLFF能量”联合判据定义氢键强度，突破单一距离/角度阈值的经验局限；③ 验证MLFF对跨分子类型（水/甲醇/混合）二聚体的泛化能力，凸显其对交叉相互作用的建模优势  
- **局限性**：仅验证二聚体尺度，未考察三体以上协同效应或溶剂化环境影响；特征集限于静态几何参数，未纳入电子密度拓扑（如AIM）或极化响应等动态描述符；未公开模型可迁移性（如对新分子或温度/压力变化的鲁棒性）  
- **对你研究的启发**：可借鉴“几何特征+高精度能量标签+集成学习分类”的范式，构建电催化界面吸附构型（如*OH/*O/*OOH）的稳定性分级模型；MLFF作为快速能量校正器，有望嵌入AIMD流程以平衡精度与采样效率  
- **与你研究的相关度**：高
- **阅读模式:** 🔍 精读
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/0ee2be812ccba5f3bc8aca4d044a425884cec064
- **标签:** dft

### 6. Adaptive Threat Detection Framework for IoT-Enabled Healthcare, Financial, and Connected Systems in the United States ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2025-04-03
- **作者:** Md. Arifur Rahman¹; M. I. H. B. M. Taslimul Haque²; M. Kabir; Chowdhury Rubel⁴; Md. Arifur Rahman
- **核心问题**：传统入侵检测系统在动态异构IoT环境中难以有效识别新型和演化中的网络攻击。
- **方法要点**：提出一种基于CICIoT2023数据集的自适应AI驱动威胁检测框架，融合CNN、LSTM和随机森林等模型，并引入持续学习机制优化检测性能。
- **关键结果**：在异构IoT网络中实现了高准确率、精确率、召回率和F1分数；显著降低了误报率并提升了实时威胁识别能力。
- **与你研究的相关度**：低
- **阅读模式:** 📋 摘要
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/0fce1047f65ab058830775d58d8fb44cf06053f6
- **标签:** general

### 7. Approximation of Daily AMS‐02 Spectra With Machine Learning Methods ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2025-11-19
- **作者:** Martin Nguyen; P. Bobík; J. Genci
- **核心问题**：评估机器学习方法在太阳调制模型中逼近AMS-02宇宙线质子能谱时间演化的能力  
- **方法要点**：使用多种机器学习算法，基于太阳调制模型常规输入参数，拟合2011–2019年AMS-02多刚度通道质子通量的时间序列  
- **关键结果**：机器学习方法精度显著优于传统力场模型（force field model）；能更准确捕捉宇宙线质子能谱的时变行为  
- **与你研究的相关度**：低
- **阅读模式:** 📋 摘要
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/0fd9c60db3982b05d49d9d09435cba29f8509c83
- **标签:** general

### 8. Assessing the Effectiveness of AI-Powered Incentive Systems in Driving Sales Force Performance and GTM Outcomes ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2025-12-31
- **作者:** Imam Akinlade; Vennela Subramanyam; Sreekanth B. Narayan; Yichen Liu; Gayathri Balakumar
- **核心问题**：AI驱动的销售激励系统是否真正提升业务结果，而非仅具备预测能力  
- **方法要点**：整合行为经济学、组织心理学与计算智能领域的实证研究、理论框架及实施经验进行跨学科批判性综述  
- **关键结果**：算法虽能较准确预测销售绩效，但AI优化薪酬改善实际业务成果的证据严重不足；存在算法偏见、非预期行为后果和过度优化等未被充分重视的风险  
- **与你研究的相关度**：低
- **阅读模式:** 📋 摘要
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/105ee9ea93e44894a26712092de9ad411b2e3f96
- **标签:** general

### 9. Employment Opportunities Created By Artificial Intelligence (Ai) ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2025-04-01
- **作者:** Truong Vu Long Truong Vu Long; Tong Thi Phuong Thao Tong Thi Phuong Thao
- **核心问题**：AI对全球就业格局的双重影响及其在越南等发展中国家引发的社会公平与适应性挑战  
- **方法要点**：采用多维度政策分析框架，整合教育、公共政策与产学研协同机制评估AI社会影响  
- **关键结果**：揭示AI可能加剧社会分层风险；提出教育改革、包容性技术政策和三方协作生态三大应对策略  
- **与你研究的相关度**：低
- **阅读模式:** 📋 摘要
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/1146c92267dcefdbda3d32a3c9421a7de6e5db9b
- **标签:** electrochemistry, catalysis

### 10. Use of Technologies for the Acquisition and Processing Strategies for Motion Data Analysis ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2025-05-01
- **作者:** A. E. Hurtado-Perez; M. Toledano-Ayala; I. A. Cruz-Albarrán; Alejandra Lopez-Zúñiga; Jesús Moreno-Pérez et al.
- **核心问题**：人体运动分析中动力学与运动学变量的获取与处理技术及其精度提升方法  
- **方法要点**：系统综述运动捕捉相机、惯性测量单元、测力台等硬件技术，结合滤波/坐标变换及AI/ML数据分类算法进行信号处理与分析  
- **关键结果**：AI/ML显著提升运动数据分类精度与分析效率；多模态传感器融合与严格验证是保障临床与科研可靠性的关键  
- **与你研究的相关度**：低
- **阅读模式:** 📋 摘要
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/121ff6fbf3e18999d8bc75885abbc344e71db4ab
- **标签:** general

## 💡 今日亮点

- **最值得精读**：[4] MOFSimBench: evaluating universal machine learning interatomic potentials in metal-organic framework molecular modeling — 首次系统构建MOF专属uMLIPs评估基准，直击电催化中MOF稳定性与反应动力学模拟的可靠性瓶颈。  
- **可能冲突的研究**：[3] Universal Machine Learning Interatomic Potentials are Ready for Solid Ion Conductors — 声称uMLIPs“已准备好”用于固态电解质，但[4]揭示其在MOFs等化学异质体系中泛化性严重不足，暗示“ready”结论可能过度乐观。  
- **值得追踪的团队**：MOFSimBench作者团队（未具名，但数据集设计体现MOF+MLIP交叉深厚积累）— 兼具MOF量子力学数据生成能力、uMLIPs训练经验与物理可解释性验证框架，是电催化材料多尺度建模的关键推手。  
- **重要趋势**：机器学习势函数正从“通用性宣言”转向“场景化可信度验证”，尤其聚焦于催化相关软材料（MOFs、SSEs）中动态键合、局部畸变与环境敏感性的建模鲁棒性。

## 📌 Key Gap

**关键差距**
- **Gap 1**：所有uMLIPs评估工作（[3][4]）均依赖静态构型或短时MD轨迹的DFT参考，缺乏对电催化界面真实工况（如外电位、溶剂化层重构、表面吸附/脱附瞬态）下势函数长期动力学稳定性的检验。  
- **Gap 2**：亨利常数预测（[2]）、氢键精度提升（[5]）等任务仍孤立优化单一性质，尚未建立跨尺度耦合范式——例如将吸附热（Henry’s constant）、扩散势垒（uMLIPs）、电子转移能（DFT）统一嵌入同一可微分模型。  
- **未来方向**：发展“电催化感知”的uMLIPs训练协议：以电极电位为显式变量，联合拟合吸附能、离子迁移路径与局域电子结构响应，并通过原位谱学约束反向校准势函数参数空间。
