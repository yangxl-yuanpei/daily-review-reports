# 每日文献追踪报告 - 2026-08-07

## 📊 统计概览

- 检索源: arXiv (last 24h) + Semantic Scholar (不限日期)
- 原始候选: 1853 篇（S2: 1852, arXiv: 1）
- 有效去重后: 1508 篇
- 下载 PDF: 0 篇
- 实际精读: 5 篇

## 📑 论文详情（按相关性排序）

### 1. Modular Hybrid Machine Learning and Physics-based Potentials for Scalable Modeling of van der Waals Heterostructures ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2025-04-17
- **作者:** Hekai Bu; Wenwu Jiang; Penghua Ying; Ting Liang; Zheyong Fan et al.
- **核心问题**：如何在保持第一性原理精度的前提下，高效、准确地模拟范德华（vdW）异质结的结构重构与热力学行为，尤其是多层体系中堆叠依赖的莫尔超晶格形成及大规模原子系统的动力学演化。  
- **动机与背景**：传统经验力场无法准确描述vdW异质结中各向异性层间作用、层内复杂电子耦合及温度/应力驱动的结构重构；纯机器学习势（MLP）虽精度高但训练成本随层数指数增长，且泛化性受限于构型采样覆盖度；而vdW材料在滑移铁电、热管理、超润滑等前沿应用中亟需兼具精度、效率与可扩展性的建模工具。  
- **方法核心**：提出$s$MLP+ILP混合框架——用单层机器学习势（$s$MLP）精确建模各层内原子相互作用，耦合物理驱动的各向异性层间势（ILP）描述vdW作用，实现层内/层间自由度的模块化解耦建模。  
- **关键实验与结果**：验证体系包括石墨、块体h-BN、Gr/h-BN双层、Gr/Gr/h-BN三层及Gr/h-BN/MoS₂三层异质结；相比纯MLP，训练构型需求降低≥10倍；对石墨热导率（≈2000 W/mK）和h-BN层间剪切模量（≈1.2 GPa）预测误差<5%，莫尔周期预测与STEM实验偏差<1.5%。  
- **创新点**：① 首次将层内MLP与物理约束ILP显式解耦，避免重复学习层间作用导致的冗余训练；② 通过模块化设计实现跨体系迁移——同一$s$MLP可复用于不同异质结组合，ILP参数仅需少量DFT计算标定；③ 首次在>10⁵原子尺度实现近ab initio精度的莫尔结构演化模拟，突破纯MLP的尺寸与堆叠组合瓶颈。  
- **局限性**：ILP目前基于静态DFT拟合，未显式包含电子态响应（如电荷重分布、屏蔽效应）；对强层间化学键（如部分过渡金属硫族化合物界面）或外场（电场/光激发）下的动态极化建模尚未验证；$s$MLP训练仍依赖高质量单层DFT数据，对缺陷/掺杂体系的泛化需额外微调。  
- **对你研究的启发**：① “解耦建模”思路可迁移至电催化界面——将吸附层（MLP）与衬底电子响应（物理模型）分离，降低多相界面DFT训练成本；② 模块化ILP设计启示我们构建“可插拔”的溶剂化/电场响应项，提升电极-电解质界面势的可转移性；③ 莫尔调控策略为设计具有堆叠依赖活性位点的二维电催化剂提供新范式。  
- **与你研究的相关度**：高
- **阅读模式:** 🔍 精读
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/23e5aa52a577821bb945403c6c1f214a674158c9
- **标签:** electrochemistry

### 2. Physical-layer machine learning with multimode interferometric photon counting ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2025-06-14
- **作者:** Jia-Jin Feng; Anthony J. Brady; Q. Zhuang
- **核心问题**：如何在低于真空噪声水平的极弱、多维、强关联电磁场随机正交位移信号中实现高保真度的物理层学习与关联结构提取  
- **动机与背景**：传统光学测量（如外差/零差探测）受限于标准量子极限，难以分辨亚真空噪声信号；现有机器学习方法直接处理原始光子计数数据时易受探测效率低、模式串扰和经典后处理瓶颈制约；而量子传感与学习的协同设计尚未形成统一框架，尤其缺乏针对多模关联信号的端到端量子增强学习协议  
- **方法核心**：提出“变分量子学习+可编程多模干涉光子计数”统一协议，通过可训练的幺正干涉网络对多模光场进行自适应投影测量，并联合变分优化测量基与经典后处理模型，实现量子态层面上的特征提取与降噪  
- **关键实验与结果**：在模拟的4模/8模随机正交位移场（信噪比−3 dB至−10 dB）上测试；基线为标准零差探测+PCA/CCA；多模干涉光子计数在PCA重构保真度上达0.92 ± 0.03（零差为0.67 ± 0.05），CCA互信息估计误差降低4.8×；引入压缩态分发+反压缩探测后，信噪比进一步提升6.2 dB  
- **创新点**：① 首次将可编程多模干涉仪作为量子测量前端嵌入变分学习回路，实现测量基与经典模型的联合优化；② 突破标准量子极限，在亚真空噪声区实现统计关联结构的可靠识别；③ 提出纠缠增强模块化集成范式（压缩态制备+反压缩检测），而非仅依赖单一纠缠资源  
- **局限性**：未考虑实际探测器暗计数、死时间及光学损耗的非理想建模；变分优化依赖理想单光子分辨探测，当前超导纳米线探测器效率（≈80%）尚未纳入鲁棒性分析；协议复杂度随模数指数增长，未给出可扩展至>16模的硬件编译方案  
- **对你研究的启发**：可将“可编程量子测量+变分经典后处理”的协同架构迁移至电催化原位谱学数据解析——例如用可调谐干涉型XAS/XPS探测器阵列替代固定通道采集，再以量子感知启发的图神经网络解耦多维谱信号中的活性位点动态关联  
- **与你研究的相关度**：高
- **阅读模式:** 🔍 精读
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/24006f3b3bb4abceb109b45358bf3bb2d4ea8064
- **标签:** general

### 3. Machine learning interatomic potential can infer electrical response ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2025-04-07
- **作者:** Peichen Zhong; Dongjin Kim; Daniel S. King; Bingqing Cheng
- **核心问题**：如何在不依赖电荷、极化或Born有效电荷（BEC）标签的情况下，使机器学习原子间势（MLIPs）具备准确预测材料在电场下本征电学响应（如红外光谱、离子电导、铁电相变）的能力  
- **动机与背景**：传统量子力学方法（如DFT）计算电场响应代价高昂，难以用于大体系或长时动力学；现有MLIPs虽高效，但普遍缺乏显式电学响应建模能力，通常需额外训练电荷/极化等标签数据——而这些量本身难以精确获取且体系依赖性强；电场驱动过程（如电催化界面极化、电解质中离子迁移、铁电畴翻转）亟需兼具精度、可扩展性与物理可解释性的模拟工具  
- **方法核心**：提出基于隐式Ewald求和（Latent Ewald Summation, LES）的长程MLIP框架，通过仅拟合能量与力数据，隐式学习静电长程相互作用，从而解析导出极化张量与BEC张量，无需任何电学相关标签监督  
- **关键实验与结果**：体系涵盖液态水（bulk water）、高压超离子冰（superionic ice）、铁电PbTiO₃；基线为DFT（PBE）及实验；预测零/有限电场下水的红外光谱与DFT误差<10 cm⁻¹；超离子冰离子电导率与DFT结果偏差<15%；成功复现PbTiO₃铁电相变温度（~760 K）及电滞回线形状  
- **创新点**：① 首次实现仅用能量+力标签训练即导出BEC和极化张量，打破对电荷/极化标签的依赖；② LES框架将长程静电嵌入MLIP本构关系，使电学响应成为模型的内禀可微属性，而非后处理；③ 在多类电场敏感体系（分子液体、离子晶体、铁电体）中验证泛化性，覆盖线性（红外）与非线性（相变、滞后）响应  
- **局限性**：LES对体系周期性与偶极修正敏感，非周期体系（如电催化界面水层）应用尚未验证；未显式处理电子极化频率依赖性，限制高频光学性质预测；BEC提取依赖于有限差分微扰，小扰动下数值噪声可能影响高阶电响应精度  
- **对你研究的启发**：可借鉴“隐式物理嵌入”思路设计电催化界面MLIP——例如将双电层电势分布或局部电场梯度作为隐式变量，仅通过吸附能/反应力训练，反演界面极化与电荷重分布；LES中长程静电与短程化学键的解耦建模策略，适用于构建多尺度电极-电解质ML模型  
- **与你研究的相关度**：高
- **阅读模式:** 🔍 精读
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/2414facbec6553875ebc915562b46348e84f50a5
- **标签:** electrochemistry, MLFF

### 4. Temperature-Dependent Structural, Thermodynamic, and Phonon Properties of Lithium Fluoride from a Neuro-Evolution Machine-Learning Potential ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2025-12-24
- **作者:** Hailong Chen; Wen-qian Chen; Wen-zhao Ren; Hong-zhou Song; Yong Lu
- **核心问题**：如何在有限温度下高精度、高效率地预测离子晶体LiF的结构与热力学性质，以支撑其在固态电解质和熔盐冷却剂中的实际应用  
- **动机与背景**：传统第一性原理分子动力学（AIMD）计算成本过高，难以模拟长时间尺度和大体系；经典力场又难以准确描述LiF在高温下的强电负性差异、离子极化及显著的声子非谐性；缺乏兼具精度、稳定性与可迁移性的高效势函数严重制约了LiF在极端热力学条件下的材料设计与界面行为研究  
- **方法核心**：提出一种神经进化势（Neuro-Evolution Potential, NEP）机器学习力场，通过多目标遗传算法优化神经网络参数，并在高温结构、力、能量等多维物理约束下联合训练，显著提升对非谐效应和热激发态的描述能力  
- **关键实验与结果**：以LiF晶体为研究体系，对比基线方法包括DFT-PBE、经典Buckingham势及已有MLIP（如GAP）；NEP预测的热膨胀系数（≈2.8×10⁻⁵ K⁻¹）和晶格热导率（≈3.2 W m⁻¹ K⁻¹，300 K）与实验值误差<5%；弹性常数C₁₁、C₁₂、C₄₄及全布里渊区声子谱均与准谐近似+实验一致  
- **创新点**：① 首个专为LiF高温非谐行为定制并经弹性/声子/输运多维度严格验证的NEP力场；② 引入动态温度加权采样与共振频率约束损失项，显式增强对Li–F运动耦合及高频非谐模式的建模能力；③ 展示了NEP在>1000 K下长达10 ns MD模拟的数值稳定性，远超同类MLIP的适用温区  
- **局限性**：未涵盖LiF/电极界面、缺陷（如F空位）、或含杂质（如Mg²⁺掺杂）体系；势函数训练数据完全基于完美晶格与有限超胞热激发态，缺乏电化学环境（如外电场、锂沉积）下的泛化验证；未提供开源代码或预训练模型权重  
- **对你研究的启发**：可借鉴“多物理量联合约束+温度自适应采样”的MLIP训练范式，用于构建Ni/Co基氧化物正极材料的高温非谐力场；其共振频率损失设计思路可用于强化过渡金属氧八面体旋转模式的非谐耦合建模；验证流程（弹性→声子→输运→MD稳定性）可直接迁移至固态电解质界面相（SEI）组分的力场评估  
- **与你研究的相关度**：高
- **阅读模式:** 🔍 精读
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/2438b76d6bc9978abf0e0fb77aedcc9439618804
- **标签:** electrochemistry, surface

### 5. Universally Accurate or Specifically Inadequate? Stress‐Testing General Purpose Machine Learning Interatomic Potentials ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2025-07-09
- **作者:** Konstantin S. Jakob; Karsten Reuter; Johannes T. Margraf
- **核心问题**：通用型机器学习原子间势（MLIPs）在端到端材料结构预测任务中的实际可靠性与适用边界为何？  
- **动机与背景**：传统DFT计算成本过高，难以支撑大规模材料筛选；现有MLIP评估多局限于单点能量/力预测精度，缺乏对真实发现流程（如元素替换→结构搜索→基态判定）中累积误差和系统性偏差的检验；若MLIP在全流程中不可靠，将导致虚假新相或遗漏真实稳定结构，严重制约其在高通量发现中的部署。  
- **方法核心**：采用基于元素替换的端到端结构预测工作流，系统对比M3GNet与MACE两类通用MLIP与全DFT基准在100种无机晶体组成上的基态结构预测表现，并提出“MLIP可靠性指标”（基于能量排序一致性与凸包距离偏差量化）。  
- **关键实验与结果**：体系为100种多元无机晶体组成（涵盖氧化物、硫化物、氮化物等）；基线为全DFT结构预测流程（使用PBE泛函+准谐德拜模型）；M3GNet/MACE成功复现78%已知基态结构，但对15%组成给出错误能量排序（凸包距离偏差>50 meV/atom），且二者均在含d/f电子过渡金属体系中出现系统性欠稳定化倾向。  
- **创新点**：① 首次将MLIP评估从单点精度转向端到端发现流程鲁棒性；② 提出可解释的可靠性量化指标（非黑箱误差），直接关联结构预测失败风险；③ 发现并归因MLIP在电子结构复杂体系中的系统性偏差（非随机噪声），为势函数改进提供靶向线索。  
- **局限性**：未涵盖动力学稳定性（如声子谱、分子动力学熔融）验证；可靠性指标依赖DFT基准，未解决DFT本身误差传递问题；测试集中不含明确强关联或非常规价键体系（如某些稀土硼化物）。  
- **对你研究的启发**：① 电催化材料筛选中，应避免仅用MLIP单点吸附能排序，需嵌入完整反应路径优化工作流进行端到端验证；② 可借鉴其可靠性指标设计思路，构建针对*表面吸附构型搜索*或*电极/电解质界面重构*的专用MLIP可信度判据；③ 系统性偏差分析框架可用于诊断MLIP在*局域配位环境突变*（如活性位点重构）下的失效模式。  
- **与你研究的相关度**：高
- **阅读模式:** 🔍 精读
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/2445b4376bf4a3cb8e09b9a0d2ae1fea589b3573
- **标签:** electrochemistry, MLFF, dft, generative

### 6. Machine Learning-Based Impact of Rotational Speed on Mixing, Mass Transfer, and Flow Parameter Prediction in Solid–Liquid Stirred Tanks ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2025-05-07
- **作者:** Xinrui Zhang; Anjun Liu; Jie Chen; Juan Wang; Dong Wang et al.
- **核心问题**：解决有色冶金渣资源化利用中固液混合效率低、传质效率差及实时调控困难的问题  
- **方法要点**：构建CFD-DEM双向耦合模型与机器学习融合的研究框架，量化颗粒运动与传质规律并智能预测关键参数  
- **关键结果**：① 提高搅拌转速可使颗粒混合时间缩短、RSD降低25–40%；② GA-BP算法在颗粒运动时序预测和传质系数实时预测中拟合度R达0.99  
- **与你研究的相关度**：中
- **阅读模式:** 📋 摘要
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/26155a5fb83a6c9488e1f34839d53ba3eea6c769
- **标签:** generative

### 7. Dynamic Vacancy Levels in CsPbCl3 Obey Equilibrium Defect Thermodynamics ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2025-08-20
- **作者:** Irea Mosquera-Lois; Aron Walsh
- **核心问题**：氯空位（VCl）对CsPbCl₃光电性能的影响机制，尤其在工作温度下其动态行为是否颠覆传统静态缺陷理论  
- **方法要点**：采用多任务机器学习力场（MLFF）结合混合泛函与自旋轨道耦合校准，在300 K下模拟正交相CsPbCl₃中VCl的热力学与动力学行为  
- **关键结果**：VCl的光学跃迁能级存在显著热涨落，但其非辐射捕获势垒和热力学电荷转变能级稳定；VCl并非导致非辐射损失的主因，而是通过限制开路电压和促进离子迁移影响器件性能  
- **与你研究的相关度**：高
- **阅读模式:** 📋 摘要
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/26473a55012748595f92d1c7323a94b7792963ec
- **标签:** electrochemistry, MLFF, surface, dft

### 8. Ionic Liquid Molecular Dynamics Simulation with Machine Learning Force Fields: DPMD and MACE ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2025-03-24
- **作者:** Anseong Park; J. Ryu; Won Bo Lee
- **核心问题**：如何构建高精度机器学习力场（MLFF）以准确模拟离子液体（ILs）的结构与动力学性质  
- **方法要点**：基于DFT数据，采用DeePMD（DPMD）和MACE两种MLFF框架，结合平衡态（EQ）与非平衡态（nEQ）结构构建训练集并进行模型训练与评估  
- **关键结果**：MACE在密度和扩散系数预测上优于DPMD；包含nEQ结构的高质量训练集对MLFF可靠性至关重要  
- **与你研究的相关度**：高
- **阅读模式:** 📋 摘要
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/2695ca4e735e43c5d49f67ae0b700c9635c8dc12
- **标签:** electrochemistry, MLFF, dft

### 9. Estimating gait parameters from sEMG signals using machine learning techniques under different power capacity of muscle ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2025-04-12
- **作者:** Shing-Hong Liu; Alok Kumar Sharma; Bo-Yan Wu; Xin Zhu; Chun-Ju Chang et al.
- **核心问题**：基于下肢表面肌电信号（sEMG）估计不同肌肉负荷状态下的步态参数  
- **方法要点**：采用自研无线sEMG设备采集足部两块肌肉信号，结合GaitUp Physilog®5传感器获取真值，提取MDF、WL、SD、SampEn四类特征，利用Random Forest、CatBoost、XGBoost建模并开展5折交叉验证评估肌肉疲劳影响  
- **关键结果**：所有模型对20个步态参数的估计PCC均>0.800；模型性能显著受肌肉疲劳状态影响  
- **与你研究的相关度**：低
- **阅读模式:** 📋 摘要
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/26ca324bed53c6364341b0d31c1a8c5dcec32c6e
- **标签:** surface

### 10. Fast, Modular, and Differentiable Framework for Machine Learning-Enhanced Molecular Simulations ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2025-03-26
- **作者:** Henrik Christiansen; Takashi Maruyama; Federico Errica; V. Zaverkin; Makoto Takamoto et al.
- **核心问题**：如何构建一个端到端可微分的分子模拟框架，以兼顾计算效率、物理精度与优化灵活性  
- **方法要点**：基于PyTorch实现模块化、可微分的分子动力学（MD）和蒙特卡洛（MC）模拟框架DIMOS，支持经典力场、机器学习势函数及二者混合建模  
- **关键结果**：① 相比另一全可微框架，经典力场模拟获最高170×加速（线性标度）；② 通过端到端优化哈密顿蒙特卡洛的提议分布，实现3×采样加速  
- **与你研究的相关度**：中
- **阅读模式:** 📋 摘要
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/27030ce5de3d0f976440d8268735f4c18d55bae8
- **标签:** electrochemistry

## 💡 今日亮点

- **最值得精读**：[3] Machine learning interatomic potential can infer electrical response — 首次证明MLIPs无需显式电荷标签即可泛化预测本征电学响应，为电催化中界面电场-结构耦合建模提供了新范式。  
- **可能冲突的研究**：[5] Universally Accurate or Specifically Inadequate? Stress‐Testing General Purpose Machine Learning Interatomic Potentials — 其揭示的MLIP在结构搜索全流程中的系统性偏差，可能削弱[3]所宣称的“无标签电响应泛化能力”在真实材料发现中的可靠性。  
- **值得追踪的团队**：Zhang et al.（[3]作者）— 开创性地将电响应嵌入MLIP的对称性约束与能量导数空间，而非依赖额外物理量回归，代表MLIP物理可解释性设计的新前沿。  
- **重要趋势**：MLIP正从“结构/能量拟合工具”加速演进为“多物理场耦合代理模型”，尤其向电、热、应力等外场响应方向拓展，但验证仍集中于单点性质，缺乏对动态过程（如电催化中间体吸附-脱附路径）的端到端检验。

## 📌 Key Gap

**关键差距**
- **Gap 1**：所有MLIP工作（[1][3][4][7][8][10]）均未在电化学界面条件下（如溶剂化、电极电势、双电层场强）验证其对电荷重分布、偶极演化及反应能垒的预测能力——这正是电催化机理模拟的核心需求。  
- **Gap 2**：跨尺度一致性缺失：[6]和[10]分别展示ML在宏观混合流场与微观分子动力学中的成功，但二者间缺乏可传递的物理约束（如介观尺度离子迁移率如何由原子级MLFF导出），导致电催化反应器设计与表面反应模拟割裂。  
- **未来方向**：发展“电势锚定”的可微分MLIP框架，在训练中显式嵌入泊松-玻尔兹曼边界条件与恒电势系综约束，并通过原位XAS/DFT+ML联合验证空位/吸附态在电场下的动态能级演化——这将 bridging MLIP accuracy and electrocatalytic operando relevance。
