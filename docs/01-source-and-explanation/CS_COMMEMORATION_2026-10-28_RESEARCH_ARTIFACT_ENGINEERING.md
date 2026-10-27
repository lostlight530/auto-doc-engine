# auto-doc-engine 仓库纪念｜2026-10-28｜CS：科研文档编译、数字产物与可引用溯源
# Repository Commemoration · 2026-10-28 · Computer Science: Research Document Compilation, Digital Artifacts, and Citable Provenance

> **Identity / 记录身份：** Independent bilingual commemorative disciplinary study · 独立新增的中英双语学科研究纪念；static inspection of repository-native scripts and research documents / 基于原生脚本与研究文档的静态核查；not a historical rewrite, runtime execution report, or certification / 不改写历史、不声称执行或认证。
>
> **CS2023 alignment / 学科坐标：** SE; FPL (Compilers); DM; HCI (Scholarly Communication). These are scholarly comparisons, not endorsements or exact implementation equivalences / 研究分类而非外部机构背书或实现等价。

## 1. 专业归属：这是 CS 的哪一类？ / Disciplinary Position

**中文** — 这个仓库属于**科研软件工程、文档编译、结构化产物表示与数字溯源**的交叉领域。它将研究文档当成有结构、有来源、有衍生关系的计算对象，而不仅是一段 Markdown 或一张 PDF。编译器思想来自 AST 和规范化转换；数字保存思想来自可追溯产物及其研究上下文；两者在本仓的 artifact record / lineage 模块相遇。

**English** — Auto Doc Engine sits at the intersection of **research software engineering, document compilation, structured artifacts, and digital provenance**. A research document is treated as a structured computational object with byte identities and declared derivative relations, not merely a Markdown string or final PDF. Compiler thinking appears in AST transformations; scholarly preservation appears in artifact records and bounded lineage.

## 2. 仓库自身如何体现？ / Repository-native Architecture and Evidence

**中文** — `core/ast_engine.py` 使用 Mistune-backed typed Markdown AST；`renderer.py` 绑定数据与模板；`incremental.py` 检测局部结构变化；`cross_ref.py` 检查本地文档图；`doctor.py`、`sarif.py` 报告诊断；`sync.py` 处理衍生格式；`artifact_record.py`、`artifact_lineage.py` 记录字节身份、断言来源、声明式关系及不继承边界；`ro_crate.py` 支持可选包装。原生技术语义见 `docs/01-source-and-explanation/ARCHITECTURE.md` 及 `docs/02-examples-and-contracts/ARTIFACT_RECORD.md` 等。

**English** — `core/ast_engine.py` exposes a Mistune-backed typed Markdown AST; `renderer.py` binds data to templates; `incremental.py` detects structural change; `cross_ref.py` examines document links; `doctor.py` and `sarif.py` expose diagnostics; `sync.py` handles derivative formats. `artifact_record.py` and `artifact_lineage.py` record byte identities, assertion bases, and declared relations with explicit non-inheritance. `ro_crate.py` provides optional Research Object packaging. Native technical authority is in `docs/01-source-and-explanation/ARCHITECTURE.md` and the subject-specific `docs/02-examples-and-contracts/**` contracts.

## 3. 人话解释 / In Plain Language

**中文** — 把一份科研报告想成**有生产履历的机器零件**：它来自哪些输入，经历哪些转换，内容和字节怎样变化，为什么新的 PDF 属于这份报告。系统能记录这些关系，却不冒充判断论文结论正确。

**English** — Think of a research paper as a **manufactured component with a traceable production history**: what inputs were used, how the structure changed, which files were derived, and what metadata accompanies handoff. Tracking production is not the same as proving the paper's conclusions.

## 4. 如何读懂而不夸大？ / Verification and Non-claim Boundaries

**中文** — PR #178 已合并的 `artifact_record.py` 源证据写入保护是有界工程修复；不把该修复声称为对并发文件系统 TOCTOU 的全面证明。AST SHA-256 是表示身份不是语义等价；RO-Crate 不自动带来独立复现、作者资格裁定或科研真实性。必须区分文档结构通过与科学内容成立。

**English** — The merged PR #178 protected a bounded source-evidence write path, not all concurrent-filesystem TOCTOU cases. AST SHA-256 reflects representation identity, not semantic equivalence. RO-Crate packaging, a valid render, or passing document checks cannot establish research truth, authorship, or independently reproduced science.

## 5. 十仓中的独特贡献 / Place in the Ten-repository Research System

**中文** — 在十仓的**研究产物表达与交接**侧，负责让产物可检查、可传递、可保留；它与 Epistemic Pipeline 的 Claim/Evidence、Sci Render 的图件证据互补，但不从它们继承有效性。

**English** — In the ten-repository system, it contributes **inspectable research artifacts and handoff**. It complements Epistemic Pipeline's claim/evidence objects and Sci Render's figure evidence without inheriting scientific validity from either.

## 6. 纪念与升华 / Commemoration and Wider Meaning

**中文** — **科研成果的生命不止于发表；能够保住其来源、变更和不确定性，才有机会被未来认真理解。**

**English** — **A research output's life does not end at publication.** Preserving its origin, transformations, and uncertainty is what makes future inspection possible.

## 外部学科对照 / External Disciplinary Anchors

- [RO-Crate specification](https://www.researchobject.org/ro-crate/specification.html)
- [W3C PROV overview](https://www.w3.org/TR/prov-overview/)
- [CS2023 knowledge areas](https://csed.acm.org/knowledge-areas/)

> **Provenance / 证据说明：** GitHub repository-native artifacts were read at the 2026-10-28 review cutoff. External sources establish disciplinary context only; independent reproduction, external certification and newly executed tests are **NOT_CLAIMED**. / 原生文件按本次时间点核读；外部来源只用于学科对照；**不声称本轮重新执行测试、独立复现或第三方认证**。
