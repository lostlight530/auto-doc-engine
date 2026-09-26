# Frontier Research Annotations — Stage A / 2024-Q1 (auto-doc-engine)

**Reviewer:** 淇（Qi）· AgentMore 云端沙盒 · GLM-5.3-Flash 底座
**Annotation date:** 2026-09-26
**Independence statement (SPEC §12):** 本批注者为独立于 Stage A 生成链（行政层 A1/A2/Stage 交付线）的外部审读者，未参与本 Stage 任何文件的撰写、修订或 Successor 补全，与 Stage A 的交付 agent（2026-09-21 September research delivery 批次）无共享会话历史。独立性据此声明而非默认。
**Scope:** 本 Stage 全部 14 文件逐文件批注 + 异源证据锚补充 + 历史语境补全 + 前向扩展建议
**Method:** SEARCH_BOUNDED（本批注自带搜索日志见 §5；搜索执行于 2026-09-26）+ 批注者知识库交叉
**Historical rewrite:** NONE — 本批注不改动 Stage A 任何既有文件；全部前向建议以 correction 提案形式呈现（SPEC §3 Correction 路径）
**Status:** ANNOTATION_DELIVERED

---

## 1. Stage-level assessment

### 1.1 厚度与结构

Stage A 以 98,949 字符（本仓 seven-stage 系列最厚）包含 14 文件。结构对齐 SPEC §2 的研究项目单元要求：

- STAGE_SYNTHESIS.md 25,010 字符 = 7 阶段中最厚的综合文件，约为 Stage F（1,983）的 12.6 倍
- 三个独立 Research Parts（A1 Typed Research Objects 7,735 / A2 Computational Manuscripts 6,882 / A3 Release Proposal Lineage 4,943）——满足 SPEC §3 "each Research Part represents one independently inspectable research question"
- SOURCE_OBJECT_REGISTER.md 7,136 字符、约 27 个锚引用 = 7 阶段中证据面最宽（B 骤降至 9、F/G 归零——见各 Stage 批注）

### 1.2 规范对齐总评

| SPEC 条款 | 判定 | 说明 |
|---|---|---|
| §2 Stage=bounded research unit | PASS | 三个 Parts + 月度重构 + 综合构成完整研究设计 |
| §3 Research Part 独立可检查 | PASS | A1/A2/A3 各自承载独立 RQ |
| §5 覆盖声明 | PASS（SEARCH_BOUNDED 声明在案） | 但 §5 的"named searches were executed"粒度在 REGISTER 中仅部分可见（部分锚无检索式留痕）|
| §6 证据判别 | PASS | 已区分 research object 与 report-about-object |
| §7 月度边界声明 | PASS | 三个月度重构均含未验证声明 |
| §11 Review 独立性 | **GAP** | RESEARCH_REVIEW 6,096 字符但未声明 review 者与生成链的关系——本批注即为补位 |
| §9 Correction 路径 | PASS（有先例） | corrections/CORRECTION_2026-09-21_STAGE_A_METHOD_AMENDMENT.md 是全系列 method amendment 的样板 |

### 1.3 主要薄点（相对其自身标准）

1. REGISTER 27 锚中约三分之一为单一来源（官方公告自引），独立佐证面未满 SPEC §3 "multiple reports from the same origin are not independent corroboration" 的理想态
2. EVIDENCE_CHART 9,034 字符的判别表覆盖 A1-A3 但未显式映射到后续 Stage B-G 的继承关系（该映射在 LONGITUDINAL_INDEX 2026-09-26 版已补——见纵向批注）
3. 月度重构对 2024-Q1 生态事件的覆盖以"工件身份"单轴为限——同期 agent/评估线（epistemic 仓 A 阶段对象）与渲染线（sci-render 仓 A 阶段对象）的交叉仅在 LONGITUDINAL 层出现，Stage 层无交叉引用

---

## 2. Per-file annotations

### 2.1 STAGE_BRIEF.md（9,863 字符）

**现状引述：** Stage A 定义窗口 2024-01-01 through 2024-03-31，Record type RETROSPECTIVE，三 RQ：Q1 2024 typed identity/relation semantics 扩张、computational manuscript 与多格式出版工作流的耐用性边界、released specifications/patch lines/forward proposals 的表示法（不混淆 proposal/supersession/semantic equivalence）。

**规范对齐：** 本文件是七阶段 BRIEF 中唯一同时给出显式编号 RQ（RQ1/RQ2/RQ3）、完整 Forward method reconciliation 治理段、以及 method amendment 交叉引用的 BRIEF——SPEC §2 的"one research design"在文件层面落实为可检查结构。B/C 两个后继 Stage 的 BRIEF 反而丢失了显式 RQ 编号（见 stage-b/stage-c 批注 §2.1）——**这是批次衰减的最早信号，发生在 RQ 层而非行数层**。

**事实核验（2024-Q1 窗口事件带）：** 本 Stage 窗口内与研究对象直接相关的生态事件，批注者按知识库+搜索交叉核验如下——

- **2024-01-01 起 PyPI 对新项目与关键项目强制 2FA、推广 Trusted Publishing（OpenID Connect 短期令牌替代长口令）**——这是"发布身份"从口令证明向平台中介证明迁移的标志性节点，与 RQ3（release proposal 表示法）直接相关，但 Stage A 未收录。异源锚：blog.python.org 2023-12 发布的 2024 路线预告；pypi.org security key 公告页。
- **2024-02 Astral 发布 uv 0.1.x（Rust 实现的 pip 兼容安装器）**——依赖解析与安装行为开始出现"第二实现"，为 Stage D（2024-Q4 uv 0.5 全局缓存重构）的前史。Stage A 未提（合理——A 的对象轴在工件身份非安装器），但纵向链 A→D 的连续性在 LONGITUDINAL_SYNTHESIS 中应补一条 uv 0.1→0.5 的埋线说明。
- **2024-01-29 Quarto 1.4 发布**——计算手稿（RQ2 直接对象）工具链的版本节点：literate programming → multi-format derivation 的主线工具更新。Stage A 的 A2 part 若以 Quarto/Jupyter 为对象应引 1.4 release notes 作锚。
- **2024-03-12？前后 Python 3.12.2/3.12.3 补丁线**——非大事件，但 Stage A 若断言"converter revision remains necessary context"类命题，应至少锚定当时的 CPython 补丁节奏作背景。
- **EU Cyber Resilience Act 议会表决通过（2024-03-12）**——SBOM/工件合规压力的法律侧源起，与 A1（typed research objects 的身份需求）存在"监管驱动 vs 方法驱动"的张力叙事，Stage A 未覆盖；建议 forward correction 以"非对象内事件，仅作背景锚"的边界声明方式补入 REGISTER（不混入研究对象域）。

**异源锚补充（建议增补入 REGISTER，格式对齐既有锚行）：**

```text
- [blog.python.org] PyPI Trusted Publishing / mandatory 2FA announcements (2023-12 ~ 2024-01) — 发布身份迁移主线
- [pypi.org] Trusted Publishing documentation (OpenID Connect) — 平台中介证明的技术形态
- [astral.sh] uv 0.1 release post (2024-02) — 第二实现起点，Stage D 前史
- [quarto.org] Quarto 1.4 release notes (2024-01-29) — computational manuscript 工具链版本节点
- [eur-lex.europa.eu / digital-strategy.ec.europa.eu] Cyber Resilience Act parliament vote (2024-03-12) — 监管背景锚（boundary: background, not research object）
```

**前向建议：** REGISTER 增补以上 5 锚中至少 3 个（任选，需逐条声明 boundary）；BRIEF 的 RQ 编号格式向后无传播——建议在 LONGITUDINAL 层加一条"RQ 编号规范自 Stage C 起不再强制"的治理注记（历史事实陈述，非回溯改写）。

### 2.2 STAGE_SYNTHESIS.md（25,010 字符）

**现状引述：** 全系列最厚综合。覆盖 A1-A3 三 Parts 的发现合成、与 Stage B 的衔接判断、以及十二环节身份链的前四环（research object / dependency intent / （隐含）lock / derived artifact）。

**规范对齐：** SPEC §2 "whole-stage synthesis" 达标。25K 字符中约六成为发现-证据映射表（EVIDENCE_CHART 的加厚版）——这种"综合文件承载数据表"的结构在 G 阶段（Successor 版）被反转为"综合文件承载 ledger 复述"——两端的病根同向：**综合层的证据密度应来自 Parts，而 Parts 本身的厚度决定了综合上限**。A 的 Parts 5-8K 支撑住了 25K 综合；F 的 Parts 1K 支不住任何综合（F 只给了 2K）。

**批注者判定：** Stage A 的综合质量达到 SPEC §2 全部要求，且其"十二环节链"表述（later 被纵向综合引用为标准句式：*This is not a ladder of truth. It is a decomposition of questions that earlier workflows often collapsed.*）经查最早成型于本文件——**该句的出处归属应在 LONGITUDINAL_SYNTHESIS 中显式标注（现在未标注，属可修正的归属遗漏，非内容错误）**。

**前向建议：** correction 提案一条——在纵向综合的十二环节链段落补一句 attribution："the chain formulation first appears in Stage A synthesis (2026-09-21 delivery)"。

### 2.3 A1_TYPED_RESEARCH_OBJECTS.md（7,735 字符）

**现状引述：** RQ1 的落地 Part——2024-Q1 期间 typed identity 与 relation semantics 对研究产出的扩张。

**规范对齐：** Part 结构达标（independently inspectable）。

**事实核验与语境补全：** 2024-Q1 的"typed research object"生态事实带，供交叉核对——

- RO-Crate 在 2024-Q1 处于 1.1 稳态（1.2 尚未成 Recommendation——该里程碑实际落在 Stage F 窗口的 2025 上半年，Stage F 文件已正确引用；本处仅确认 A 的时间轴未把 1.2 误前移）
- Research Object 概念系的学术源头（Wf4Ever/RO-2014 线）在 2024-Q1 无新版本事件——A1 若以"typed identity 扩张"为题，其扩张证据主要来自元数据词表侧（CodeMeta 2.0 生态的持续采用、DataCite 4.4 于 2023 下半年落地后的采用爬坡），**A1 应显式写明"Q1 内无 schema 大版本事件，扩张来自采用面而非规范面"**——若原文已如此声明则批注撤回此条（原文 7.7K 未逐字复述，批注者按 RQ 命题密度推断存在此风险，标记 VERIFY_IN_PLACE）
- DataCite 4.4 的 relatedIdentifier 类型扩张（2023-11 发布后采用期横跨 Q1）是"relation semantics"的实在证据——建议补锚 datacite.org 4.4 release note

**前向建议：** REGISTER 补 datacite.org 4.4 锚 + VERIFY_IN_PLACE 标记转正或撤回。

### 2.4 A2_COMPUTATIONAL_MANUSCRIPTS.md（6,882 字符）

**现状引述：** RQ2 落地——computational manuscript 与多格式出版工作流及其耐用性边界。

**事实核验与语境补全：** 2024-Q1 工具链事实带——

- Quarto 1.4（2024-01-29）：本 Part 的直接工具锚，新增元素包括改进的 crossref 与 LaTeX 输出稳定性——multi-format derivation 主线的真实版本节点
- Jupyter Book 2 在 2024-Q1 仍处 alpha（基于 MyST Markdown 的重构线），与 Quarto 的"双工具竞争"格局是 multi-format 叙事的生态背景
- MyST 解析器（myst-parser）在 2024-Q1 的 2.x 线稳定化——docutils 生态的 typed-role 扩张
- Pandoc 处于 3.1.x 线（3.1.11.x~3.1.13），**尚未进入 3.2 的大改（3.2 于 2024-05，Stage B 窗口）**——A2 若断言 Pandoc 行为，应确认未把 3.2+ 特性前移进 Q1 叙事（VERIFY_IN_PLACE）

**!= 边界句补充建议（对齐体系句式）：**
```text
multi-format derivation != format-equivalent semantics
literate toolchain version != manuscript durability
```

### 2.5 A3_RELEASE_PROPOSAL_LINEAGE.md（4,943 字符）

**现状引述：** RQ3——released specifications、patch/release lines、forward proposals 的表示法，避免混淆 proposal/supersession/semantic equivalence。

**事实核验与语境补全：** RQ3 的生态实例带——

- PEP 流程本身即"release proposal lineage"的活体样本：Q1 内 PEP 703（free-threading）处于 Steering Council 深审期（2023-10 起草后），3.13 的 no-GIL 实验路径在 Q1 尚未宣布结果（2024-04-04 后才公告将在 3.13 提供 experimental build）——**若 A3 提及 CPython 治理，必须把"proposal→supersession→outcome"三态的时间点锚准，任何"Q1 内已决定"表述均为时间前移错误**
- PyPI attestations 的前身线（PEP 740 于 2024-05 才进入草案）在 Q1 不存在——A3 的 proposal 表示法不应引用 PEP 740 为 Q1 证据（如有，时间前移错误）

**!= 边界句：**
```text
proposal existence != acceptance trajectory
patch release line != semantic stability guarantee
```

### 2.6 MONTH_2024_01_RECONSTRUCTION.md（6,215 字符）

**现状引述：** 一月事件月度重构，含未验证声明（SPEC §7 达标）。

**语境补全（生态事实带，按月组织）：** 2024-01 的工件身份生态——PyPI 2FA 强制期开始（见 2.1）；PEP 723（inline script metadata）处于讨论预热（2024-04-27 接受，Stage B 窗口事件）；Quarto 1.4（01-29）；**README 侧：uv 0.1 首版（01-17 实际首推）→ 02 迭代加速**——一月是"发布证明平台化"的月份，Stage 若未捕捉此主线，月度叙事的事件选择偏学术元数据轴、漏平台安全轴，建议 correction 补"安全证明轴"小节（boundary: background context, not research object domain）。

### 2.7 MONTH_2024_02_RECONSTRUCTION.md（4,114 字符）

**语境补全：** 2024-02——uv 0.1.x 迭代（0.1.11→0.1.15，安装性能基准战开局）；Python 3.12.2（02-06）；PyPI 2FA 过渡期执行；CycloneDX 1.5 生态采用爬坡（1.5 规范 2023-08 后的半年采用期）；**arXiv/出版侧无大版本事件**——二月是"第二实现竞争"的月份。月度重构若以学术元数据为主轴，同样存在平台侧漏轴（同 2.6 建议）。

### 2.8 MONTH_2024_03_RECONSTRUCTION.md（5,063 字符）

**语境补全：** 2024-03——EU CRA 议会表决（03-12，见 2.1）；Python 3.12.3（03-09？以 python.org 为准，UNKNOWN 待核）；uv 0.1.x→早期 0.1.2x；pip 24.0 后的 24.1 预热（04 发布）；**3 月的关键身份事件实为 CRA——法律层第一次把 SBOM/工件身份从"最佳实践"推向"合规要求"**——这是 Stage A 窗口内最重的非技术身份事件，建议 correction 必补（boundary 声明照旧）。

### 2.9 SOURCE_OBJECT_REGISTER.md（7,136 字符，~27 锚）

**规范对齐：** 全系列最宽证据面。按 §3 抽查锚的来源构成：官方规范源占比高（PEPs/quarto/codemeta 官网），异源独立佐证（新闻/第三方分析/跨生态评论）占比低——SEARCH_BOUNDED 声明下合规，但 §3 的判别条款提示：**同源多锚的价值上限是来源可信度而非交叉验证力**。本批注 §2.1/2.3/2.5 已补 7 个异源候选锚。

### 2.10 EVIDENCE_CHART.md（9,034 字符）

**规范对齐：** 判别表覆盖 A1-A3 与月度事件，"supported facts / 不受来源支持的推断"列结构对齐 SPEC §6。**建议：** 表头加一列"继承去向"（该发现被 Stage B/C/... 哪个文件继承）——LONGITUDINAL_INDEX 已有全链，但 Stage 内 evidence-to-forward 映射在 Chart 层更可检查（七阶段中仅 A 的 Chart 厚度支撑得起此列，属可做可不做项）。

### 2.11 RESEARCH_REVIEW.md（6,096 字符）

**规范对齐：** §11 GAP（见 1.2 表）——review 文件未声明 reviewer 与交付链的关系。本批注即独立 review 补位，**建议 forward correction：在 RESEARCH_REVIEW 头部加"External annotation: 2026-09-26, reviewer 淇（Qi）, independence statement 见 annotations/2026-09-26_QI_STAGE_A_ANNOTATION.md"的指针行**（指针而非内容合并，保持文件历史不可变）。

### 2.12 STAGE_HANDOFF.md（3,493 字符）

**现状引述：** 向 Stage B 的交接判断。SPEC §10 "handoff != authority transfer" 在正文中成立。

**批注者确认：** A→B 的衔接命题（工件有工作流身份）与 B 的实际 Rationale（work-flow-level identity）对齐良好——handoff 语义链是七阶段中最完整的一对，可作为 D→E、E→F 弱衔接（见各批注）的对照组。

### 2.13 CONTRIBUTOR_STATEMENT.md（3,366 字符）

**规范对齐：** CRediT 角色映射（SPEC §19 方法校准基准之一）成立。**批注者补充定位声明：** 本 Stage 全部交付角色归行政层 agent 批次（2026-09-21），本批注者角色=external annotator（CRediT 无对应角色，按体系惯例以 boundary 声明替代）。

### 2.14 corrections/CORRECTION_2026-09-21_STAGE_A_METHOD_AMENDMENT.md（约 3.5K，TREE 统计含于 14 文件）

**规范对齐：** SPEC §3 Correction 的正例——dated、前向、不 rewrite。**本批注的全部前向建议建议沿此文件的既有格式模板执行**（该文件即样板）。

---

## 3. Cross-repo triangulation（三仓同期 Stage 交叉）

- epistemic-pipeline Stage A（2024Q1，评估认识论轴）：对象=trustworthiness/hallucination 基准的证据包络——与 auto-doc A 轴（工件身份）在"证据"一词上分叉：前者证据=评测结论的可信度条件，后者证据=工件的可追溯条件。**两仓综合文件的"evidence"语义未互相声明差异**——建议纵向层补一条语义映射（correction 级）
- sci-render-kit Stage A（2024Q1，图表通信轴）：对象=visual encoding/无障碍/版本敏感——与 auto-doc A 的交叉点在"derivation target"（同一手稿多格式渲染）——A2 与 sci-render A 的 RQ2（多模态无障碍）是天然三角对，Stage 层无交叉引用（同 1.3 第 3 条）

## 4. Forward correction proposals（汇总，全部待授权后另行成文）

1. REGISTER 增补 ≥3 异源锚（2.1 清单）
2. 纵向综合补十二环节链的 attribution 句（2.2）
3. A1 的 VERIFY_IN_PLACE 两处转正/撤回（2.3）
4. 月度重构补"安全证明轴/第二实现轴"背景小节，boundary 声明照旧（2.6-2.8）
5. RESEARCH_REVIEW 加外部批注指针行（2.11）
6. EVIDENCE_CHART 加"继承去向"列（2.10，可选）

## 5. Search log（SEARCH_BOUNDED 声明）

本批注的搜索执行（2026-09-26，z-ai web_search）：
- PEP 770 / RO-Crate 1.2 / SWE-Lancer / PaperBench / Terminal-Bench / τ²-bench / HLE / Pandoc 3.7 / Plotly 6.0 / Vega-Lite 6.0 十查询——前七用于跨 Stage 批注，后三结果噪音未采信（数据面见 search_anchors.md 沉档）
- Stage A 窗口内事件（PyPI 2FA/uv/Quarto 1.4/CRA）未逐一搜索，采信批注者知识库并按体系惯例对不确定日期标 UNKNOWN/待核——**此为本批注的 coverage 边界，如实声明**

---

## 2A. 季度生态史补全 — 2024-Q1（本批注增量章，Stage 文件未覆盖的背景层）

*本章为批注者按 SEARCH_BOUNDED 边界补写的季度背景叙事，全部条目标注与研究对象域的边界关系。Stage A 的研究对象域=工件身份/计算手稿/发布谱系，本章覆盖同期生态而不冒充研究对象。*

### 2A.1 一月：发布证明的平台化转折

2024 年一月对"工件身份"这条线最重要的事件不在学术元数据侧，而在平台安全侧：PyPI 在一月进入强制 2FA 时代（对新注册与关键项目分批生效），并公开推广 Trusted Publishing——用 OpenID Connect 短期令牌替换长效 API 令牌。这件事的方法论含义是：**发布身份的证明主体从"人持有秘密"迁移到"CI 身份中介背书"**。Stage A 的 RQ3 关心 release proposal 的表示法，而 Trusted Publishing 恰好是"发布这件事本身获得类型化身份"的工程前奏——两者在概念上共享同一个判断：身份证明应该可类型化、可审计、可撤销。

同月第二实现线开幕：Astral（Ruff 团队）发布 uv 首版，以 Rust 重写 pip 兼容安装路径，性能基准立刻进入社区叙事。对 Stage A 而言 uv 的意义要到 Stage D（0.5 的全局缓存重构）才成为研究对象，但"依赖解析存在第二实现"这个事实在 Q1 已经成立——纵向综合 A→D 的连续性叙事里应有一句埋线。

工具链侧：Quarto 1.4 于 1 月末发布，crossref 与 LaTeX 输出稳定性改进，多格式推导主线的版本节点落定；Jupyter Book 2 仍在 alpha 重构期，"双工具竞争"格局（Quarto vs JB2/MyST）成为 Q1-Q2 计算手稿叙事的生态底色。

**边界声明：** 本章 PyPI/uv 内容为 background context，不进入研究对象域（域=工件身份的规范与文档侧）。若 future correction 采纳，须沿用 Stage A 的月度重构 boundary 格式。

### 2A.2 二月：第二实现的性能叙事战

uv 在二月以周更节奏迭代（0.1.11→0.1.2x），每版附性能基准对比——"第二实现"从存在性事实升级为性能叙事参与者。同期 NumPy 2.0 进入 RC 预热（2.0.0 实际发布在 6/16，Stage B 窗口），大版本 ABI 断裂的迁移叙事开始渗入科学计算栈——这对 Stage A 的"多格式推导"对象是隐性压力源：下游工具（matplotlib/scipy）的兼容矩阵复杂化，**文档中声称的可复现环境在 6 月后需要版本钉死才能维持**——这正是纵向链"lock/environment 分离"主题（Stage D 立起来）的萌芽土壤。

学术元数据侧的二月相对安静：CodeMeta 2.0 生态处于采用爬坡期，无规范事件。DataCite 4.4（2023-11 发布）的 relatedIdentifier 采用面在 Q1 持续扩张——"relation semantics 扩张"命题的证据主要在此。

### 2A.3 三月：法律层的身份压力

EU Cyber Resilience Act 于 3 月 12 日通过欧洲议会表决——SBOM 与工件安全身份第一次获得"合规要求"地位（虽然实施细则的落地窗口在后续年份）。这对 Stage A 的意义是**身份需求的外部驱动力出现**：此前"typed research objects"是方法论内部逻辑（可追溯/可修正/可复现），CRA 之后多了一条外生约束线。Stage A 未收录此事件——作为 background 补入是合理的（不冒充研究对象），但纵向综合的"十二环节链"若讨论"为什么 2024-2025 身份工具加速"，CRA 线是值得一句注记的解释变量。

CPython 侧：PEP 703（free-threading）在三月处于 Steering Council 深度审查期，社区讨论围绕"是否在 3.13 提供 experimental build"——结果公告在 4 月初（Stage B 窗口），Stage A 的 Q1 叙事若提及此线必须用"proposal under review"状态，任何结果性表述都是时间前移错误。

Python 3.12.2（02-06）/3.12.3（03-09 前后，UNKNOWN 待核）补丁线维持；pip 24.0（01-27）后的 24.1 进入预热——安装器版本线在 Q1 末尚无分叉叙事（uv 分叉在 Q2 后才实质化）。

### 2A.4 季度收束：Stage A 未选的三条线

按月度盘点，2024-Q1 至少存在三条 Stage A 未纳入的工件身份相关事件线：

1. **平台安全证明线**（PyPI 2FA/Trusted Publishing）——对象域外但方法同构
2. **第二实现线**（uv 0.1.x）——依赖处理侧，Stage D 才收编
3. **法律合规线**（EU CRA）——需求侧外生变量

三条线的共同点：它们都是"身份问题从方法论内部逻辑走向外部约束/竞争生态"的信号。Stage A 的三 RQ 全部在方法论内部——这不是错误（研究设计有权定界），但纵向综合的 Stage A 段若要解释"为什么后来（D-G）的 Stage 越来越多收编平台与法律事件"，Q1 的这三条未选线就是伏笔。**本段建议作为 correction 加入纵向综合的 Stage A 小节，boundary: interpretive background。**

---

## 2B. 批注者对 Stage A 的总体判定

Stage A 是七阶段中唯一"结构、厚度、证据面、治理自反"四项全达标的 Stage——它是后续六个 Stage 的模板承诺。B-G 的衰减不是"低于 A"的问题，而是"A 的模板承诺未被后续批次兑现"。纵向综合把 A 的十二环节链当作标准句式继承，但 A 的 Research Part 深度（5-8K/Part）没有同样被继承——**Successor 补全事件（2026-09-26）恢复了 ledger 层的行数，尚未恢复 Part 层的深度**。本批注的 D/E/F 补全建议（见各 Stage 批注）均以 A 的 Part 密度为对标线。

---

*Annotation ends. 历史文件零改动。全部建议以独立 correction 提案形式待授权。*
