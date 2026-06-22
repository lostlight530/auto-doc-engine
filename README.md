# 🚀 auto-doc-engine

> **AST-driven incremental multi-format document generation system.**

[🇨🇳 简体中文](README_zh.md) | [🇺🇸 English](README.md)

---

## 📖 Overview

`auto-doc-engine` is a modern document generation system that treats documents not as flat strings, but as structured data (Abstract Syntax Trees). Designed for high-automation scenarios (CI/CD, automated reporting, API docs), it efficiently binds data from multiple sources into dynamic documents, and distributes them across multiple formats seamlessly.

## ✨ Core Differences (vs `doc-forge`)

| Dimension | `doc-forge` | `auto-doc-engine` |
|:---|:---|:---|
| **Template Engine** | `string.Template` (No logic) | **Jinja2** (Conditionals, loops, macros) |
| **Operation Level** | String replacement | **AST node manipulation** (Safe & Structural) |
| **Update Strategy** | Full overwrite | **Recursive LCS Incremental updates** (Zero index-avalanche via Virtual DOM strategy) |
| **Data Source** | CSV only | **Multi-source** (CSV, SQLite, JSON, API) |
| **Output** | Markdown only | **Synchronized Multi-format** (MD, HTML, DOCX, PDF) |
| **Dependencies** | Zero deps | `Jinja2` + `mistune` + `Pandoc` (Optional) |
| **Metadata** | None | **Change history & Provenance chain** |

## 💡 Core Concepts

- **🌲 AST Engine**: Manipulates the document's Abstract Syntax Tree.
- **⚡ Incremental**: Tracks structural changes using **Recursive LCS (Longest Common Subsequence)**, preventing index avalanches and updating only specific diffs, preserving human edits.
- **🔄 Sync**: Define once in Markdown, output everywhere in parallel.
- **🎨 Template**: Rich Jinja2 logic templates.
- **🔗 Data Binding**: Binds multi-source data directly to document nodes.

## 🚀 Quick Start

```bash
# 1. Install dependencies
pip install jinja2 mistune pandas pyyaml

# 2. Render document with data binding
python core/renderer.py

# 3. Parse, modify and generate the AST
python core/ast_engine.py

# 4. Compute Incremental Diff
python core/incremental.py

# 5. Sync to multiple formats safely
python core/sync.py
```

## 📚 Documentation

- [Architecture Design](ARCHITECTURE.md)
- [Examples](examples/README.md)

## 📁 Directory Structure

```text
auto-doc-engine/
├── README.md              ← You are here
├── ARCHITECTURE.md        ← Architecture logic & philosophy
├── core/                  ← Core Engines
│   ├── renderer.py        ← Data binding & Jinja2 Renderer
│   ├── ast_engine.py      ← Mistune-powered AST engine
│   ├── incremental.py     ← Path-based diff & tracker
│   └── sync.py            ← Secure multi-format sync
├── templates/             ← Jinja2 templates
├── incremental/           ← Change tracking storage
├── sync/                  ← Sync targets config
└── tests/                 ← Comprehensive test suite
```

## 📄 License

MIT License
