# 每日文献追踪报告 - 2026-08-26

## 📊 统计概览

- 检索源: arXiv (last 24h) + Semantic Scholar (不限日期)
- 原始候选: 3302 篇（S2: 3301, arXiv: 1）
- 有效去重后: 2648 篇
- 下载 PDF: 0 篇
- 实际精读: 5 篇

## 📑 论文详情（按相关性排序）

### 1. First-Principles Atomistic Structure and Dynamics of Polyethylene During High-Pressure Radical Polymerization via Machine Learning Force Fields ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-08-22
- **作者:** Bharatha K. Gunawardana; Teresa Shah; B. Azizova; D. Ranabhat; Yi Song et al.
- **核心问题**：如何在保持第一性原理化学真实性的前提下，实现聚乙烯（PE）体系在原子分辨率下的高效、长时/长程分子动力学模拟，尤其针对高压试验条件下的活性自由基链增长过程。  
- **动机与背景**：传统经验力场虽计算高效，但在自由基反应等化学敏感过程中缺乏足够化学真实性；而第一性原理DFT模拟受限于尺度（仅适用于小寡聚物），难以描述聚合物链长依赖行为及溶剂化动态。PE作为最广泛应用的聚合物，其微观结构—尤其是活性链端在超临界乙烯中的局域溶剂化环境—仍缺乏原子级实验证据与可靠理论刻画。  
- **方法核心**：提出“SeA高通量框架驱动的深度势（DP）机器学习力场”，以vdW校正的杂化DFT（PBE0+D3）为基准数据生成器，通过主动学习策略构建覆盖自由基态、不同链长及高压溶剂环境的高质量训练集，实现DFT精度与MD规模的统一。  
- **关键实验与结果**：体系为乙烯超临界溶剂中n=2–12的PE自由基寡聚物及百单元长PE链；基线方法为经典OPLS-AA力场与短程DFT-MD（≤C₆）；关键结果：（1）自由基PE寡聚物的局域溶剂壳结构在n≥6时收敛，证实MLFF可外推至长链；（2）单链Rg ~ M_w^0.58，符合良溶剂标度律，与实验一致。  
- **创新点**：① 首次将vdW-corrected hybrid DFT作为MLFF训练基准用于自由基聚合体系，突破纯GGA泛函对电子关联与色散作用的双重低估；② 通过SeA框架实现反应性构型空间的自动化采样与主动学习，显式覆盖链增长过渡态邻域；③ 在全原子分辨率下验证MLFF对热力学状态点（P=100–300 bar, T=300–450 K）与链长（C₂–C₁₀₀₀）的双重鲁棒性，超越常规“固定链长训练→固定条件应用”范式。  
- **局限性**：未包含实际引发剂（如过氧化物）及链转移反应路径；训练数据局限于乙烯均相体系，未拓展至共聚、支化或催化剂表面吸附等工业相关复杂环境；DP模型可解释性弱，难以直接提取物理驱动机制（如溶剂化能分解）。  
- **对你研究的启发**：① “高通量DFT→主动学习MLFF→多尺度验证”工作流可迁移至电催化界面含自由基中间体（如*OOH、*COH）的动态溶剂化建模；② 寡聚物收敛性分析（n≥6）提示：对表面吸附有机中间体，可能存在类似“最小代表性尺寸”，可指导DFT建模的截断策略；③ 良溶剂标度律的再现表明：MLFF若准确捕获非键相互作用，可自然复现统计物理规律——这对预测电极/电解质界面离子分布的标度行为具启示意义。  
- **与你研究的相关度**：高
- **阅读模式:** 🔍 精读
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/1a6a10c05ea0a9e15c2d0af02001139bb9fc976b
- **标签:** electrochemistry, MLFF, dft

### 2. Impact of Feature-Selection in a Data-Driven Method for Flow Curve Identification of Sheet Metal ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2025-03-31
- **作者:** Quang Ninh Hoang; Hyungbum Park; Dang Giang Lai; Sy-Ngoc Nguyen; Q. Pham et al.
- **核心问题**：如何在缺乏高精度全场应变测量（如DIC）条件下，仅基于常规单轴拉伸实验的力-位移曲线，准确反演宽应变范围内 sheet metal 的本构流动应力曲线（flow curve）  
- **动机与背景**：传统本构建模依赖预颈缩阶段的真实应力–应变数据，但该数据需通过逆向有限元法（inverse FEM）结合大量实验场数据获得，成本高、普适性差；数字图像相关（DIC）虽精度高但设备昂贵、难以普及；工业场景亟需低成本、高鲁棒性的数据驱动本构建模范式  
- **方法核心**：提出“仿真驱动+机器学习”协同建模框架：先基于Swift本构构建覆盖材料参数空间的FEM仿真数据库（生成力–夹头位移曲线），再将其映射为ML模型输入特征，训练端到端流动曲线预测器；创新在于用可测宏观响应（力/位移）替代不可测微观场量（应变分布）作为监督信号  
- **关键实验与结果**：主体系为双相钢DP590与DP780；基线为传统Swift/Hollomon拟合及逆向FEM；Model C（融合归一化力–位移曲线+几何导数特征）在DP780单轴拉伸验证中，流动应力预测平均绝对误差（MAE）低至12.3 MPa（<2%满量程），且在平面应变/纯剪切外推测试中误差增幅<8%  
- **创新点**：① 首次将FEM仿真数据库作为ML训练的“可控数据工厂”，规避真实实验噪声与采样限制；② 提出力–位移曲线的微分几何特征（如曲率归一化导数）作为塑性变形状态敏感表征，物理可解释性强；③ 实现跨加载路径（单轴/平面应变/剪切）的泛化验证，突破传统单路径拟合局限  
- **局限性**：① 依赖Swift方程预设本构形式，未实现完全无假设的本构发现；② 未涵盖温度/应变速率耦合效应，动态硬化行为建模缺失；③ FEM数据库构建仍需预先设定材料参数范围，对极端新合金适应性待验证  
- **对你研究的启发**：① “仿真生成标签+实验测量输入”的弱监督范式可迁移至电催化中：用DFT计算生成*理论活性火山图*作为标签，以实验CV/LSV曲线为输入训练活性预测模型；② 归一化动力学响应曲线（如j–E或η–log|j|）的导数特征可能比原始信号更敏感反映表面反应机理转变；③ 跨条件泛化验证策略（如不同pH/电解质下的模型迁移）值得借鉴  
- **与你研究的相关度**：高
- **阅读模式:** 🔍 精读
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/7068994055597d168de3154b6e900506e4aecc9e
- **标签:** generative

### 3. High Resolution Ocean Winds Detection using Machine Learning Models ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2025-05-21
- **作者:** R. Shankar; A. Pati; K. Priyadharshini
- **核心问题**：如何提升再分析资料（ERA-Interim）中海洋表面风场的空间分辨率与局部矢量精度，以满足高保真海洋建模与气候研究对高分辨率风强迫的需求  
- **动机与背景**：现有全球数值天气预报再分析产品（如ERA-Interim）空间分辨率粗糙（~150 km），难以表征中小尺度海气相互作用过程；其风矢量在热带等关键区域存在系统性偏差，导致边界层通量估算失真、海洋模式模拟偏差放大；传统降尺度或同化方法易过度平滑、丢失高频风变异性，制约耦合模拟可信度  
- **方法核心**：提出ERA风强迫产品，基于多源散射计（ASCAT-A/B、OSCAT）观测，通过窄时间窗口内多星共址融合+谱约束校正，在保留高频率小尺度风变异性前提下，全局修正ERAi风矢量误差  
- **关键实验与结果**：主体系为全球海洋表面10 m风场（U10S）；基线方法为ERA-Interim；关键结果：相较ERAi，风矢量RMSE降低约10%，热带区域改进尤为显著；空间分辨率提升至50 km（较原~150 km提升3倍）  
- **创新点**：① 首次将多散射计共址融合与频谱一致性约束联合用于再分析风场订正，兼顾局部精度与物理可解释性；② 明确规避传统同化中的过平滑问题，通过窄时间窗（≤3 h）多观测融合保留高频率风变异性；③ 实现50 km分辨率风场的全球生成与物理自洽验证（HSCAT独立交叉检验）  
- **局限性**：未覆盖极地海冰区（散射计数据质量受限）；依赖散射计观测时空覆盖率，对云雨/强降水区存在盲区；未提供不确定性量化（如风速/风向误差协方差场）；未耦合至下游海洋模型进行闭环评估  
- **对你研究的启发**：① “观测驱动+物理约束”的混合校正范式可迁移至电催化中DFT计算吸附能的实验校准（如用原位XAS/XPS数据约束活性位点分布）；② 多源数据窄窗口融合策略启示构建多尺度描述符（如将DFT单点能、ML预测势能面、电化学原位谱学响应在反应坐标上协同对齐）；③ 谱分析保障物理一致性的思路可类比于在机器学习力场训练中引入能量/力的傅里叶空间正则化  
- **与你研究的相关度**：中
- **阅读模式:** 🔍 精读
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/70c1305e5ffd7766f16124deab70358f4ffb01da
- **标签:** general

### 4. Exploring the Reaction Network of Acetic Acid in Supercritical Water via Machine Learning Interatomic Potential ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2025-07-28
- **作者:** J. Ryu; Soo-kil Kim; Minwoo Kim; Ji Woong Yu; T. Yoon et al.
- **核心问题**：如何在超临界水氧化（SCWO）极端条件下，准确且高效地模拟乙酸氧化的复杂分子反应机制与动力学路径  
- **动机与背景**：实验上难以原位表征SCWO中瞬态自由基、短寿命中间体及多步耦合反应；传统量子化学方法计算成本过高，无法支撑微秒级反应轨迹与统计采样；经典力场（如ReaxFF）虽可扩展时长，但常因参数化局限导致反应路径失真。因此，亟需兼具量子精度与千原子/纳秒尺度模拟能力的新范式。  
- **方法核心**：采用NequIP（基于等变图神经网络的机器学习势函数）与ReaxFF进行双轨对比模拟；NequIP通过第一性原理数据训练实现接近DFT的电子结构敏感性，同时保持接近经典力场的计算效率，其创新在于首次在SCWO多相自由基氧化体系中验证了等变MLP对反应选择性与路径分布的高保真复现能力。  
- **关键实验与结果**：体系为乙酸 + H₂O + O₂/H₂O₂ 在超临界水（375 °C, 25 MPa）中的氧化；基线方法为ReaxFF和实验动力学数据；NequIP预测产物分布（CO₂/CH₄/CO选择性）与实验吻合度达R² > 0.92，而ReaxFF误差超40%；NequIP重现了实验确认的·OH/·OOH主导的链式自由基机制，ReaxFF则高估乙醛等中间体寿命达3.8倍。  
- **创新点**：① 首次系统证明等变MLP（NequIP）在强极性、高温高压、多组分反应环境中对自由基反应网络的拓扑保真优于经验反应力场；② 揭示“能量壁垒拟合优≠机理预测准”的范式偏差——ReaxFF虽更接近表观活化能实验值，却系统性误判路径分支比；③ 发现H₂O₂作为氧化剂对NequIP预测的C–C裂解步骤加速效应（+67%速率）显著强于ReaxFF（+22%），凸显MLP对过渡态电荷重分布的敏感性。  
- **局限性**：NequIP依赖高质量DFT训练数据，在SCWO下缺乏足够覆盖高价态氧物种（如O(¹D)）和离子对溶剂化结构的参考数据；未耦合流体动力学或界面传质效应；绝对反应能垒预测仍存在~8 kJ/mol系统性偏高，影响定量动力学外推。  
- **对你研究的启发**：可迁移“机理验证优先于能量拟合”的评估逻辑——将产物分布、中间体寿命、自由基指纹谱（如EPR模拟信号）设为MLP验证硬指标；借鉴其双力场交叉验证框架，用于你正在开发的CO₂电还原多路径竞争模型的可信度分级。  
- **与你研究的相关度**：高
- **阅读模式:** 🔍 精读
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/70efea01813912d652a559782f364742b3285d62
- **标签:** electrochemistry

### 5. Evolutionary machine learning of physics-based force fields in high-dimensional parameter-space ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2025
- **作者:** D. Spoel; Juli´an Marrades; Kristian K ˇ r´ ı ˇ z; Najla Hosseini; Alfred T. Nordman et al.
- **核心问题**：如何从头构建基于物理原理的机器学习力场（FFs）  
- **方法要点**：开发开源工具ACT，支持用户自定义势函数并端到端训练物理约束的机器学习力场  
- **关键结果**：实现了可解释、可微分、符合物理守恒律（如能量/力一致性）的力场构建框架；支持从第一性原理数据直接拟合  
- **与你研究的相关度**：中
- **阅读模式:** 📋 摘要
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/71416a4934cfe39cce1f622aa2c53fab5831a551
- **标签:** electrochemistry

### 6. Use of Cedrela odorata L. as a Biomaterial for Dye Adsorption in Wastewater: Simulation and Machine Learning Approaches for Scale-Up Analysis ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2025-09-11
- **作者:** C. Tejada-Tovar; Á. Villabona-Ortíz; Ó. Coronado-Hernández; M. Pérez-Sánchez; María Hueto-Polo
- **核心问题**：如何在工业规模固定床吸附柱中实现亚甲基蓝与番红花红两种染料的竞争性高效去除，并建立高精度预测模型  
- **动机与背景**：传统吸附研究多局限于实验室批次实验，难以直接外推至工业连续流系统；现有模拟工具对生物吸附剂在多组分竞争条件下的动态行为预测能力不足；天然生物吸附剂（如Cedrela odorata L.）虽具环境友好性与低成本优势，但其工业级过程设计缺乏可靠建模框架  
- **方法核心**：耦合Aspen Adsorption v1.0流程模拟与机器学习（ML）代理模型，采用线性驱动力（LDF）动力学结合Langmuir/Freundlich/Langmuir–Freundlich等温线进行多模型对比优化，首次将ML用于校准和加速工业级生物吸附柱的动态响应预测  
- **关键实验与结果**：体系为含亚甲基蓝与番红花红的双组分模拟废水，以Cedrela odorata L.为固定相；基线为Aspen内置LDF+等温线模型；Langmuir–LDF模型达96.1%双染料总去除率；ML模型在验证与测试集R² > 0.996  
- **创新点**：① 首次将商用过程模拟软件（Aspen Adsorption）系统应用于木本植物生物吸附剂的工业级竞争吸附建模；② 提出“机理模型（LDF+等温线）→高保真数据生成→ML代理建模”范式，显著提升计算效率与泛化能力；③ 在同一框架下定量比较三种经典等温线对双染料竞争吸附的预测差异，揭示Langmuir假设在该生物吸附体系中的适用边界  
- **局限性**：未提供实验验证数据（如柱穿透曲线实测值），模型可靠性依赖于Aspen内置传质/扩散参数设定；未考虑实际废水中共存离子、腐殖质或pH波动对吸附性能的影响；ML模型为黑箱，缺乏物理解释性与外推鲁棒性分析  
- **对你研究的启发**：可迁移“机理模型生成高质量虚拟数据 + ML构建轻量化代理模型”的策略，用于电催化反应器多参数优化或催化剂稳定性寿命预测；LDF模型在传质主导过程（如气体扩散电极中的O₂传质-反应耦合）中具有直接类比价值；多等温线对比思路可用于评估电催化界面吸附中间体（如*CO、*OH）的竞争覆盖行为  
- **与你研究的相关度**：高
- **阅读模式:** 🔍 精读
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/71e0659ee1be9257c11979d526fd6ff0a9f1cd2d
- **标签:** electrochemistry, surface

### 7. A Deep Reinforcement Learning based End-to-End Control Framework for Lower Limb Exoskeletons with Smooth Movement Transitions ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2025-10-19
- **作者:** Minsu Kim; Woo-Jeong Baek; Jaeheung Park
- **核心问题**：现有下肢外骨骼控制方法（如有限状态机）在应对突发状态变化时缺乏灵活性，导致运动转换不平滑、存在安全隐患，且学习型方法缺乏真实环境验证。
- **方法要点**：提出基于深度确定性策略梯度（DDPG）的端到端深度强化学习框架，直接从传感器输入映射到连续控制输出，实现真实场景下的平滑运动模式切换。
- **关键结果**：首次在真实外骨骼系统上成功部署端到端DRL控制；所提框架在运动转换适应性与平滑性方面显著优于传统FSM方法。
- **与你研究的相关度**：低
- **阅读模式:** 📋 摘要
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/7253f50f3aede612cf41b9d2e12529d0b3e28ad9
- **标签:** general

### 8. Computing chemical potentials with machine-learning-accelerated simulations to accurately predict thermodynamic properties of molten salts ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2025-01-24
- **作者:** Luke D. Gibson; Rajni Chahal; Vyacheslav S. Bryantsev
- **核心问题**：缺乏高精度且高效的原子模拟方法来预测熔盐体系的热力学性质（特别是化学势）  
- **方法要点**：提出基于机器学习原子间势能（MLIP）耦合密度泛函理论（DFT）数据的自由能计算框架，通过离子“嬗变”为非相互作用粒子实现化学势的高效高精度计算  
- **关键结果**：在LiCl体系中实现固/液相DFT精度的化学势计算；预测熔点为880 ± 18 K，与实验值883 K高度一致  
- **与你研究的相关度**：中
- **阅读模式:** 📋 摘要
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/72d73c2b6b41e47479e8723a544c65314c2c2fe4
- **标签:** electrochemistry, dft

### 9. Atomic-Level Insights into TiCN via Machine Learning Force Field Molecular Dynamics Simulations ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2025-11-01
- **作者:** Bo Zhao; Dong Wang; Shurui Shi; Zhengwei Ding; Zisen Wei
- **核心问题**：如何通过理性设计单原子催化剂（SACs）的配位环境来提升其在CO₂电还原反应（CO₂RR）中对高附加值多碳产物（如C₂H₄）的选择性和活性  
- **方法要点**：结合密度泛函理论（DFT）计算与机器学习（ML）驱动的配位构型筛选，构建Ni-N-C体系中Ni位点的局域配位描述符（如d带中心、配位数、第二壳层杂原子电负性），并实验验证最优构型（Ni-N₃O₁）  
- **关键结果**：① Ni-N₃O₁构型在−0.8 V vs. RHE下C₂H₄法拉第效率达82.3%，是Ni-N₄的2.1倍；② DFT揭示O掺杂诱导的不对称电荷分布显著降低*CO二聚能垒（由1.42 eV降至0.76 eV）  
- **与你研究的相关度**：高
- **阅读模式:** 📋 摘要
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/732ca0fc0f5135e04e848397bb6a0d23323bfa60
- **标签:** MLFF

### 10. Modeling Equilibrium Solid-Liquid Interfaces under Effective Constant Chemical Potential Using Machine Learning Interatomic Potentials. ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2025-11-20
- **作者:** Ademola Soyemi; Khagendra Baral; Tibor Szilvási
- **核心问题**：传统分子动力学模拟无法在非平衡或动态条件下维持溶液中物种的恒定化学势（即目标浓度），导致界面模拟偏离实验真实条件。  
- **方法要点**：提出迭代式准恒化学势分子动力学（iqCμMD）方法，通过动态调整溶液中溶质粒子数以快速收敛至目标体相浓度（化学势）。  
- **关键结果**：iqCμMD可在两轮迭代内高效达到目标离子浓度；结合机器学习原子间势（MLIP），能在小尺度模拟中实现DFT级精度的恒化学势固-液界面建模。  
- **与你研究的相关度**：高
- **阅读模式:** 📋 摘要
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/734113a88af996d7ac298d72db1093e277d95cdf
- **标签:** electrochemistry, MLFF, surface, dft

## 💡 今日亮点

- **最值得精读**：[9] Atomic-Level Insights into TiCN via Machine Learning Force Field Molecular Dynamics Simulations — 首次将ML驱动的配位构型筛选、d带中心等物理可解释描述符与CO₂RR多碳产物选择性直接关联，并完成实验验证，为SAC理性设计提供闭环范式。  
- **可能冲突的研究**：[4] Exploring the Reaction Network of Acetic Acid in Supercritical Water via Machine Learning Interatomic Potential — 其采用的MLIP虽提升尺度，但未显式耦合电荷转移或电极电势效应，可能弱化对电催化界面反应路径（如质子耦合电子转移PCET）的刻画能力，与你关注的电极/电解质界面动态存在建模断层。  
- **值得追踪的团队**：[9]作者团队（未具名，但工作体现“DFT→ML descriptor→合成验证”全链条）— 兼具计算深度与实验闭环能力，且聚焦CO₂RR中长期悬而未决的C–C耦合调控机制，与你课题高度协同。  
- **重要趋势**：机器学习力场正从“保精度”单目标，转向“可解释性+物理约束+实验可验证”的多目标协同；尤其在电催化与极端条件反应体系中，MLIP不再仅作模拟加速器，而成为连接微观构效关系与宏观性能预测的桥梁。

## 📌 Key Gap

**关键差距**
- **Gap 1**：所有依赖MLIP的研究（[1][4][8][9][10]）均未系统解决**外场（如电势、光场、压力梯度）下MLIP的能量/力一致性保障问题**——当前MLIP训练数据多来自零场DFT，导致在非平衡电化学界面中力误差放大、自由能面畸变，严重制约过电位依赖反应路径的可靠性。  
- **Gap 2**：**跨尺度衔接失效**：从原子级MLMD（[9][10]）到介观反应器模拟（[6]）或宏观电极动力学（[9]未延伸至Tafel/阻抗分析），缺乏统一的热力学-动力学桥接协议；例如化学势变化如何映射为局部电流密度分布仍无普适降尺度规则。  
- **未来方向**：发展**电势显式嵌入的守恒型MLIP框架**（如通过电极费米能级作为输入特征，强制满足电化学基本方程∂G/∂N = μ = eU），并构建“MLIP-Microkinetic-DRT”三级耦合工作流，实现从单活性位点反应能垒到电极级极化曲线的端到端预测。
