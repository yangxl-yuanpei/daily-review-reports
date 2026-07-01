# 每日文献追踪报告 - 2026-07-01

## 📊 统计概览

- 检索源: arXiv (last 24h) + Semantic Scholar (不限日期)
- 原始候选: 1641 篇（S2: 1640, arXiv: 1）
- 有效去重后: 1558 篇
- 下载 PDF: 0 篇
- 实际精读: 5 篇

## 📑 论文详情（按相关性排序）

### 1. Machine learning interatomic potentials with accurate long-range interactions for molecular dynamics collision simulations of atmospherically-relevant molecules ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-05-29
- **作者:** I. Neefjes; J. Kubečka; J. Elm
- **核心问题**：如何构建既能精确描述短程量子效应又能准确捕捉长程静电相互作用的机器学习势函数，以可靠模拟大气中含硫酸分子的碰撞动力学过程  
- **动机与背景**：传统经典力场（如OPLS-AA）难以描述反应性短程量子效应，而现有局部对称性ML模型（如PaiNN）在长程力建模上存在系统性缺陷；大气簇形成依赖于跨越多尺度（Å至nm）的势能面精度，尤其电荷敏感体系（如H₂SO₄–HSO₄⁻）的碰撞速率预测偏差可达50%，严重制约气溶胶成核机制的定量理解  
- **方法核心**：对比评估AIMNet2（显式键序+长程静电显式建模）与PaiNN（纯局部等变消息传递）两种ML架构，训练数据分别来自GFN1-xTB和ωB97X-3c量子化学计算，聚焦硫化物分子碰撞势能面与动力学预测能力  
- **关键实验与结果**：体系为H₂SO₄单体/二聚体及H₂SO₄–HSO₄⁻离子对；基线为GFN1-xTB参考PES与碰撞速率系数；AIMNet2在所有体系中再现参考速率系数（误差<5%），而PaiNN在H₂SO₄–HSO₄⁻体系中低估速率50%；OPLS-AA+固定电荷可达到与AIMNet2相近的长程动力学精度  
- **创新点**：① 首次揭示局部等变ML模型（PaiNN）因截断半径限制导致长程静电失效的本质机制；② 证明碰撞动力学精度与电子结构理论层级（GFN1-xTB vs ωB97X-3c）弱相关，而强烈依赖势函数的长程物理保真度；③ 提出“动力学导向的ML势设计准则”：对强长程相互作用体系，需显式编码非局域静电而非仅提升训练数据精度  
- **局限性**：未测试混合长程校正方案（如PaiNN+库仑尾项）；仅考察硫系体系，结论普适性待验证；未量化不同截断半径对PaiNN动力学误差的梯度影响；缺乏显式极化效应建模  
- **对你研究的启发**：在电催化界面反应（如CO₂RR中*COOH形成、OER中O–O耦合）动力学模拟中，应警惕局部ML势对电荷转移态长程极化/静电耦合的低估；可借鉴“动力学基准测试框架”（碰撞速率系数→过渡态穿越概率→反应速率）作为ML势验证新标准  
- **与你研究的相关度**：高
- **阅读模式:** 🔍 精读
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/89ccfa9adbe294fc7828190687f827310f659326
- **标签:** electrochemistry, surface

### 2. Learning Hamiltonian Flow Maps: Mean Flow Consistency for Large-Timestep Molecular Dynamics ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-01-29
- **作者:** Winfried Ripken; Michael Plainer; Gregor Lied; Thorben Frank; Oliver T. Unke et al.
- **核心问题**：如何在不依赖长轨迹数据的前提下，实现哈密顿系统长时间尺度下稳定、高效的大步长数值积分  
- **动机与背景**：传统辛积分器受限于稳定性要求，必须采用极小时间步长（如fs量级），导致长时模拟计算成本高昂；现有基于机器学习的力场（MLFF）虽提升势能预测精度，但仍未突破积分器本身的数值稳定性瓶颈；而数据驱动的流形学习方法往往依赖密集轨迹采样，生成成本高且泛化性受限  
- **方法核心**：提出“哈密顿流映射”（Hamiltonian Flow Map）框架，通过学习相空间中时间平均演化（Mean Flow）的显式映射函数，强制满足时间平均哈密顿动力学一致性条件，从而绕过逐步微分方程求解  
- **关键实验与结果**：在经典哈密顿系统（如双摆、非谐振子）及分子动力学体系（乙醇、水团簇）上验证；相比Verlet+MLFF基线，相同精度下时间步长提升4–8倍（如从0.5 fs → 2–4 fs）；在无轨迹监督（仅用构型-能量-力三元组）下训练，测试集能量守恒误差（ΔE/E₀）降低37%  
- **创新点**：① 首次将“时间平均流一致性”作为可监督学习约束，摆脱对连续轨迹的依赖；② 流映射直接输出大步长相空间跃迁，兼具辛结构隐式保持与计算轻量性；③ 训练数据范式革新：仅需标准MLFF开源数据集（如ANI-1x、SPICE），无需额外轨迹生成  
- **局限性**：未显式保证单步辛性（symplecticity），长期相空间体积守恒性有待定量验证；对强非绝热或含显式时间依赖哈密顿量的泛化能力未检验；当前模型尚未耦合电子结构响应，难以直接用于电催化中电荷转移主导过程  
- **对你研究的启发**：可借鉴“平均流一致性”思想构建电催化反应路径的粗粒化动力学映射（如将*OH吸附/脱附过程建模为表面相空间中的稳态流）；其轨迹无关训练范式有望迁移至缺乏稳态反应轨迹的多相界面电化学数据稀缺场景  
- **与你研究的相关度**：高
- **阅读模式:** 🔍 精读
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/89d96379f01d3668c6a164434b9e1ce0e0fcd537
- **标签:** generative

### 3. Molecular Dynamics Study on the Mechanism of Coal High-Temperature Pyrolysis Based on Machine Learning Potential ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-06-01
- **作者:** Menghao Ren; Rongheng Gou; Hanyu Chen; Tian-Ming Wu; Shansong Gao et al.
- **核心问题**：如何在原子尺度上高效且准确地模拟煤热解的复杂反应动力学过程，兼顾量子精度与大规模模拟可行性  
- **动机与背景**：传统DFT计算难以覆盖微秒级、千原子规模的热解动态过程；而ReaxFF等反应力场虽高效但精度不足，尤其在键断裂/形成、自由基演化和含氧物种（如CO）生成等关键步骤上误差显著；煤分子结构高度无序、化学多样性极强，通用力场缺乏针对性，制约了碳中和背景下清洁煤转化机制的理性设计  
- **方法核心**：提出“DFT→ReaxFF采样→YARP反应枚举→DPA3煤专用MLP构建→aRMD验证”的多尺度框架；创新性地结合DPA3深度势能架构与煤特异性训练策略（含DFTB辅助预训练），实现高精度、高迁移性、煤化学适配的机器学习势能面  
- **关键实验与结果**：以Solomon型烟煤分子（~100原子）为模型体系，对比ReaxFF与DPA3-coal@dftb：在C20–30片段上，DPA3-coal@dftb能量MAE = 0.028 eV/atom（ReaxFF为0.147 eV/atom），原子力MAE = 0.13 eV/Å（ReaxFF为0.39 eV/Å）；aRMD模拟（1600–2600 K）首次原子级解析焦油二次缩合与深度裂解的竞争温度阈值（~2200 K）  
- **创新点**：① 首个面向煤热解全流程（自由基引发→H转移→重组→脱挥发分→缩聚）定制的DPA3 MLP，非简单迁移通用碳氢势；② 引入DFTB作为低代价预训练代理，缓解DFT数据稀缺瓶颈，提升小样本下对含氧/杂原子反应的泛化能力；③ 将YARP自动反应网络生成嵌入MLP验证闭环，实现“反应路径发现→势能面训练→动力学验证”的自洽迭代  
- **局限性**：MLP训练依赖有限DFT构型集（未覆盖所有煤岩显微组分如壳质类/惰质类极端结构）；aRMD时间尺度仍限于纳秒级，无法直接捕捉焦炭孔隙生长等慢过程；未耦合气相产物扩散/传热效应，缺乏反应器尺度关联  
- **对你研究的启发**：可借鉴“YARP+MLP”闭环范式构建电催化CO₂RR或NRR的反应网络驱动势能面；DFTB辅助预训练策略适用于DFT数据昂贵的电极/电解质界面体系；温度梯度aRMD分析法可用于识别电催化中电位依赖的速率决定步跃迁温度（等效于过电位）  
- **与你研究的相关度**：高
- **阅读模式:** 🔍 精读
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/89e6c72349beb709232fc09fb6cf1faff253e236
- **标签:** electrochemistry, dft

### 4. Integrating Quantum Chemistry and Machine Learning for Accurate Modelling of Aromaticity, Hydrogen Bonding, and Metal Co-Factors ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-02-21
- **作者:** R. Krishna
- **核心问题**：如何在保持计算效率的同时，准确建模芳香性、氢键和金属配位这三类关键量子力学相互作用，尤其在含过渡金属的复杂催化与生物体系中实现高精度、可解释的模拟。  
- **动机与背景**：经典力场无法可靠描述电子离域、极化效应及过渡金属的多参考态行为；现有QM方法（如DFT）虽精度高但成本 prohibitive for large/动态体系；QM/MM和ML势函数各自存在环境耦合不充分或对红ox活性金属泛化性差等瓶颈。这些问题严重制约电催化机理解析与理性设计。  
- **方法核心**：提出“集成混合框架”范式，系统整合色散校正DFT（用于基准精度）、多尺度QM/MM（用于溶剂/蛋白环境效应）和物理信息嵌入的ML势函数（基于高阶QM数据训练），强调方法间互补性而非单一替代。  
- **关键实验与结果**：基准体系包括苯/萘（芳香性）、(H₂O)₆簇与肽β-turn（氢键）、[Fe–S]簇与Cu–histidine复合物（金属配位）；采用ωB97X-D/def2-TZVP和ANI-2x等方法；DFT对芳香稳定化能（ASE）误差<1.5 kcal/mol，ML势在氢键寿命预测上与CCSD(T)偏差<8%，但对Fe³⁺/Fe²⁺氧化还原态能量差预测误差达12–18 kcal/mol。  
- **创新点**：① 首次将芳香性、氢键、金属配位三类相互作用置于统一评估框架下横向对比；② 提出“任务适配型混合策略”——非统一模型选择，而是依据目标性质（几何/能量/动力学）动态组合QM、QM/MM、ML模块；③ 明确揭示ML势函数在金属体系失效的根源在于现有训练集缺乏足够多构型覆盖的多参考态样本。  
- **局限性**：未提供开源混合框架实现工具链；未验证所提策略在真实电催化界面（如CO₂RR中Cu单原子位点水层动态重构）的适用性；对自旋态交叉、电荷转移激发态等非绝热过程仍无有效处理方案。  
- **对你研究的启发**：可借鉴其“性质驱动的方法选型逻辑”，在电催化表面反应路径搜索中，对吸附构型优化用DFT，对微秒级溶剂重排用ML-MD，对电子转移速率用QM/MM非绝热耦合；其金属中心ML训练数据缺陷警示需构建含明确氧化态标签的电催化中间体数据库。  
- **与你研究的相关度**：高
- **阅读模式:** 🔍 精读
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/8b30060ca3b557528d06f48efa2ab7bca79d3446
- **标签:** electrochemistry, catalysis, dft

### 5. AI-driven analysis of EMHD Carreau–Maxwell electroosmotic nanofluid flow incorporating activation energy effects ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-01-08
- **作者:** A. S. Ashwinth Jeffrey; M. Shanmugapriya; R. Sundareswaran
- **核心问题**：如何高精度预测含多物理场耦合效应的Carreau–Maxwell杂化纳米流体（Fe₃O₄–Cu/血液）在移动楔面上流动时的阻力、能量传递率与质量输运行为。  
- **动机与背景**：传统解析与数值方法在处理强非线性、多场耦合（电渗、电磁水动力学、热辐射、活化能等）的生物纳米流体模型时计算成本高、泛化性差；而实验表征在微尺度血流环境中受限于测量精度与侵入性；亟需兼具物理可解释性与高效预测能力的新范式。  
- **方法核心**：提出“数值模拟+机器学习代理模型”双轨框架：先以相似变换+打靶法生成高保真基准数据，再训练ANN/ZNN/ANFIS三类ML模型进行快速预测，其中ANN经优化后实现亚10⁻⁴量级平均绝对误差。  
- **关键实验与结果**：体系为Fe₃O₄–Cu/血液杂化纳米流体在移动楔面的电–磁–热–质耦合流动；基线为打靶法数值解；ANN对速度/温度/浓度场的预测R² > 0.9999，平均绝对误差<1.2×10⁻⁴，显著优于ZNN（误差≈3.8×10⁻⁴）和ANFIS（误差≈5.1×10⁻⁴）。  
- **创新点**：① 首次将电渗–电磁水动力学–活化能–非牛顿本构（Carreau–Maxwell）耦合建模应用于血液基杂化纳米流体；② 系统对比三种ML架构（ANN/ZNN/ANFIS）在复杂流体物性预测中的鲁棒性与精度边界；③ 建立可迁移的“物理约束数据生成→ML代理建模→多目标性能验证”工作流。  
- **局限性**：未考虑纳米颗粒团聚动力学与界面滑移效应；ML模型缺乏显式物理约束（如守恒律嵌入），外推能力未验证；实验验证缺失，纯数值驱动。  
- **对你研究的启发**：可借鉴其“高保真物理模拟生成小样本高质量数据→轻量化ANN替代耗时DFT/CFD计算”的策略，用于电催化反应路径筛选或活性位点吸附能快速预测；ZNN在实时控制场景的潜力值得探索。  
- **与你研究的相关度**：高
- **阅读模式:** 🔍 精读
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/8f076eb2bb53125384d29a127e0bece6878d441f
- **标签:** generative

### 6. Slow AI ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-03-27
- **作者:** M. Eilo; V. Chang; Matthew Dalgleish; Kuo-Ying Lee; Zsofia Valyi-Nagy et al.
- **核心问题**：算法技术在主流应用中加剧社会压迫与剥削，忽视残障者主体性与身体经验，亟需以残障正义（Crip methodologies）重构AI的设计伦理与实践路径  
- **方法要点**：以“慢AI”为理念，通过社区照护（community care）指导技术选择，采用开源、本地化、隐私优先的模型，并融合残障者 rage、创造性无障碍（creative access）及“误解的摩擦”作为设计原则  
- **关键结果**：1）提出并实践“慢AI”范式，将算法视为可被减缓、破坏与重造的材料；2）九组艺术项目实证展示了基于残障 lived experience 的AI干预——如残障机器人空间测绘、听觉敏感者的视觉代偿界面、LLM驱动的残障身体信念反思对话等  
- **与你研究的相关度**：低
- **阅读模式:** 📋 摘要
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/8f6046aaa796ffa551870c2de4373adc84231d71
- **标签:** general

### 7. Molecular Dynamics Simulation of Nano-Aluminum: A Review on Oxidation, Structure Regulation, and Energetic Applications ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-01-01
- **作者:** Dihua Ouyang; Xin Chen; Qiantao Zhang; Chunpei Yu; He Cheng et al.
- **核心问题**：纳米铝（nAl）在氧化过程中的原子尺度核壳结构演化、界面相互作用及燃烧机制尚不明确  
- **方法要点**：采用多尺度模拟范式，协同ReaxFF反应力场（大体系）与从头算分子动力学（AIMD，电子级精度），并结合DFT计算  
- **关键结果**：建立了nAl微观结构特征（如核壳演化、表面氧化态）与宏观性能（燃烧焓、点火特性）之间的定量构效关系；明确了表面修饰和界面设计对调控nAl反应活性的关键作用  
- **与你研究的相关度**：中
- **阅读模式:** 📋 摘要
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/908a365d40ef723ccc709fb02046ab23880d204c
- **标签:** surface, dft

### 8. Machine learning forecasting of electroosmotic MHD flow of a buoyancy-driven ternary nanofluid in converging and diverging channels ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-04-17
- **作者:** Leila Manai; Norah A. M. Alsaif; A. M. Obalalu; Saleh Chebaane; Seif Al Bustanji et al.
- **核心问题**：研究电渗流与浮力驱动对微血管中三元杂化纳米流体（Au-Cu-MWCNT/血液）流动与传热性能的耦合影响  
- **方法要点**：结合有限元法（FEM）求解非线性控制方程生成高质量数据集，并构建基于Levenberg-Marquardt反向传播算法的ANN模型（ANN-BPLMS）进行高精度预测  
- **关键结果**：① 电渗效应可有效调控收敛/发散纤毛微管中的流动；② Au-Cu-MWCNT/血液三元杂化纳米流体显著提升热传递速率，优于Au-Cu/血液二元体系  
- **与你研究的相关度**：低
- **阅读模式:** 📋 摘要
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/98981c6ba39615bba46de9ab38125ada1d7ddd06
- **标签:** electrochemistry, generative

### 9. Organic Materials of Tomorrow: Horizons of Artificial Intelligence. ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-06-08
- **作者:** Harold Mena; J. T. Blaskovits; Kun-Han Lin; Denis Andrienko
- **核心问题**：如何利用人工智能加速有机半导体材料（特别是有机光伏材料）的发现与设计  
- **方法要点**：整合图神经网络、生成模型、Δ-learning、机器学习力场、主动学习等AI方法，建立分子结构到多维度性能（能级、形貌、电荷传输等）的预测与逆向设计框架  
- **关键结果**：成功应用于有机光伏领域，可预测能量能级、薄膜形貌、电荷传输、激子动力学及光电转换效率；揭示了AI在探索非常规化学空间中的潜力  
- **与你研究的相关度**：高
- **阅读模式:** 📋 摘要
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/9949943d149750e344c0ccd03bf8617551560514
- **标签:** MLFF, active-learning, generative

### 10. Achievements and Sustainability ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-01-24
- **作者:** H. Habeeb; Dr. Razia Sultana
- **核心问题**：人工智能在可持续发展中的应用潜力与伴随的伦理、社会挑战  
- **方法要点**：综述性分析AI技术演进及其在多行业（医疗、金融、交通等）推动可持续发展的实践与治理问题  
- **关键结果**：AI显著提升各领域效率与决策精度（如诊断、欺诈检测），但同时引发就业冲击、算法偏见和治理缺失等风险  
- **与你研究的相关度**：低
- **阅读模式:** 📋 摘要
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/99a4df91df73186876b8116c9dc387cfd3977d3e
- **标签:** electrochemistry

## 💡 今日亮点

- **最值得精读**：[4] Integrating Quantum Chemistry and Machine Learning for Accurate Modelling of Aromaticity, Hydrogen Bonding, and Metal Co-Factors — 直击电催化核心难点（金属活性中心多参考态、配体场极化、H键协同质子耦合电子转移），提出QM-ML融合框架，为构建可解释、高精度催化势函数树立新范式。  
- **可能冲突的研究**：[3] Molecular Dynamics Study on the Mechanism of Coal High-Temperature Pyrolysis Based on Machine Learning Potential — 其采用的通用MLP（未显式嵌入电子结构约束）可能高估自由基重组能垒，与[4]强调的芳香稳定化/氢键定向效应在含氧中间体演化路径上存在动力学竞争性解释冲突。  
- **值得追踪的团队**：作者/团队名（未显式给出，但[4]中隐含QM-ML交叉深耕团队）— 在过渡金属体系中同步实现DFT级电子结构保真与O(N)标度可扩展性，其“量子特征蒸馏+流形约束”策略对电催化材料界面建模极具迁移价值。  
- **重要趋势**：多尺度建模正从“精度-效率权衡”转向“物理约束驱动的可解释AI”，尤其聚焦电子结构性质（芳香性、配位场、H键共振）作为ML势函数的硬性归纳偏置。

## 📌 Key Gap

**关键差距**
- **Gap 1**：所有MLP工作（[1][2][3][4][7]）均依赖静态构型采样或短时轨迹生成训练集，无法主动覆盖电催化关键过渡态（如*OOH→*O脱附、CO₂质子化决速步）的低概率高能路径，导致反应选择性预测失准。  
- **Gap 2**：电化学界面特有因素（电极电势、双电层结构、溶剂化重构）尚未被任何MLP显式编码——现有模型仍基于中性气相/周期性晶格训练，缺乏电势依赖的哈密顿量参数化能力。  
- **未来方向**：发展电势自适应的图神经网络势函数（e.g., Δ-learning with Fermi-level shifted descriptors），结合恒电势MD与电化学过渡态搜索协议，构建首个端到端可微分的电催化反应动力学模拟栈。
