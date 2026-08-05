# auto-doc-engine

> AST-driven incremental multi-format document generation system.

[简体中文](README_zh.md) | [English](README.md)

---

## Overview

`auto-doc-engine` is a modern document generation system that treats documents not as flat strings, but as structured data (Abstract Syntax Trees). Designed for high-automation scenarios (CI/CD, automated reporting, API docs), it efficiently binds data from multiple sources into dynamic documents, and distributes them across multiple formats seamlessly.

## Core Differences (vs `doc-forge`)

| Dimension | `doc-forge` | `auto-doc-engine` |
|:---|:---|:---|
| **Template Engine** | `string.Template` (No logic) | **Jinja2** (Conditionals, loops, macros) |
| **Operation Level** | String replacement | **AST node manipulation** (Safe & Structural) |
| **Update Strategy** | Full overwrite | **Recursive LCS Incremental updates** (Zero index-avalanche via Virtual DOM strategy) |
| **Data Source** | CSV only | **Multi-source** (CSV, SQLite, JSON, API) |
| **Output** | Markdown only | **Synchronized Multi-format** (MD, HTML, DOCX, PDF) |
| **Dependencies** | Zero deps | `Jinja2` + `mistune` + `Pandoc` (Optional) |
| **Metadata** | None | **Change history & Provenance chain** |

## Capability Matrix

| Module | Status | Description |
|--------|--------|-------------|
| `core/renderer.py` | **Implemented** | Data binding & Jinja2 rendering |
| `core/ast_engine.py` | **Implemented** | Mistune-powered AST engine |
| `core/incremental.py` | **Implemented** | Recursive LCS path-based diff |
| `core/sync.py` | **Implemented** | Multi-format synchronization |
| SQLite backend | Optional | Requires `sqlite3` + schema config |
| API data binding | Optional | Requires endpoint + auth config |
| `cross_ref.py` | **Experimental** | Not integrated into main chain |
| `template_prewarm.py` | **Experimental** | Not integrated into main chain |
| `self_observe.py` | **Experimental** | Not integrated into main chain |
| `async_conduit.py` | **Experimental** | Not integrated into main chain |
| `memory_lattice.py` | **Experimental** | Not integrated into main chain |
| `restart_protocol.py` | **Experimental** | Not integrated into main chain |

## Quick Start

```bash
# 1. Install dependencies
pip install jinja2 mistune pandas pyyaml

# 2. Render document with data binding
python core/renderer.py

# 3. Parse and generate AST
python core/ast_engine.py

# 4. Compute incremental diff
python core/incremental.py

# 5. Sync to multiple formats
python core/sync.py
```

## Documentation

- [Architecture Design](ARCHITECTURE.md)
- [Examples](examples/README.md)

## License

MIT License
