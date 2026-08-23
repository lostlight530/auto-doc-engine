# 架构设计与科研边界

[简体中文](ARCHITECTURE_zh.md) | [English](ARCHITECTURE.md)

> 当前架构校准日期：2026-08-23。本文件描述仓库已经实现的行为与明确边界；未来互操作方向统一标记为 `proposed`。

## 1. 核心定位

`auto-doc-engine` 是一个 AST 驱动的文档工具包，用于可检查的文档生成、结构变化检测、跨文档健康检查与可选格式转换。

它追求的不是“自动化越多越好”，而是**证据可保留、失败可见、能力边界可检查的自动化**：文档结构、变换、引用、可选依赖和输出状态都应能够被审计，而不是被一个笼统的“成功”掩盖。

本仓库不是语义真理引擎、协作合并系统、不可变溯源账本，也不是所有格式都已打通的生产发布流水线。

## 2. 规范数据流

```text
JSON / CSV 数据源
      |
      v
Jinja2 数据绑定 + Markdown 文本
      |
      v
Mistune Markdown AST
      |
      +--> 结构差异记录
      |
      +--> 跨文档引用 / 健康分析
      |
      v
Markdown 渲染
      |
      v
可选格式同步
      |
      v
产物 + 显式结果 / 错误状态
```

当前模块仍可独立调用。这张图描述它们的架构组合关系，不代表所有阶段已经被接成一条经过完整验证的生产入口。

## 3. 核心不变量

### 3.1 AST 优先，而不是字符串替换优先

`core/ast_engine.py` 使用 Mistune 将受支持的 Markdown 结构解析为有类型节点。只要仓库已经为相应内容建立 AST 契约，结构操作就应优先基于解析结果进行。

不支持的节点应显式失败，而不是静默重解释。解析后再渲染提供的是结构级契约，不保证字节级或排版级无损还原。

### 3.2 结构 diff 是变化检测器，不是合并引擎

`core/incremental.py` 会渲染节点、计算 SHA-256 摘要（匹配/记录时使用截短摘要），再利用 `difflib.SequenceMatcher` 比较同层节点签名，输出 `add`、`modify`、`delete`、`unchanged` 变化记录。

这也修正了旧架构文档中的两个过度声明：

- 当前实现使用的是 SHA-256，不是 MD5；
- 计算出结构差异，并不等于能够自动、无冲突地保留任意人工编辑。

本仓当前没有通用 patch 应用、冲突解决、内容所有权或 CRDT/merge 层。人工编辑保护必须由上层工作流提供，直到仓库出现对应的可执行契约。

### 3.3 数据绑定保持有界

`core/renderer.py` 当前已接入 JSON 与 CSV 数据源，通过 Jinja2 渲染模板。SQLite 与网络/API 数据源尚未集成。因此“数据源无关”只能作为架构方向，不能写成当前已经普遍实现的能力。

### 3.4 跨文档结构是一张可诊断图，而不是语义知识图谱

`core/cross_ref.py` 基于解析后的 Markdown 链接建立文档与标题引用关系，并区分：

- 已存在的合法目标；
- 带候选建议的 `near_miss` 断链；
- 指向缺失/规划中文档的 `dangling` 引用；
- 可汇总为 backlog 的重复缺失目标。

这是一张文档结构图，不表示被链接内容在语义上等价，也不自动构成知识图谱。

### 3.5 文档健康检查只是结构证据

`core/frontmatter.py`、`core/readability.py` 与 `core/doctor.py` 组成文档健康层，可报告 frontmatter schema 问题、断链、孤儿文档、环引用、可读性启发指标以及图节点/边统计。

通过 doctor 只代表对应的已实现谓词通过，不证明事实正确、科研结论有效、翻译正确或已经达到同行评审标准。

### 3.6 格式同步受能力与环境约束

`core/sync.py` 使用参数列表调用外部命令，不使用 `shell=True`。

当前目标语义如下：

| 目标 | 常规路径 | 当前边界 |
| --- | --- | --- |
| Markdown | 平台 `cp` 命令 | 当前还不是跨平台 Python 文件复制抽象 |
| HTML | Pandoc | 只有 `sync_with_fallback()` 在 Pandoc 缺失时可走 Mistune fallback |
| DOCX | Pandoc | fallback 不伪造 DOCX，只明确报告 Markdown-only |
| PDF | Pandoc + 当前配置的 XeLaTeX | 依赖本地工具链 |
| EPUB | Pandoc | 依赖本地工具链 |

转换器缺失或 subprocess 失败必须保留为显式失败/不支持状态，不能计作多格式生成成功。

## 4. 溯源与 Research Object 边界

仓库新增根级 [Research Contract](RESEARCH_CONTRACT.md)，用于统一本仓与 `epistemic-pipeline`、`sci-render-kit` 之间的证据语言。

最重要的边界是：

```text
产物身份 != 语义真理
溯源 != 独立复现
结构 diff != 安全合并
健康检查 != 科学验证
```

RO-Crate 1.3 于 2026-06-22 发布为 Recommendation，本仓只把它记录为**未来互操作映射目标**。当前任何输出、manifest 或历史文件都不应被称为 RO-Crate；只有增加符合规范的 exporter/validator 与可执行测试后，状态才可以升级。

## 5. 可复现性分级

本仓在 `RESEARCH_CONTRACT.md` 中采用以下本地术语：

- `R0 Traceable`：存在元数据和来源引用；
- `R1 Replay-addressable`：输入、配置、版本、摘要与命令足以定位目标 replay；
- `R2 Environment-bounded`：额外记录运行时、依赖和外部工具假设；
- `R3 Reproduced`：已经真正执行独立重跑，并按声明的判据比较结果。

这些是项目内部 doctrine，不是外部标准。仅生成 metadata 文件绝不能被描述为 `R3`。

## 6. 2026-08-23 外部依赖证据

“上游最新”与“本仓已验证”必须分开：

- Mistune `>=3.2.1` 继续作为仓库文档中的安全下限。2026-08-23 查询 PyPI，最新观察版本为 3.3.4。记录该版本并不表示本仓已经验证所有 3.3.x 行为。
- Pandoc 最新观察版本为 3.10.2（2026-08-11 发布）。它在本仓仍是可选本地依赖；仅因为上游版本更新，不能把本仓证据自动升级为“已验证 3.10.2”。

## 7. 架构原则

1. **实现事实高于文案。** 代码与文档冲突时，应修正文档或为实现补上可执行契约。
2. **不伪造成功。** 可选依赖缺失、不支持节点、断链和转换失败都必须保持可见。
3. **不做语义膨胀。** Hash、AST、链接和可读性指标是结构证据，不是真理证明。
4. **不能靠文案完成集成。** 实验模块和跨仓协议在没有进入规范主链与测试之前仍是非集成状态。
5. **外部标准必须带版本与本地状态。** 规范、依赖或研究对象格式均应同时标明日期/版本以及本仓 `implemented / optional / experimental / proposed` 状态。

## 8. 主要参考资料

检索日期：2026-08-23

- [RO-Crate 1.3 Specification](https://www.researchobject.org/ro-crate/1.3/)
- [FAIR Principle R1.2](https://www.go-fair.org/fair-principles/r1-2-metadata-associated-detailed-provenance/)
- [Mistune on PyPI](https://pypi.org/project/mistune/)
- [Pandoc releases](https://github.com/jgm/pandoc/releases)
