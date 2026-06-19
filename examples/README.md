# 🧪 auto-doc-engine Examples

[🇨🇳 简体中文](README_zh.md) | [🇺🇸 English](README.md)

---

This directory contains complete usage examples for the `auto-doc-engine`.

## 📊 Example: Weekly Report Generation

This example demonstrates how to take a raw CSV file and convert it into a fully formatted, multi-format weekly report.

### 1. Prepare Data Source
```bash
cat > data/weekly_data.csv << 'EOF_CSV'
week,task,status,owner
2026-W25,AST Engine Refactor,Done,Alice
2026-W25,Incremental Diffing,Done,Bob
2026-W25,Multi-Format Sync,In-Progress,Carol
EOF_CSV
```

### 2. Bind Data & Generate Document
Run the renderer to bind the CSV data to our Jinja2 template and parse it into an AST:
```bash
python core/renderer.py
```

### 3. Compute Incremental Changes
Analyze the structural diffs compared to the last generation and update the tracker YAML safely:
```bash
python core/incremental.py
```

### 4. Sync Multiple Formats
Generate Markdown and HTML securely:
```bash
python core/sync.py
```

---

## 🛠 More Capabilities

| Example Name | Description |
|:---|:---|
| **Paper Summary** | Generates structured academic paper summaries from JSON APIs |
| **Project Status** | Binds to SQLite databases to generate robust project risk assessments |
