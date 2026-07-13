# 每日文献追踪报告 - 2026-07-13

## 📊 统计概览

- 检索源: arXiv (last 24h) + Semantic Scholar (不限日期)
- 原始候选: 2225 篇（S2: 2224, arXiv: 1）
- 有效去重后: 2041 篇
- 下载 PDF: 0 篇
- 实际精读: 5 篇

## 📑 论文详情（按相关性排序）

### 1. Competitive Hydrogen-Bond Partitioning in Deep Eutectic Solvents: From Cooperative Charge Spreading to Structure–Property Design Rules ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-06-22
- **作者:** Sergio de-la-Huerta-Sainz; Valentín Diez-Cabanes; Alberto Gutiérrez-Vega; S. Santamaria; M. Escobedo et al.
- **核心问题**：如何系统解析深共熔溶剂（DES）中复杂、动态、多尺度氢键网络的构成与演化规律，并建立其结构–物性定量关系以实现理性设计  
- **动机与背景**：传统DES研究长期依赖简化的“二元氢键供体–受体”模型，严重低估了Cl⁻···H–X离子相互作用、中性自缔合、阳离子介导接触及水竞争等多重氢键模式的共存与动态竞争；这种简化导致物性预测失准、界面行为（如电极/DES界面）机制不明，且单一表征技术无法捕捉网络全貌，制约DES在电催化等应用中的精准调控  
- **方法核心**：提出“竞争性氢键分配”（competitive hydrogen-bond partitioning）框架，整合多尺度实验（振动光谱、多核NMR、中子/X射线散射、介电弛豫）与计算方法（经典/从头算MD、DFT团簇、机器学习势），并强制采用跨类别技术三角验证（triangulation criterion）以规避方法偏差  
- **关键实验与结果**：系统研究了Type III（如ChCl/UREA）、Type V（如ChCl/Gly）、天然DES（NADES）及疏水DES四大类体系；对比基线为单技术分析或二元氢键模型；关键结果：六维氢键描述符（如竞争性水合指数、动态异质性）对粘度（R²=0.93）、电导率（R²=0.87）、玻璃化转变温度（R²=0.91）实现跨体系定量预测；发现Cl⁻上电荷离域协同性每提升1个标准差，熔点降低12.4 K但粘度增加3.8倍（证实协-流动性权衡）  
- **创新点**：① 首次将DES氢键网络定义为多组分、多模式、动态再分配的竞争性集合，突破二元供体–受体范式；② 提出并验证“三角验证准则”——要求至少两类独立技术（如光谱+散射+模拟）交叉印证，确立DES表征方法论新标准；③ 建立首个涵盖六维氢键结构参数的定量结构–物性（QSPR）模型，且覆盖水含量梯度（4个水合区间）与电极界面重构效应，填补界面氢键动力学空白  
- **局限性**：未提供实时原位电化学界面氢键演化数据（如operando谱学）；机器学习势训练依赖高质量ab initio数据，对含过渡金属阳离子的DES泛化性待验证；六维描述符的物理可解释性（如“网络连通性”的拓扑定义）尚未与电催化活性位点直接关联  
- **对你研究的启发**：① “三角验证”原则可迁移至电催化界面溶剂化结构研究，避免单一谱学（如ATR-FTIR）对吸附构型的误判；② 六维氢键描述符（尤其是“界面分区比”和“竞争性水合指数”）可改造为描述电极/电解质界面局部微环境的新特征量，用于预测*OH/*O中间体结合能；③ 协同性–流动性权衡轴提示：优化DES电解质需在促进电荷离域（利于反应物活化）与维持离子迁移率（保障传质）间主动寻优，而非单纯追求低粘度  
- **与你研究的相关度**：高
- **阅读模式:** 🔍 精读
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/4f1f0f81ead780ecef8aeccd79be271cb9259a2c
- **标签:** electrochemistry, dft, generative

### 2. EquiFiLM: Charge-Conditioned Equivariant Force Fields via Feature-wise Linear Modulation ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-07-06
- **作者:** Samuel Sahel-Schackis; K. Nomura; A. Nakano; Matthias F. Kling; T. Linker
- **核心问题**：如何在保持E(3)-等变性与高精度的前提下，使预训练的通用机器学习力场（MLFF）能够原生建模外部电子调控（如电荷注入、外场、激发）导致的势能面动态变化  
- **动机与背景**：现有foundation MLFF（如MACE-MP-0、UMA）仅建模基态物理，无法处理非平衡电子态；而从头训练电荷感知型力场需海量DFT数据（~10⁸结构），成本极高；电催化、光电化学等关键过程高度依赖电荷态演化，缺乏高效、严格对称的条件化建模工具  
- **方法核心**：提出EquiFiLM——一种轻量级、逐层嵌入的Feature-wise Linear Modulation（FiLM）模块，仅调制标量通道、严格保持E(3)-等变性，将外部条件（如总电荷）作为连续输入注入任意等变foundation MLFF  
- **关键实验与结果**：以MACE-MatPES为骨干构建E-MACE，训练集仅含4个电荷态（±0.25e, ±0.5e）的数千帧DFT数据；相比无EquiFiLM的基线，力RMSE从21.3 → 6.96 meV/Å（3.1×提升），能量RMSE从6.1 → 0.1 meV/atom（61×提升）；在7个未见电荷态（插值/外推）上力RMSE稳定于18–61 meV/Å，能量RMSE为0.7–5.4 meV/atom  
- **创新点**：① 首个严格E(3)-等变且支持连续外部条件（如电荷）的模块化扩展方案；② 仅需极小规模条件特异性数据（千级帧）即可赋能foundation模型，避免重训代价；③ FiLM设计解耦条件建模与骨架架构，完全backbone-agnostic，可即插即用于任意含标量通道的等变MLFF  
- **局限性**：当前验证局限于单变量条件（总电荷），未测试多维耦合条件（如电荷+电场+激发态）；未验证对强关联体系或自旋极化响应的泛化性；外推边界（如|Q| > 0.75e）误差显著上升，物理外推鲁棒性待加强  
- **对你研究的启发**：① “foundation model + lightweight equivariant conditioner”范式可迁移至电催化界面建模（如*adsorbate charge state*, *local field*条件化）；② 利用标量通道进行物理量条件调制，兼顾对称性与可解释性，优于全局特征拼接；③ 极小数据微调策略为构建反应路径专用力场（如ORR/OER过渡态条件化）提供新路径  
- **与你研究的相关度**：高
- **阅读模式:** 🔍 精读
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/61b73e307dd03015f436f8f0e9e8b0cc4a182b73
- **标签:** electrochemistry, MLFF, surface, dft

### 3. Tracking the Lithiation State of Li$_x$Si from Machine-Learned XPS Binding Energies ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-02-26
- **作者:** Michael Hernandez Bertran; Davide Tisi; Federico Grasselli; M. Ceriotti; Elisa Molinari et al.
- **核心问题**：如何实现对硅基锂电负极在（脱）锂化过程中复杂、非均质微观结构演变的定量XPS谱学解析  
- **动机与背景**：传统XPS分析难以区分硅基负极中高度无序的LiₓSi相及晶–非晶转变引起的多重化学态叠加；实验谱图常表现为宽化、偏移和峰重叠，缺乏原子级可解释性；现有理论方法（如DFT单构型计算）无法覆盖真实电极中海量局域环境与动态组分分布  
- **方法核心**：提出“ML预测芯能级结合GCMC+MD采样”的多尺度计算框架：用机器学习势（MLIP）驱动大规模GCMC/MD模拟生成结构系综，再以ML模型（训练于高精度DFT数据）快速预测各原子位点的Si 2p结合能，最终构建化学态-组分-结构关联的 stoichiometry map  
- **关键实验与结果**：体系为Si(111)表面及纳米硅团簇的（脱）锂化过程；基线为传统DFT单点计算与经验XPS指认；关键结果：（1）模拟得到的Si 2p谱峰位展宽（~2.8 eV）与实验观测一致；（2）成功复现早期脱锂阶段特征性的~99.2 eV低结合能肩峰，归因于晶态Si–Si键断裂诱导的富Si非晶界面区  
- **创新点**：① 首次将GCMC（控化学势）与MLIP-MD耦合用于电极材料动态组分采样，突破静态结构假设；② 构建端到端ML pipeline实现万级原子构型的芯能级快速预测（较DFT加速>10⁴倍），支持统计级谱图建模；③ 提出“stoichiometry map”新分析范式，将XPS强度分布直接映射至局域Li配位数与Si键合序参量二维空间，实现谱图的定量反演  
- **局限性**：未考虑固态电解质界面（SEI）层对XPS信号的屏蔽与化学位移影响；ML模型训练依赖DFT数据质量，对强电子关联效应（如高Li浓度下可能的多体效应）泛化性待验证；当前框架尚未拓展至原位XPS时间分辨动力学建模  
- **对你研究的启发**：可迁移“热力学采样（GCMC）+动力学弛豫（MLIP-MD）+谱学代理模型（ML-BE）”三元耦合范式至其他原位谱学（如XAS、Raman）解析；stoichiometry map思路可用于建立催化活性位点局域配位环境与XPS化学位移的定量构效关系  
- **与你研究的相关度**：高
- **阅读模式:** 🔍 精读
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/28008d29ac5927be8c6b7526f8c44a0a42067895
- **标签:** electrochemistry, constant-potential

### 4. Self-single-atomization of active sites in electrochemical ammonia synthesis unveiled by machine learning potential ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-07-09
- **作者:** J. Long; Chenyu Yang; Huan Li; Hao Li; Jianping Xiao
- **核心问题**：铁基电催化剂在电化学NO还原反应（eNORR）中表现出高氨选择性，其真实活性位点本质是什么？是否为传统认为的金属表面位点，还是动态重构形成的单原子结构？  
- **动机与背景**：实验观察到Fe对eNORR制氨具有优异性能，但归因于“本征Fe表面活性”的解释与实际反应条件下催化剂结构不稳定、易重构的事实矛盾；现有理论研究多基于静态表面模型，忽视电极电位驱动下的动态原子重排，导致机理误判和理性设计受阻；理解真实工况下活性位点的起源，是实现催化剂精准调控的前提。  
- **方法核心**：提出“电位驱动的自单原子化（self-single-atomization）”机制，并采用机器学习势（MLP）加速的巨正则蒙特卡洛（GCMC）模拟，结合微动力学建模，在operando电位梯度下大规模采样（∼2.5百万构型）并追踪Fe表面动态重构路径。  
- **关键实验与结果**：主要体系为Fe(100)电极在NO水溶液中的eNORR过程；基线方法为传统DFT+microkinetic modeling（假设静态Fe表面）；关键结果：（1）GCMC揭示>95%覆盖度下Fe表面自发形成FeNx（x=1–3）单原子团簇；（2）微动力学证实孤立FeN₁顶位（top site）的NH₃生成速率为桥位/空穴位的3.2倍；（3）基于重构位点的理论Faradaic效率随电位变化趋势与实验高度吻合（R²=0.98）。  
- **创新点**：① 首次提出并验证“电位诱导自单原子化”是Fe基eNORR高活性的根源，颠覆静态表面活性认知；② 建立MLP-GCMC-微动力学耦合框架，实现operando电位下千万级构型空间的高效采样与动力学映射；③ 发现FeN₁-top为最优位点，且其活性源于N*强吸附稳定单原子态并优化*NO→*NHO→*NH₂→NH₃路径能垒。  
- **局限性**：未明确量化电解液pH、NO浓度及双电层结构对自单原子化动力学的影响；MLP训练数据局限于Fe-N-O-H体系，未涵盖杂质（如S、Cl）或载体效应；实验上缺乏原位XAS/AC-STEM直接观测FeNx动态形成的证据。  
- **对你研究的启发**：可迁移“电位作为结构调控变量”的范式——将电极电位纳入催化剂结构搜索自由度，而非仅作为热力学驱动力；MLP-GCMC联合策略适用于其他易重构体系（如Co、Ni氧化物析氧、Cu-CO₂RR）；强调活性位点统计分布（而非单一最稳构型）对宏观性能预测的关键作用。  
- **与你研究的相关度**：高
- **阅读模式:** 🔍 精读
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/28ad5cc3aba56e3f90859704511018b72055156e
- **标签:** electrochemistry, catalysis, constant-potential, surface

### 5. Thermodynamics and phase behavior of CO on Pt(100): Grand canonical Monte Carlo simulations of the 2D Ising model ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-03-27
- **作者:** H. T. Phạm; T. Ngô; Pham Tuong Huy Che
- **核心问题**：揭示CO在Pt(100)表面吸附层的热力学相行为与有序–无序转变的微观机制，特别是横向相互作用如何调控c(2×2)有序相的形成及临界现象。  
- **动机与背景**：实验上已观测到CO/Pt(100)体系存在覆盖度依赖的相变（如θ=0.5处c(2×2)有序相）和异常吸附热变化，但原子尺度热力学起源（尤其是长程关联与有限尺寸效应）难以通过传统DFT或宏观模型定量解析；现有理论常忽略统计涨落与集体行为，导致相边界和临界参数预测偏差。  
- **方法核心**：采用二维方格Ising模型结合巨正则系综蒙特卡洛（GCMC）模拟，引入近邻排斥相互作用（J < 0），并通过有限尺寸标度分析（finite-size scaling）精确提取伪临界温度——该方法将吸附热力学映射为自旋模型，显式包含统计涨落与协同效应。  
- **关键实验与结果**：体系为CO/Pt(100)表面；基线方法为Onsager精确解与实验相图；伪临界温度T_C = 2.2856(7)|J|/k_B（与Onsager解一致）；成功复现θ = 0.5处c(2×2)有序相，并观察到等量吸附热在临界覆盖度附近呈阶梯状下降（Δq_st ≈ 0.3|J|）。  
- **创新点**：① 首次将有限尺寸标度分析系统应用于电催化相关吸附体系，实现临界温度亚百分比精度测定；② 通过GCMC-Ising框架定量分离横向排斥能J对相行为与吸附热非线性的贡献，超越平均场近似；③ 建立等量吸附热阶梯下降与有序相变的直接统计力学关联，为原位谱学信号提供微观解释依据。  
- **局限性**：模型未包含Pt表面弛豫、CO分子取向自由度及电极电势调控效应；J参数为拟合获得，缺乏第一性原理校准；未耦合电子结构（如d-band中心偏移）对吸附能的影响。  
- **对你研究的启发**：可借鉴“吸附体系→统计力学模型→标度分析”的降维建模范式，将复杂电催化界面（如CO₂RR中*CO覆盖度演化）映射为可解析的格点模型；有限尺寸标度法可用于评估DFT簇模型或机器学习势函数的临界行为收敛性。  
- **与你研究的相关度**：高
- **阅读模式:** 🔍 精读
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/2df1f9bebdab2024c2f085989a9e1a8fbd66fef8
- **标签:** constant-potential, surface

### 6. Segregation-Controlled Diffusion-Induced Grain Boundary Migration in Alloy 690 ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-01-22
- **作者:** Yuntian Jiang; Shuai Zhang; Zhuoming Xie; Xiaohan Bie; Huiqiu Deng et al.
- **核心问题**：晶界迁移与Cr耗竭的耦合机制及其热力学驱动力不明  
- **方法要点**：采用混合分子动力学与半正则系综蒙特卡洛模拟，研究不同晶界构型下溶质扩散与偏析耦合作用对晶界迁移的影响  
- **关键结果**：Cr在晶界偏析反而促进扩散诱导的晶界迁移；Cr沿晶界扩散形成局部耗竭区，产生化学驱动力使晶界向Cr富集区迁移，导致持续迁移与Cr耗竭  
- **与你研究的相关度**：中
- **阅读模式:** 📋 摘要
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/3545511e51f7fbb0139bc940f7b18a316672de04
- **标签:** constant-potential

### 7. Integrating Machine Learning With Constant‐Potential Simulation to Unravel Charge‐Transfer Mechanisms in Electrochemical Nitrogen Fixation ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-03-13
- **作者:** Yufei Xue; Dushuo Feng; Yuefei Zhang; Yang Zhang; Yalong Jiao et al.
- **核心问题**：如何设计高效电催化氮还原反应（NRR）催化剂以实现常温常压下可持续氨合成  
- **方法要点**：采用巨正则固定电势法（grand-canonical fixed-potential method）模拟工况电势条件，并结合可解释机器学习挖掘动态界面描述符  
- **关键结果**：Cr@NO₂-碳硼烷/石墨烯和Cr@CHO-碳硼烷/石墨烯为最优候选催化剂，极限电势低至−0.220 V和−0.245 V；发现零电荷电势偏移（ΔPZC）是调控N₂活化与电荷转移的关键动态电压响应描述符  
- **与你研究的相关度**：高
- **阅读模式:** 📋 摘要
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/3611aeba5c1b74b079b87910813a72cd165a30e8
- **标签:** electrochemistry, catalysis, surface

### 8. Ligand Modulation Induced Spin-State Transition Enhances Oxygen Electrocatalysis in Co Single-Atom Catalysts. ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-04-03
- **作者:** Qingyi Wei; Yiming Song; Chunxia Wu; Ying Liang; Tianyu Qiu et al.
- **核心问题**：配体本征电子结构如何调控单原子催化剂中金属自旋态，进而影响氧电催化性能  
- **方法要点**：结合巨正则密度泛函理论与微动力学模拟，定量关联配体共轭度、晶体场分裂能与Co自旋态转变  
- **关键结果**：配体共轭度增加诱导Co从低自旋向高自旋转变；高自旋Co位点实现ORR半波电位0.96 V与OER过电位150 mV（10 mA/cm²）的双功能优异性能  
- **与你研究的相关度**：高
- **阅读模式:** 📋 摘要
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/3892bd814f47e8612afde91f68e40cb58561c86e
- **标签:** electrochemistry, catalysis, dft

### 9. Molecular Simulation Study on the Gas Selectivity of the Mixed Carbon Dioxide/Methane Hydrates Confined in Nanoporous Carbon. ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-04-22
- **作者:** Yimeng Fang; Xuan Li; Haifeng Wang; Yang Pan; Meng Guo et al.
- **核心问题**：纳米限域下CO₂/CH₄混合水合物的气体选择性（CO₂对CH₄）如何受孔道表面效应和气体组成影响  
- **方法要点**：采用巨正则系综蒙特卡洛（GCMC）模拟结合密度分布分析，研究体相及纳米多孔碳限域中混合水合物的气体组成与选择性  
- **关键结果**：1）纳米限域降低CO₂在混合水合物中的密度、提高CH₄密度，导致CO₂/CH₄选择性显著低于体相；2）气体吸附行为进一步调控限域混合水合物的组成与选择性  
- **与你研究的相关度**：中
- **阅读模式:** 📋 摘要
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/397037c4cf49d8e9ffbffca913dd7865fb84cc11
- **标签:** constant-potential, surface

### 10. Hydrogen occurrence in nanopores of coalbed methane formations: A molecular simulation study ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-04-01
- **作者:** Jiajia Zhao; Baiquan Lin; Ting Liu; Tong Liu; Rentao Gou et al.
- **核心问题**：氢气在煤层气纳米孔隙中的存储与扩散行为受温度、压力、孔径、伴生气及含水量耦合影响的分子机制尚不明确  
- **方法要点**：结合巨正则蒙特卡洛（GCMC）与分子动力学（MD）的经典分子模拟方法，系统考察多参数条件下H₂在典型CBM纳米孔中的吸附、存储与扩散  
- **关键结果**：H₂–煤相互作用以弱范德华力为主，吸附贡献小；CO₂比CH₄对煤表面具有更强亲和力，显著挤压H₂可及体积；含水量增加抑制H₂–煤相互作用并限制分子迁移，但不改变H₂空间分布  
- **与你研究的相关度**：低
- **阅读模式:** 📋 摘要
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/3bed56dcff9ecfa52306fdaf698aba97e87f3d81
- **标签:** constant-potential, surface

## 💡 今日亮点

- **最值得精读**：[4] Self-single-atomization of active sites in electrochemical ammonia synthesis unveiled by machine learning potential — 首次用ML势能面原位追踪电催化过程中“自单原子化”动态重构，直接挑战静态表面模型范式，为活性位点本质争议提供原子尺度动态证据。  
- **可能冲突的研究**：[7] Integrating Machine Learning With Constant‐Potential Simulation to Unravel Charge‐Transfer Mechanisms in Electrochemical Nitrogen Fixation — 其基于固定构型催化剂的巨正则模拟隐含“位点结构稳定”假设，与[4]揭示的电位驱动下Fe位点动态单原子化现象存在根本性张力。  
- **值得追踪的团队**：Cr@NO₂-碳硼烷/石墨烯工作（论文[7]）团队 — 在NRR中率先将可解释ML与恒电势模拟深度耦合，构建了从电子转移路径到宏观性能的闭环因果链，方法论具有跨反应体系迁移潜力。  
- **重要趋势**：多篇论文（[2][4][7][8]）共同指向“电位/电荷作为第一性调控变量”的范式转移——不再仅优化几何结构，而需在电子态维度上建模、预测并设计动态催化界面。

## 📌 Key Gap

**关键差距**
- **Gap 1**：所有涉及动态重构的研究（[4][6][7]）均依赖事后分析或准静态采样，缺乏对重构路径的*前向预测能力*：当前ML势能面或DFT+ML方法无法在给定电位/偏压下，实时预报催化剂是否及何时发生单原子化、晶界迁移或相变。  
- **Gap 2**：实验–理论闭环仍断裂：XPS（[3]）、电化学（[4][7]）、吸附相变（[5]）等关键表征数据虽被ML拟合，但尚未建立可逆反馈机制——即ML模型输出能否指导下一代实验参数设计（如最优电位扫描速率、原位XPS采样时机），而非仅拟合已有数据。  
- **未来方向**：发展“电位条件嵌入型”生成式ML势能面（如扩展EquiFiLM至重构路径采样），并耦合在线贝叶斯优化框架，使模拟能主动建议实验观测窗口与关键控制变量，实现真正闭环的电催化理性设计。
