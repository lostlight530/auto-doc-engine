# 🧪 auto-doc-engine 示例

[🇨🇳 简体中文](README_zh.md) | [🇺🇸 English](README.md)

---

本目录记录了 `auto-doc-engine` 当前已验证的入口用法。下列每条命令都是自包含的，并已对照当前源码实际运行过。

## 📊 示例：周报生成

### 1. 使用内置示例上下文渲染
`core/renderer.py` 使用内置示例上下文渲染 `templates/jinja2/weekly_report.j2`（不需要外部数据文件）：
```bash
python core/renderer.py
```

### 2. 绑定你自己的 CSV 数据
`DataBindingEngine.load_data()` 当前读取 JSON 和 CSV。绑定真实 CSV 文件的方式：
```bash
cat > data/weekly_data.csv << 'EOF_CSV'
week,task,status,owner
2026-W25,AST引擎重构,完成,Alice
2026-W25,增量更新引擎开发,完成,Bob
2026-W25,多格式同步加固,进行中,Carol
EOF_CSV

cat > templates/jinja2/csv_demo.j2 << 'EOF_TPL'
# 本周任务

{{ rows|table(['week', 'task', 'status', 'owner']) }}
EOF_TPL

python -c "
from core.renderer import DataBindingEngine
engine = DataBindingEngine()
context = engine.load_data('data/weekly_data.csv')
print(engine.render('csv_demo.j2', context))
"
```

### 3. 计算增量变更记录
`core/incremental.py` 对两份内置 Markdown 文档做结构化 Diff，并向 `incremental/diff_tracker.yaml` 追加一条生成记录（该路径是已被 gitignore 的运行态产物）：
```bash
python core/incremental.py
```

### 4. 同步多格式文档
`core/sync.py` 转换一份示例文档：`markdown` 目标使用 `cp`，当 Pandoc 不可用时 `html` 目标回退到基于 mistune 的渲染器。输出写入已被 gitignore 的 `output/` 目录：
```bash
python core/sync.py
```

### 5. 构建跨文档引用图
`core/cross_ref.py` 索引两篇临时 Markdown 文档，建立双向引用，并通过 `validate()` 报告断链：
```bash
python core/cross_ref.py
```

---

## 🛠 仅有模板的场景

以下模板存在于 `templates/jinja2/`，但其目标数据源适配器**尚未集成**（见根目录 README 的能力矩阵）。你仍然可以通过 `load_data()`（JSON/CSV）自行加载数据来渲染它们：

| 模板 | 目标场景 | 缺失的适配器 |
|:---|:---|:---|
| `paper_summary.j2` | 结构化学术论文摘要 | JSON API 获取器（可改用本地 JSON 文件） |
| `project_status.j2` | 项目风险与里程碑报表 | SQLite 数据源 |
