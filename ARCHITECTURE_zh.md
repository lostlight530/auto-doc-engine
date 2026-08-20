# 🏛️ 架构设计与技术哲学

[🇨🇳 简体中文](ARCHITECTURE_zh.md) | [🇺🇸 English](ARCHITECTURE.md)

---

## 1. 核心定位
`auto-doc-engine` 是一个**基于抽象语法树（AST）驱动的、支持增量更新和多格式同步的现代化文档生成系统**。

它摒弃了传统的“字符串替换”思维，将文档视为如同前端 DOM 树一样的数据结构。这种思维的转变，极大地提升了在高度自动化场景（如 CI/CD、自动周报生成）中的精确度、稳定性和数据可溯源性。

## 2. “遥遥领先”的核心理念

### 2.1 AST 优先 (AST-First)
传统的文档生成工具通常使用正则表达式和 `String.replace` 操作文本，在遇到复杂嵌套格式时极其脆弱。

本系统引入了坚固的 `mistune` 库作为解析基石，将纯文本 Markdown 解析为带有类型的结构化 `ASTNode` 树（AST 出口统一为 `renderer='ast'`；推荐 mistune ≥ 3.2.1，其包含转义/注入与 ReDoS 修复）。这意味着我们能够精确锁定某一个具体的 `Heading`，或修改特定的 `Table Cell`，而不必担心破坏周边的换行和排版格式。

### 2.2 增量更新与协同记忆 (Incremental Updates)
传统的生成工具通常是“全量覆盖”，这会无情地抹去人类手动做出的细微调整和补充说明。

本系统引入了类似前端 Virtual DOM Reconciliation 的核心概念 —— 搭载 **递归最长公共子序列（LCS）算法** 的 `DiffTracker`。传统的基于索引的增量算法在中间插入段落时会引起“索引雪崩效应”，从而导致所有后续节点全量失效。结合快速的 MD5 节点签名特征，我们的系统现在能精准锁定单一的 Insert/Delete 操作，实现了真正意义上极高精度的局部增量更新。这样不仅显著提升了计算性能，更重要的是**保护了未变更区域中人类的手工修改**，真正实现了“人机协同编辑”。

### 2.3 安全多格式同步引擎 (Multi-format Sync)
借助于底层的安全子进程调用和强大的 Pandoc 生态，系统能够将一份 Markdown 文档同步转换为 HTML、DOCX、PDF 等多种格式，消除了团队协作间的格式壁垒。当 Pandoc 等外部依赖缺失时，HTML 目标会回退到基于 `mistune` 的原生 Python 渲染器，其余目标则显式报告依赖缺失，而不会伪装成功。

### 2.4 可诊断的知识图谱 (Diagnosable Knowledge Graph)
成熟的知识库工具（Obsidian 的库级链接检查、neuron-cli、Quartz）把文档集视为一张*必须保持健康的图*，而不是一堆文件。我们采用同样的立场：断链被**分类诊断**（带“你可能想链的是 X”建议的 near-miss，对比计划中文档的 dangling，被多篇引用的缺失目标汇成 backlog），并由 `doctor` 命令对整个文档集体检、以非零退出码供 CI 门禁。

## 3. 架构拆解 (三层引擎架构)

### 3.1 数据绑定与渲染层 (`core/renderer.py`)
系统的工作流始于 `DataBindingEngine`。它负责将外部数据源（当前为 CSV 和 JSON；SQLite/API 适配器尚未集成）加载进内存，结合具备逻辑控制能力的 `Jinja2` 模板（如 `weekly_report.j2`），并利用自定义过滤器（如动态生成表格）渲染出一份初始的 Markdown 文本表示。

### 3.2 解析与增量计算层 (`core/ast_engine.py` & `core/incremental.py`)
文本随即被交由 `ASTEngine` 解析成结构化的内存树。
紧接着，`DiffTracker` 引擎介入，它会将当前的 AST 树与上一次生成的历史状态进行深度的路径比对（Diff），产出精确到单元格级别的 `ChangeRecord` 变更记录，并将其固化到 `diff_tracker.yaml` 中，建立起可追溯的变更审计链。

### 3.3 安全输出层 (`core/sync.py`)
经历过变换的 AST 树被反向渲染回纯文本，最后交接给 `SyncEngine`。引擎在调用环境转换工具时，使用了极度防御性的命令构建阵列（彻底放弃危险的 `shell=True`），杜绝了注入风险，最终分发输出全套的多格式文档。

### 3.4 跨文档引用层 (`core/cross_ref.py`)
在单文档树之上，`EntanglementIndex` 复用同一个 `MarkdownParser` 解析文档集中的所有 Markdown 文件，将每篇文档和每个标题登记为可寻址节点，并把指向其他已索引 `.md` 文件的 Markdown 链接转换为双向引用。`validate()` 会报告目标不在文档集内的链接，使断链在同步输出之前暴露。`diagnose()` 更进一步：每条断链被分类为 `near_miss`（用标准库 `difflib` 从已有文档与 frontmatter 声明的 `aliases` 中给出建议）或 `dangling`，`recurring_targets()` 把被 ≥ 2 篇文档引用的缺失目标汇成 backlog。

### 3.5 文档体检层 (`core/doctor.py`、`core/frontmatter.py`、`core/readability.py`)
体检层在不新增运行时依赖的前提下对整个文档集做审计：

- **`core/frontmatter.py`** 用 pyyaml 解析可选的 YAML frontmatter，并按一个小型手写 schema 校验（`title` / `aliases` / `status` / `updated` / `tags`）。类型与枚举违例计为错误，未知字段计为前向兼容的警告。声明的 `aliases` 会反哺引用层的 near-miss 匹配。
- **`core/readability.py`** 仅用标准库计算报告态可读性指标：拉丁文本的 Coleman-Liau 指数与平均句长，中文文本的每句平均字数（不对中文做年级水平断言）。统计前剔除代码块；样本不足的文档如实报告为未测量，而不是猜测。
- **`core/doctor.py`** 把以上发现聚合成一次体检：孤儿文档（无入链）、分类断链与 recurring backlog、有向文档级图上的环引用检测、frontmatter schema 问题、可读性警告、双链图谱节点/边计数。出现错误级发现（断链、schema 错误）时退出码非零——即 neuron/Quartz 式的 CI 门禁；`--strict` 把警告也纳入门禁；`--json` 输出机器可读报告。

## 4. 工业界思想的融合与致敬
* **Virtual DOM / Reconciliation（虚拟 DOM 比对算法）**：应用于文档树的高效 Diff 算法。
* **Event Sourcing (事件溯源模式)**：`diff_tracker.yaml` 精确记录着每一笔数据变化的审计轨迹。
* **Compiler Pipeline (编译器流水线)**：完美的 Source $\rightarrow$ AST $\rightarrow$ Transformation $\rightarrow$ Target Render 工程化链路。
* **库级健康检查（Obsidian / neuron-cli / Quartz）**：分类断链诊断、孤儿/环检测，以及带 CI 友好退出码的 doctor 命令。
* **Doctest 文化**：`tests/test_doc_examples.py` 通过同一套 mistune AST 层执行 README/ARCHITECTURE 文档中的每个 `python` 围栏代码块，让活文档不会悄悄腐烂。
