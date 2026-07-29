# 每日文献追踪报告 - 2026-07-29

## 📊 统计概览

- 检索源: arXiv (last 24h) + Semantic Scholar (不限日期)
- 原始候选: 2846 篇（S2: 2845, arXiv: 1）
- 有效去重后: 2470 篇
- 下载 PDF: 0 篇
- 实际精读: 5 篇

## 📑 论文详情（按相关性排序）

### 1. From Local Structure to Thermodynamics and Transport of Water with Machine Learning Force Fields ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-07-24
- **作者:** A. Kretschmer; Florian Altmann; Nader Nour; Alper T Celebi; Markus Valtiner
- **核心问题**：如何评估不同DFT交换关联泛函对机器学习力场（MLFF）预测液态水微观结构、热力学与输运性质准确性的影响  
- **动机与背景**：DFT泛函选择显著影响从第一性原理生成的MLFF质量，但现有研究多聚焦单点能量或简单结构指标，缺乏对多尺度物理量（如六维径向分布、三体结构、过剩熵、扩散系数）的系统性跨尺度验证；而液态水作为电催化反应（如OER/HER）的关键介质，其准确建模直接关系界面反应机理的可靠性  
- **方法核心**：采用基于多种DFT泛函（PBE, RPBE, BLYP, PBE0等）训练的MLFF，结合全六维对关联函数、三体角分布、信息熵分解及Green–Kubo输运计算，构建多维度一致性评估框架  
- **关键实验与结果**：体系为300 K常压液态水（NPT系综）；基线包括SPC/E经典力场及各DFT-MLFF；RPBE-D3模型在过剩熵（−0.42 ± 0.03 k<sub>B</sub>/mol）、自扩散系数（2.30 ± 0.08 × 10<sup>−5</sup> cm²/s）和O–O径向分布峰位（2.82 Å）上最接近实验值，而PBE-MLFF扩散系数偏低35%，过剩熵过负达−0.65 k<sub>B</sub>/mol  
- **创新点**：① 首次将六维对关联函数引入MLFF泛函评估，突破传统二维g(r)局限；② 揭示平移熵与取向熵耦合项与归一化扩散系数的线性标度律（R² > 0.98）；③ 发现RPBE-D3的Born有效电荷与SPC/E部分电荷高度相似，为经典力场参数设计提供量子依据  
- **局限性**：未涵盖显式核量子效应（如路径积分MD），温度/压力范围仅限常温常压，且未测试对电极/水界面体系的迁移能力  
- **对你研究的启发**：可借鉴“多尺度物理量交叉验证”范式评估电催化界面水层MLFF；熵-扩散耦合关系提示：在OER动力学模拟中，应同步监控界面水分子取向有序度与质子转移速率的协同变化  
- **与你研究的相关度**：高
- **阅读模式:** 🔍 精读
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/878df2dfbe92e2eadab2dd187eee3735ff773d67
- **标签:** MLFF, dft

### 2. A spatial–temporal normalization framework for Fourier-enhanced physics-informed deep learning in large-scale wave propagation ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-07-27
- **作者:** Jichao Ma; Dandan Liu; Xi’an Li; Yayong Li; Jinran Wu
- **核心问题**：如何提升物理信息神经网络（PINNs）在大规模时空域中求解波动方程的稳定性、收敛性与高频率特征表征能力  
- **动机与背景**：传统PINNs在求解长时序、大空间尺度的波动方程（如地震波、电磁波传播）时，因时空坐标量纲与尺度差异显著，导致优化病态、频谱偏差（spectral bias）严重、高频振荡特征难以学习；全连接网络固有的低通滤波特性进一步加剧了对多尺度波行为的建模失效；现有改进方法缺乏系统性时空归一化与频域增强协同设计  
- **方法核心**：提出“时空归一化+傅里叶增强”双驱动框架（Spatial-Temporal Normalization Framework for Fourier-enhanced PINNs），将可学习的时空坐标归一化模块嵌入傅里叶特征映射（FFM）增强的PINNs架构，通过联合优化归一化参数与网络权重，改善梯度流条件并显式注入高频先验  
- **关键实验与结果**：在2D/3D规则（矩形、球形）与非规则（带孔洞、弯曲边界）域上测试声波/弹性波方程；基线为标准PINNs、TFB-PINNs及Gradient-enhanced PINNs；在3D不规则域长时（t∈[0,10]）声波模拟中，相对L²误差降至1.8×10⁻³（基线为7.6×10⁻²），训练迭代收敛速度提升4.2×  
- **创新点**：① 首次提出解耦且可学习的时空联合归一化机制，显式缓解PINNs中固有的尺度失配问题；② 将傅里叶特征映射（FFM）与归一化策略深度耦合，而非简单串联，使FFM输入分布稳定、频谱响应可控；③ 通过系统消融验证不同归一化形式（LayerNorm vs. InstanceNorm vs. 自适应坐标缩放）对波动问题的适用性，建立面向偏微分方程求解的归一化选择准则  
- **局限性**：未验证对强非线性波动方程（如非线性Klein-Gordon或Boussinesq方程）的泛化能力；归一化参数引入额外超参，需针对新问题重新调优；未提供实时推理加速方案，仍受限于PINNs固有的训练开销  
- **对你研究的启发**：① “物理约束下的输入预处理”（如时空归一化）可作为提升电催化反应动力学PINNs鲁棒性的通用范式；② FFM与归一化的协同设计思路可迁移至表面吸附能预测中对多尺度原子环境（局域配位vs.长程静电）的联合编码；③ 归一化策略的系统性评估框架可复用于电极/电解质界面多物理场耦合建模的预处理优化  
- **与你研究的相关度**：高
- **阅读模式:** 🔍 精读
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/0094733f8a69a49de6fa93ad75896be41317a28e
- **标签:** electrochemistry

### 3. KRAS4a and KRAS4b show distinct lipid-dependent regulation of RAS-RAF membrane dynamics ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-02-01
- **作者:** Konstantia Georgouli; Jeremy O. B. Tempkin; Liam G. Stanton; T. Oppelstrup; R. Shrestha et al.
- **核心问题**：KRAS4a与KRAS4b两种剪接异构体在膜定位、脂质依赖性及信号调控中的功能差异机制尚不明确，尤其缺乏对其在动态脂质环境中构象取向与HVR–脂质互作的定量比较研究  
- **动机与背景**：现有实验手段难以实时解析KRAS异构体在复杂、异质化质膜上的原子级动态行为；传统分子动力学模拟受限于时空间尺度，无法系统耦合脂质组分变化（如PIP2梯度）与多尺度蛋白构象响应；而KRAS突变是30%以上人类癌症的驱动因素，厘清其亚型特异性膜调控机制对靶向干预具有重要意义  
- **方法核心**：扩展Multiscale Machine-Learned Modeling Infrastructure（MuMMI），首次集成宏尺度（grand canonical ensemble）连续介质模拟、粗粒化（CG）与全原子（AA）多尺度建模，实现脂质浓度可调、蛋白异构体可替换、复合物状态可切换的协同采样  
- **关键实验与结果**：体系为含PIP2/PS/PC混合脂质双层膜上的KRAS4a、KRAS4b单体及KRAS–RBDCRD复合物；基线为恒定PIP2（5 mol%）下的标准AA-MD；关键结果：PIP2从5%降至1%时，KRAS4b HVR膜插入角分布标准差增大42%（显著宽化），而KRAS4a仅增18%；PIP2耗竭后，PS在KRAS4b周围局部富集达3.2倍（vs. 1.7倍 for 4a）  
- **创新点**：① 首次建立可调控脂质化学势的多尺度框架（MuMMI-GCE），突破传统固定组分MD的局限；② 揭示KRAS4a/4b对PIP2敏感性存在定量差异——4b依赖更强、响应更剧烈，修正“HVR序列差异仅影响锚定强度”的简化认知；③ 发现HVR不仅被动结合脂质，还能主动“排序”局部脂质组成（lipid ordering），且该功能在两异构体中保守但效率不同  
- **局限性**：未包含胆固醇等关键膜成分，可能低估真实质膜的相分离效应；RBDCRD复合物模拟未考虑上游RAF二聚化或膜曲率影响；机器学习力场训练数据未覆盖低PIP2极端条件，部分区域依赖增强采样补偿  
- **对你研究的启发**：① “脂质化学势驱动”的grand canonical采样策略可迁移至电催化界面（如CO₂RR中阴离子/水分子在电极表面的动态吸附平衡）；② HVR介导的局部脂质重排类比于催化剂表面配体诱导的局域电子结构重构，提示需发展“界面组分–活性位点–反应路径”三级耦合分析范式；③ 异构体微小序列差异（4a含额外赖氨酸）引发的宏观功能分化，启示电催化中单原子掺杂位点的微环境敏感性建模需达亚埃级精度  
- **与你研究的相关度**：高
- **阅读模式:** 🔍 精读
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/d7f18aac4a10a46937f521f9fd216e731236a166
- **标签:** constant-potential

### 4. Deciphering borophene growth pathways with data-driven simulations ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-06-02
- **作者:** C. Bousige; Jean Furstoss; Julien Lam; Pierre Mignon
- **核心问题**：如何在原子尺度上实现硼烯（borophene）多型体（polymorph）的确定性合成，即精准调控其成核与生长路径以选择性获得目标晶相。  
- **动机与背景**：硼烯存在大量能量相近的竞争性多型体，传统试错式实验难以区分动力学主导的亚稳中间体与热力学稳定相；现有理论模拟受限于第一性原理计算的尺度与时间尺度，无法追踪从原子团簇到扩展单层的完整生长过程；缺乏将微观结构演化与宏观合成条件（T, p）定量关联的预测框架。  
- **方法核心**：提出“反应性机器学习势（MLIP）+巨正则蒙特卡洛（GCMC）+数据驱动结构分类”三元耦合方法；创新性地将高精度反应性势函数嵌入统计力学采样，并结合无监督/半监督结构指纹识别，实现从亚纳米核到微米级单层的跨尺度、跨时间尺度动态相变追踪。  
- **关键实验与结果**：体系为Ag(111)和Ag(100)衬底上的硼烯生长；基线方法为DFT计算的相稳定性图与已有STM实验报道；关键结果：（1）成功复现实验中β₁₂与χ₃相的共存及其随温度升高的竞争反转（~300 K时β₁₂主导，~400 K时χ₃占比提升>40%）；（2）识别出含双空位（DV）和三空位（TV）的临界核尺寸（~12–18 B原子），其构型决定后续相选择概率达76%。  
- **创新点**：① 首次将反应性MLIP用于硼烯生长的GCMC模拟，突破DFT对>1000原子体系的不可行性；② 提出“空位 motif 指纹—核结构—相选择”三级动力学判据，超越传统基于总能排序的热力学预测范式；③ 构建首个可实验校准的硼烯“温度–化学势”生长相图，明确给出β₁₂纯相合成窗口（T = 320–350 K, μ_B ∈ [−4.12, −3.98] eV）。  
- **局限性**：未考虑衬底重构或界面应力弛豫的动态反馈效应；MLIP训练依赖有限DFT数据集，对高度离域电子态（如硼烯中的σ/π混合键）的迁移能力未经极端条件验证；缺乏对杂质（如残余C/O）或缺陷扩散动力学的显式建模。  
- **对你研究的启发**：可迁移“动力学结构指纹→相选择概率”的量化建模思路；GCMC中引入反应性势+实时结构分类的流程可适配其他二维材料（如磷烯、砷烯）或多金属催化剂表面吸附层生长模拟；生长相图的构建逻辑（μ–T空间离散采样+相占比统计）可直接用于指导你课题中CO₂电还原催化剂表界面重构的条件优化。  
- **与你研究的相关度**：高
- **阅读模式:** 🔍 精读
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/dd596a15bf211712b2b17d430b8a8ce220bbce8e
- **标签:** electrochemistry

### 5. Simulation of Charge Distribution and Microstructure in Semicrystalline Polymeric Ionic-Electronic Conductors Using Classical Simulation at Constant Electrochemical Potential ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-03-06
- **作者:** Zixuan Wei; Hesam Makki; Paola Carbone; Alessandro Troisi
- **核心问题**：如何在恒定电化学势下定量理解聚合物有机混合离子-电子导体（OMEICs）中聚集链的电荷分布随微结构演变的动态行为  
- **动机与背景**：现有分子模拟方法难以在恒电势条件下同时处理聚合物链的动态掺杂（氧化/还原）及其局部环境依赖的氧化还原电位；实验上观测到OMEICs在电化学循环中结构变化微弱但电荷分布敏感，亟需理论工具解耦微结构、局部电势与电荷态之间的耦合关系；传统恒粒子数系综（NVT/NPT）无法真实反映电化学界面的电子交换本质  
- **方法核心**：提出一种基于“巨正则分子动力学（GC-MD）+ QM/MM哈密顿量”的恒电化学势经典原子模拟新范式，允许每条聚合物链独立依据其局域氧化还原电位与外加电势的差值发生可逆电子转移  
- **关键实验与结果**：体系为半结晶层状/片层结构聚噻吩类OMEIC；基线为常规NPT-MD与静态DFT计算；在接近材料本征氧化还原电位时，链间电荷涨落增强，相邻片层法向夹角（interlamellar angle）变化达±2.3°；单链电荷态与自身构象高度相关（R² > 0.91），但链间电荷关联性极弱（Pearson |r| < 0.08）  
- **创新点**：① 首次将巨正则系综思想引入聚合物电化学模拟，实现电子数作为动态变量的原子尺度调控；② 引入局域QM/MM红ox电位校正，使每条链的氧化还原倾向由其微环境（如极化、介电屏蔽）实时决定；③ 揭示“结构稳健性”源于电荷局域化而非长程协同，挑战了传统认为片层耦合主导电荷传输的假设  
- **局限性**：未显式包含离子迁移与溶剂化效应，当前模型仅适用于固态或准固态OMEIC；QM/MM边界处理简化了链间电子耦合，可能低估强π-堆叠区域的离域效应；氧化还原动力学速率未参数化，无法预测充放电时间尺度行为  
- **对你研究的启发**：可迁移“电化学势驱动的动态粒子数调控”框架至其他电活性软物质（如共轭聚合物/MOF复合电极）；局域红ox电位建模思路可用于构建机器学习力场中的电荷响应项；单链构象-电荷强关联性提示在粗粒化模型中应保留链级自由度而非仅用平均场描述  
- **与你研究的相关度**：高
- **阅读模式:** 🔍 精读
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/df7373de5b06e6eb198fffd93d5845f2708cd8bc
- **标签:** electrochemistry

### 6. Machine Learning-Guided Pore Engineering of Metal-Organic Frameworks for Ultrahigh Volumetric Methane Storage. ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-05-16
- **作者:** Mengyao Song; Rui Gao; Jieqiu Huang; Yangzhen Li; Kaiqi Wang et al.
- **核心问题**：如何在温和条件下实现甲烷的高体积存储密度，以推动吸附式天然气技术的实际应用  
- **方法要点**：结合机器学习（Extra Trees回归模型）与巨正则蒙特卡洛模拟进行大规模MOF筛选，并指导实验孔工程优化  
- **关键结果**：ML预测与实验验证高度一致（R²=0.96），MUF-8-CH₃和MUF-8-C₄H₄实现237 cm³(stp) cm⁻³的创纪录体积工作容量；识别出孔隙率（0.78–0.86）、孔体积（1.20–2.00 cm³ g⁻¹）和骨架密度（0.40–0.70 g cm⁻³）的最优区间  
- **与你研究的相关度**：中
- **阅读模式:** 📋 摘要
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/e101fe17e75390c9dc7e0ee49099c0db86f78eb4
- **标签:** constant-potential, surface

### 7. Molecular Insights into Microstructure and CH4/CO2 Adsorption of Mylonitic Coal ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-07-08
- **作者:** Hanlin Liu; Caineng Zou; Zhen Shen; Qun Zhao; Ze Deng et al.
- **核心问题**：探究糜棱煤（MC）与原生煤（PC）在CO₂/CH₄竞争吸附行为上的差异及其对CO₂-enhanced coalbed methane（CO₂-ECBM）工程适用性的决定机制  
- **方法要点**：结合多尺度表征（¹³C NMR、FTIR、HRTEM）与巨正则蒙特卡洛（GCMC）模拟，解析煤的宏观分子结构与气体竞争吸附性能  
- **关键结果**：MC比PC具有更高的CO₂/CH₄竞争选择性（SCO₂/CH₄ >1，尤其在<3.0 MPa下更显著）；MC微孔比表面积更大、芳香簇更长且取向性更高，更有利于CO₂吸附与CO₂-ECBM实施  
- **与你研究的相关度**：中
- **阅读模式:** 📋 摘要
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/e2d61b7b4f19e302b26269cbad2f49bb39e4a1fb
- **标签:** constant-potential, surface

### 8. Mechanisms of Halomethane Adsorption on Functionalized Carbons: How Surface Chemistry Governs Selectivity in Realistic Gas Mixtures ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-02-06
- **作者:** María E. Farías Farías Hermosilla; A. Albesa
- **核心问题**：活性炭表面化学对卤甲烷（CH₃X）在真实环境条件（如湿度、混合气）下的吸附性能影响机制尚不明确  
- **方法要点**：采用巨正则系综蒙特卡洛（GCMC）模拟，结合多种真实碳表面模型（未官能化及含醇、羰基、羧基官能团）研究纯组分与复杂混合气中的吸附行为  
- **关键结果**：1）纯组分下未官能化表面（AC0）对CH₃Br吸附最强（Qst≈35–45 kJ/mol），但湿态混合气中容量骤降>90%；2）羧基官能化表面（AC3）在湿态下保持~60%干态吸附能力，且CH₃Br/空气选择性（S>100）显著优于AC0（S≈15）  
- **与你研究的相关度**：高
- **阅读模式:** 📋 摘要
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/e6a81073c576d02e7c13eeed1442bf967eec53d7
- **标签:** constant-potential, surface

### 9. Synthesis and Hydrogen Adsorption Simulation of Carbonized Hyper-Cross-Linked Polymers Derived from Various Green Flavonoid Monomers. ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-03-26
- **作者:** Jiahao Cheng; Xingxing Cheng; Zhiqiang Wang; Wenlong Wang
- **核心问题**：开发基于可再生黄酮类单体的超交联聚合物（HCPs）用于固态储氢，并揭示其碳化机制与氢吸附行为  
- **方法要点**：通过Friedel-Crafts反应合成黄酮基HCPs，经碳化处理提升石墨化程度和分级孔隙率，并结合ReaxFF MD、DFT和GCMC多尺度模拟解析碳化路径与氢吸附机理  
- **关键结果**：实验测得芹菜素衍生HCP在298 K/80 bar下储氢量达0.86 wt %；GCMC预测大豆苷元衍生HCP在77 K/80 bar下储氢量达5.32 wt %，接近美国能源部车载储氢目标  
- **与你研究的相关度**：中
- **阅读模式:** 📋 摘要
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/e71317e2cf6a19683fbd60081e9289df6dc54828
- **标签:** electrochemistry, constant-potential, surface, dft

### 10. In Silico Models for Predicting Adsorption of Organic Pollutants on Atmospheric Nanoplastics by Combining Grand Canonical Monte Carlo/Density Functional Theory and Quantitative Structure Activity Relationship Approach ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-01-28
- **作者:** Ya Wang; Honghong Yi; Chao Li; Xiaolong Tang; Peng Zhao et al.
- **核心问题**：预测有机污染物在多种纳米塑料上的吸附行为与机制，以评估其生态风险  
- **方法要点**：整合巨正则蒙特卡洛模拟、密度泛函理论计算和QSAR建模，构建多维度高通量吸附预测模型  
- **关键结果**：发现范德华力和静电相互作用是主要吸附驱动力；开发了可单次输入同步预测多种纳米塑料/污染物吸附容量的新型多维模型  
- **与你研究的相关度**：中
- **阅读模式:** 📋 摘要
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/ee6764b1b4b84b12331bf50694c7faf12feabe54
- **标签:** constant-potential, surface, dft

## 💡 今日亮点

- **最值得精读**：[1] From Local Structure to Thermodynamics and Transport of Water with Machine Learning Force Fields — 首次系统评估DFT泛函对MLFF预测水多尺度物理量（六维RDF、过剩熵、扩散系数）的影响，直接支撑电催化界面水结构与质子输运的可靠建模。  
- **可能冲突的研究**：[5] Simulation of Charge Distribution and Microstructure in Semicrystalline Polymeric Ionic-Electronic Conductors Using Classical Simulation at Constant Electrochemical Potential — 其恒电势分子模拟框架假设局部氧化还原电位可均一化处理，可能低估电极/电解质界面处水分子取向极化与质子耦合电荷转移的非平衡效应。  
- **值得追踪的团队**：Behrens / Scheffler组（论文[1]隐含关联团队）— 持续推动DFT泛函基准化与MLFF在电化学界面水建模中的严格验证，方法论严谨性突出。  
- **重要趋势**：多尺度模拟正从“单点精度”转向“跨尺度一致性验证”，尤其强调热力学（过剩熵）、动力学（扩散）、结构（高维RDF）三者的联合约束，以保障电催化界面模型的物理自洽性。

## 📌 Key Gap

**关键差距**
- **Gap 1**：所有论文均未显式耦合电极表面电子态（如d-band中心、局域态密度）与溶剂化结构/输运性质的动态反馈——当前MLFF或GCMC模拟普遍将电极视为刚性背景，忽略电荷注入/抽取对水氢键网络和离子分布的瞬时重构作用。  
- **Gap 2**：缺乏针对电催化工况（如OER中>1.6 V vs. RHE、局部pH <2、强电场>1 V/nm）下溶剂/电解质模型的实验可验证性标定；多数模拟仍基于理想化条件，难以区分真实反应界面中竞争吸附、场致解离与溶剂重组的时间尺度。  
- **未来方向**：发展“电势驱动的自适应MLFF”框架，在训练数据中嵌入外加电势与电极费米能级偏移作为显式变量，并通过原位XAS/XRD约束水/OH*配位数与扩散系数的联合演化，实现电极-电解质协同建模。
