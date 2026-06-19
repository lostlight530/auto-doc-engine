# 🏛️ Architecture Design & Philosophy

[🇨🇳 简体中文](ARCHITECTURE_zh.md) | [🇺🇸 English](ARCHITECTURE.md)

---

## 1. Core Positioning
`auto-doc-engine` is a **modern document generation system driven by Abstract Syntax Trees (AST)**. It supports path-based incremental updates and multi-format synchronization.

By discarding the traditional "string replacement" mindset, it treats documents as data structures (much like a DOM tree in web development). This drastically improves precision, stability, and traceability in automated document workflows.

## 2. The "Cutting-Edge" Philosophy

### 2.1 AST-First Approach
Traditional document generation tools rely heavily on Regular Expressions and `String.replace()`. They become extremely fragile when encountering complex or nested markdown formats.

Our system leverages the robust `mistune` library to parse plain Markdown text into a structured, typed `ASTNode` tree. This allows us to accurately target a specific `Heading` or mutate a single `Table Cell` without corrupting the surrounding formatting.

### 2.2 Incremental Updates & Collaborative Memory
Standard static site generators or documentation tools perform "full overwrites", which erase any manual micro-adjustments made by humans.

We introduce a concept similar to React's Virtual DOM — the `DiffTracker`. By calculating hashes based on precise structural paths, the system only updates the data nodes that actually changed. This not only boosts performance but **preserves human edits in unchanged areas**, achieving true human-machine collaborative editing.

### 2.3 Secure Multi-Format Sync Engine
Powered by secure subprocess calls and the Pandoc ecosystem, our Sync Engine breaks down formatting silos. It takes a single Markdown source of truth and safely synchronizes it into HTML, DOCX, and PDF formats. If external dependencies fail, it elegantly falls back to a native Python HTML renderer.

## 3. Architecture Breakdown (The 3-Layer Engine)

### 3.1 Data Binding & Render Layer (`core/renderer.py`)
The pipeline begins with the `DataBindingEngine` consuming external data sources (CSV, JSON, SQL). It injects this data into `Jinja2` templates (e.g., `weekly_report.j2`), utilizing custom filters (like auto-generating tables) to render an initial markdown representation.

### 3.2 AST & Incremental Layer (`core/ast_engine.py` & `core/incremental.py`)
The raw text is then parsed by `ASTEngine` into an in-memory structural tree.
Next, the `DiffTracker` steps in. It diffs the current tree against the historical state, producing granular `ChangeRecord` objects. These records are permanently logged in `diff_tracker.yaml`, forming an indisputable audit trail.

### 3.3 Secure Output Layer (`core/sync.py`)
Once the AST is finalized and re-rendered to text, the `SyncEngine` takes over. We implemented a defensive command builder (expressly avoiding `shell=True` vulnerabilities) to safely invoke environment conversion tools, outputting the final suite of multi-format documents.

## 4. Industry Inspirations
* **Virtual DOM Reconciliation**: Used for the granular document diffing algorithm.
* **Event Sourcing**: Accurately tracking every single mutation history in `diff_tracker.yaml`.
* **Compiler Pipeline Design**: Source $\rightarrow$ AST $\rightarrow$ Transformation $\rightarrow$ Target Render.
