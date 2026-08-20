# auto-doc-engine

> AST 驱动的文档渲染、解析、差异计算与可选格式转换工具集。

[简体中文](README_zh.md) | [English](README.md)

## 概览

`auto-doc-engine` 当前由几个可独立调用的 Python 模块组成：Jinja2 模板渲染、Mistune Markdown AST 解析、结构化差异计算、带分类断链诊断的跨文档引用索引、`doctor` 体检命令、frontmatter schema 校验、可读性指标，以及基于外部命令的格式同步。仓库已有单元测试覆盖其中一部分接口，但尚未提供一个经过端到端验证的统一生产流水线。

下表中的状态以当前云端源码和测试为依据：

- **已实现**：当前仓库中存在实现，并有源码或现有测试支持所述边界。
- **可选**：实现依赖本机工具、额外配置或尚未覆盖的运行环境。
- **实验性**：源码存在，但没有接入一条规范的主链路。
- **当前未集成**：当前云端仓库没有对应适配器或实现，不能作为已交付能力使用。

## 能力矩阵

| 能力 | 状态 | 当前证据与边界 |
|---|---|---|
| [`core/renderer.py`](core/renderer.py) | 已实现 | 使用 Jinja2 渲染模板，提供 `table` 与 `bullet_list` 过滤器；`load_data()` 当前只读取 JSON 和 CSV。空表格数据返回 `MISSING_DATA_FIELD`。 |
| [`core/ast_engine.py`](core/ast_engine.py) | 已实现 | 使用 Mistune 将受支持的 Markdown 节点映射为内部 AST，并可重新渲染；遇到未映射节点会抛出 `UNSUPPORTED_AST_NODE`。 |
| [`core/incremental.py`](core/incremental.py) | 已实现 | 计算 AST 节点的新增、修改、删除和未变记录；现有测试覆盖中间插入、段落修改和表格行插入。它不等同于对任意人工编辑的自动保留承诺。 |
| [`core/sync.py`](core/sync.py) | 已实现（接口）/ 可选（转换） | 以参数列表调用外部命令并返回逐目标结果；HTML、DOCX、PDF、EPUB 依赖 Pandoc，PDF 还依赖 XeLaTeX。当前测试只验证部分命令结构，没有覆盖完整多格式转换链路。 |
| [`core/cross_ref.py`](core/cross_ref.py) | 已实现 | 基于 AST 构建标题索引与双向跨文档链接图；只有指向其他已索引 `.md` 文件的 Markdown 链接会建立引用。在 `validate()` 之外，`diagnose()` 把每条断链分类为 `near_miss`（用 `difflib` 给出“你可能想链的是 X”建议，候选含 frontmatter `aliases`）或 `dangling`（计划中文档），`recurring_targets()` 把被 ≥ 2 篇引用的缺失目标输出为 backlog。由 `tests/test_cross_ref.py` 与 `tests/test_diagnostics.py` 覆盖。 |
| [`core/doctor.py`](core/doctor.py) | 已实现 | `python core/doctor.py <docs_dir>` 对文档集做体检：孤儿文档（无入链）、分类断链、环引用检测、frontmatter schema 问题、可读性指标、双链图谱节点/边计数。存在错误级发现时退出码非零（可供 CI 门禁），`--strict` 下警告也计非零。由 `tests/test_doctor.py` 覆盖。 |
| [`core/frontmatter.py`](core/frontmatter.py) | 已实现 | 用 pyyaml 解析可选 YAML frontmatter，并按手写 schema 校验（`title` / `aliases` / `status` / `updated` / `tags`）；未知字段计警告，类型与枚举违例计错误。`aliases` 同时支撑断链 near-miss 匹配。由 `tests/test_frontmatter.py` 覆盖。 |
| [`core/readability.py`](core/readability.py) | 已实现 | 纯标准库可读性指标：拉丁文本的 Coleman-Liau 指数与平均句长，中文文本的每句平均字数；统计前剔除代码块。仅报告态（只警告，本身不做门禁），由 `doctor` 消费。由 `tests/test_readability.py` 覆盖。 |
| 可执行文档示例 | 已实现 | `tests/test_doc_examples.py` 通过 mistune AST 层解析 README/ARCHITECTURE 文档并执行其中每个 `python` 围栏代码块，防止文档示例腐烂。 |
| SQLite 数据源 | 当前未集成 | 当前 `DataBindingEngine.load_data()` 没有 SQLite 分支。 |
| API 数据源 | 当前未集成 | 当前仓库没有网络数据源适配器、鉴权配置或对应测试。 |
| `core/template_prewarm.py`、`core/self_observe.py`、`core/async_conduit.py`、`core/memory_lattice.py`、`core/restart_protocol.py` | 实验性 | 文件存在，但没有接入一个经过验证的规范入口。 |
| 本地 V2 参考包 | 当前未集成 | `core/*_v2.py`、`core/declarative_engine.py` 和 `tests/test_v2.py` 不在当前云端树中；本地参考材料及其测试报告不构成仓库实现证据。 |

API/SQLite 适配器、完整多格式转换、上述实验性模块和本地 V2 参考包并不是同一条经过验证的云端流水线。

## 依赖与失败行为

| 依赖或环境 | 用途 | 缺失或失败时的当前行为 |
|---|---|---|
| Python 3 | 运行模块和测试 | 无可用解释器时无法运行。 |
| `jinja2` | 模板渲染 | 导入渲染器失败；模板不存在或模板错误由 Jinja2 抛出异常。 |
| `mistune` | Markdown AST 与 HTML 回退 | 导入相关模块失败；不支持的 AST 节点由解析器显式报错。**推荐 mistune ≥ 3.2.1**（含转义/注入与 ReDoS 修复）；AST 出口统一为 `renderer='ast'`。 |
| `pyyaml` | 同步目标配置、差异历史持久化、frontmatter 解析 | 读取配置、读写历史或校验 frontmatter 时导入失败。 |
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
python -m unittest tests.test_cross_ref -v
python -m unittest tests.test_diagnostics -v
python -m unittest tests.test_frontmatter -v
python -m unittest tests.test_doctor -v
python -m unittest tests.test_readability -v
python -m unittest tests.test_doc_examples -v
```

成功标准是以上命令均以退出码 `0` 结束（`make test` 会运行同一组命令）。依赖缺失、外部转换器不可用或命令返回非零都应记录为失败或未验证，不能计作成功。

五个核心模块也包含独立演示入口，可按需运行：

```bash
python core/renderer.py
python core/ast_engine.py
python core/incremental.py
python core/sync.py
python core/cross_ref.py
python core/frontmatter.py
python core/readability.py
```

这些命令分别演示模块行为，不代表一次调用即可完成从数据源到全部输出格式的统一流程；增量和同步演示还可能产生本地运行态文件。

## 文档体检（doctor）

对任意 Markdown 文档目录做体检——发现断链或 frontmatter schema 错误时退出码非零，可直接接入 CI 门禁：

```bash
python core/doctor.py path/to/docs
python core/doctor.py path/to/docs --strict   # 警告（孤儿、环、可读性）也计为失败
python core/doctor.py path/to/docs --json     # 机器可读报告
```

同样的体检也可以以库方式调用：

```python
import tempfile
from pathlib import Path
from core.doctor import run_doctor

with tempfile.TemporaryDirectory() as tmp:
    docs = Path(tmp)
    (docs / "a.md").write_text("# A\n\nSee [B](b.md).\n", encoding="utf-8")
    (docs / "b.md").write_text("# B\n\nBack to [A](a.md).\n", encoding="utf-8")
    report = run_doctor(tmp)
    assert report.doc_count == 2
    assert report.link_diagnostics == []
    assert report.exit_code() == 0
```

断链不再只是罗列，而是分类诊断：`near_miss` 携带“你可能想链的是 X”建议（候选包括已有文档与 frontmatter 声明的 `aliases`），`dangling` 表示计划中的文档；被 ≥ 2 篇文档引用的 dangling 目标会作为 recurring backlog 输出：

```python
import tempfile
from pathlib import Path
from core.cross_ref import EntanglementIndex

with tempfile.TemporaryDirectory() as tmp:
    docs = Path(tmp)
    (docs / "getting-started.md").write_text("# Getting Started\n", encoding="utf-8")
    (docs / "a.md").write_text(
        "# A\n\nSee [guide](gettng-started.md) and the [plan](plan.md).\n",
        encoding="utf-8",
    )
    index = EntanglementIndex(index_path=str(docs / "index.json"))
    index.build(tmp)
    kinds = {d.target: d.kind for d in index.diagnose()}
    assert kinds["gettng-started.md"] == "near_miss"   # 建议：getting-started.md
    assert kinds["plan.md"] == "dangling"              # 计划中的文档
```

## 当前仓库地图

```text
auto-doc-engine/
├── README.md / README_zh.md
├── ARCHITECTURE.md / ARCHITECTURE_zh.md
├── CITATION.cff
├── core/
│   ├── renderer.py
│   ├── ast_engine.py
│   ├── incremental.py
│   ├── sync.py
│   ├── cross_ref.py
│   ├── doctor.py
│   ├── frontmatter.py
│   ├── readability.py
│   └── 其他实验模块
├── templates/jinja2/
├── sync/targets.yaml
└── tests/
    ├── test_all.py
    ├── test_cross_ref.py
    ├── test_diagnostics.py
    ├── test_doctor.py
    ├── test_doc_examples.py
    ├── test_frontmatter.py
    ├── test_incremental.py
    ├── test_readability.py
    └── test_readme_contract.py
```

## 已知限制

- 当前没有统一的公共 facade、CLI 或覆盖全链路的集成测试（`doctor` 是面向文档集的体检 CLI，不是流水线 facade）。
- JSON/CSV 加载与模板渲染存在，但 SQLite/API 仍需设计、实现和测试。
- AST 只接受代码中已映射的节点类型；解析再渲染可能改变格式，不能视为字节级保真。
- 差异跟踪器报告结构差异；是否安全应用变更、冲突处理和人工编辑保留仍需上层流程验证。
- 多格式结果受 Pandoc、XeLaTeX、`cp`、目标配置和操作系统影响；仓库当前没有证明所有目标在所有环境中可用。
- 可读性指标与 near-miss 建议是带明确阈值的启发式信号，不构成对写作质量或链接意图的保证。
- `MANIFEST.yaml` 是与能力矩阵对齐的声明性清单，其本身不能单独作为实现证据。

## 文档

- [中文架构说明](ARCHITECTURE_zh.md)
- [中文示例说明](examples/README_zh.md)
- [English README](README.md)

## 许可证

MIT License
