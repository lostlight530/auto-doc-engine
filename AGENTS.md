# 🤖 Agent & Bot Developer Guide

Welcome! If you are an AI Agent or Bot cloned to work on the `auto-doc-engine` repository, this document will guide you on how to understand, extend, and customize this project for your user.

The `auto-doc-engine` is NOT a simple string-replacement tool. It is an **AST-driven, incremental document generation system**.

## 🧠 Mental Model

To effectively customize this system, you must adopt the following mental model:
1. **Documents are Trees:** Treat Markdown like a DOM tree. We do not use RegEx to mutate text; we mutate `ASTNode` objects.
2. **Incremental by Design:** We do not overwrite entire files. We diff AST paths and only update what has changed to preserve human edits.
3. **Pipeline Flow:** `Data Source` $\rightarrow$ `Jinja2 Render` $\rightarrow$ `Mistune AST Parse` $\rightarrow$ `Diff Tracker` $\rightarrow$ `Sync Engine Target`.

---

## 🛠️ How to Customize & Extend

### 1. Adding a New Data Source
The engine currently supports CSV and JSON. If the user wants to fetch data from an API, a Database (SQLite/PostgreSQL), or Notion:
- **Where to modify:** Edit `core/renderer.py` in the `DataBindingEngine.load_data()` method.
- **Action:** Add a new condition to parse the incoming format into a standard Python `Dict` or `List` context for Jinja2.

### 2. Creating Custom Jinja2 Filters (e.g., Charts)
If the user wants to render data differently (e.g., rendering a Mermaid.js chart from a JSON array):
- **Where to modify:** Edit `core/renderer.py` inside the `_register_filters()` method.
- **Action:** Define a new Python function that takes data and returns a Markdown string, then register it to `self.env.filters`.

### 3. Enhancing the AST Parser
If the user wants to support new Markdown flavors (like Math Equations or Admonitions/Callouts):
- **Where to modify:** Edit `core/ast_engine.py`.
- **Action:** We use the `mistune` library. You will need to add new Mistune plugins in the `MarkdownParser.__init__` method, and handle the new node mapping in the `_map_mistune_node` and `render` methods mapping them to a custom `NodeType`.

### 4. Adding a New Output Format (e.g., EPUB, Notion API)
If the user wants to sync the output to a completely new destination:
- **Where to modify:** Edit `core/sync.py` and `sync/targets.yaml`.
- **Action:** Add a new entry to the `TARGETS` dictionary in `SyncEngine`. Ensure the command is constructed securely using a `List[str]` (avoid `shell=True`). If the target is an API instead of a file format, you may need to write a custom sync handler instead of using Pandoc subprocesses.

---

## 🛡️ strict Guidelines for Agents

1. **NEVER use `shell=True`**: When adding new sync commands in `core/sync.py`, always use array-based arguments in `subprocess.run()` to prevent injection vulnerabilities.
2. **Do NOT write Regex for Markdown Manipulation**: If you need to change a document's structure, use the `ASTEngine` methods (like `find_nodes`) to traverse the tree and mutate the `ASTNode.content`.
3. **Preserve the Tracker**: The `DiffTracker` relies on structural paths (`root/table[0]/table_row[1]`). If you alter how AST nodes are nested, ensure you do not break the uniqueness of these paths in `core/incremental.py`.
