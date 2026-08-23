# auto-doc-engine

> AST 驱动的文档编译、结构化差异、文档图谱健康检查与标准诊断交换工具集

[简体中文](README_zh.md) | [English](README.md) | [架构](ARCHITECTURE_zh.md) | [示例](examples/README_zh.md)

## 当前定位

`auto-doc-engine` 把 Markdown 当成带类型的文档结构，而不是一段等待字符串替换的文本。当前仓库由多个可独立调用的模块组成，**还不是一个覆盖所有数据源与所有格式的统一生产流水线**。

今天的核心原则是：**先有可验证事实，再有能力声明**。解析、Diff、跨文档引用、体检与标准交换各自有清晰边界。

## 能力矩阵

状态口径：**已实现** = 有当前源码与仓库证据支撑；**可选** = 依赖外部环境；**实验性** = 文件存在但未接入规范主链；**当前未集成** = 当前仓库没有对应交付实现。

| 能力 | 状态 | 当前证据与边界 |
|---|---|---|
| `core/renderer.py` | 已实现 | Jinja2 渲染，当前数据加载为 JSON/CSV，提供 `table` 与 `bullet_list` 过滤器 |
| `core/ast_engine.py` | 已实现 | Mistune 驱动 Markdown AST 映射与重新渲染，不支持节点显式失败 |
| `core/incremental.py` | 已实现 | 输出 add/modify/delete/unchanged 结构差异；它是 Diff，不等于自动无冲突合并 |
| `core/sync.py` | 已实现接口 / 可选转换 | 参数列表式子进程；HTML 可回退 Mistune，DOCX/PDF/EPUB 依赖外部工具 |
| `core/cross_ref.py` | 已实现 | AST 文档/标题索引、引用图、near-miss / dangling 分类、重复缺失目标 backlog |
| `core/doctor.py` | 已实现 | 聚合断链、孤儿、环、frontmatter、可读性与图统计；错误级发现返回非零退出码 |
| `core/sarif.py` | 已实现 | 将 doctor 发现导出为 **SARIF 2.1.0 + Errata 01** 保守子集，带稳定版本化 partial fingerprint |
| `core/frontmatter.py` | 已实现 | YAML frontmatter 解析与手写 schema 校验 |
| `core/readability.py` | 已实现 | 拉丁/CJK 报告态可读性启发式，不包装成写作质量保证 |
| 可执行文档 | 已实现 | 本地文档检查可执行 README / ARCHITECTURE 中的 Python 围栏示例 |
| SQLite / API 数据源 | 当前未集成 | 没有当前生产适配器与对应实现契约 |
| `template_prewarm` / `self_observe` / `async_conduit` / `memory_lattice` / `restart_protocol` | 实验性 | 源码存在，但没有接入经过验证的规范入口 |

## 当前架构

```text
数据 -> 模板 -> Markdown AST -> 结构 Diff -> 文档图 -> 健康诊断 -> Text / JSON / SARIF -> 可选格式同步
```

这不是“模块越多越先进”，而是同一个确定性思想沿着整个链路展开：**不能因为某个文件存在，就把能力当成完成；不能因为命令执行过，就把输出当成正确**。

## Python API 示例

AST 层可以直接调用，不依赖任何 GitHub 工作流：

```python
from core.ast_engine import MarkdownParser

root = MarkdownParser().parse("# Research note\n")
assert root.children
```

## Doctor 与 SARIF

人类可读 / JSON 体检：

```bash
python core/doctor.py path/to/docs
python core/doctor.py path/to/docs --strict
python core/doctor.py path/to/docs --json
```

标准结果交换：

```bash
python core/sarif.py path/to/docs -o output/doctor.sarif
python core/sarif.py path/to/docs --strict -o output/doctor.sarif
```

SARIF 出口面向 OASIS SARIF 2.1.0（含 Approved Errata 01），使用稳定 `ruleId` 和 `autoDocFinding/v1` partial fingerprint，让下游系统可以跨多次体检关联同一个逻辑发现。这里使用 SARIF 作为**诊断结果交换容器**，不把 Markdown 体检包装成“源码静态分析器”。

## 本地检查

需要时可以手动检查确定性的 Python 能力面：

```bash
python -m pip install jinja2 "mistune>=3.2.1" pyyaml
make test
```

这些检查覆盖 README 事实契约、renderer / AST / sync、增量 Diff、跨文档图、健康层、可执行文档与 SARIF 出口。它们只是**本地维护工具，不是 GitHub 合并门禁**。

Pandoc / XeLaTeX 等环境相关转换器仍然是**可选**能力；缺失时明确报告，不把未验证环境伪装成成功。

## 依赖与失败行为

- Python 运行依赖：`jinja2`、`mistune>=3.2.1`、`pyyaml`
- 可选外部工具：Pandoc、XeLaTeX、当前 Markdown 复制命令
- 未支持 AST 节点、断链、frontmatter 错误、外部转换器缺失与 CLI 用法错误均显式暴露
- `output/`、`incremental/` 是运行态产物，不是跟踪的源码目录

## 仓库地图

```text
auto-doc-engine/
├── core/
│   ├── renderer.py
│   ├── ast_engine.py
│   ├── incremental.py
│   ├── sync.py
│   ├── cross_ref.py
│   ├── doctor.py
│   ├── sarif.py
│   ├── frontmatter.py
│   └── readability.py
├── templates/jinja2/
├── sync/targets.yaml
├── tests/
├── examples/
├── CITATION.cff
└── MANIFEST.yaml
```

## 已知边界

- 当前仍没有一个覆盖全部数据源、全部目标格式并经过端到端验证的统一公共 facade
- AST 解析再渲染是结构语义，不承诺 Markdown 字节级保真
- DiffTracker 报告结构差异，本身不负责安全应用冲突变更
- 可读性与 near-miss 是带阈值的启发式信号
- SARIF 是诊断互操作 profile，不代表任何下游平台已经完成兼容性认证

## 引用与许可

软件引用元数据位于 `CITATION.cff`（CFF 1.2.0），许可证为 MIT
