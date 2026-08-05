# auto-doc-engine

> AST 驱动的文档渲染、解析、差异计算与可选格式转换工具集。

[简体中文](README_zh.md) | [English](README.md)

## 概览

`auto-doc-engine` 当前由几个可独立调用的 Python 模块组成：Jinja2 模板渲染、Mistune Markdown AST 解析、结构化差异计算，以及基于外部命令的格式同步。仓库已有单元测试覆盖其中一部分接口，但尚未提供一个经过端到端验证的统一生产流水线。

下表中的状态以当前云端源码和测试为依据：

- **已实现**：当前仓库中存在实现，并有源码或现有测试支持所述边界。
- **可选**：实现依赖本机工具、额外配置或尚未覆盖的运行环境。
- **实验性**：源码存在，但没有接入一条规范的主链路。
- **当前未集成**：当前云端仓库没有对应适配器或实现，不能作为已交付能力使用。

## 能力矩阵

| 能力 | 状态 | 当前证据与边界 |
|---|---|---|
| [`core/renderer.py`](core/renderer.py) | 已实现 | 使用 Jinja2 渲染模板；`load_data()` 当前只读取 JSON 和 CSV。空表格数据返回 `MISSING_DATA_FIELD`。 |
| [`core/ast_engine.py`](core/ast_engine.py) | 已实现 | 使用 Mistune 将受支持的 Markdown 节点映射为内部 AST，并可重新渲染；遇到未映射节点会抛出 `UNSUPPORTED_AST_NODE`。 |
| [`core/incremental.py`](core/incremental.py) | 已实现 | 计算 AST 节点的新增、修改、删除和未变记录；现有测试覆盖中间插入、段落修改和表格行插入。它不等同于对任意人工编辑的自动保留承诺。 |
| [`core/sync.py`](core/sync.py) | 已实现（接口）/ 可选（转换） | 以参数列表调用外部命令并返回逐目标结果；HTML、DOCX、PDF、EPUB 依赖 Pandoc，PDF 还依赖 XeLaTeX。当前测试只验证部分命令结构，没有覆盖完整多格式转换链路。 |
| SQLite 数据源 | 当前未集成 | 当前 `DataBindingEngine.load_data()` 没有 SQLite 分支。 |
| API 数据源 | 当前未集成 | 当前仓库没有网络数据源适配器、鉴权配置或对应测试。 |
| `core/cross_ref.py`、`core/template_prewarm.py`、`core/self_observe.py`、`core/async_conduit.py`、`core/memory_lattice.py`、`core/restart_protocol.py` | 实验性 | 文件存在，但没有接入一个经过验证的规范入口。 |
| 本地 V2 参考包 | 当前未集成 | `core/*_v2.py`、`core/declarative_engine.py` 和 `tests/test_v2.py` 不在当前云端树中；本地参考材料及其测试报告不构成仓库实现证据。 |

API/SQLite 适配器、完整多格式转换、上述实验性模块和本地 V2 参考包并不是同一条经过验证的云端流水线。

## 依赖与失败行为

| 依赖或环境 | 用途 | 缺失或失败时的当前行为 |
|---|---|---|
| Python 3 | 运行模块和测试 | 无可用解释器时无法运行。 |
| `jinja2` | 模板渲染 | 导入渲染器失败；模板不存在或模板错误由 Jinja2 抛出异常。 |
| `mistune` | Markdown AST 与 HTML 回退 | 导入相关模块失败；不支持的 AST 节点由解析器显式报错。 |
| `pyyaml` | 同步目标配置与差异历史持久化 | 读取配置或读写历史时导入失败。 |
| `pandoc` | HTML、DOCX、PDF、EPUB 转换 | 目标结果返回 `ERROR: pandoc 未安装`，不会把该目标报告为成功。 |
| `xelatex` | Pandoc PDF 后端 | Pandoc 子进程失败，错误文本写入该目标的结果。 |
| `cp` 命令 | 当前 Markdown 复制目标 | 在缺少 `cp` 的环境中子进程失败并返回 `ERROR`；Windows 上应特别检查。 |

`DiffTracker.record_generation()` 会按配置写入 YAML 运行态记录，`core/sync.py` 的演示会写入 `output/`。这些生成内容不是当前仓库中已跟踪的源目录。

## 快速验证

在仓库根目录创建隔离环境并安装当前测试所需依赖：

```bash
python -m venv .venv
# 按当前 shell 激活 .venv
python -m pip install jinja2 mistune pyyaml
```

运行 README 契约和现有测试：

```bash
python -m unittest tests.test_readme_contract -v
python tests/test_all.py
python tests/test_incremental.py
```

成功标准是三个命令均以退出码 `0` 结束。依赖缺失、外部转换器不可用或命令返回非零都应记录为失败或未验证，不能计作成功。

四个核心文件也包含独立演示入口，可按需运行：

```bash
python core/renderer.py
python core/ast_engine.py
python core/incremental.py
python core/sync.py
```

这些命令分别演示模块行为，不代表一次调用即可完成从数据源到全部输出格式的统一流程；增量和同步演示还可能产生本地运行态文件。

## 当前仓库地图

```text
auto-doc-engine/
├── README_zh.md
├── ARCHITECTURE_zh.md
├── core/
│   ├── renderer.py
│   ├── ast_engine.py
│   ├── incremental.py
│   ├── sync.py
│   └── 其他实验模块
├── templates/jinja2/
├── sync/targets.yaml
└── tests/
    ├── test_all.py
    ├── test_incremental.py
    └── test_readme_contract.py
```

## 已知限制

- 当前没有统一的公共 facade、CLI 或覆盖全链路的集成测试。
- JSON/CSV 加载与模板渲染存在，但 SQLite/API 仍需设计、实现和测试。
- AST 只接受代码中已映射的节点类型；解析再渲染可能改变格式，不能视为字节级保真。
- 差异跟踪器报告结构差异；是否安全应用变更、冲突处理和人工编辑保留仍需上层流程验证。
- 多格式结果受 Pandoc、XeLaTeX、`cp`、目标配置和操作系统影响；仓库当前没有证明所有目标在所有环境中可用。
- `MANIFEST.yaml` 中的能力声明和运行态路径仍需后续校准，不能单独作为实现证据。

## 文档

- [中文架构说明](ARCHITECTURE_zh.md)
- [中文示例说明](examples/README_zh.md)
- [English README](README.md)

## 许可证

MIT License