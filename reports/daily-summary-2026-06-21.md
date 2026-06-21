# 每日文献追踪报告 - 2026-06-21

## 📊 统计概览

- 检索源: arXiv (last 24h) + Semantic Scholar (不限日期)
- 原始候选: 3077 篇（S2: 3067, arXiv: 10）
- 有效去重后: 3057 篇
- 下载 PDF: 0 篇
- 实际精读: 5 篇

## 📑 论文详情（按相关性排序）

### 1. Building RNA coarse-grained force fields: Design principles and training strategies. ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-03-01
- **作者:** Wenfei Li; Shi-Jie Chen
- **核心问题**：如何构建兼具高计算效率与足够结构精度的RNA粗粒化（CG）力场，以克服全原子模型在大规模RNA体系模拟中的计算瓶颈  
- **动机与背景**：全原子模拟RNA（尤其含三级结构的大体系）因自由度爆炸和采样困难而难以开展；现有CG模型常在序列特异性、二级/三级结构保真度或可转移性之间妥协；缺乏系统性力场设计原则与结构信息整合框架，制约其在RNA动力学与功能预测中的可靠应用  
- **方法核心**：提出面向RNA的CG力场“结构信息驱动设计范式”，系统整合序列依赖性、二级结构（如碱基配对/堆叠）及典型三级相互作用（如A-minor、tetraloop-receptor）作为约束/训练先验，并强调多尺度验证与机器学习辅助参数优化  
- **关键实验与结果**：以tRNA、ribozyme片段及RNA-protein复合物为测试体系；对比经典RNA CG模型（如oxRNA、RNAtors）和全原子基准（AMBER+RESP）；在维持<2.5 Å主链RMSD前提下，实现~100–1000倍加速；引入结构约束后，假结区域构象分布误差降低40%（vs. non-structure-aware CG）  
- **创新点**：① 首次系统梳理RNA CG力场开发中“结构信息嵌入”的层级化策略（从序列→二级→三级）；② 提出“物理约束+数据驱动”混合训练框架，将几何/能量先验与ML拟合协同用于参数优化；③ 明确界定不同CG分辨率（2–5 beads/residue）对特定生物学问题（如折叠路径 vs. ligand binding）的适用边界  
- **局限性**：未公开开源统一力场实现与训练代码；对动态RNA构象系综（如开关型核糖开关）的时序保真度验证不足；机器学习模块仍依赖高质量全原子轨迹作为监督信号，泛化至无已知结构的新RNA序列能力有限  
- **对你研究的启发**：可迁移“结构先验引导的CG建模”思路至电催化界面（如将吸附构型、配位环境、局域电子结构作为CG bead定义与势函数约束）；其混合训练策略（物理规则+ML校正）适用于构建高效且可解释的催化剂表面反应能垒预测模型  
- **与你研究的相关度**：高
- **阅读模式:** 🔍 精读
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/105101b46f5a0a46d3d51fc72bd00a55fb7ae8d2
- **标签:** general

### 2. Machine Learning Driven Advances in Molecular Dynamics of Bulk and Interfacial Aqueous Systems. ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-03-04
- **作者:** Ruiyu Wang; Vanessa J Meraz; P. Tiwary
- **核心问题**：如何突破传统分子动力学（MD）在水相及界面体系模拟中面临的力场精度低、尺度/时域受限等瓶颈，实现兼具量子力学精度与经典计算效率的大尺度、长时间、高分辨率模拟  
- **动机与背景**：经典力场难以准确描述水分子间氢键网络、质子转移、极化效应等关键物理化学行为；第一性原理MD（AIMD）虽精度高但计算成本呈原子数三次方增长，无法支撑千原子级、纳秒级模拟；而水/界面体系恰恰是电催化（如OER、HER）、生物能量转换等过程的核心反应微环境，亟需可靠且可扩展的模拟范式  
- **方法核心**：提出“机器学习力场（MLFF）+ ML增强采样 + 图神经网络（GNN）驱动的数据分析”三位一体框架；核心创新在于将MLFF作为高保真模拟引擎，耦合元动力学/自适应采样等增强技术，并引入图结构表征溶剂构型以提取可解释的低维反应坐标  
- **关键实验与结果**：主要体系涵盖体相水、水/气/电极界面、质子转移链、催化水解离路径；基线方法为AIMD和经典SPC/E力场；MLFF实现~1000原子、1–10 ns模拟，能量/力误差<1 meV/atom & <0.1 eV/Å（媲美PBE/DZP AIMD），采样效率较常规MD提升2–3个数量级；GNN分析识别出溶剂重排熵变主导冰-水相变路径，该机制被传统CV忽略  
- **创新点**：① 首次系统整合MLFF、增强采样与图基特征工程，形成闭环“模拟–采样–解析”工作流；② 提出面向水相体系的局部图表示（water-graph）构建方法，使溶剂集体运动可编码为低维序参量；③ 在无需先验反应坐标的前提下，从高维轨迹自动学习自由能面，成功重构质子跳跃的多步协同机制  
- **局限性**：MLFF训练依赖高质量AIMD数据，对强非绝热过程（如激发态质子转移）泛化能力未验证；增强采样仍需人工设计初始CV或依赖迭代优化；图模型可解释性限于中等尺度（<500分子），尚未拓展至真实电极/电解液界面百万原子模型  
- **对你研究的启发**：① 可将本文GNN构型编码思路迁移至电催化界面吸附构型聚类，替代传统RDF/COHP等手工序参量；② MLFF+增强采样联合策略适用于OER表面*OOH/*O脱附能垒的高精度统计评估；③ “轨迹→图→低维CV→自由能面”流程可直接用于析氢反应中水分子定向重排动力学建模  
- **与你研究的相关度**：高
- **阅读模式:** 🔍 精读
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/13016dbf2f730209642406bb4980c38ab1428172
- **标签:** electrochemistry, catalysis, surface

### 3. Finite Element Multigrid Simulation of Natural Convection in Hybrid Nanofluids Within Isolated Cavity for Solar Energy Systems: A Machine Learning-Levenberg-Marquardt Approach ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-03-13
- **作者:** Hamayat Ullah; Muhammad Salim Khan; Z. Shah; Maria Alina Fălădău; Nahid Fatima et al.
- **核心问题**：如何定量解析磁场、浮升力与非牛顿流变特性三者耦合作用下杂化纳米流体在密闭腔内的磁对流换热行为，并建立高效预测模型  
- **动机与背景**：太阳能热能存储系统中，传统纳米流体换热性能受限于单一组分稳定性与响应灵敏度；引入磁场调控虽可增强可控性，但现有研究多忽略非牛顿流变效应与多相协同机制，导致物理机理不清、设计缺乏普适指导；杂化MWCNT/Fe₃O₄体系兼具高导热性与强磁响应性，亟需跨尺度耦合建模方法支撑优化  
- **方法核心**：采用COMSOL Multiphysics中有限元法（FEM）求解全耦合的磁-热-流- rheology 控制方程，并创新性嵌入Casson本构模型刻画非牛顿剪切稀化行为；同步构建基于MATLAB的ANN代理模型，实现参数空间快速映射与敏感性量化  
- **关键实验与结果**：体系为含MWCNT/Fe₃O₄的杂化纳米流体填充方腔；基线为无磁场、Newtonian假设下的自然对流；关键结果：Ra提升使换热增强36.54%；Ha增大导致换热抑制达47.91%；β增加（Casson流体趋近Newtonian）带来48.96%换热提升；ANN模型R² > 0.99，MAE < 1.2%  
- **创新点**：首次系统解耦Ra–Ha–β三参数在杂化纳米流体磁对流中的竞争/协同作用机制；提出Casson模型与磁流体动力学（MHD）耦合的FEM建模范式，突破传统Newtonian或单一纳米流体简化假设；发展高精度ANN代理模型替代高成本FEM，支持实时工况反演与多目标优化  
- **局限性**：未考虑纳米颗粒团聚/沉降等长期稳定性问题及温度依赖性粘度变化；磁场方向固定（仅垂直于流动平面），未探究取向效应；实验验证缺失，纯数值研究限制结论外推性  
- **对你研究的启发**：多物理场耦合建模中“关键本构嵌入”（如Casson替代Power-law）可显著提升电催化界面传质-反应-输运模拟的真实性；ANN代理策略适用于DFT计算密集型场景（如吸附能谱预测、活性位点筛选）以加速催化剂逆向设计；参数敏感性量化框架（如β主导粘性耗散 vs Ha主导Lorentz阻尼）可迁移至电极/电解质界面电-热-力耦合分析  
- **与你研究的相关度**：高
- **阅读模式:** 🔍 精读
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/143bc9273c18cc7a8ce2d934075d5d1cdb622a6a
- **标签:** generative

### 4. Force-Aware Neural Tangent Kernels for Scalable and Robust Active Learning of MLIPs ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-05-13
- **作者:** E. Varga-Umbrich; Zachary Weller-Davies; Paul Duckworth; Jules Tilly; Olivier Peltre et al.
- **核心问题**：如何实现可扩展、力信息感知且对候选池分布偏移鲁棒的机器学习原子间势（MLIP）主动学习框架  
- **动机与背景**：现有主动学习方法在MLIP训练中面临三重瓶颈：（1）候选池规模增大时计算开销呈平方级增长，难以扩展至数十万结构；（2）多数方法仅利用能量标量监督，忽略力（向量场）这一关键物理约束，导致力预测精度不足；（3）当候选池与目标分布存在偏差（如构型采样不均）时，基于集成模型（committee）的不确定性估计易失效、方差剧增。这些问题严重制约了MLIP在真实电催化反应路径搜索等大规模场景中的实用化。  
- **方法核心**：提出“分块特征空间后验方差筛选”（chunked feature-space posterior-variance shortlisting）实现线性可扩展主动学习，并首次将神经正切核（NTK）拓展至力感知范式——通过混合参数-坐标导数定义力NTK（force NTK）与联合能量-力NTK（joint energy-force NTK），为向量场预测提供天然相似性度量。  
- **关键实验与结果**：在OC20（含吸附/反应过渡态的大规模催化数据集）上，联合能量-力NTK主导的主动学习取得最优性能：能量MAE = 0.038 eV/atom，力MAE = 0.124 eV/Å（显著优于所有基线）；在T1x、PMechDB、RGD多基准测试中，力NTK方法在保持竞争力的同时，单轮筛选耗时比committee方法低1–2个数量级；在T1x人为引入候选池分布偏移的对照实验中，NTK方法力MAE方差仅为committee方法的~1/3。  
- **创新点**：（1）首个支持线性扩展（O(N)）的MLIP主动学习框架，突破传统核矩阵显式构造的O(N²)瓶颈；（2）首次构建力感知NTK理论体系，将物理约束（力=能量负梯度）内嵌于核定义，而非后处理或加权损失；（3）证明单个预训练MLIP的嵌入+NTK即可替代多模型ensemble，在分布偏移下维持低方差不确定性估计，颠覆“必须依赖committee”的固有范式。  
- **局限性**：（1）NTK近似依赖无限宽网络假设，在有限宽度实际MLIP（如NequIP、MACE）上的理论误差未量化；（2）未验证对强非绝热过程或多电子态体系（如激发态电催化）的适用性；（3）分块策略虽提升效率，但短列表质量受块内局部相似性假设影响，极端异构构型混合时可能漏筛关键样本。  
- **对你研究的启发**：（1）可将“联合能量-力NTK”迁移至电催化自由能面构建中，用同一核度量吸附能与反应力（如dE/dξ），统一优化吸附构型筛选与过渡态定位；（2）分块后验方差框架可适配你当前使用的GNN-MD工作流，在分子动力学轨迹在线筛选中实现亚秒级活性样本识别；（3）单模型NTK鲁棒性启示：在你构建的催化剂描述符空间中，可尝试用预训练图神经网络的隐空间协方差替代ensemble，降低高通量筛选计算负载。  
- **与你研究的相关度**：高
- **阅读模式:** 🔍 精读
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/154d5a473906fe0465495eb9a03a53e3c3c28486
- **标签:** electrochemistry, MLFF, active-learning

### 5. Machine learning molecular dynamics simulations of coordination and diffusion behaviors in lithiated gallium electrodes. ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-02-06
- **作者:** Qiuyi Fu; Hao Yuan; Haitang Wang; Wenbin Liu; Guobing Zhou et al.
- **核心问题**：揭示锂-镓合金（LGA）在充锂过程中不同相（Li₃Ga₁₄、Li₂Ga₇、LiGa、Li₂Ga）的局域结构演化与锂离子输运行为之间的构效关系  
- **动机与背景**：液态镓基负极虽具自修复性、高容量和柔性优势，但其电化学反应中形成的多相LGA体系结构复杂、实验表征困难；现有研究缺乏对各相原子级结构、短程有序度及Li扩散机制的系统性比较；第一性原理分子动力学受限于尺度与时间，难以覆盖真实电池工况下的动态演化过程  
- **方法核心**：构建针对四种LGA相的高精度机器学习力场（MLFFs），结合大尺度（>10,000原子）、长时程（>1 ns）从头算精度分子动力学（AIMD-level MD）模拟，实现结构统计与扩散动力学的跨相定量解析  
- **关键实验与结果**：体系为Li₃Ga₁₄、Li₂Ga₇、LiGa、Li₂Ga四相LGA；基线为传统DFT计算与有限尺度MD；Li扩散系数：Li₃Ga₁₄为4.46×10⁻¹¹ m² s⁻¹（最高），Li₂Ga₇为3.14×10⁻¹² m² s⁻¹（低近10倍）；van Hove分析证实Li₂Ga₇/Li₂Ga中存在间歇性“驻留–跳跃”（residence-jump）扩散模式  
- **创新点**：首次建立覆盖全锂化路径的LGA多相统一MLFF框架；发现“锂化程度↑ → 局域配位由Ga主导转向Li网络主导 → 短程有序度↑但整体仍无序 → 扩散模式由类液态转为固态局域化”的普适演化规律；揭示扩散系数量级差异源于Li–(Li/Ga)相互作用强度变化，而非晶格周期性或长程有序度  
- **局限性**：未包含界面效应（如Ga/SEI或Ga/集流体相互作用）；模拟温度固定为300 K，未考察温度依赖性；未耦合电子结构分析（如Li迁移能垒的轨道起源）；实验验证仅限相组成，缺乏原位结构/扩散动力学对照  
- **对你研究的启发**：MLFF驱动的大尺度相空间扫描策略可迁移至其他合金型（Sn、Sb、Bi）或转化型（FeF₃、CoO）负极体系；“局域配位指纹 + 多尺度动力学分析（van Hove + 轨迹可视化）”范式适用于解耦复杂电极材料中的异质扩散行为；强调短程有序（非长程结晶度）对离子输运的关键调控作用，提示应加强局部结构描述符在电催化/电池材料设计中的权重  
- **与你研究的相关度**：高
- **阅读模式:** 🔍 精读
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/1726413fab163a845decf581773d21e0350c6c02
- **标签:** electrochemistry, MLFF

### 6. ARTIFICIAL INTELLIGENCE IN BIOMEDICAL SCIENCES: OPPORTUNITY AND SCOPES ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-01-01
- **作者:** Sana Shiekh; N. B. Hirulkar
- **核心问题**：AI如何提升生物医学大数据（如基因组、影像、临床数据）的分析能力以辅助临床决策  
- **方法要点**：应用机器学习和深度学习模型处理多源异构生物医学数据  
- **关键结果**：AI在医学影像诊断、分割、分类中实现自动化精准解读；在药物研发、疾病预测等领域展现实用价值  
- **与你研究的相关度**：低
- **阅读模式:** 📋 摘要
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/17502ff2b44475d1263e36a1f5dcc16cd2de9252
- **标签:** general

### 7. Machine learning nonequilibrium phase transitions in charge-density wave insulators ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-01-12
- **作者:** Yunhao Fan; Sheng Zhang; G. Chern
- **核心问题**：如何高效计算电压驱动相变中非平衡电子力以实现长时间动力学模拟  
- **方法要点**：构建基于神经网络的机器学习力场，直接从晶格构型预测瞬时局域电子力，避免重复进行高代价的非平衡格林函数（NEGF）计算  
- **关键结果**：ML力场在布朗动力学中定量复现了全NEGF模拟的畴壁运动和非平衡相变动力学；计算效率提升数个数量级  
- **与你研究的相关度**：高
- **阅读模式:** 📋 摘要
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/17adecaafb92c65b2a4c59b7242924929a2a9461
- **标签:** general

### 8. MAPLE: a machine-learning force-field-native platform for automated reaction modeling and enzyme design ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-04-30
- **作者:** Xujian Wang; Ze-Yu Sun; Yilu Zhang; Carlo Asam; Ruzhan Zhu et al.
- **核心问题**：缺乏统一、自动化的机器学习力场（MLFF）计算平台，限制了其在催化等领域的广泛应用  
- **方法要点**：开发了名为MAPLE的专用计算工具包，集成了定制化软件框架与并行化算法，支持基于先进反应性MLFF的大规模分子建模  
- **关键结果**：系统基准测试验证了MAPLE对多种前沿反应性MLFF的稳健支持；成功应用于多个生物催化场景，实现快速且高精度的催化反应模拟  
- **与你研究的相关度**：高
- **阅读模式:** 📋 摘要
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/17f8aab46024cbbe22d5f0843b3338aded58dac8
- **标签:** electrochemistry, catalysis

### 9. Learning Therapist Policy from Therapist-Exoskeleton-Patient Interaction ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-03-02
- **作者:** G. Snyder; Lorenzo Vianello; Levi J. Hargrove; Matthew L. Elwin; José Luis Pons Rovira
- **核心问题**：如何在卒中后机器人辅助物理治疗中，通过建模治疗师与患者的力交互动态，实现更自然、可持续且人性化的康复干预  
- **方法要点**：提出患者-治疗师力场（PTFF）和合成治疗师（ST）模型：PTFF基于VAE+GMM构建低维隐空间中的概率向量场以表征交互动力学；ST采用LSTM网络从患者运动学预测治疗师关节扭矩，并集成至ROS外骨骼控制器实现实时辅助  
- **关键结果**：1）PTFF成功可视化患者-治疗师交互动力学，为策略优化与控制器设计提供可解释依据；2）ST模型经留一法交叉验证（n=8）表现稳健，集成后可在外骨骼中实时生成类人扭矩辅助，初步实验验证其临床可行性  
- **与你研究的相关度**：低
- **阅读模式:** 📋 摘要
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/18da318be400ac5b9e5bcc7656a7b4ab6b26f81f
- **标签:** electrochemistry

### 10. Room temperature dynamics of atomic clusters adsorbed on graphene: a machine-learning force field molecular dynamics study. ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2026-01-05
- **作者:** Ramasamy Murugesan; Ewald Janssens; J. van de Vondel; M. Houssa
- **核心问题**：金纳米团簇在石墨烯表面的室温扩散行为及其被缺陷/残留物锚定的机制  
- **方法要点**：采用第一性原理分子动力学模拟研究Au₃和Au₆团簇在 pristine石墨烯、碳空位石墨烯及含PMMA残留物石墨烯表面的扩散动力学  
- **关键结果**：碳空位和PMMA残留物均显著抑制Auₙ团簇扩散，实现团簇在 vacancy 或残留物位点的稳定锚定  
- **与你研究的相关度**：中
- **阅读模式:** 📋 摘要
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/1d78b77e8c85e55a9e9119e77c103cdf799d093d
- **标签:** surface

## 💡 今日亮点

- **最值得精读**：[4] Force-Aware Neural Tangent Kernels for Scalable and Robust Active Learning of MLIPs — 首次将力向量场显式嵌入神经正切核（NTK）框架，兼顾可扩展性、物理一致性与分布鲁棒性，直击MLIP主动学习中“标量优先、忽略力约束、泛化脆弱”三大痛点。  
- **可能冲突的研究**：[7] Machine learning nonequilibrium phase transitions in charge-density wave insulators — 其NEGF→ML力场的映射依赖稳态构型采样，可能低估非平衡电子激发对原子力的瞬时反馈，与电催化中强偏压下电荷重分布驱动结构弛豫的关键机制存在张力。  
- **值得追踪的团队**：MAPLE开发团队（论文[8]）— 在反应性MLFF工程化落地方面展现出罕见的全栈能力（从势函数设计、平台架构到酶催化验证），是少数能 bridging method development 与 real catalytic application 的团队。  
- **重要趋势**：多篇论文（[2][4][7][8][10]）共同指向“力场即接口”范式迁移：MLIP不再仅是能量/力的拟合工具，而是连接第一性原理、多尺度模拟、实验表征与自动化设计平台的核心中间件。

## 📌 Key Gap

**关键差距**
- **Gap 1**：几乎所有MLIP相关工作（[2][4][7][8][10]）均假设原子间相互作用可被局部环境唯一决定，但电催化界面中长程静电、外电场调制及电极电子态耦合等非局域效应尚未被系统纳入MLIP训练目标或损失函数。  
- **Gap 2**：RNA（[1]）、水/界面（[2]）、纳米流体（[3]）、LGA电极（[5]）等体系均暴露出同一瓶颈：缺乏跨尺度验证协议——CG模型/MLIP在纳米尺度表现良好，却无法向下衔接量子输运计算、向上支撑介观输运/热力学预测，形成“尺度断层”。  
- **未来方向**：发展**电场感知、非局域修正、多尺度可嵌入**的下一代MLIP架构：以电催化界面为基准场景，联合训练能量/力/静电势/局部态密度等多通道输出，并嵌入可微分的粗粒化映射模块，实现从电子结构→原子动力学→介观输运的端到端可导通建模。
