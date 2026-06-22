# 🏛️ 架构设计与技术哲学

[🇨🇳 简体中文](ARCHITECTURE_zh.md) | [🇺🇸 English](ARCHITECTURE.md)

---

## 1. 核心定位
`auto-doc-engine` 是一个**基于抽象语法树（AST）驱动的、支持增量更新和多格式同步的现代化文档生成系统**。

它摒弃了传统的“字符串替换”思维，将文档视为如同前端 DOM 树一样的数据结构。这种思维的转变，极大地提升了在高度自动化场景（如 CI/CD、自动周报生成）中的精确度、稳定性和数据可溯源性。

## 2. “遥遥领先”的核心理念

### 2.1 AST 优先 (AST-First)
传统的文档生成工具通常使用正则表达式和 `String.replace` 操作文本，在遇到复杂嵌套格式时极其脆弱。

本系统引入了坚固的 `mistune` 库作为解析基石，将纯文本 Markdown 解析为带有类型的结构化 `ASTNode` 树。这意味着我们能够精确锁定某一个具体的 `Heading`，或修改特定的 `Table Cell`，而不必担心破坏周边的换行和排版格式。

### 2.2 增量更新与协同记忆 (Incremental Updates)
传统的生成工具通常是“全量覆盖”，这会无情地抹去人类手动做出的细微调整和补充说明。

本系统引入了类似前端 React Virtual DOM Reconciliation 的核心概念 —— 搭载 **递归最长公共子序列（LCS）算法** 的 `DiffTracker`。传统的基于索引的增量算法在中间插入段落时会引起“索引雪崩效应”，从而导致所有后续节点全量失效。结合快速的 MD5 节点签名特征，我们的系统现在能精准锁定单一的 Insert/Delete 操作，实现了真正意义上极高精度的局部增量更新。这样不仅显著提升了计算性能，更重要的是**保护了未变更区域中人类的手工修改**，真正实现了“人机协同编辑”。

### 2.3 安全多格式同步引擎 (Multi-format Sync)
借助于底层的安全子进程调用和强大的 Pandoc 生态，系统能够将一份 Markdown 文档一键同步转换为精美的 HTML, DOCX, PDF 等多种格式，一举消除了团队协作间的信息孤岛和格式壁垒。

## 3. 架构拆解 (三层引擎架构)

### 3.1 数据绑定与渲染层 (`core/renderer.py`)
系统的工作流始于 `DataBindingEngine`。它负责将外部数据源（如 CSV、JSON 或 API 结果）加载进内存，结合具备逻辑控制能力的 `Jinja2` 模板（如 `weekly_report.j2`），并利用自定义过滤器（如动态生成表格）渲染出一份初始的 Markdown 文本表示。

### 3.2 解析与增量计算层 (`core/ast_engine.py` & `core/incremental.py`)
文本随即被交由 `ASTEngine` 解析成结构化的内存树。
紧接着，`DiffTracker` 引擎介入，它会将当前的 AST 树与上一次生成的历史状态进行深度的路径比对（Diff），产出精确到单元格级别的 `ChangeRecord` 变更记录，并将其固化到 `diff_tracker.yaml` 中，建立起不可篡改的数据溯源链。

### 3.3 安全输出层 (`core/sync.py`)
经历过变换的 AST 树被反向渲染回纯文本，最后交接给 `SyncEngine`。引擎在调用环境转换工具时，使用了极度防御性的命令构建阵列（彻底放弃危险的 `shell=True`），杜绝了注入风险，最终分发输出全套的多格式文档。

## 4. 工业界思想的融合与致敬
* **Virtual DOM / Reconciliation（虚拟 DOM 比对算法）**：应用于文档树的高效 Diff 算法。
* **Event Sourcing (事件溯源模式)**：`diff_tracker.yaml` 精确记录着每一笔数据变化的审计轨迹。
* **Compiler Pipeline (编译器流水线)**：完美的 Source $\rightarrow$ AST $\rightarrow$ Transformation $\rightarrow$ Target Render 工程化链路。
