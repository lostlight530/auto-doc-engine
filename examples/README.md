# auto-doc-engine 示例 / Example

本目录包含 auto-doc-engine 的完整使用示例。

## 示例：周报生成 / Weekly Report Generation

```bash
# 1. 准备数据源 / Prepare data source
cat > data/weekly_data.csv << 'EOF'
week,task,status,owner
2026-W25,AST引擎重构,完成,Alice
2026-W25,增量更新引擎,完成,Bob
2026-W25,多格式同步,进行中,Carol
EOF

# 2. 使用模板生成 / Generate with template
python core/ast_engine.py generate \
  templates/jinja2/weekly_report.j2 \
  --data data/weekly_data.csv \
  --output output/report.md

# 3. 同步多格式 / Sync to formats
python core/sync.py sync output/report.md --targets html,docx
```

## 更多示例 / More Examples

| 示例 | 说明 |
|------|------|
| 论文摘要 / Paper Summary | 从 CSV 数据生成结构化论文摘要 |
| 项目状态 / Project Status | 多数据源绑定的项目状态报告 |
