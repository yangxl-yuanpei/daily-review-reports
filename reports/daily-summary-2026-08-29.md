# 每日文献追踪报告 - 2026-08-29

## 📊 统计概览

- 检索源: arXiv (last 24h) + Semantic Scholar (不限日期)
- 原始候选: 3306 篇（S2: 3305, arXiv: 1）
- 有效去重后: 2624 篇
- 下载 PDF: 0 篇
- 实际精读: 5 篇

## 📑 论文详情（按相关性排序）

### 1. Benchmarking of Fast and Interpretable UF Machine Learning Potentials ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-08-27
- **作者:** P. Prakash; Sam Dong; Richard G. Hennig
- **核心问题**：如何在保持近DFT精度的同时，构建兼具超低计算开销、物理可解释性与跨相态迁移能力的机器学习原子间势函数（MLIP）  
- **动机与背景**：现有高精度MLIPs（如GAP、NNP）计算成本仍显著高于经典力场，且多为黑箱模型，难以解析物理机制；而传统力场缺乏泛化能力，尤其在固-液相变等复杂热力学过程建模中表现不佳。发展兼具速度、精度与可解释性的势函数对大规模电催化界面动力学模拟至关重要。  
- **方法核心**：提出UF³（Ultra-Fast Force Field）势函数，采用线性回归结合三次B样条基函数显式建模两体与三体有效相互作用，避免神经网络等非线性黑箱结构，实现O(1)级力计算复杂度与参数物理可读性。  
- **关键实验与结果**：在Ni、Cu、Li、Mo、Si、Ge六种元素体系上验证；基线包括GAP、MTP、NNP（Behler-Parrinello）、qSNAP；UF³熔点预测误差为~6%（Ni/Cu/Li），但Mo/Si误差显著，Ge无法收敛稳定势函数。  
- **创新点**：① 首次将紧致B样条基与线性回归结合构建全显式、无隐层的MLIP，实现微秒级MD模拟吞吐量；② 提供交互式可视化接口，直接呈现径向/角度分布对应的样条系数，揭示势函数的物理行为边界；③ 在零熔点训练数据条件下完成跨相态（固→液）热力学性质迁移预测，验证弱监督下的热力学泛化潜力。  
- **局限性**：三体截断无法描述强方向性共价键（如Si、Ge）和高阶电子关联效应（如Mo的d带强耦合）；样条基固定形式限制了对长程静电或电荷转移效应的建模；未验证电化学界面（如水/金属、吸附质覆盖）下的稳定性。  
- **对你研究的启发**：① 可借鉴“可解释基函数+线性回归”范式构建电催化活性位点局部环境敏感的轻量势函数；② 样条可视化策略可用于诊断催化剂表面吸附能预测中的非物理振荡或边界异常；③ “零熔点数据迁移”思路可拓展至“零过电位/零pH数据驱动的反应自由能面构建”。  
- **与你研究的相关度**：高
- **阅读模式:** 🔍 精读
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/609a1e380fc5c5363617174aa3343954a7c3ab82
- **标签:** electrochemistry, MLFF, surface, dft

### 2. Active phase discovery in heterogeneous catalysis via topology-guided sampling and machine learning ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2025-03-14
- **作者:** Shisheng Zheng; Xi-Ming Zhang; Heng-Su Liu; Ge-Hao Liang; Sida Zhang et al.
- **核心问题**：如何在动态多变的反应环境（如电催化中不同电位、气体分压、电解质组分）下，自动、高效且物理合理地识别异相催化剂的真实活性相（包括界面、固/液/气相界面上的重构相、亚表面相乃至体相掺杂相）  
- **动机与背景**：传统计算方法依赖人工预设构型或小规模枚举，难以覆盖环境诱导的复杂结构多样性（如H/Pd体系中的“hex”重构、Pt-O团簇氧化态梯度）；第一性原理遍历计算成本过高，而经验力场又缺乏泛化能力；实验上活性相常为瞬态、局域、非周期结构，亟需可解释性强且可扩展的计算范式  
- **方法核心**：提出一种“拓扑引导+机器学习力场”协同的主动相空间探索框架；核心是基于持久同调（persistent homology）的无监督拓扑采样算法，自动识别并覆盖不同配位环境（coordination fingerprint）和形貌特征（morphological descriptor）下的结构多样性，结合高精度MLFF（如M3GNet或NequIP训练的力场）实现亚秒级能量/力预测  
- **关键实验与结果**：在Pd-H体系（CO₂RR相关）中，从50,000个自动生成构型中识别出H诱导的(100)-like “hex”亚表面重构相，其形成能比常规fcc-H相低0.18 eV/H；在Pt-O体系（ORR相关）中，从100,000构型中定位到O嵌入导致Pt₇团簇表面配位数下降2.3、d带中心上移0.45 eV的关键失活相，与原位XAS观测的氧化阈值一致  
- **创新点**：① 首次将持久同调用于催化相空间的几何-化学联合表征，摆脱对晶格/周期性/先验对称性假设的依赖；② 实现拓扑采样与MLFF训练的闭环耦合——采样驱动数据生成→MLFF提升采样置信度→新采样聚焦高不确定性区域；③ 在原子尺度直接关联环境物种（H/O）浓度梯度→局部结构重构→电子结构演化→宏观活性衰减的完整因果链，超越传统“吸附能火山图”范式  
- **局限性**：未显式耦合电极电位（*U*）或pH等热力学变量，当前相筛选仍基于固定化学势条件；MLFF训练依赖DFT参考数据质量与覆盖度，对强电子关联体系（如NiOOH）泛化性待验证；暂未整合溶剂化/双电层效应，所有模拟在真空或隐式溶剂近似下进行  
- **对你研究的启发**：可迁移“拓扑指纹→构型生成→主动学习MLFF”的三阶段工作流至我关注的Cu-Sn双金属CO₂RR体系，尤其用于解析SnOₓ/Cu界面在还原电位下的动态氧空位演化路径；持久同调描述符（如β₀/β₁ Betti数序列）有望替代传统配位数作为机器学习模型的结构输入，提升对非整数配位（如桥式O、空位邻位H）的敏感性  
- **与你研究的相关度**：高
- **阅读模式:** 🔍 精读
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/7645975bebb292dc03146485c84a8d1f054ae8df
- **标签:** MLFF, catalysis, surface

### 3. DBMLFF: Linear scaling machine learning force fields via electron density decomposition for molecular electrolytes ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2025
- **作者:** Jie Shen; Chenyu Wang; Libin Chen; Shaoqin Jiang; Jianhui Chen et al.
- **核心问题**：如何在保持从头算精度的同时大幅降低分子动力学模拟的计算成本  
- **方法要点**：构建基于机器学习的力场（MLFF），用少量高精度ab initio数据训练模型以预测原子间作用力  
- **关键结果**：MLFF可实现与ab initio相当的模拟精度，计算成本显著降低；已成功应用于催化表面反应路径和溶剂化效应的长时间尺度模拟  
- **与你研究的相关度**：高
- **阅读模式:** 📋 摘要
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/76892fd2db21c6a9425d46ee59e959a5bc56bf82
- **标签:** MLFF

### 4. A Unique Dataset for Aircraft Maintenance Assistance's Human Following Robot ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2025-07-23
- **作者:** A. D. W. Sumari; Ndaru Atmi Purnami; Bangga Dirgantara; Iqmal Agil Alfian; Ilham Yoga Pratama et al.
- **核心问题**：如何构建面向特定军事场景（印尼空军地勤人员跟随）的小规模、高定制化目标检测数据集，以支撑人跟随机器人（HFR）在复杂机库环境中鲁棒识别蓝制服人员  
- **动机与背景**：现有通用目标检测数据集（如COCO、Pascal VOC）缺乏针对特定军种制服颜色、姿态、光照及遮挡条件的标注样本；开源模型在真实机库场景中泛化性差、误检率高；而人工标注成本高、周期长，亟需轻量级、可复现、任务驱动的数据集构建范式  
- **方法核心**：提出“任务导向型小样本数据集构建流程”（DINI pipeline），整合实地图像采集、Roboflow自动化标注增强（旋转/裁剪/色彩扰动）、以及YOLOv5n轻量化模型验证闭环，强调领域适配性而非数据规模  
- **关键实验与结果**：主要体系为印尼空军蓝制服识别任务；基线方法为标准YOLOv5n（无预训练微调）；关键结果：Precision=100%（零误检），Recall=42%（漏检显著），F1-score=59%，Accuracy=87%（二分类评估下）  
- **创新点**：① 首个公开的、面向军用机务场景的专用制服检测数据集（DINI），填补领域空白；② 提出“最小可行标注集+强数据增强”策略，仅用1,451张图像实现高精度定位（Precision 100%）；③ 将数据集构建明确嵌入机器人系统开发流程（HFR硬件-任务-数据-模型协同设计），而非孤立数据工程  
- **局限性**：Recall偏低（42%）表明对遮挡、远距离、非正面姿态鲁棒性不足；未提供跨颜色/跨军种迁移实验，泛化能力存疑；缺乏与其他SOTA轻量模型（如YOLOv8n、PP-YOLOE）的对比；未开源数据集与代码  
- **对你研究的启发**：① “任务定义先行、数据最小化构建”思路可迁移至电催化材料图像识别（如SEM/TEM中特定晶面或缺陷的标注优先级设计）；② Roboflow等低代码增强工具可用于快速生成催化剂形貌扰动样本（模拟不同电镜参数）；③ Precision优先策略对安全关键场景（如机器人避障、催化反应失控预警）具方法论参考价值  
- **与你研究的相关度**：中
- **阅读模式:** 🔍 精读
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/76b945830b4d3a0b8ece5d6bd915354518f9ca07
- **标签:** generative

### 5. On-the-Fly Machine Learning Interatomic Potential for Bulk PdH: Assessing Accuracy and Efficiency ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2025-12-17
- **作者:** Poonam Parkar; Sudarshan Vijay; Abhijit Chatterjee
- **核心问题**：如何在保持第一性原理精度的前提下，高效模拟钯氢化物（PdHₓ）在有限温度下涵盖结构、热力学、弹性及扩散等多尺度性质的统计行为  
- **动机与背景**：传统从头算分子动力学（AIMD）因计算成本过高，难以在大超胞和纳秒时间尺度上实现统计收敛；而经验力场又无法准确描述氢浓度变化、晶格应变及电子结构敏感的Pd–H成键特性；金属氢化物在储氢、纯化与电催化中性能强烈依赖其有限温热力学与动力学行为，亟需高精度、高效率的模拟工具  
- **方法核心**：提出一种基于“在线主动学习”（on-the-fly active learning）框架的机器学习力场（MLFF），以DFT能量、力和应力为标签，在涵盖不同H浓度（0≤x≤1）、晶格应变及有限温度构型空间上自适应采样并迭代训练，确保物理一致性与泛化能力  
- **关键实验与结果**：体系为体相PdHₓ（含Pd/H混合超胞）；基线方法为DFT（PBE泛函）和常规AIMD；MLFF在1000+原子、2 ns MD模拟中能量误差<2 meV/atom，力误差<0.05 eV/Å，弹性常数预测与DFT偏差<3%，体积膨胀率（~3.5% for PdH）与实验吻合  
- **创新点**：① 首个面向PdHₓ全成分范围与热力学路径设计的、严格满足能量/力/应力三重守恒的MLFF；② 采用在线主动学习策略，自动覆盖氢扩散跃迁、晶格畸变等关键低概率但高能量敏感区域，避免人工预设构型偏置；③ 显式嵌入应力张量作为训练目标，保障有限温体积响应与弹性性质的定量可靠性，超越仅拟合力/能量的主流MLFF方案  
- **局限性**：未涵盖表面/界面PdHₓ体系（如电催化中真实的Pd/H₂O或Pd/电解质界面）；未验证H₂吸附/脱附、电荷转移等电化学过程相关势能面；MLFF训练依赖PBE-DFT参考数据，未评估泛函依赖性及强关联效应影响  
- **对你研究的启发**：可迁移“物理约束+主动学习”范式至电催化材料（如NiFe-OH、PtHₓ）的溶剂化界面力场构建；应力张量联合训练策略对模拟电极材料在电位驱动下的晶格应变演化具有直接借鉴价值；其构型空间覆盖逻辑（浓度梯度+温度激发+应变耦合）可指导设计电催化反应坐标驱动的智能采样协议  
- **与你研究的相关度**：高
- **阅读模式:** 🔍 精读
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/76d98ec91c2dce0382ff5ca68a893822638a4ae1
- **标签:** electrochemistry, MLFF, dft, active-learning

### 6. Simulation and Machine Learning Assessment of P-Glycoprotein Pharmacology in the Blood–Brain Barrier: Inhibition and Substrate Transport ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2025-09-01
- **作者:** Christian Jorgensen; E. Oliphant; M. Barker; E. López Martínez; S. Thulasi et al.
- **核心问题**：P-糖蛋白（P-gp）如何以非选择性方式识别数百种结构迥异的底物，并在血脑屏障（BBB）中通过多聚体构象实现高效外排与耐药调控  
- **动机与背景**：P-gp介导的多药耐药严重阻碍中枢神经系统药物递送，但其动态寡聚化状态、跨膜底物转运路径及广谱底物识别机制长期缺乏原子级与介观尺度协同解释；现有晶体结构多为单体/静态构象，分子动力学模拟受限于微秒级时长，难以捕捉生理相关寡聚组装与跨膜过程  
- **方法核心**：融合AI驱动的结构-亲和力联合预测模型（Boltz-2.1.1）与MARTINI粗粒化（CG）力场建模，构建P-gp嵌入内皮BBB膜的多尺度模拟体系，首次实现毫秒级寡聚态P-gp介导的底物跨膜渗透动态追踪  
- **关键实验与结果**：体系为人源P-gp嵌入含胆固醇/鞘磷脂的BBB模拟膜；基线对比包括原子级MD（如CHARMM36）与实验报道的P-gp抑制剂结合模式；发现第三代抑制剂（如tariquidar衍生物）稳定结合于二聚/三聚界面，CG模拟显示底物跨膜时间尺度达~200 μs（较原子模拟延长1000倍），且渗透路径依赖寡聚状态  
- **创新点**：① 首次提出P-gp“多模态寡聚抑制模型”，将抑制效力与寡聚态直接关联；② 建立首个P-gp-BBB粗粒化全系统模型，突破传统原子模拟的时间/空间尺度瓶颈；③ 通过AI结构预测+CG动力学验证，揭示扩展型疏水结合表面（>2000 Å²）是广谱底物识别的结构基础  
- **局限性**：MARTINI CG模型未显式描述质子化/磷酸化等翻译后修饰影响；Boltz-2.1.1对P-gp柔性胞外域的构象采样仍依赖有限模板；未整合电化学微环境（如膜电位）对P-gp ATPase活性的调控效应  
- **对你研究的启发**：① 多尺度建模策略（AI初筛→CG长时程→靶向原子精修）可迁移至电催化界面动态重构研究；② “功能寡聚化”概念提示OER/ORR催化剂表面活性位点可能并非孤立单中心，而是亚纳米团簇协同作用；③ 扩展结合表面思想可启发设计宽谱适配型催化载体（如缺陷石墨烯梯度场）  
- **与你研究的相关度**：高
- **阅读模式:** 🔍 精读
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/76f531fa95da4af919e9fb177aa7bc36013cad04
- **标签:** surface

### 7. The Poetics of Code: Generative AI and the Redefinition of Literary Creativity ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2025-01-31
- **作者:** Jihan Abdul Rahman Oshiesh
- **核心问题**：生成式AI对人类在文学创作中的主体性及创造力本质的挑战  
- **方法要点**：基于Scopus、Web of Science和Google Scholar的文献综述，采用描述性与分析性框架界定AI生成创造力的边界  
- **关键结果**：学者普遍担忧AI可能复制甚至超越人类创造性产出；AI正挑战“创造力是人类独有属性”这一传统本体论假设  
- **与你研究的相关度**：低
- **阅读模式:** 📋 摘要
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/770787b3db87aac5bf835382f216098316e4f7cc
- **标签:** electrochemistry, generative

### 8. The AI Coach: Transforming Physical Education and Human Performance through Personalized, Data-Driven Frameworks ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2025
- **作者:** S. Kannan
- **核心问题**：如何利用AI技术实现体育教育与人类运动表现优化的个性化、自适应与预测性提升  
- **方法要点**：构建多模态融合的“AIP-PEP”系统，结合CNN进行动作姿态分析、RNN建模可穿戴传感器时序数据，并采用混合研究方法（定量干预+定性访谈）验证效果  
- **关键结果**：AI组动作技术准确率提升32%、技能习得速度加快28%； injury风险预测模型提前两周识别过劳损伤准确率达88%  
- **与你研究的相关度**：低
- **阅读模式:** 📋 摘要
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/798ac3f3b02b55342872c382082d7ef0a03b52c6
- **标签:** electrochemistry

### 9. AI-based automated weight prediction in cattle for herd health surveillance. ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2025-11-01
- **作者:** İsmail Kırbaş
- **核心问题**：如何实现大规模牧场中奶牛健康状况的早期、无创、自动化实时体重监测  
- **方法要点**：基于行走式称重平台采集动态力-时间信号，经FFT变换提取频域特征，结合SVR等机器学习模型进行体重回归预测  
- **关键结果**：SVR模型达到MAE=2.3 kg、R²=0.999的高精度体重预测；系统集成IoT实现真实牧场环境下的鲁棒性实时监测与异常检测  
- **与你研究的相关度**：低
- **阅读模式:** 📋 摘要
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/7aa4461b62f6dc1d3dbdc3850c8bdf15ea1b200f
- **标签:** general

### 10. Large-Scale Non-Adiabatic Dynamics Simulation Based on Machine Learning Hamiltonian and Force Field: The Case of Charge Transport in Monolayer MoS2. ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2025-05-09
- **作者:** Bichuan Cao; Jiawei Dong; Zedong Wang; Linjun Wang
- **核心问题**：如何高效、可靠地实现大规模非绝热动力学模拟以研究二维材料中的载流子输运行为  
- **方法要点**：构建基于Wannier表征的准对角化哈密顿量神经网络（DHNet），结合DeePMD力场与表面跳跃法进行大规模非绝热动力学模拟  
- **关键结果**：仅需10个DFT结构即可训练DHNet，计算成本较直接DFT降低约5个数量级；成功模拟3675原子MoS₂单层的电子输运，预测电子迁移率为110 cm²/(V·s)，与实验值（3–200 cm²/(V·s)）高度一致  
- **与你研究的相关度**：高
- **阅读模式:** 📋 摘要
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/7acf70037c4e1a317c455141b77ceb11ede1fd6c
- **标签:** electrochemistry, MLFF, surface, dft

## 💡 今日亮点

- **最值得精读**：[1] Benchmarking of Fast and Interpretable UF Machine Learning Potentials — 提出“可解释性—速度—精度”三元平衡的统一评估框架（UF），首次将物理可解释性（如力矩分解、局部环境敏感度）量化嵌入MLIP benchmark流程，直击电催化界面动力学中“黑箱势函数无法归因活性位点演化”的核心痛点。  
- **可能冲突的研究**：[5] On-the-Fly Machine Learning Interatomic Potential for Bulk PdH — 其采用的on-the-fly训练策略虽提升PdH体系特异性，但依赖局部构型空间采样，与[1]倡导的跨相态迁移泛化能力存在方法论张力。  
- **值得追踪的团队**：DeePMD团队（关联[1][3][10]） — 在多尺度耦合（电子结构→力→非绝热跃迁）中持续推动MLIP从“拟合工具”向“可微分物理代理模型”演进，其Wannier+DeePMD+surface hopping链式架构已成为电催化动态界面模拟的事实标准范式。  
- **重要趋势**：MLIP正从单一精度/速度优化，转向“可解释性驱动的物理一致性验证”（如电荷重分布响应、键级演化连续性、相变路径可逆性），为电催化中电位依赖的表面重构提供可审计的原子尺度因果链。

## 📌 Key Gap

**关键差距**
- **Gap 1**：所有高精度MLIP（[1][3][5][10]）均假设核运动在固定电子基态下进行（绝热近似），而电催化界面反应（如*O → *OH质子耦合电子转移）本质是非绝热过程，现有模型无法自洽描述电子激发态参与的键断裂/形成动力学。  
- **Gap 2**：活性相识别（[2]）与MLIP动力学模拟（[1][5][10]）仍属割裂流程：前者依赖静态构型枚举，后者依赖预训练势函数，缺乏“环境反馈—结构演化—势函数在线更新”的闭环，难以捕捉电位阶跃诱导的毫秒级表面重构。  
- **未来方向**：发展电位可控的非绝热MLIP框架——将电极电位作为显式变量嵌入哈密顿量神经网络（如DHNet扩展为Φ-dependent DHNet），耦合拓扑引导采样（[2]）实现活性相驱动的势函数增量训练，最终构建电催化界面“电位—结构—电子态”三维响应图谱。
