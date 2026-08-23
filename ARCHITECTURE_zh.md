# 架构与技术哲学

[English](ARCHITECTURE.md) | [README](README_zh.md)

## 1. 核心命题：文档自动化首先是编译器问题

`auto-doc-engine` 同时把文档集看成三种对象：

1. 可以解析与渲染的**类型化语法树**
2. 可以明确描述变化的**版本化结构**
3. 引用与元数据会发生失真的**知识图谱**

因此系统遵循编译器纪律，而不是自由文本替换。上层能力尽量复用下层已经产生的证据，不再偷偷引入第二套解析器或隐藏成功条件。

## 2. 六层架构

```text
[数据绑定]
    ↓
[Markdown AST]
    ↓
[结构 Diff]
    ↓
[跨文档图]
    ↓
[健康诊断]
    ↓
[诊断互操作] ──> Text / JSON / SARIF
    ↓
[可选格式同步] ─> Markdown / HTML / DOCX / PDF / EPUB
```

### 2.1 数据绑定 — `core/renderer.py`

`DataBindingEngine` 当前实现 JSON / CSV 加载与 Jinja2 渲染。SQLite 与网络 API 在拥有真实适配器、失败契约与测试之前维持“当前未集成”。

### 2.2 AST 契约 — `core/ast_engine.py`

Mistune 是唯一 Markdown 解析边界。受支持节点映射到类型化 `ASTNode`；不支持的结构显式报错，不静默拍平。推荐 Mistune 基线保持 3.2.1 及以上，以覆盖该安全基线之后的 3.x 修复。

### 2.3 结构变化 — `core/incremental.py`

`DiffTracker` 对同层 AST 节点做对齐，输出 `add`、`modify`、`delete`、`unchanged`。这一层的语义边界很重要：它**描述变化**，不宣称自动解决人类与 Agent 的并发编辑冲突，也不等于安全 patch 应用器。

### 2.4 文档图 — `core/cross_ref.py`

`EntanglementIndex` 复用同一个 Markdown 解析器建立文档/标题索引与有向文档链接图。缺失目标被分类成 `near_miss` 与 `dangling`；被多篇文档重复引用的缺失目标提升为明确 backlog 信号。

### 2.5 健康模型 — `core/doctor.py`、`core/frontmatter.py`、`core/readability.py`

`doctor` 把已有证据聚合成一次体检：

- 断链是错误
- frontmatter 类型/枚举违例是错误
- 孤儿、指定类型的环、未知 frontmatter 字段与可读性信号是警告
- `--strict` 把警告也纳入退出码门禁
- `--json` 输出项目原生机器可读模型

可读性与链接建议始终是启发式信号。它们提示“值得检查”，不等于证明文章写得差或推荐链接一定是作者本意。

### 2.6 诊断互操作层 — `core/sarif.py`

2026-08-23 校准新增标准交换边界：`core/sarif.py` 将同一份 doctor 发现映射为 OASIS SARIF 2.1.0 + Approved Errata 01 的保守结果子集。

映射坚持：

- 稳定命名空间 `ruleId`：`doc.link.*` / `doc.frontmatter.*` / `doc.graph.*` / `doc.readability.*`
- SARIF `level` 保留 doctor 的 error / warning 语义
- 文档相对 URI 作为 artifact location
- `autoDocFinding/v1` partial fingerprint 由稳定发现身份计算，不掺入时间戳
- run properties 保存文档数量和图节点/边统计

这里的 SARIF 是**结果交换 profile**，不把 Markdown 文档体检包装成源码静态分析，也不声称实现了 SARIF 的全部可选能力。

## 3. 输出与同步边界

`core/sync.py` 位于文档语义之后。外部命令统一使用参数数组调用，不使用 `shell=True`。工具缺失保持可观察失败；HTML 可使用 Mistune 本地回退，其余格式保留真实外部依赖。

格式同步保持可选，是因为一台没有出版工具链的机器也应该能完成文档正确性审计。

## 4. 验证架构

当前有两层互补门禁：

- **仓库契约**：`make test` 执行确定性 Python 测试，覆盖活文档与 SARIF 映射
- **持续契约**：`.github/workflows/ci.yml` 在 PR 与 `main` push 上使用 Python 3.12 跑同一命令

CI 不负责凭空证明 Pandoc / XeLaTeX 等环境相关转换器，而是防止源码、能力声明、示例和诊断语义彼此漂移。

## 5. 架构硬规则

1. **一套解析契约**：新增 Markdown 结构能力扩展 AST 层，不另起正则替换旁路
2. **声明不能领先事实**：MANIFEST / README 必须跟随实现证据
3. **诊断身份稳定**：SARIF `ruleId` 与 fingerprint 版本属于对外互操作契约，破坏性变化必须升版本
4. **严重级别显式**：每个新发现必须明确属于错误还是警告
5. **禁止隐藏 shell**：外部工具继续使用参数数组，不开 `shell=True`
6. **环境诚实**：可选出版工具缺失必须可见
7. **实验性就是未接线**：文件能 import 不等于正式能力

## 6. 标准与思想来源

- 编译器流水线：source → AST → analysis → diagnostics → targets
- Virtual-DOM 式 reconciliation：用于结构变化描述
- 知识库健康思想：用于断链、孤儿与环的图级推理
- OASIS SARIF 2.1.0 + Errata 01：用于标准诊断结果传输
- Citation File Format 1.2.0：用于机器可读软件引用
- 可执行文档文化：示例属于仓库契约，不是装饰性文案

## 7. 非目标

当前仓库不宣称自己是通用文档数据库、实时协作编辑器、任意 Markdown 字节级保真转换器或完整生产级格式转换服务。这些问题需要不同的正确性契约。
