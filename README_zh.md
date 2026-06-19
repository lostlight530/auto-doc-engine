# 🚀 auto-doc-engine

> **AST 驱动的增量多格式同步文档生成系统**

[🇨🇳 简体中文](README_zh.md) | [🇺🇸 English](README.md)

---

## 📖 概览

`auto-doc-engine` 是一个现代化的文档生成系统。它不再把文档当作一堆需要被正则替换的“死字符串”，而是将文档看作像前端 DOM 一样的**结构化数据（AST 树）**。专为高度自动化的场景（如 CI/CD、日常报表生成、API 文档同步）设计，它能高效、精确地将多源数据注入文档，并一键分发为多种格式。

## ✨ 核心差异（对比 `doc-forge`）

| 维度 | `doc-forge` | `auto-doc-engine` (本作) |
|:---|:---|:---|
| **模板引擎** | `string.Template`（无逻辑） | **Jinja2**（支持条件、循环、宏、自定义过滤器） |
| **操作层级** | 字符串暴力替换 | **AST 节点安全操作**（精准无损） |
| **更新策略** | 全量覆盖 | **虚拟 DOM 式增量更新**（保留人类的手工修改） |
| **数据源** | 单一 CSV | **多源绑定**（CSV, SQLite, JSON, API） |
| **输出格式** | 仅 Markdown | **多格式同步分发**（MD, HTML, DOCX, PDF） |
| **外部依赖** | 零依赖 | 站在巨人的肩膀上：`Jinja2` + `mistune` + `Pandoc` |
| **元数据与历史** | 无 | **提供节点级别的变更历史记录与溯源链** |

## 💡 核心理念

- **🌲 AST 优先**：操作文档结构，而不是操作字符串。
- **⚡ 增量更新**：通过节点路径 Hash 追踪变更，只重新生成变化的段落。
- **🔄 多格式同步**：一次 Markdown 定义，多格式安全并行输出。
- **🎨 逻辑模板**：基于 Jinja2 构建强大的前端视图层。
- **🔗 数据绑定**：打破文档边界，让外部数据直接驱动内容刷新。

## 🚀 快速开始

```bash
# 1. 安装系统核心依赖
pip install jinja2 mistune pandas pyyaml

# 2. 数据绑定与模板渲染测试
python core/renderer.py

# 3. 运行 AST 引擎进行文档的解析与重组
python core/ast_engine.py

# 4. 执行增量 Diff 算法，计算文档变化
python core/incremental.py

# 5. 安全地同步输出多格式文档
python core/sync.py
```

## 📚 文档指引

- [架构设计与技术哲学](ARCHITECTURE_zh.md)
- [运行示例说明](examples/README_zh.md)

## 📁 目录结构拆解

```text
auto-doc-engine/
├── README_zh.md           ← 您在这里
├── ARCHITECTURE_zh.md     ← 架构设计思想
├── core/                  ← 引擎核心代码
│   ├── renderer.py        ← 数据绑定与渲染中心
│   ├── ast_engine.py      ← 基于 mistune 的语法树引擎
│   ├── incremental.py     ← 路径驱动的增量更新追踪器
│   └── sync.py            ← 安全的多格式同步引擎
├── templates/             ← Jinja2 业务模板库
├── incremental/           ← 变更追踪器 YAML 存储
├── sync/                  ← 目标输出格式配置文件
└── tests/                 ← 综合单元测试套件
```

## 📄 协议

MIT License
