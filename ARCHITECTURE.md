# 🏛️ Architecture Design & Philosophy

[🇨🇳 简体中文](ARCHITECTURE_zh.md) | [🇺🇸 English](ARCHITECTURE.md)

---

## 1. Core Positioning
`auto-doc-engine` is a **modern document generation system driven by Abstract Syntax Trees (AST)**. It supports path-based incremental updates and multi-format synchronization.

By discarding the traditional "string replacement" mindset, it treats documents as data structures (much like a DOM tree in web development). This drastically improves precision, stability, and traceability in automated document workflows.

## 2. The "Cutting-Edge" Philosophy

### 2.1 AST-First Approach
Traditional document generation tools rely heavily on Regular Expressions and `String.replace()`. They become extremely fragile when encountering complex or nested markdown formats.

Our system leverages the robust `mistune` library to parse plain Markdown text into a structured, typed `ASTNode` tree (the AST exit point is uniformly `renderer='ast'`; mistune ≥ 3.2.1 is recommended for its escaping/injection and ReDoS fixes). This allows us to accurately target a specific `Heading` or mutate a single `Table Cell` without corrupting the surrounding formatting.

### 2.2 Incremental Updates & Collaborative Memory
Standard static site generators or documentation tools perform "full overwrites", which erase any manual micro-adjustments made by humans.

We introduce a concept similar to React's Virtual DOM Reconciliation — the `DiffTracker` equipped with a **Recursive LCS (Longest Common Subsequence) Algorithm**. Traditional parsers suffer from "index avalanches" when a node is inserted in the middle. Our LCS approach combined with fast MD5 node signatures prevents this, ensuring that the system only identifies the exact insertion/deletion without corrupting the un-mutated subsequent nodes. This not only boosts performance but **preserves human edits in unchanged areas**, achieving true human-machine collaborative editing.

### 2.3 Secure Multi-Format Sync Engine
Powered by secure subprocess calls and the Pandoc ecosystem, our Sync Engine breaks down formatting silos. It takes a single Markdown source of truth and safely synchronizes it into HTML, DOCX, and PDF formats. If external dependencies are missing, HTML output falls back to a native Python renderer based on `mistune`, while other targets report the missing dependency explicitly instead of claiming success.

### 2.4 Diagnosable Knowledge Graph
Mature knowledge-base tools (Obsidian's vault link checks, neuron-cli, Quartz) treat a document set as a *graph that must stay healthy*, not a pile of files. We adopt the same stance: broken links are **classified** (near-miss with "did you mean" suggestions vs. dangling/planned documents, with recurring targets surfaced as a backlog), and a `doctor` command audits the whole set and exits non-zero so CI can gate on document health.

## 3. Architecture Breakdown (The 3-Layer Engine)

### 3.1 Data Binding & Render Layer (`core/renderer.py`)
The pipeline begins with the `DataBindingEngine` consuming external data sources (currently CSV and JSON; SQLite/API adapters are not yet integrated). It injects this data into `Jinja2` templates (e.g., `weekly_report.j2`), utilizing custom filters (like auto-generating tables) to render an initial markdown representation.

### 3.2 AST & Incremental Layer (`core/ast_engine.py` & `core/incremental.py`)
The raw text is then parsed by `ASTEngine` into an in-memory structural tree.
Next, the `DiffTracker` steps in. It diffs the current tree against the historical state, producing granular `ChangeRecord` objects. These records are persistently logged in `diff_tracker.yaml`, forming a traceable audit trail.

### 3.3 Secure Output Layer (`core/sync.py`)
Once the AST is finalized and re-rendered to text, the `SyncEngine` takes over. We implemented a defensive command builder (expressly avoiding `shell=True` vulnerabilities) to safely invoke environment conversion tools, outputting the final suite of multi-format documents.

### 3.4 Cross-Document Reference Layer (`core/cross_ref.py`)
Above single-document trees, the `EntanglementIndex` reuses the same `MarkdownParser` to parse every Markdown file in a document set. Each document and each heading becomes an addressable node, and Markdown links that target other indexed `.md` files become bidirectional references. `validate()` reports links whose targets fall outside the document set, so broken cross-references surface before synchronization. `diagnose()` goes further: every broken link is classified as `near_miss` (close existing documents or declared frontmatter `aliases` are suggested via stdlib `difflib`) or `dangling`, and `recurring_targets()` surfaces missing targets referenced by ≥ 2 documents as a backlog.

### 3.5 Document Health Layer (`core/doctor.py`, `core/frontmatter.py`, `core/readability.py`)
The health layer audits an entire document set without adding runtime dependencies:

- **`core/frontmatter.py`** parses optional YAML frontmatter with pyyaml and validates it against a small hand-written schema (`title` / `aliases` / `status` / `updated` / `tags`). Type and enum violations are errors; unknown fields are forward-compatible warnings. Declared `aliases` feed the near-miss matcher of the reference layer.
- **`core/readability.py`** computes report-mode readability metrics with the standard library only: the Coleman-Liau grade and average sentence length for Latin prose, and average characters per sentence for CJK prose (no grade-level claim for Chinese). Fenced code is excluded; documents with too little material are reported as unmeasured rather than guessed.
- **`core/doctor.py`** aggregates everything into one audit: orphan documents (no inbound links), classified broken links and the recurring backlog, reference cycles on the directed doc-level graph, frontmatter schema issues, readability warnings, and graph node/edge counts. It exits non-zero on error-level findings (broken links, schema errors) — the neuron/Quartz-style CI gate — and `--strict` extends the gate to warnings. `--json` emits a machine-readable report.

## 4. Industry Inspirations
* **Virtual DOM Reconciliation**: Used for the granular document diffing algorithm.
* **Event Sourcing**: Accurately tracking every single mutation history in `diff_tracker.yaml`.
* **Compiler Pipeline Design**: Source $\rightarrow$ AST $\rightarrow$ Transformation $\rightarrow$ Target Render.
* **Vault Health Checks (Obsidian / neuron-cli / Quartz)**: Classified link diagnostics, orphan/cycle detection, and a doctor command with CI-friendly exit codes.
* **Doctest Culture**: `tests/test_doc_examples.py` executes every `python`-fenced block in the README/ARCHITECTURE documents through the same mistune AST layer, so living documentation cannot silently rot.
