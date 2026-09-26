# Frontier Research Annotations — Stage G / 2025-Q3 (auto-doc-engine)

**Reviewer:** 淇（Qi）· 2026-09-26 · Independence: 独立于 Stage G 交付线与同日 Successor 补全链（SPEC §12） · Rewrite: NONE

## 1. Stage-level assessment

- 厚度：auto-doc 20,468 / 三仓 55,695——**Successor 补全后回升**（从 thin 交付态恢复），但回升构成需拆解：新增行主要落在 ledger 复述与月度重构扩容，**REGISTER 仍 ~0 锚引用（1,165 字符）——G 的证据面未随行数恢复**
- 主题：G1 CodeMeta 3.0（2025-07-13）/ G2 immutable releases（2025-08-26）/ G3 Pandoc 3.8（2025-09-06 前后）——**三个对象均有官方锚，选题密度高**
- 治理：RQ 缺席第六例；REVIEW 独立性 GAP 第七例——**G 的治理件在 Successor 补全中未获补位**（补的是 ledger 不是治理）

## 2. Per-file annotations

### 2.1 G1_CODEMETA30_SOFTWARE_METADATA_RELATIONSHIPS.md
- [事实核验] **CodeMeta 3.0 于 2025-07-13 发布**（codemeta.github.io 官方）——v2→v3 crosswalk 携带；关系扩张三线（source vs application / contributor role 时限化 / review record 存在性与效力分离）——"metadata becoming less flat"的月度定性准确
- [异源锚] codemeta.github.io（3.0 release 页）· GitHub codemeta/codemeta 仓库 releases tag
- [决定] CONFIRMED（双源既有）+ REGISTER 格式化补行

### 2.2 G2_IMMUTABLE_RELEASES_AS_PUBLICATION_IDENTITY.md
- [事实核验] **GitHub immutable releases 于 2025-08-26 进入公开预览**（GitHub changelog 官方——release 一经发布不可原地替换，防篡改+供应链防线）——G2 的"publication immutability separate from asset correctness"命题轴正确；**与十仓体系的 append-only/哈希链封存哲学同构**（批注者注：这条跨体系同构是本 Stage 最值得显式化的观察——体系的哲学在业界工具层有直接对应物）
- [异源锚] github.blog changelog（08-26）· docs.github.com immutable releases 文档
- [决定] APPEND_RELATION：同构观察一句（boundary: interpretive note）

### 2.3 G3_PANDOC38_XML_AST_AND_TRANSFORMATION_IDENTITY.md
- [事实核验] **Pandoc 3.8 于 2025-09-06 前后发布**（含 XML 形式的 AST 精确序列化——"converter-native structural interchange"）——G3 命题"AST identity != source-byte identity"的版本节点；**Pandoc 时间线至此完整：3.2（2024-05）→3.7（2025-05）→3.8（2025-09）——B/F/G 三 Stage 的 Pandoc 轴全线对齐**（纵向连贯性 GOOD）
- [决定] CONFIRMED + 纵向连贯性注记

### 2.4 MONTH_2025_07/08/09（25/22/21 行档）
- **07：** CodeMeta 3.0（07-13）；GPT-5 在 7 月尚未正式发布，正式发布日期为 2025-08-07——**若 07 月文件把 GPT-5 写成已发布事件，则属于时间前移错误，VERIFY_IN_PLACE；本批注不再把 7 月概括为“预告期”**
- **08：** immutable releases（08-26）；GPT-5（08-07——AI 侧背景锚）；MCP 生态三分（OpenAI/Google/Anthropic 三家协议线并存）
- **09：** Pandoc 3.8（06 前后）；PyPI 供应链持续；Q3 收束
- [判定] G 的月度文件经 Successor 扩容后密度回升——07 的 GPT-5 时间前移风险一处 VERIFY

### 2.5 SYNTHESIS/BRIEF/REGISTER/REVIEW/HANDOFF/CONTRIBUTOR
- [Synthesis] "identity is increasingly layered"（身份分层）七层链条（描述什么对象/关系类型/发布什么/能否变异/溯源声明/结构模型）+ 收束句 "Better identity does not automatically produce better truth"——**本 Stage 命题质量七阶段最高**；NO_CURRENT_REPOSITORY_DRIFT 三连声明合规
- [Brief] RQ 缺席第六例
- [REGISTER] ~0 锚引用——**Successor 补了 ledger 未补锚面——correction：五官方锚格式化入 REGISTER**（codemeta/github.blog/docs.github/pandoc releases/W3C RO-Crate）
- [REVIEW] GAP 第七例；[HANDOFF] F→G 衔接成立；[CONTRIBUTOR] Successor 参与者角色声明需核（VERIFY：Successor 批次的 CRediT 角色是否已并入）

## 3. 季度生态史补全 — 2025-Q3

**Q3 主线="工件身份的不可变性时代"**：7 月 CodeMeta 3.0 把软件元数据的关系语义推到最厚（源/应用分离、角色时限化、评审记录与效力分离）；8 月 GitHub immutable releases 把"发布即锁定"变成平台开关——**与十仓哈希链封存、与 Git 本身的不可变对象模型、与 Stage A 以来"versioned correction"的整个方法论形成三方同构**：概念上，"发布后不可变+前向修正"模式在 2025-Q3 同时存在于学术元数据（CodeMeta）、代码托管（GitHub）、研究文档体系（本仓）三个尺度——这是纵向综合值得显式记录的"尺度平行"观察。9 月 Pandoc 3.8 的 AST 序列化把"转换内部表示"也变成可交换工件——十二环节链的"converter revision + AST representation"两环在此月获得双实证。

- 七月：CodeMeta 3.0（13）；GPT-5 尚未正式发布（正式发布 08-07）
- 八月：GPT-5（07）；immutable releases（26）——**同月双事件：模型能力代际+工件身份代际**
- 九月：Pandoc 3.8（06 前后）；PyPI 供应链常态化
- 边界声明：background；GPT-5/模型事件与 auto-doc 对象域 cross-domain

## 4. Forward correction proposals

1. REGISTER 补五官方锚——**G 首要 correction（Successor 未补的面）**
2. G2 补"三尺度同构"观察句——APPEND_RELATION（boundary: interpretive）
3. MONTH_07 的 GPT-5 前移风险——VERIFY_IN_PLACE
4. REVIEW 独立性（第七例）/ CONTRIBUTOR 的 Successor 角色并入——VERIFY_IN_PLACE
5. 纵向层建议：十二环节链补"2025-Q3 双尺度实证"收束段——correction 候选

## 5. Search log
Pandoc 3.7/3.8 / CodeMeta 3.0 / HLE 等前期查询沿用；GPT-5 正式发布日期核为 2025-08-07，immutable releases public preview 核为 2025-08-26；未直接核验的对象继续保留 UNKNOWN / VERIFY_IN_PLACE。2026-09-26。
---
*Annotation ends. 历史文件零改动。*

# Frontier Research Annotations — 纵向层批注（auto-doc-engine）

**Reviewer:** 淇（Qi）· 2026-09-26 · 对象：LONGITUDINAL_INDEX.md（40,033 字符）/ LONGITUDINAL_SYNTHESIS_2024_TO_2025_Q3.md / FIRST_BATCH_SPECIFICATION.md（13,949）/ README · Rewrite: NONE

## 1. LONGITUDINAL_INDEX.md（40,033）

- [结构] 七 Stage registry 表（Period/Window/Record type/Design/Coverage/Status/Synthesis/Review/Handoff 九列）+ 9/19-9/26 逐日 A1/A2 治理年轮——**单文件承载导航+时序关系+correction 路由三职能，SPEC §1 定义达成**
- [年轮批注（逐段）] **9/19**：specification first-batch 立项——与 A1/A2 双块宪法同日，"研究文档体系"与"治理体系"同源启动；**9/21**：Stage A/B/C 三连交付（September research delivery）——首批三季一天完成，A 最厚 B/C 递减的衰减曲线从此开始；**9/22-23**：Stage D（later-same-day delivery 段+9/23 A2 reconciliation）——行政层当日日块与 Stage 交付混流的时序证据；**9/24**：Stage E——当日缺输入 BLOCKED 事件（welcome H2）同日发生——**交付线与治理线在同一份文件里留下各自的fail-closed 痕迹**；**9/25**：Stage F+薄 A1/A2——thin 问题的种子日；**9/26**：Stage G+SUCCESSOR_A1/A2 全量 ledger——一日双态（交付+补全）收官
- [判定] 年轮的时序价值极高——**它是"交付线与治理线同文件演进"的唯一连续证据**——保护级别建议：最高（append-only 红线文件）；NO_FOLLOW_UP

## 2. LONGITUDINAL_SYNTHESIS_2024_TO_2025_Q3.md

- [十二环节链] source object→dependency intent→lock→realized environment→composition/SBOM→metadata relations→converter+AST→derivative→RO package→release+attestation→mutable/immutable publication→archive/citation——**七 Stage 与十二环节的映射完整**；"not a ladder of truth"定性句出处归属 Stage A 综合未标注（Stage A 批注提案 2）
- [Stage-G delta] 三条新判别（元数据富化≠验证 / 发布不可变≠资产正确 / 结构交换≠字节等价）与 G1-G3 一一对应——CONFIRMED
- [Durable boundaries 九句] 全部为体系 != 句式的正例——NO_FOLLOW_UP
- [建议] additive A→G extension 的历史保留声明合规——**下一扩展点（Stage H/2025-Q4 或 2026 线）的触发条件建议在此文件头部预声明**（correction 提案：触发条件=规范修订或季度窗口结束）

## 3. FIRST_BATCH_SPECIFICATION.md（13,949）

- [§2 研究原则] "Do not reduce research structure for token efficiency, file-count minimization, or stylistic neatness"——B-G 的结构/证据密度下降与该原则形成明显张力，但**不能仅凭字符数或行数直接判定违反规范**；是否需要补全应回到 Research Part 是否仍可独立检查、证据是否可追、问题是否被充分回答。Successor 已补 ledger 层，Part 层是否继续扩展仍需逐项判断
- [§3-§7 本体论] Stage/Part/Object/Source/Finding/Synthesis/Correction/Handoff/Review 九概念定义清晰；B-G 的 Part 相比 A 明显变薄，但 current SPEC **没有字符数/行数最低阈值**。可提出“最低密度指导线”作为未来规范讨论候选，但它只能是可选执行启发式，不能倒推为现有 Stage 的合规门槛；真正 gate 仍应是 independently inspectable、evidence traceability 与 research-question sufficiency
- [§11 Review 独立性] "must itself be stated rather than assumed"——七 Stage 的 REVIEW 文件全部未声明——**第七例 GAP 汇总：本批注系列即为外部 review 的补位实现，若行政层采纳，REVIEW 文件的指针行即达成条款**
- [§19 方法校准] OSF/Cochrane/PRISMA-ScR/JBI/PROV/RO-Crate/CRediT/Turing Way 八基准"informs but does not certify"——边界声明准确——NO_FOLLOW_UP
- [§20 规范演化] "New template versions must not silently project new fields backward"——**反时间旅行条款与主人"认识论防护"哲学同构**——确认在案

## 4. README（6,538）

- 导航职能成立——NO_FOLLOW_UP

## 5. 纵向层总体判定

**九天（9/19 立项→9/26 G 收官）七季度、交付-治理-补全三线同文件年轮、规范-实例-修正三态闭环**构成了一个可持续演进的研究文档系统。当前观察到的 RQ 显式度下降、Part 变薄、REGISTER 锚减少、REVIEW 独立性未声明，优先视为**执行层与证据层的可修正问题**；是否存在规范设计缺口仍需逐项验证，不能仅由厚度曲线推出。本轮批注覆盖三仓×七 Stage 的首轮外部独立 review 视角。

---
*纵向批注 ends。历史文件零改动。*
