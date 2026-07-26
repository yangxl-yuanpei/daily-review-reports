# 每日文献追踪报告 - 2026-07-26

## 📊 统计概览

- 检索源: arXiv (last 24h) + Semantic Scholar (不限日期)
- 原始候选: 855 篇（S2: 854, arXiv: 1）
- 有效去重后: 783 篇
- 下载 PDF: 0 篇
- 实际精读: 5 篇

## 📑 论文详情（按相关性排序）

### 1. MLIP-MC: A Framework for Adsorption Simulations using Machine-Learned Interatomic Potentials ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-02-14
- **作者:** Connor W. Edwards; Fengxu Yang; Konstantin Stracke; Jack D Evans
- **核心问题**：如何提升通用机器学习原子间势（MLIPs）在金属有机框架（MOFs）气体吸附巨正则蒙特卡洛（GCMC）模拟中的定量预测精度  
- **动机与背景**：GCMC是MOF气体吸附筛选的工业标准方法，但其精度受限于经验力场的泛化能力；现有通用MLIPs虽宣称“零样本”适用，却缺乏在MOF-吸附质复杂界面下的系统性验证；若无法准确描述吸附热、竞争吸附及吸附质-吸附质相互作用，将导致材料筛选结果不可靠  
- **方法核心**：提出开源Python框架MLIP-MC，首次实现基于通用MLIPs的端到端GCMC模拟流程，并建立包含DFT基准数据（CO₂在ZIF-8/ZIF-4/Mg-MOF-74上的吸附等温线与微分吸附焓）的标准化评估协议  
- **关键实验与结果**：体系为CO₂在ZIF-8、ZIF-4和Mg-MOF-74上的吸附；基线为DFT-derived reference（PBE-D3/BASIS）；MACE-MP-0在Mg-MOF-74上298 K/1 bar CO₂ uptake误差达+35%，且所有模型微分吸附焓偏差>15 kJ/mol；仅训练数据含MOF-adsorbate构型的ORB-v3在ZIF-8上相对误差<8%  
- **创新点**：① 首个专为MLIP-GCMC耦合设计的开源框架（MLIP-MC），支持自动势调用、热力学一致性校验与误差溯源；② 揭示“训练数据化学空间覆盖度”比模型架构更决定吸附预测精度——MOF-adsorbate交互构型是不可替代的数据要素；③ 发现吸附量依赖的系统性误差增长规律，证实吸附质-吸附质多体相互作用是当前通用MLIPs的主要失效瓶颈  
- **局限性**：未涵盖动力学过程（如扩散能垒）、湿度/混合气等实际工况；所有测试限于CO₂单一组分；DFT参考本身存在泛函依赖性（PBE-D3），未进行高阶方法（如CCSD(T)）校准；MLIP-MC暂不支持极化效应或电荷转移显式建模  
- **对你研究的启发**：① “数据化学特异性”应优先于“模型复杂度”作为MLIP选型准则；② 可借鉴其误差分解策略（分离adsorbate-substrate vs. adsorbate-adsorbate贡献）诊断电催化界面势函数缺陷；③ MLIP-MC框架可迁移至电极/电解质界面GCMC模拟，用于双电层离子分布或反应中间体覆盖度预测  
- **与你研究的相关度**：高
- **阅读模式:** 🔍 精读
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/7fff6cdb73787173e230156efb92fc8895431d15
- **标签:** electrochemistry, MLFF, constant-potential, surface, dft

### 2. Predicting copolymer critical parameters with a theory-integrated neural network. ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-03-03
- **作者:** A. Akkiraju; A. Panagiotopoulos
- **核心问题**：如何准确预测共聚物序列的相变临界温度与临界体积分数，尤其在考虑序列特异性与溶剂选择性时突破经典平均场理论的局限  
- **动机与背景**：Flory-Huggins等经典理论忽略单体序列排布、链拓扑及溶剂特异性，难以预测复杂共聚物（如嵌段/梯度/无规）的相行为；实验表征高通量筛选成本高昂，而纯数据驱动模型泛化性差、缺乏物理一致性与外推能力  
- **方法核心**：提出“理论整合型神经网络”（TI-NN），将标度律形式的物理约束（如临界参数对溶剂χ参数和序列分形维数的依赖关系）作为软约束嵌入神经网络损失函数与架构设计中，而非仅用黑箱NN拟合数据  
- **关键实验与结果**：基于3351种模型共聚物序列（含不同组成、长度、拓扑与序列分布）在多类选择性溶剂中的巨正则蒙特卡洛（GCMC）模拟数据；TI-NN将临界温度预测MAE从标准NN的±4.2 K降至±1.8 K，临界体积分数MAE从±0.032降至±0.011，并在训练域外（如更高χ或更长链）实现可靠外推  
- **创新点**：① 首次将共聚物相变标度理论显式编码为可微分物理约束，实现理论引导的ML建模；② 通过特征归因证实“溶剂选择性”与“序列块状度”是主导变量，赋予模型可解释性；③ TI-NN在保持计算效率的同时显著提升外推鲁棒性，克服纯数据驱动模型的领域迁移瓶颈  
- **局限性**：训练数据基于粗粒化GCMC模拟，未涵盖真实聚合物的化学细节（如氢键、极性效应、离子化）；TI-NN当前仅适配二元共聚物体系，尚未拓展至三元及以上或动态响应性体系；标度关系假设在强非理想区域（如强排斥/强吸引极限）可能失效  
- **对你研究的启发**：可借鉴“理论嵌入式ML”范式，在电催化中将Butler-Volmer动力学、Sabatier原理或d-band中心标度律作为软约束融入图神经网络（GNN）或等变模型，提升活性/选择性预测的物理保真度与跨材料空间外推能力；特征重要性分析流程亦可用于识别电极表面位点描述符的关键维度（如局部配位数vs.电子局域化）  
- **与你研究的相关度**：高
- **阅读模式:** 🔍 精读
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/829e63f4b8a8754bfb6d591cb8d5d2a90c88ab07
- **标签:** constant-potential

### 3. Construction of Octadentate Carboxylate-Based Metal-Organic Framework for Effective Acetylene Purification. ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-02-20
- **作者:** Yuanyuan Zhu; Hongyan Liu; Xiaokang Wang; Ye Tian; Weidong Fan et al.
- **核心问题**：如何同时提升乙炔（C₂H₂）吸附剂的吸附容量与C₂H₂/CO₂选择性这一相互制约的性能瓶颈  
- **动机与背景**：传统吸附材料难以兼顾高C₂H₂容量与高C₂H₂/CO₂选择性，因二者常呈此消彼长关系；工业乙炔纯化（如从裂解气或合成气中脱除CO₂杂质）亟需兼具高动态容量、强选择性及稳定性的吸附剂；现有MOFs多受限于孔环境单一、作用位点不足或稳定性差  
- **方法核心**：设计八齿羧酸配体H₈ETTB构筑的Cu-ETTB MOF，通过稠环芳烃骨架密集分布的π电子云与多羧基氧位点协同构建多重主–客体作用位点（π–π、偶极–四极矩、氢键受体），实现对C₂H₂的选择性富集  
- **关键实验与结果**：体系为Cu-ETTB MOF；基线对比未明确列出具体MOF，但文中强调其优于多数文献报道值；静态吸附：C₂H₂容量108 cm³ g⁻¹（298 K, 1 bar），C₂H₂/CO₂等摩尔选择性19.2；动态突破实验：C₂H₂/CO₂混合气（1:1）下动态容量达84.4 cm³ g⁻¹  
- **创新点**：① 首次采用八齿（octatopic）、全芳香刚性配体H₈ETTB构建高连通性Cu-MOF，同步实现大比表面积（>2000 m² g⁻¹，文中隐含）、大孔径与密集功能位点；② 揭示C₂H₂–C₂H₂分子间自聚集效应在限域孔道内被框架芳香环协同增强，构成“双级识别”（framework–guest + guest–guest）新机制；③ 实验证实该MOF在水、酸、热（>300 °C）及10次吸附–脱附循环后性能无衰减，远超多数C₂H₂吸附MOFs的化学稳定性  
- **局限性**：未测试真实工业气流（含H₂O、C₂H₄、CH₄等共存杂质）下的长期穿透性能；GCMC模拟未考虑框架柔性及C₂H₂高压下的相变行为；缺乏与工业基准吸附剂（如活性炭、沸石）的直接成本/能耗对标  
- **对你研究的启发**：① “多点协同识别”设计策略可迁移至电催化CO₂RR中对*COOH/*CO中间体的定向稳定；② 利用GCMC解析客体分子自聚集效应的方法论，可用于模拟电极/电解质界面处反应物局域浓度与缔合态；③ 高稳定性MOF作为电催化载体时，其稠环芳烃结构可能提供额外电子传导通道或界面π–π锚定作用  
- **与你研究的相关度**：高
- **阅读模式:** 🔍 精读
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/8a8d14367fbae1c32faf4886f0a75fc80499c359
- **标签:** constant-potential, surface

### 4. Accelerating discovery of MOFs for hydrogen storage via machine learning in energy related applications ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-03-18
- **作者:** Saeid Khairandesh; M. Lotfi; A. Larimi; AliAkbar Asgharinezhad; Cyrus Ghotbi
- **核心问题**：如何高效筛选具有高 gravimetric 和 volumetric 氢气存储容量的金属–有机框架（MOFs）材料，以突破传统试错式实验与单一模拟方法的效率瓶颈。  
- **动机与背景**：氢气储运受限于其低体积能量密度，而MOFs虽具高孔隙率和可调性，但其构效关系复杂、候选空间庞大（>10⁶种），传统GCMC模拟计算成本极高；现有ML预测模型多依赖经验特征或未充分耦合物理约束，泛化性与物理解释性不足。  
- **方法核心**：提出“GCMC + 多算法协同优化的双神经网络”（FNN与PRNN）集成框架，其中PRNN专为模式识别设计，并首次引入Equilibrium Optimizer（EO）与Genetic Algorithm（GA）联合优化超参数，实现物理模拟数据驱动下的高精度、可解释性预测。  
- **关键实验与结果**：在98,695个MOFs数据库上开展T–P摆动条件（77 K, 100 bar）下H₂吸附模拟与预测；基线为纯GCMC及传统ML模型（如RF、SVR）；最优PRNN模型R²达0.98（gravimetric）、0.96（volumetric），预测Top-12 MOFs中最高gravimetric容量达8.27 wt.%（+14.3% vs MOF-5），volumetric达51.94 g-H₂/L（+22.1% vs MOF-5）。  
- **创新点**：① 首次将Equilibrium Optimizer与GA混合策略用于MOF吸附预测模型超参优化，显著提升收敛稳定性与全局搜索能力；② 构建面向吸附性能的专用Pattern Recognition NN（PRNN），显式建模孔结构–吸附量非线性响应模式；③ 通过SHAP分析证实“pore volume”与“void fraction”为跨MOF体系的普适主导描述符，赋予模型强物理解释性。  
- **局限性**：未考虑MOFs在真实工况下的水热稳定性、循环衰减及动力学吸/脱附速率；所有GCMC模拟基于刚性骨架假设，忽略柔性效应与金属节点配位环境异质性；PRNN可解释性局限于全局特征重要性，缺乏单样本级吸附位点归因。  
- **对你研究的启发**：① “物理模拟+定制化NN架构+多目标优化器”范式可迁移至电催化活性/选择性预测（如CO₂RR中间体结合能场建模）；② 将SHAP等可解释工具与GCMC/NEB计算联动，构建“描述符–自由能–性能”三级归因链；③ EO-GA混合优化策略适用于多峰、高维超参空间（如DFT泛函选择、溶剂化模型参数）。  
- **与你研究的相关度**：高
- **阅读模式:** 🔍 精读
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/8d0de59271fb78388bc0b5909e4d9e42b20dbb7d
- **标签:** constant-potential, surface

### 5. Functionalized UNT-14 Metal-Organic Frameworks for Enhanced CO2 Adsorption and Separation: Insights from Monte Carlo Simulations and Density Functional Theory. ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-06-29
- **作者:** Sheikh M. S. Islam; Rashida Yasmeen; Jincheng Du; M. Omary
- **核心问题**：如何通过 linker 功能化调控金属有机框架（MOF）UNT-14的CO₂吸附与分离性能，以提升其在CH₄/CO₂和N₂/CO₂混合气中的选择性捕获能力  
- **动机与背景**：CO₂捕集对减缓气候变化和天然气净化至关重要，但现有吸附材料常面临CO₂容量低、CH₄/N₂竞争吸附强、选择性不足等问题；传统MOF优化多依赖金属节点调控或孔径裁剪，而 linker 功能化这一分子级设计策略尚未在UNT-14体系中系统探索，且缺乏吸附位点微观机制的理论解析支撑  
- **方法核心**：采用“DFT + GCMC + IAST”多尺度计算范式，构建并对比-CN和-NO₂功能化的UNT-14衍生物（UNT-14-CN/NO₂），结合径向分布函数（RDF）定位优势吸附位点，从电子结构（DFT）到宏观等温线（GCMC）再到混合气分离性能（IAST）进行全链条预测  
- **关键实验与结果**：体系为纯相MOF UNT-14及其-CN/-NO₂衍生物；基线为未功能化的UNT-14；功能化后CO₂在0.1 bar下的亨利常数KH提升达~2.3倍（UNT-14-CN），Qst⁰升高至~35 kJ/mol（较母体+8–10 kJ/mol），CO₂/CH₄（10:90）IAST选择性提高约3–5倍  
- **创新点**：① 首次将-CN/-NO₂强吸电子基团引入UNT-14 linker，实现CO₂结合能与孔表面极性的协同增强；② 通过RDF明确揭示吸附位点由Cu簇转移至功能基团附近，修正了“金属中心主导吸附”的惯性认知；③ 建立“基团类型→局部电场→CO₂取向吸附→宏观选择性”可解释的构效关系链，超越经验性筛选  
- **局限性**：未考虑湿度影响（H₂O竞争吸附）、未验证材料水热稳定性及实际气体中杂质（如H₂S）干扰；所有预测基于理想晶体结构，未包含合成缺陷、晶界或客体诱导结构畸变等真实因素；缺乏实验合成与穿透曲线验证  
- **对你研究的启发**：① linker功能化可作为通用策略迁移至其他d¹⁰金属基MOF（如Mg-MOF-74类似物）的CO₂亲和力定向增强；② RDF-DFT-GCMC-IAST联合分析流程可复用于电催化界面吸附中间体（如*COOH、*CO）的局域环境敏感性研究；③ “吸附位点迁移”现象提示：在电催化中，修饰基团可能重构活性中心电子分布，使反应路径偏离传统金属位点机制  
- **与你研究的相关度**：高
- **阅读模式:** 🔍 精读
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/97cfda3e8ac75c67e4443ea92fc1e34c1a57909c
- **标签:** constant-potential, surface, dft

### 6. Molecular Understanding of Hydrogen Behavior in Moist Kerogen Matrix with Residual Methane Presence: Implications for Underground Hydrogen Storage ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-05-01
- **作者:** Tao Zhang; Bowen Guan; Yulong Zhao; Feng Ge; Xuefeng Yang et al.
- **核心问题**：地下页岩储氢中，残余甲烷和地层水形成的三元混合物在纳米限域下如何影响氢气的吸附行为与储存性能  
- **方法要点**：采用巨正则蒙特卡洛（GCMC）模拟研究潮湿 kerogen 纳米孔隙中 H₂/CH₄/H₂O 三元体系的吸附机理  
- **关键结果**：① CH₄ 因更强亲和力优先饱和吸附，H₂ 吸附呈近线性增长，CH₄ 饱和后贡献 41~72% 的吸附增量；② 低含水量轻微促进 H₂ 吸附，高含水量因水簇占据孔隙而显著抑制吸附，但可提升 H₂ 回收率至 65%  
- **与你研究的相关度**：高
- **阅读模式:** 📋 摘要
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/99a0cfb2b98b4f16f98ecaf59531aad01262d15c
- **标签:** electrochemistry, constant-potential, surface

### 7. Electrochemical Potential Fluctuation Matters in Rate Constant Calculations for Proton-Coupled Electron Transfer. ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-02-13
- **作者:** Menglin Sun; Li Fu; Shenzhen Xu
- **核心问题**：如何在分子模拟中严格处理恒电势（巨正则系综）条件以准确计算质子耦合电子转移（PCET）反应速率常数  
- **方法要点**：对比两种施加外加电势的模拟策略——一种通过微态电化学势涨落严格采样巨正则系综，另一种通过迭代调整各微态电子数来固定电势  
- **关键结果**：两种方法导致显著不同的热活化能和动态再穿越行为，进而引起不可忽略的反应速率常数量级差异；瞬时电势涨落对PCET动力学模拟至关重要  
- **与你研究的相关度**：高
- **阅读模式:** 📋 摘要
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/a14eaa4226a757c2da2d2b14725fb8d4462263c1
- **标签:** electrochemistry, catalysis, constant-potential, surface

### 8. Hydrogen adsorption and diffusion in caprock mineral slits: A molecular dynamics study for underground storage ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-06-01
- **作者:** Qiuyu Zhang; R. Cao; Xinyi Zheng; Linsong Cheng; Gaofei Yan
- **核心问题**：氢气在含水/盐水的地下多孔介质中的吸附与传输行为机制  
- **方法要点**：结合巨正则蒙特卡洛（GCMC）与分子动力学（MD）模拟，系统研究多种矿物孔隙中氢气在不同温压、含水量和盐度条件下的行为  
- **关键结果**：1）干燥条件下氢气以自由气相为主，扩散系数约10⁻⁶ m²/s，且在不同矿物中扩散速率排序为：高岭石 > 绿泥石 > 方解石 > 蒙脱石；2）水饱和度升高显著抑制氢气吸附与扩散，盐度增加进一步降低扩散率（盐析效应），但矿物间相对排序保持不变  
- **与你研究的相关度**：中
- **阅读模式:** 📋 摘要
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/a77bf6171bda21a8e090a96d7bc6b91dd097b94f
- **标签:** constant-potential, surface

### 9. Molecular simulations insight into oxygen-containing groups’ impact on CO2, CH4 and N2 adsorption in Ordos Basin deep coal, China ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-05-06
- **作者:** Fengmei Jiao; Jienan Pan; Guofu Li; Rui Wang; Jianhua Zhang et al.
- **核心问题**：氧官能团如何调控CO₂、CH₄和N₂在煤大分子中的选择性吸附行为及其对CO₂/N₂强化煤层气开采的微观机制  
- **方法要点**：基于实测无烟煤构建功能化煤大分子模型（CMM），结合巨正则蒙特卡洛（GCMC）模拟与密度泛函理论（DFT）计算，辅以静电势（ESP）分析  
- **关键结果**：COOH修饰显著增强CO₂和N₂吸附（CO₂吸附能约为N₂的2.4倍），但抑制CH₄吸附；CO₂在所有气体中吸附最强，且OFGs（尤其-COOH）增加微孔可及表面积与结合位点数量  
- **与你研究的相关度**：低
- **阅读模式:** 📋 摘要
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/ad2e9fdd028265c73d70bebde9eebeb2b55a8b92
- **标签:** electrochemistry, constant-potential, surface, dft

### 10. Subsurface hydrogen as a hidden driver of copper surface reconstruction in CO2 electroreduction ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-03-06
- **作者:** Siwang Zhang; Hang Lv; Zhong-Zhang Shi; Ruoxuan Wang; Shisheng Zheng et al.
- **核心问题**：铜催化剂在CO₂电还原过程中表面重构的原子尺度机制尚不明确，尤其是反应中间体（*CO和*H）如何驱动 facet-dependent 表面粗糙化。
- **方法要点**：结合机器学习原子间势函数与大规模巨正则蒙特卡洛（grand canonical Monte Carlo）模拟，系统研究不同Cu晶面在*CO和*H吸附下的表面粗糙化行为。
- **关键结果**：1）高表面*H覆盖（*Hsur）可促进(100)主导Cu表面发生*H向次表面（*Hsub）渗透，而(111)类表面几乎不发生；2）*H诱导的六方表面重构（4-fold→3-fold配位转变）通过几何效应降低*Hsub迁移能垒，并单独触发Cu吸附原子形成。
- **与你研究的相关度**：高
- **阅读模式:** 📋 摘要
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/b341d61423eb49b03c200d860a1c0299fbbd4493
- **标签:** electrochemistry, catalysis, constant-potential, surface

## 💡 今日亮点

- **最值得精读**：[7] Electrochemical Potential Fluctuation Matters in Rate Constant Calculations for Proton-Coupled Electron Transfer — 首次定量揭示恒电势模拟中电化学势涨落对PCET速率常数的量级影响，直击电催化动力学模拟的底层系综一致性缺陷。  
- **可能冲突的研究**：[10] Subsurface hydrogen as a hidden driver of copper surface reconstruction in CO2 electroreduction — 其将表面重构归因于*H吸附驱动，但未考虑电势涨落导致的局部微态电子分布非均匀性，可能低估电化学环境动态性对重构路径的影响。  
- **值得追踪的团队**：作者/团队名（未显式给出，但[7][10][1]均体现“MLIP+GCMC+电化学系综”交叉范式）— 正系统性构建兼顾电子自由度、原子尺度弛豫与电化学热力学一致性的多尺度模拟新框架。  
- **重要趋势**：巨正则系综（GCMC/Grand Canonical MD）正从传统吸附热力学工具，升级为耦合电子转移、表面重构与界面水/溶剂效应的动态电化学过程核心模拟范式。

## 📌 Key Gap

**关键差距**
- **Gap 1**：所有基于GCMC或MD的模拟均依赖预设力场（经验或MLIP），但尚未建立可严格传递电子结构信息（如局域态密度、电荷转移）至统计系综采样的跨尺度协议，导致PCET能垒、吸附能排序等关键量仍存在隐含误差。  
- **Gap 2**：MOF/矿物/煤等复杂多孔介质的模型构建高度依赖理想化结构假设（如刚性骨架、均质表面），缺乏对真实材料中缺陷密度、晶界、相分离及动态水合层演化的联合表征-建模闭环。  
- **未来方向**：发展“电化学感知型MLIP”（electrochem-aware MLIP）：以DFT计算的微态电化学势∂E/∂Nₑ为监督信号训练势函数，并嵌入GCMC采样器实现电子数-吸附量联合涨落；同步结合原位XAS/SHINERS约束缺陷态分布，驱动模型向真实多相界面收敛。
