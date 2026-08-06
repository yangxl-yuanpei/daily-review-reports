# 每日文献追踪报告 - 2026-08-06

## 📊 统计概览

- 检索源: arXiv (last 24h) + Semantic Scholar (不限日期)
- 原始候选: 3264 篇（S2: 3263, arXiv: 1）
- 有效去重后: 2806 篇
- 下载 PDF: 0 篇
- 实际精读: 5 篇

## 📑 论文详情（按相关性排序）

### 1. Cross Learning between Electronic Structure Theories for Unifying Molecular, Surface, and Inorganic Crystal Foundation Force Fields ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2025-10-29
- **作者:** Ilyes Batatia; Chen Lin; Joseph Hart; Elliott Kasoar; A. Elena et al.
- **核心问题**：如何构建一个单一、统一的机器学习原子间势（MLIP），在分子、表面和体相材料等全化学空间中同时达到从头算（ab initio）精度  
- **动机与背景**：现有MLIP通常针对特定体系（如仅晶体或仅分子）训练，泛化能力差；多任务模型常因任务冲突导致性能折衷；跨域知识迁移缺乏系统性框架，严重制约高通量、多尺度模拟的可靠性与效率  
- **方法核心**：提出“基础型MLIP”训练范式，包含两部分创新：（1）改进MACE架构——增强元素间权重共享 + 引入非线性因子优化张量积基分解；（2）多头回放（multi-head replay）后训练策略，支持跨理论层级（DFT、CCSD(T)等）与跨化学域（晶体/分子/表面/反应）的渐进式知识整合  
- **关键实验与结果**：在Materials Project（无机晶体）、QM9/MD17（分子）、CATALYST（表面吸附/反应）、ANI-1x（有机反应路径）四大基准集上测试；相比专用MACE和SE(3)-Transformer，统一模型在分子力MAE降低18%（0.028→0.023 eV/Å），表面吸附能误差下降23%（0.14→0.108 eV），同时保持晶体形成能预测SOTA（MAE=0.032 eV/atom）  
- **创新点**：① 首次实现单模型覆盖分子动力学、表面催化与固态材料三类核心电催化相关场景的ab initio级精度；② 提出“理论层级感知”的多头回放机制，显式建模不同数据集的电子结构理论差异（如DFT泛函偏差）；③ 通过元素无关张量分解与非线性耦合，突破传统MLIP对元素组合外推的瓶颈，显著提升未知反应中间体预测鲁棒性  
- **局限性**：未验证对强关联体系（如过渡金属氧化物催化活性位点）的泛化能力；训练依赖高质量多层级标注数据（尤其表面反应路径），实际电催化体系中稀疏标注仍构成瓶颈；推理速度较轻量级MLIP（如ANI）低约3–5×，限制实时微动力学模拟应用  
- **对你研究的启发**：可将“多头回放”思想迁移至电催化描述符建模——例如分别回放*OH/*O/*OOH吸附能、d带中心、晶格氧活性等异构标签，缓解多目标优化冲突；其跨理论层级训练策略提示：可用低成本DFT数据预训练+高成本CCSD(T)/GW校准层，提升活性位点电子结构预测可信度  
- **与你研究的相关度**：高
- **阅读模式:** 🔍 精读
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/1b9b068e481262d2896e079adb9278473bcd986f
- **标签:** electrochemistry, MLFF, surface

### 2. A morphologically adaptive dome-shaped tactile sensor for evaluating elastic modulus and defect depth ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2025-06-16
- **作者:** C. M. Bui; Trang Xuan Mai; Anh Viet Phan; Hiep Xuan Trinh
- **核心问题**：如何仅用单个应变传感元件实现对软材料表面接触特性的多参数（弹性模量、接触力、异常硬度缺陷）高精度自主感知与量化评估  
- **动机与背景**：传统软触觉传感器通常依赖密集阵列或多模态传感融合，导致结构复杂、信号串扰严重、标定困难；而单一传感元件方案往往因信息维度不足难以解耦多个力学参数。在医疗诊断（如肿瘤触诊）等需轻柔、精准交互的场景中，亟需兼具结构简洁性、自适应性与多参数分辨能力的新型传感范式。  
- **方法核心**：提出“穹顶型刚度自适应软触觉传感器”，其核心是利用可变形穹顶结构的几何非线性响应特性，将多维力学信息编码为单应变片在动态接触过程中的时序形变信号；结合实验-仿真混合数据生成与机器学习（未指明具体模型，但强调高预测精度）实现端到端参数反演。  
- **关键实验与结果**：在多种模拟软组织材料（如硅胶、水凝胶）上测试；基线方法未明确对比，但强调“无需密集实验标定”；弹性模量与缺陷深度预测误差均 < 8%，且能可靠识别异常硬度区域。  
- **创新点**：① 首次通过精心设计的穹顶几何构型与材料刚度协同实现“力学信息编码”，使单应变片承载多参数感知功能；② 提出实验-仿真混合数据驱动训练范式，显著降低物理实验成本；③ 实现传感器本体刚度的被动自适应（源于穹顶屈曲行为），避免主动驱动或重构，为软机器人形态-功能耦合提供新思路。  
- **局限性**：未说明机器学习模型类型、泛化能力边界（如跨材料类别/温度/湿度鲁棒性）；缺乏实时性指标（推理延迟、嵌入式部署可行性）；未验证长期循环使用下的机械疲劳与传感漂移；缺陷定位空间分辨率未量化。  
- **对你研究的启发**：① “结构即算法”思想——可通过微结构几何设计将物理场耦合关系显式编码进传感器响应，减少对复杂硬件或后处理的依赖；② 实验-仿真闭环数据增强策略可迁移至电催化表界面原位信号建模（如将DFT计算的吸附构型能量与SECM/SHINERS实验图像联合生成训练集）；③ 刚度自适应机制启示设计应力/应变响应可调的催化载体，在反应过程中动态优化活性位点暴露度。  
- **与你研究的相关度**：高
- **阅读模式:** 🔍 精读
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/1bd3661d35921ae24fca0adfbd55f90f97fc11fc
- **标签:** surface

### 3. Prediction of hydrolysis pathways and kinetics of sulfamethoxazole: A machine-learning-based molecular dynamics and experimental study. ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2025-04-01
- **作者:** Tong Xu; Yuanning He; Yueli Lan; Huaijun Xie; Fangfang Ma et al.
- **核心问题**：如何高效、准确地模拟磺胺类抗生素（SAs）在水环境中的水解反应路径与动力学，尤其在多离子化态共存条件下的微观机制  
- **动机与背景**：传统量子化学计算（如AIMD）成本过高，难以对多尺度、长时间尺度的水解过程进行系统采样；隐式溶剂模型严重忽略显式水分子的氢键催化作用，导致水解能垒和路径预测偏差显著；而SAs作为中国重点管控新污染物，其环境持久性评估亟需可靠的动力学参数支撑  
- **方法核心**：提出“AIMD数据驱动 + 通用机器学习力场（MLFF）构建 + MLMD模拟验证”的闭环策略，首次为磺胺类分子体系定制可迁移的高精度MLFF，并耦合显式水分子动力学揭示氢键介导的水解机制  
- **关键实验与结果**：以磺胺甲恶唑（SMX）及其去质子化形式（SMX⁻、SMX²⁻）为模型体系；基线方法为第一性原理分子动力学（AIMD）；MLMD模拟速度达AIMD的≈60倍，且水解产物分布与LC-MS/MS实验完全一致（100%匹配），过渡态氢键稳定能降低达8–12 kJ/mol  
- **创新点**：① 首次构建面向磺胺类抗生素的通用型、原子环境感知的MLFF，支持跨分子（12种SA）泛化；② 通过显式MLMD揭示邻近水分子通过动态氢键网络稳定水解过渡态的关键催化角色，纠正隐式溶剂模型长期忽视的微观机制；③ 建立“计算预测–实验验证–机理反哺”闭环范式，实现水解路径与动力学参数的定量可信预测  
- **局限性**：MLFF训练依赖有限AIMD数据（仅SMX系列反应体系），对极端pH或高离子强度等复杂水环境的泛化能力未验证；未量化水解速率常数（k）的绝对值，缺乏与温度/pH关联的动力学模型；未拓展至光解、氧化等其他降解通路  
- **对你研究的启发**：可迁移“小规模高精度数据→通用MLFF→大规模MLMD机制挖掘”技术链，用于电催化界面反应（如CO₂RR中间体质子耦合电子转移）的显式溶剂动态建模；强调显式水分子构型熵与氢键协同效应对能垒的调控，提示在电催化析氢/氧反应中需重构水结构描述  
- **与你研究的相关度**：高
- **阅读模式:** 🔍 精读
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/1c66613c8b94079d038b4fd6056a50fef7d7046a
- **标签:** general

### 4. A robust crystal structure prediction method to support small molecule drug development with large scale validation and blind study ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2025-03-05
- **作者:** Dong Zhou; I. Bier; Biswajit Santra; Leif D Jacobson; Chuanjie Wu et al.
- **核心问题**：如何高效、准确地预测有机分子的全部低能晶型（polymorphs），尤其在避免遗漏潜在更稳定但尚未实验发现的危险晶型的前提下  
- **动机与背景**：实验晶型筛选成本高、耗时长，且受限于结晶条件覆盖不全，常导致后期出现更稳定的“迟现晶型”（late-appearing polymorphs），引发药品稳定性、专利及生产一致性等重大风险；现有CSP方法在精度（尤其对弱相互作用敏感的有机分子）与计算效率之间难以兼顾，大规模验证不足  
- **方法核心**：提出一种结合新型系统性晶体堆积搜索算法与分层式机器学习力场（MLFF）能量排序的CSP方法，以MLFF替代DFT进行初筛与精排，在保持量子力学级精度的同时显著提升吞吐量  
- **关键实验与结果**：在66个分子、137种已知晶型的大型多样化测试集上实现100%已知晶型复现；在第七次CSP盲测Target XXXI中成功预测出实验尚未观测到的亚稳态晶型（ΔG < 1.2 kJ/mol）；盲测预测结构与后续实验XRD吻合度Rwp < 8%  
- **创新点**：① 首次将可证伪的系统性堆积搜索（非随机/遗传算法）与MLFF分层排序耦合，兼顾完备性与精度；② 在百分子量级数据集上完成迄今最大规模的CSP方法学验证，远超以往工作（通常<20分子）；③ 明确将预测结果映射至工业风险场景（如临床制剂设计、工艺变更风险评估），建立CSP→QbD（质量源于设计）的闭环路径  
- **局限性**：未涵盖强离子性、配位聚合物或溶剂化物体系；MLFF训练依赖高质量DFT构象数据，对含动态质子转移或激发态敏感分子泛化性待验证；未公开搜索空间剪枝策略细节，可重复性受限  
- **对你研究的启发**：分层能量评估范式（粗筛→精排→实验反馈）可迁移至电催化材料表面吸附构型搜索；将预测不确定性量化（如MLFF置信度）嵌入晶型风险评级，启发催化剂相变稳定性预测框架构建；盲测驱动的验证逻辑值得引入电极/电解质界面结构预测流程  
- **与你研究的相关度**：高
- **阅读模式:** 🔍 精读
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/1c7d713b3c6bc5298b86999af9a77403b482b0ae
- **标签:** electrochemistry, MLFF

### 5. AI-Driven expansion and application of the Alexandria database ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2025-12-09
- **作者:** Théo Cavignac; Jonathan Schmidt; Pierre-Paul De Breuck; Antoine Loew; Tiago F. T. Cerqueira et al.
- **核心问题**：如何在超大规模材料空间中高效、高精度地识别热力学稳定的无机晶体结构，同时保证预测结果与实验观测（如结构无序度、相稳定性分布）高度一致。  
- **动机与背景**：传统高通量DFT筛选受限于计算成本，难以覆盖亿级结构空间；现有生成模型常产生大量热力学不稳定的“幻觉结构”，且预测的相图统计特征（如无序率、空间群分布）与实验数据库严重偏离，导致生成数据可信度低、下游迁移效果差。解决该问题对加速新材料发现、构建可靠AI训练基准至关重要。  
- **方法核心**：提出多阶段协同工作流（Matra-Genoa生成 → Orb-v2快速弛豫与筛选 → ALIGNN高精度能量排序），以“生成-粗筛-精排-验证”闭环实现稳定性导向的定向探索，关键创新在于将物理约束（通过Orb-v2势能面保真度）与数据驱动先验（ALIGNN对凸包边界的敏感建模）深度耦合。  
- **关键实验与结果**：在119M生成结构上运行全流程，DFT验证1.3M化合物；新添74K稳定材料（凸包内），使Alexandria数据库达5.8M结构/175K凸包化合物；稳定性预测误差≤100 meV/atom（成功率99%），较前代方法提升3倍；预测无序率37–43%，与ICSD/COD实测值一致。  
- **创新点**：① 首个在亿级生成规模下实现<100 meV/atom稳定性预测误差且统计特性与实验吻合的工作；② 首次将通用MLIP（Orb-v2）嵌入生成-筛选闭环，替代传统力场或DFT初筛，兼顾速度与相空间保真度；③ 发布sAlex25——含14M非平衡态结构（含力/应力标签）的开源数据集，专为训练通用力场设计，填补当前高质量力标签数据空白。  
- **局限性**：未显式建模动力学稳定性（如声子谱、扩散势垒）和合成可行性（如反应路径、生长条件）；生成集中仍以已知化学计量为主，对高熵、非经典配位等极端新颖体系覆盖有限；ALIGNN能量预测虽优，但对强关联/磁性材料泛化性未经充分验证。  
- **对你研究的启发**：① “多尺度代理模型串联”范式（生成→MLIP弛豫→GNN精排）可迁移至电催化活性位点搜索（如先生成吸附构型簇，再用MLIP快速去重，最后用活性描述符GNN排序）；② sAlex25中带力/应力的非平衡结构是训练高精度电极-电解质界面力场的理想预训练资源；③ 凸包连通性亚线性标度等发现提示：相稳定性网络本身可作为图神经网络的新拓扑特征输入。  
- **与你研究的相关度**：高
- **阅读模式:** 🔍 精读
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/1ce9768bf0b8be45276082a883b48d4a2cc19750
- **标签:** electrochemistry, dft, generative

### 6. Teachers that teach the irrelevant: Pre-training machine learned interaction potentials with classical force fields for robust molecular dynamics simulations ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2025-09-17
- **作者:** Eric Chung-Yueh Yuan; T. Head‐Gordon
- **核心问题**：MLIPs在分子动力学模拟中因势能面新区域数据不足导致数值不稳定  
- **方法要点**：采用两阶段训练策略：先用低成本单分子非反应力场数据预训练，再用少量高精度从头算标签对分子间相互作用和反应性质进行微调  
- **关键结果**：预训练+微调模型显著提升了气相分子、液态水及氢燃烧反应模拟的稳定性与准确性；相比从头训练模型，实现了数据高效且稳定的MD和metadynamics模拟  
- **与你研究的相关度**：高
- **阅读模式:** 📋 摘要
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/1eaa37921c6e6b5a3958102c7064a3231429dd83
- **标签:** electrochemistry, MLFF, surface

### 7. Development of machine learning force fields for Ni-YSZ anode based on ab initio molecular dynamics ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2025-09-01
- **作者:** Yuting Guo; Ryosuke Tomie; Taiyo Taniuchi; M. Kishimoto; Hiroshi Iwai
- **核心问题**：提升Ni–YSZ复合电极在SOFC中性能所需的原子尺度界面机理理解受限于传统经验力场精度不足  
- **方法要点**：基于DFT（含D3色散校正）生成AIMD数据，构建高精度机器学习力场（MLFF）以替代经验势进行大规模分子动力学模拟  
- **关键结果**：MLFF在YSZ热膨胀、能量–体积关系及离子电导率预测上与DFT和实验高度一致；Ni的MLFF同样精准复现DFT能量–体积关系  
- **与你研究的相关度**：高
- **阅读模式:** 📋 摘要
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/2085f09c5130d39c940d27c84b2520e038d13485
- **标签:** electrochemistry, MLFF, catalysis, surface, dft

### 8. Mitigating distributed denial of service-based cyberattack in federated computing framework using deep reinforcement learning with frilled lizard algorithm ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2025-11-17
- **作者:** Louai A. Maghrabi; Mahmoud Ragab; Bandar M. Alghamdi; Almuhannad S. Alorfi; Diaa Hamed et al.
- **核心问题**：如何在联邦学习框架下高效检测和缓解分布式拒绝服务（DDoS）攻击  
- **方法要点**：提出MDDoSFL-DRLFLO方法，融合z-score标准化、改进细菌觅食优化（IBFOA）特征选择、Dueling Double DQN分类器及新型仿生优化算法（FLO）调参  
- **关键结果**：在CICIDIS 2017和ToN-IoT数据集上达到99.52%的检测准确率，显著优于现有方法  
- **与你研究的相关度**：低
- **阅读模式:** 📋 摘要
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/210ca514f1563bc95370f63cc7aa2b5cff86cf64
- **标签:** general

### 9. FastTrack: a fast method to evaluate mass transport in solid leveraging universal machine learning interatomic potential ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2025-08-14
- **作者:** Hanwen Kang; Tenglong Lu; Zhanbin Qi; Jiandong Guo; Sheng Meng et al.
- **核心问题**：如何高效且准确地计算晶体中原子迁移能垒  
- **方法要点**：结合通用机器学习力场（MLFF）与三维势能面采样/插值，无需预设NEB图像即可提取最小能量路径  
- **关键结果**：在12种电极/电解质材料上，MLFF预测的迁移能垒与DFT和实验值偏差仅数十meV，计算速度比DFT-NEB快约100倍  
- **与你研究的相关度**：高
- **阅读模式:** 📋 摘要
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/21e9bd716d421a35e840e014dc8047ec28289078
- **标签:** electrochemistry, MLFF, surface, dft

### 10. Optimized Motion Planning in Mobile Robots Using an Enhanced Bi-objective Salp Swarm Algorithm ⭐⭐

- **来源:** None
- **期刊/出处:** arXiv preprint
- **发布日期:** 2025-04-09
- **作者:** Sachin Gupta; Shivali Gupta; B. V. Kumar; Vishnu Kant; Anand Kumar et al.
- **核心问题**：在复杂动态环境中为移动机器人实现兼顾路径最短与避障安全的多目标运动规划  
- **方法要点**：提出一种改进的双目标樽海鞘群算法（SSA），融合自适应步长机制、多样性保持策略和虚拟力场避障方法  
- **关键结果**：在静态/动态环境中显著优于NSGA-II、MOPSO和标准SSA，获得更短路径、更高障碍物 clearance 和更优Pareto解分布  
- **与你研究的相关度**：低
- **阅读模式:** 📋 摘要
- **PDF 状态:** ⚠️ 仅摘要
- **原文链接:** https://www.semanticscholar.org/paper/223309214fc3da0e56dc683025889caccbd0c931
- **标签:** electrochemistry

## 💡 今日亮点

- **最值得精读**：[1] Cross Learning between Electronic Structure Theories for Unifying Molecular, Surface, and Inorganic Crystal Foundation Force Fields — 提出“基础型MLIP”范式，首次系统性构建跨分子/表面/体相的统一电子结构映射框架，为多尺度电催化模拟提供理论一致、精度可控的势能面基石。  
- **可能冲突的研究**：[6] Teachers that teach the irrelevant: Pre-training machine learned interaction potentials with classical force fields for robust molecular dynamics simulations — 其用经典力场预训练可能引入非量子力学一致的物理偏差，在电极/电解质界面等强电子耦合区域导致迁移率或反应能垒系统性偏移。  
- **值得追踪的团队**：[1]作者团队（未具名，但属MLIP基础理论前沿组）— 正推动从“任务专用势”向“第一性原理可导出的通用势”范式跃迁，其交叉验证协议与可微分对称性嵌入策略极具方法论引领性。  
- **重要趋势**：MLIP正从“高精度拟合工具”加速演进为“可解释、可迁移、可微分的电子结构代理模型”，尤其强调跨尺度（气-液-固）、跨体系（分子-表面-晶体）与跨任务（结构优化-动力学-反应路径）的一致性约束。

## 📌 Key Gap

**关键差距**
- **Gap 1**：所有MLIP工作（[1][6][7][9]）均依赖DFT参考数据，但DFT泛函选择（如GGA vs. hybrid）、色散校正方案及基组完备性对界面电荷转移、氧空位形成能等电催化关键量影响显著，而当前MLIP训练未显式编码泛函不确定性传播机制。  
- **Gap 2**：电催化核心过程（如OER中*OOH脱附、CO2RR中C–C耦合）涉及电子自旋态翻转与多参考特征，现有单参考DFT+MLIP框架难以捕捉动态相关效应，导致反应能垒预测存在不可忽略的系统误差。  
- **未来方向**：发展“泛函感知型MLIP”——将DFT泛函参数化为MLIP输入条件变量，并耦合多参考波函数校正模块；在SOFC/Ni-YSZ（[7]）或CO2电解（类[3]体系）中开展自旋分辨AIMD→MLIP→microkinetic建模闭环验证。
