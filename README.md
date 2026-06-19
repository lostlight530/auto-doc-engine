# auto-doc-engine

> 自动文档引擎 — AST 驱动的增量多格式同步生成系统 | AST-driven incremental multi-format document generation

## 核心差异 / Key Differences（vs `doc-forge`）

| 维度 / Dimension | doc-forge | auto-doc-engine |
|------|-----------|-----------------|
| 模板引擎 / Template Engine | string.Template（无逻辑 / no logic） | Jinja2（条件、循环、宏 / conditionals, loops, macros） |
| 操作层级 / Operation Level | 字符串替换 / String replace | AST 节点操作 / AST node manipulation |
| 更新策略 / Update Strategy | 全量覆盖 / Full overwrite | 增量更新（只改变化部分）/ Incremental (changed parts only) |
| 数据源 / Data Source | CSV 单一 / CSV only | CSV/SQLite/JSON/API 多源 / Multi-source |
| 输出格式 / Output | Markdown 单一 / Markdown only | Markdown + HTML + DOCX + PDF 同步 / Synchronized multi-format |
| 依赖 / Dependencies | Python 标准库零依赖 / Zero deps | Jinja2 + Pandoc（可选 / optional） |
| 自动化 / Automation | GitHub Actions 定时 / Scheduled | 事件触发 + 文件监听 + 定时 / Event + watch + cron |
| 元数据 / Metadata | 无 / None | 文档变更历史 + 溯源链 / Change history + provenance chain |

## 核心概念 / Core Concepts

```
AST 引擎 / AST Engine     → 操作文档的抽象语法树 / Manipulate document AST
增量引擎 / Incremental    → 追踪变更，只更新差异 / Track changes, update diffs only
多格式同步 / Sync         → 一次定义，多格式输出 / Define once, output everywhere
模板层 / Template         → Jinja2 逻辑模板 / Jinja2 logic templates
数据绑定 / Data Binding   → 多数据源绑定到文档节点 / Multi-source binding to document nodes
```

## 快速开始 / Quick Start

```bash
# 1. 定义文档模板 / Define document template
# templates/weekly_report.j2
# 2. 定义数据源 / Define data source
# data/weekly_data.csv
# 3. 生成 / Generate
python core/ast_engine.py generate templates/weekly_report.j2 --data data/weekly_data.csv
# 4. 同步多格式 / Sync formats
python core/sync.py sync output/report.md --targets html,docx
```

## 设计理念 / Design Philosophy

1. **AST 优先 / AST First**：操作文档结构，不是字符串 / Operate on structure, not strings
2. **增量更新 / Incremental**：只重新生成变化的段落 / Regenerate only changed sections
3. **多格式同步 / Multi-format Sync**：一次定义，多格式并行输出 / Define once, output in parallel
4. **数据源无关 / Data Source Agnostic**：支持 CSV/SQLite/JSON/API 绑定
5. **变更可追溯 / Traceable Changes**：每次生成保留完整的变更历史 / Full change history per generation

## 目录结构 / Directory Structure

```
auto-doc-engine/
├── README.md
├── MANIFEST.yaml
├── core/                  ← 引擎核心 / Engine core
│   ├── ast_engine.py      ← AST 文档操作引擎 / AST document engine
│   ├── incremental.py     ← 增量更新引擎 / Incremental update engine
│   └── sync.py            ← 多格式同步 / Multi-format sync
├── templates/             ← Jinja2 模板 / Jinja2 templates
│   ├── jinja2/
│   │   ├── weekly_report.j2
│   │   ├── paper_summary.j2
│   │   └── project_status.j2
├── incremental/           ← 增量追踪 / Incremental tracking
│   └── diff_tracker.yaml
├── sync/                  ← 同步目标配置 / Sync target config
│   └── targets.yaml
└── tests/                 ← 测试 / Tests
    └── test_all.py
```

## 协议 / License

MIT
