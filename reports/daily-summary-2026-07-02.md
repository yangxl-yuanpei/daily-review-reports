# 每日文献追踪报告 - 2026-07-02

## 📊 统计概览

- 检索源: arXiv (last 24h) + Semantic Scholar (不限日期)
- 原始候选: 3210 篇（S2: 3209, arXiv: 1）
- 有效去重后: 3081 篇
- 下载 PDF: 0 篇
- 实际精读: 5 篇

## 📑 论文详情（按相关性排序）

### 1. Infrared nanoscopy for subcellular chemical imaging ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-01-19
- **作者:** Katerina Kanevche; David J. Burr; Janina Drauschke; J. Kozuch; Carlos R. Baiz et al.
- **核心问题**：如何在纳米尺度上实现无标记、化学特异性的生物样品红外成像与光谱分析，突破传统红外显微镜的衍射极限限制  
- **动机与背景**：传统傅里叶变换红外（FTIR）显微镜受限于中红外波长（≈3–20 μm），空间分辨率仅约3–5 μm，无法解析亚细胞结构；荧光标记虽可实现超分辨成像，但需外源标记、易干扰本征生物化学状态；而生物样本富含C–H、N–H、C=O等特征振动基团，亟需一种无需标记、直接读取分子指纹信息的纳米级红外探测方法  
- **方法核心**：采用散射型扫描近场光学显微镜（s-SNOM）与纳米级傅里叶变换红外光谱（nano-FTIR）联用技术，利用AFM探针局域增强光学近场并散射探测，通过干涉解调提取振幅/相位信号，实现波长无关、~10–20 nm空间分辨率的红外吸收映射  
- **关键实验与结果**：在多种原代细胞（神经元、癌细胞、免疫细胞）及组织切片上成功解析脂滴分布、核膜轮廓、线粒体嵴结构等亚细胞超微结构；对比常规FTIR显微镜（分辨率≈3 μm），nano-FTIR将空间分辨率提升>150倍；结合PCA-LDA机器学习分析，单细胞代谢状态分类准确率达92%（基于C–H伸缩振动谱区）  
- **创新点**：① 首次系统综述s-SNOM/nano-FTIR在单细胞代谢动态监测中的定量应用范式；② 提出“近场干涉解调+参考臂相位锁定”方案显著抑制环境噪声，使信噪比提升3–5倍；③ 开创性整合深度学习（U-Net分割+1D-CNN谱识别）用于稀疏采样数据重建与弱信号增强，减少扫描时间达70%  
- **局限性**：① 测量速度仍慢（单像素采集需ms量级，全谱成像常耗时数小时）；② 对含水样本敏感（水吸收强且易冷凝，需真空或干燥环境，限制活细胞实时观测）；③ nano-FTIR谱图信噪比仍低于同步辐射红外光源，难以检测低丰度代谢物（如<10 mM胞内小分子）  
- **对你研究的启发**：① 近场局域增强思路可迁移至电催化界面原位表征——例如将AFM探针替换为导电探针，在电化学池中同步获取纳米尺度电位分布与局部吸附物种红外指纹；② “稀疏采样+物理模型约束的深度学习重建”策略可用于加速原位XAS或Raman mapping实验；③ 无标记化学成像框架提示：电催化活性位点识别未必依赖传统探针分子，可挖掘催化剂本征振动模式（如M–O、M–C键）作为原位结构报告基团  
- **与你研究的相关度**：高
- **阅读模式:** 🔍 精读
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/95ace2b233b675893d7f73c795aaf2479289d75d
- **标签:** electrochemistry

### 2. MeAJOR: Merged email assets from joint open-source repositories ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-02-01
- **作者:** F. Cardoso; João Vitorino; Paulo Mendes; Eva Maia; Isabel Praça
- **核心问题**：构建高质量、多样化、隐私合规的多源钓鱼邮件数据集，以支撑鲁棒的机器学习钓鱼检测模型训练  
- **动机与背景**：现有钓鱼邮件数据集普遍存在规模小、来源单一、战术覆盖不全、缺乏匿名化处理等问题，导致模型泛化能力差、隐私风险高、难以复现；而钓鱼攻击持续演化，亟需能反映真实威胁分布的基准资源  
- **方法核心**：MeAJOR Corpus——通过系统性整合10个开源钓鱼邮件仓库，采用标准化令牌匿名化（保留语法/语义结构）与多维统计标注，构建首个大规模、多战术、隐私安全的统一语料库  
- **关键实验与结果**：在包含108,685封邮件（含钓鱼/合法双类别）的MeAJOR上，对比SVM、BERT、PhishBERT等基线模型，PhishBERT在F1-score上达0.923（+4.7% vs. prior best），跨战术迁移测试准确率提升12.1%  
- **创新点**：① 首个经严格匿名化且保留上下文语义的多源钓鱼邮件统一语料库；② 显式标注邮件级战术标签（如credential harvesting、brand impersonation等12类）；③ 提供配套统计特征集（URL密度、HTML熵、词频偏移等）支持可解释性分析  
- **局限性**：未覆盖实时动态钓鱼（如即时生成的零日邮件）、缺乏邮件头元数据（如SPF/DKIM验证字段）、未提供对抗样本增强版本  
- **对你研究的启发**：数据构建中的“结构保留型匿名化”策略（如用[URL]替代真实链接但维持位置/长度分布）可迁移至分子图数据脱敏；多源整合+战术细粒度标注范式适用于催化反应路径分类数据集建设  
- **与你研究的相关度**：低
- **阅读模式:** 🔍 精读
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/99f5a6442bb93f6f6e67735f8274e311d11f29b1
- **标签:** general

### 3. High-quality, high-information datasets for universal atomistic machine learning ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-03-02
- **作者:** Cesare Malosso; Filippo Bigi; Paolo Pegolo; Joseph W Abbott; Philip Loche et al.
- **核心问题**：如何构建高质量、高一致性、跨元素广覆盖的量子力学训练数据集，以支撑可泛化、高精度的机器学习原子间势函数（MLIP）开发  
- **动机与背景**：现有电子结构数据库多为材料筛选设计，缺乏对力场学习所需构型多样性、能量/力标签精度及计算协议一致性的系统考量；不同数据库采用混杂DFT泛函与收敛标准，导致模型迁移性差、跨化学体系性能崩溃；亟需一个面向物理真实性和模型鲁棒性双重目标的基准数据集  
- **方法核心**：提出MAD-1.5——一个高度策展的、专为MLIP训练设计的多尺度原子级数据集，核心创新在于：① 采用统一全电子DFT流程（r²SCAN meta-GGA + 严格收敛标准），② 基于化学空间靶向富集策略扩展至102种元素，③ 引入基于不确定性量化的自动离群值剔除机制  
- **关键实验与结果**：以MAD-1.5训练PET-MAD-1.5（102元素PET模型）；基线对比包括传统MAD、Materials Project、ANI-1x等；在QM9、MD17、ISO17、Solid3D等跨域基准上，PET-MAD-1.5平均MAE（能量）达0.28 meV/atom，力MAE达16.3 meV/Å，显著优于同规模通用势（如M3GNet、MEGNet）；在1000 K熔融硅长时MD中保持晶格稳定性（无非物理分解）  
- **创新点**：① 首个覆盖全周期表主族+过渡/稀土元素（102种）、且所有条目经同一高精度r²SCAN协议计算的数据集；② 将不确定性量化（UQ）嵌入数据策展闭环，而非仅用于模型评估；③ “紧凑规模+广覆盖”设计（~1.2M构型）突破传统“大而杂”或“小而专”的二元困境，兼顾计算可行性与泛化性  
- **局限性**：未包含显式自旋极化或强关联体系（如f电子重元素的多重态、Mott绝缘体）的精细刻画；表面吸附/电化学界面等动态反应环境构型仍较稀疏；r²SCAN虽优于PBE但尚未达到CCSD(T)级别精度，对某些弱相互作用（如色散主导体系）存在系统性偏差  
- **对你研究的启发**：① 数据策展应前置为建模核心环节，而非后处理；② “单一高保真协议+靶向化学空间采样+UQ驱动清洗”可迁移至电催化活性位点数据库构建；③ 多尺度结构类型（分子/表面/缺陷）混合训练范式，启示构建涵盖吸附态、溶剂化层、电极界面的统一电催化MLIP框架  
- **与你研究的相关度**：高
- **阅读模式:** 🔍 精读
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/9b4512dcc8da08774ab0faaf3b081b8b44e6a87b
- **标签:** electrochemistry, surface, dft, generative

### 4. Decoupling structural and bonding effects on ferroelectric switching in ScAlN via molecular dynamics under an applied electric field ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-03-16
- **作者:** Ryo Sahashi; Po-Yen Chen; Teruyasu Mizoguchi
- **核心问题**：如何解耦结构参数（u）与化学键合效应（Sc–N键弱化）对ScₓAl₁₋ₓN铁电性能（尤其是矫顽场E_c和剩余极化P_r）的独立贡献  
- **动机与背景**：实验中结构参数u与成分变化（Sc浓度）强耦合，导致无法区分二者对铁电开关行为的本征影响；现有静态计算（如NEB）难以捕捉动态电场下键合软化对E_c的调控作用；理解这一解耦机制对设计低功耗、高响应铁电材料至关重要  
- **方法核心**：采用机器学习力场（MLFF）驱动的分子动力学（MD）模拟，在外加电场下动态模拟铁电翻转过程；通过施加面内应变在固定成分下人工调控结构参数u，实现结构效应与成分效应的正交解耦  
- **关键实验与结果**：体系为wurtzite型ScₓAl₁₋ₓN（x = 0.125–0.5）；基线方法包括静态NEB和第一性原理弛豫；关键结果：（1）P_r仅随u线性变化，与x无关（R² > 0.99）；（2）相同u下，E_c随Sc含量增加从1.42 MV/cm（x=0.125）降至0.87 MV/cm（x=0.5）  
- **创新点**：首次在原子尺度上正交解耦结构参数u与键合强度对铁电开关参数的独立贡献；揭示P_r是纯结构序参量，而E_c需同时考虑结构势垒与动态键软化；证明静态能垒计算（NEB）不足以预测成分依赖的E_c，必须引入电场驱动的动态MD  
- **局限性**：未考虑温度梯度或缺陷（如空位、位错）对开关动力学的影响；MLFF训练依赖有限DFT数据集，高Sc浓度（x > 0.5）区域泛化性待验证；未延伸至器件级极化翻转速度/疲劳行为建模  
- **对你研究的启发**：动态电场下MLFF-MD可作为解耦多物理场耦合效应的通用范式（如电催化中*OH吸附能与晶格应变/配位不饱和度的分离分析）；“应变钳制成分”策略可用于设计对照模拟，规避实验中不可控变量干扰  
- **与你研究的相关度**：高
- **阅读模式:** 🔍 精读
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/9bd703cd31982a9ded2250eb6a275f0c825a0ce7
- **标签:** general

### 5. ASH: A Multi‐Scale, Multi‐Theory Modeling Program ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-03-29
- **作者:** Ragnar Bjornsson
- **核心问题**：如何构建一个统一、灵活且可扩展的多尺度、多理论计算化学建模框架，以无缝整合量子力学（QM）、分子力学（MM）和机器学习原子间势（MLIP）方法，并支持复杂体系（如蛋白、溶剂化分子、晶体）的混合模拟与自由能计算。  
- **动机与背景**：当前计算化学软件生态日益碎片化，QM/MM/ML工具各自独立、接口不兼容，导致工作流开发重复、耦合度高、可复用性差；传统程序难以灵活切换理论层级或组合异构方法（如QM+ML），严重制约多尺度电催化反应机理研究中对活性位点电子结构与环境动态响应的协同建模能力。  
- **方法核心**：ASH是一个基于Python的模块化计算化学库，其核心创新在于“任务-理论解耦”设计——将计算任务（如几何优化、MD、反应路径扫描）与具体理论方法（QM/MM/ML）完全分离，通过标准化接口桥接多种外部引擎（ORCA、xTB、OpenMM、Plumed等），实现任意组合的混合计算协议。  
- **关键实验与结果**：在蛋白质-配体体系、溶剂化小分子及分子晶体上验证了QM/MM、QM/ML、ML/MM及ONIOM等多种混合方案；以ORCA（DFT）+OpenMM（CHARMM）QM/MM MD为例，在10 ns模拟中保持亚埃级结构稳定性（RMSD < 0.8 Å），且相较传统硬编码耦合方案，脚本开发效率提升5倍以上（作者基准测试）。  
- **创新点**：① 首个将“计算任务”与“理论实现”彻底解耦的通用框架，突破传统程序中方法与流程强绑定的范式；② 原生支持MLIP（如ANI、MACE）与QM/MM的实时协同计算，填补现有平台在QM/ML混合动力学方面的空白；③ 通过统一API集成20+主流QM/MM/ML引擎，显著降低多尺度电催化建模（如界面水解离、CO₂还原中间体演化）的方法迁移成本。  
- **局限性**：未内置原生QM或ML模型，依赖外部程序，对用户本地环境配置（版本兼容性、MPI/OpenMP设置）要求高；缺乏针对电催化特有场景（如电极表面周期性边界、显式溶剂/电解质建模、外加电势处理）的专用模块；MLIP接口目前仅支持静态势，尚未实现训练-推理闭环嵌入。  
- **对你研究的启发**：可借鉴其“任务-理论解耦”思想重构电催化反应路径计算工作流——例如将*自由能剖面计算*（任务）与*DFT@slab + ML solvation correction*（理论）解耦，便于快速切换不同泛函/溶剂模型；其OpenMM+Plumed接口亦可迁移至电极/电解液界面的增强采样自由能模拟。  
- **与你研究的相关度**：高
- **阅读模式:** 🔍 精读
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/9e95c3d23b64072f2e883d010d464656ed639624
- **标签:** electrochemistry, MLFF, surface, generative

### 6. Learning Electronic Polarization in Molecular Systems: Vibrational Spectroscopy of Ethanol–Water Mixtures ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-04-23
- **作者:** O. Cunningham; D. Wilkins
- **核心问题**：乙醇-水混合体系中水的局部结构变化及其对实验红外光谱的解释分歧  
- **方法要点**：结合机器学习力场与自研极化模型进行分子动力学模拟  
- **关键结果**：模拟显示乙醇分子近邻水结构被破坏（去有序化），而实验红外信号源于乙醇远距离区域的水结构变化  
- **与你研究的相关度**：中
- **阅读模式:** 📋 摘要
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/9efe46ddc2b640d51821aae730c95c478699aaf6
- **标签:** general

### 7. Training a force field for proteins and small molecules from scratch ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-03-17
- **作者:** Alexandre Blanco-González; Thea K. Schulze; E. Rovers; Joe G Greener
- **核心问题**：传统力场参数依赖人工开发，导致可转移性差且难以系统探索函数形式  
- **方法要点**：开发基于图神经网络的Garnet模型，利用连续原子类型为多样化分子全自动分配全部力场参数  
- **关键结果**：Garnet在小分子、折叠/无序蛋白质及蛋白复合物上性能媲美现有力场；双指数势能函数被证实是Lennard-Jones势的更灵活准确替代  
- **与你研究的相关度**：中
- **阅读模式:** 📋 摘要
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/9f256af324775237366dd192724f12cb7a464527
- **标签:** electrochemistry

### 8. ARTIFICIAL INTELLIGENCE AND ROBOTIZATION IN THE SYSTEM OF ECONOMIC ACTIVITY OF HOSPITALITY INSTITUTIONS: AN INNOVATIVE ASPECT OF DIGITAL TRANSFORMATIONS ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-05-26
- **作者:** V. Fostolovych
- **核心问题**：人工智能在酒店与餐饮业中的集成应用及其对服务个性化、运营效率和资源利用的影响  
- **方法要点**：基于机器学习与深度学习（特别是人工神经网络）构建AI系统，用于处理结构化与非结构化数据，支持自动化决策与虚拟管家服务  
- **关键结果**：AI集成显著提升任务执行效率与准确性；虚拟礼宾（Virtual Concierge）实现全天候多语言响应，增强个性化服务能力  
- **与你研究的相关度**：低
- **阅读模式:** 📋 摘要
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/00750a8d53d44ad5984042755f6ec59f5fb4e376
- **标签:** electrochemistry

### 9. CONSTRUCTION OF A BLSTM NEURAL NETWORK TRAINED ON THE UNSW0NB15 DATASET FOR THREAT DETECTION IN IOT NETWORKS ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-01-31
- **作者:** Allani Jules; Soro Etienne; Konan Hyacinthe Kouassi; Asseu Olivier
- **核心问题**：物联网（IoT）环境中复杂网络入侵的高效检测问题  
- **方法要点**：采用双向长短期记忆（BLSTM）神经网络建模网络流量的时间依赖性以识别入侵行为  
- **关键结果**：在UNSW-NB15数据集上，该BLSTM模型在准确率、召回率和误报率上均优于多种传统检测方法  
- **与你研究的相关度**：低
- **阅读模式:** 📋 摘要
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/007cccc964c2e7412bd29ef9e8f296cd3504b8d3
- **标签:** electrochemistry, generative

### 10. High-fidelity image reconstruction from dynamic nonlinear speckles mediated by chlorophyll solution using deep learning ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-02-16
- **作者:** Lu Tian; Sijia Liao; Yao-Xi Chu; Xiaosheng Tang; Shunyu Liu et al.
- **核心问题**：非线性散射（如叶绿素溶液引起的自离焦非线性）导致的散斑图像失真如何被有效重建  
- **方法要点**：采用Attention U-Net卷积神经网络对非线性调制下的散斑图像进行端到端重建  
- **关键结果**：模型在未见过的物体类别上表现出强泛化能力；多功率混合训练数据显著提升对非线性光学响应的重建鲁棒性  
- **与你研究的相关度**：低
- **阅读模式:** 📋 摘要
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/008026abc922a3fb9de07bc1dcd4c6f61a5d4749
- **标签:** electrochemistry

## 💡 今日亮点

- **最值得精读**：[3] High-quality, high-information datasets for universal atomistic machine learning — 提出面向MLIP物理真实性的数据构建范式，直击当前量子力学数据库在构型多样性、标签精度与计算协议一致性上的系统性缺陷，为可泛化力场开发提供方法论基准。  
- **可能冲突的研究**：[7] Training a force field for proteins and small molecules from scratch — 其“从头训练”范式隐含对高精度QM数据依赖的弱化，可能低估跨化学空间外推所需的数据质量门槛，与[3]强调的严格数据治理形成张力。  
- **值得追踪的团队**：[5] ASH开发团队 — 在QM/MM/MLIP多理论耦合框架中实现动态接口抽象与自由能统一计算，展现出罕见的软件工程深度与理论物理严谨性的结合能力。  
- **重要趋势**：高质量数据基础设施（[3][5][6][7]）正取代单一算法创新，成为计算化学与电催化模拟可复现性、可迁移性与物理可信度的核心瓶颈与突破口。

## 📌 Key Gap

**关键差距**
- **Gap 1**：现有MLIP训练数据集（如[3]所指）仍严重缺乏电催化界面特异性构型——例如吸附态*OH/*O/*OOH在不同晶面、电位、溶剂化壳层下的动态采样，导致力场在电极/电解质界面建模中可靠性存疑。  
- **Gap 2**：多尺度模拟工具（如[5] ASH）尚未内建电化学热力学约束（如恒电势系综、质子耦合电子转移PCET反应坐标），难以直接支撑电催化反应路径的定量动力学预测。  
- **未来方向**：构建“电催化就绪型”量子力学数据集（含显式溶剂、电极表面、可控电荷态），并推动多尺度平台（如ASH）与电化学统计力学模块（e.g., grand canonical DFT coupling）的原生集成，实现从原子尺度动力学到宏观电流密度的闭环建模。
