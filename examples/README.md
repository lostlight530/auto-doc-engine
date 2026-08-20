# 🧪 auto-doc-engine Examples

[🇨🇳 简体中文](README_zh.md) | [🇺🇸 English](README.md)

---

This directory documents the currently verified entry points of `auto-doc-engine`. Every command below is self-contained and has been run against the current source tree.

## 📊 Example: Weekly Report Generation

### 1. Render from the Built-in Sample Context
`core/renderer.py` renders `templates/jinja2/weekly_report.j2` with a built-in sample context (no external data file required):
```bash
python core/renderer.py
```

### 2. Bind Your Own CSV Data
`DataBindingEngine.load_data()` currently reads JSON and CSV. To bind a real CSV file:
```bash
cat > data/weekly_data.csv << 'EOF_CSV'
week,task,status,owner
2026-W25,AST Engine Refactor,Done,Alice
2026-W25,Incremental Diffing,Done,Bob
2026-W25,Multi-Format Sync,In-Progress,Carol
EOF_CSV

cat > templates/jinja2/csv_demo.j2 << 'EOF_TPL'
# Weekly Tasks

{{ rows|table(['week', 'task', 'status', 'owner']) }}
EOF_TPL

python -c "
from core.renderer import DataBindingEngine
engine = DataBindingEngine()
context = engine.load_data('data/weekly_data.csv')
print(engine.render('csv_demo.j2', context))
"
```

### 3. Compute Incremental Changes
`core/incremental.py` diffs two built-in Markdown documents and appends a generation record to `incremental/diff_tracker.yaml` (a gitignored runtime artifact):
```bash
python core/incremental.py
```

### 4. Sync Multiple Formats
`core/sync.py` converts a sample document: the `markdown` target uses `cp`, and the `html` target falls back to the mistune-based renderer when Pandoc is unavailable. Outputs land in the gitignored `output/` directory:
```bash
python core/sync.py
```

### 5. Build a Cross-Document Reference Graph
`core/cross_ref.py` indexes two temporary Markdown documents, links them bidirectionally, and reports broken references via `validate()`:
```bash
python core/cross_ref.py
```

---

## 🛠 Template-Only Scenarios

The following templates exist under `templates/jinja2/`, but their intended data-source adapters are **not integrated** (see the capability matrix in the root README). They can still be rendered with data you load yourself via `load_data()` (JSON/CSV):

| Template | Intended Scenario | Missing Adapter |
|:---|:---|:---|
| `paper_summary.j2` | Structured academic paper summaries | JSON API fetcher (use a local JSON file instead) |
| `project_status.j2` | Project risk and milestone reports | SQLite data source |
