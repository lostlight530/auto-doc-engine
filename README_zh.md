# auto-doc-engine

> AST 驱动的科研文档编译、结构差异证据、过程披露元数据、跨文档诊断、SARIF 交换与可选 RO-Crate 1.3 研究对象打包

[English](README.md) · [架构](ARCHITECTURE_zh.md) · [科研契约](RESEARCH_CONTRACT.md) · [过程披露](PROCESS_DISCLOSURE.md) · [前沿校准](FRONTIER_ALIGNMENT.md) · [示例](examples/README_zh.md)

## 当前定位

`auto-doc-engine` 把 Markdown 当成**有结构、有来源、有边界、可携带过程上下文的科研产物**，而不是等待字符串替换的一段文本

当前规范主链是：

```text
JSON / CSV / YAML
        ↓
Jinja2 数据绑定
        ↓
Markdown Typed AST
        ↓
结构差异记录
        ↓
跨文档图 + 元数据诊断
        ↓
产物级 AI / 人工复核过程披露
        ↓
Text / JSON / SARIF 证据
        ↓
Markdown / 可选 Pandoc 格式
        ↓
可选 RO-Crate 1.3 元数据包
```

这里的重点不是“自动化越多越好”，而是每一层都能说明：**输入是什么、输出是什么、失败怎么暴露、证据能证明到哪一步**

仓库不声称自动科研真值判断、作者资格裁定、自动同行评审、publisher AI policy 合规认证或仅靠 metadata 完成独立复现

## 能力矩阵

状态口径：**已实现** = 当前源码已有真实实现；**可选** = 依赖外部运行环境；**实验性** = 独立源码存在但没有接入规范主链；**当前未集成** = 当前仓库没有交付实现

| 能力 | 状态 | 当前边界 |
|---|---|---|
| `core/renderer.py` | **已实现** | Jinja2 + JSON / CSV / YAML/YML；SQLite 与网络 API 数据源当前未集成 |
| `core/ast_engine.py` | **已实现** | Mistune 3.x Typed AST，支持表格、删除线、图片、有序列表等声明子集，不支持结构显式失败 |
| `core/incremental.py` | **已实现** | SHA-256 + sibling sequence alignment 输出 add/modify/delete/unchanged；不是自动合并器 |
| `core/cross_ref.py` | **已实现** | Markdown 本地引用图、标题索引、aliases、near-miss/dangling 诊断与重复缺失目标 backlog |
| `core/frontmatter.py` | **已实现** | title/description/authors/sources/license/doi/language/artifact_id 等有界科研元数据，并支持 `ai_assistance` / `ai_tools` / `human_review` / `disclosure_ref` 过程披露 |
| `core/readability.py` | **已实现** | 拉丁/CJK 描述性启发式，剔除 fenced code；不是写作质量评分 |
| `core/doctor.py` | **已实现** | 汇总文档诊断并提供 Text/JSON 与本地退出状态；不是 GitHub 合并门禁 |
| `core/sarif.py` | **已实现** | OASIS SARIF 2.1.0 + Approved Errata 01 保守结果 profile |
| `core/sync.py` | **已实现 / 可选转换** | Markdown 使用 Python 原生复制；HTML/DOCX/PDF/EPUB 依赖可选 Pandoc/XeLaTeX 环境 |
| `core/ro_crate.py` | **已实现 profile** | 写出 RO-Crate 1.3 核心 JSON-LD 结构；不冒充外部 validator 已认证 |
| SQLite / 网络 API 数据源 | **当前未集成** | 没有当前生产适配器 |
| `template_prewarm` / `async_conduit` / `memory_lattice` / `restart_protocol` / `self_observe` | **实验性** | 已校准语义和局部实现，但仍不接主链 |

## 数据绑定

```python
from core.renderer import DataBindingEngine

engine = DataBindingEngine()
context = engine.load_data("data/research.yaml", strict=True)
markdown = engine.render("paper_summary.j2", context)
assert markdown
```

当前支持 `.json`、`.csv`、`.yaml`、`.yml`

- 默认 `strict=False` 保留历史宽松行为
- `strict=True` 时，缺文件、未知扩展名、非法顶层结构都会显式失败

这让普通模板使用保持简单，同时给科研流水线留下 fail-fast 入口

## 科研 frontmatter 与过程披露

文档可以声明一个小而明确的研究元数据层：

```yaml
---
title: Evidence synthesis
description: Structured summary of declared sources
status: draft
updated: 2026-08-26
authors: [lostlight530]
sources:
  - https://www.researchobject.org/ro-crate/specification/1.3/
license: MIT
language: zh-CN
artifact_id: summary-2026-08-26
ai_assistance: used
ai_tools:
  - 由作者声明的 provider/model 或工具标识
human_review: reviewed
disclosure_ref: PROCESS_DISCLOSURE.md
---
```

过程字段的有界枚举：

```text
ai_assistance: none | used | not_declared
human_review: reviewed | partial | not_reviewed | not_declared
```

`ai_tools` 是作者或上游系统提供的人类可读标识；仓库不会自动去厂商 registry 验真

`disclosure_ref` 可以指向更完整的 methods / process disclosure，仓库默认只记录引用，不自动解引用或认证内容

校验行为：

- 类型/枚举错误 → error
- `ai_assistance: used` 但没有有效 `ai_tools` → warning
- 已列出 `ai_tools`，但 `ai_assistance` 缺失 / `none` / `not_declared` → warning

warning 不是“已经正确”，只是让历史文档仍可读取，同时把不一致显式暴露出来

这些字段只回答：

> **这个 artifact 自己声明了怎样的 AI assistance 与人工复核过程？**

它们不回答：

```text
谁应该算作者
是否完成 peer review
模型/工具身份是否被第三方证明
内容是否科学正确
是否符合某家期刊的 AI policy
```

详细语义见 `PROCESS_DISCLOSURE.md`

## Doctor 与 SARIF

```bash
python core/doctor.py path/to/docs
python core/doctor.py path/to/docs --json
python core/doctor.py path/to/docs --strict
```

Doctor 当前检查：

- 未解析的本地 Markdown 链接
- orphan 文档
- 选定的有向引用环
- frontmatter 元数据问题，包括非法过程披露字段
- readability 描述性信号
- 文档图节点/边统计

`--strict` 只是改变**当前命令的本地退出状态**，不是 GitHub Actions、分支保护或 PR 合并条件

SARIF：

```bash
python core/sarif.py path/to/docs -o output/doctor.sarif
```

SARIF 使用稳定 namespaced `ruleId` 与 `autoDocFinding/v1` partial fingerprint，把同一套诊断转换成标准结果容器；它不把 Markdown 体检包装成源码静态分析认证或科研同行评审

## 多格式同步

```python
from core.sync import SyncEngine

results = SyncEngine().sync_with_fallback(
    "report.md",
    targets=["markdown", "html", "docx"],
    output_dir="output",
)
```

Markdown 输出使用 Python 标准库复制，Windows / Linux / macOS 不依赖同一个 shell 命令

`sync/targets.yaml` 中的 `pandoc_path` 参与运行时解析；Pandoc 缺失时明确报告，HTML 可以走 Mistune fallback，DOCX/PDF/EPUB 不伪造成功

## RO-Crate 1.3

RO-Crate 1.3 于 **2026-06-22** 发布，是当前观察到的 long-term release

仓库有真实 writer：

```bash
python core/ro_crate.py output report.md report.html \
  --name "Research artifact set" \
  --description "Rendered report and interoperable metadata" \
  --author lostlight530 \
  --license MIT
```

也可以在 `SyncEngine(..., emit_ro_crate=True)` 或 `sync/targets.yaml` 中选择性开启

当前输出包括：

- `ro-crate-metadata.json` → `CreativeWork` metadata descriptor
- `./` → Root `Dataset`
- 成功产物 → `File` data entities
- `contentSize` / `encodingFormat`
- 作者 → contextual `Person`
- 文件 SHA-256 → byte identity `PropertyValue`

**边界必须保留：** 这是 `auto-doc-engine/ro-crate@1` 的实现 profile，不等于任何外部 validator 已经跑过，也不等于科研结果被独立复现

今天新增的 `ai_assistance` / `ai_tools` / `human_review` / `disclosure_ref` 仍是**项目 frontmatter 元数据**；当前 RO-Crate writer 不会擅自把它们伪装成 RO-Crate 标准属性

## 结构差异

`core/incremental.py` 使用 SHA-256 语义，并把重复 add/delete subtree 代码收敛为单一路径

```text
old AST + new AST
    ↓
normalized subtree text
    ↓
SHA-256 identity
    ↓
sibling sequence alignment
    ↓
add / modify / delete / unchanged
```

历史记录使用原子替换写入，并限定每个文档最多保留最近 50 条摘要

这仍然只是 **change detector**，不负责自动 patch、冲突解决、所有权或多人协作合并

## AST 更新

`core/ast_engine.py` 当前语义：

- shallow signature 使用 SHA-256
- 支持已声明的 strikethrough / image / linebreak / ordered-list 等结构
- heading 文本递归抽取
- 不支持的 parse/render node 显式失败

Parse → Render 是**规范化结构语义**，不是 Markdown 字节级保真承诺

## Cross-reference

跨文档引用层：

- 递归读取格式化 heading 文本
- 使用 URL parser 区分外部 URL 与本地路径
- 支持 percent-decoding 和文档集 root-relative `.md` 链接
- near-miss cutoff / BFS depth / recurring threshold 有明确参数边界
- 持久化 index 明确只存 node/ref graph，aliases 与诊断状态重新从源文档构建

`near_miss` 只是 lexical hint，不等于推断作者真正意图

## Readability

`core/readability.py` 同时识别 ``` 与 `~~~` fenced code，并只输出描述性信号

它不会把 Coleman-Liau 或 CJK 平均句长包装成：

- 写作质量
- 无障碍合规
- 科研质量
- 同行评审结果

## 三仓 handoff

```text
auto-doc-engine
artifact identity + declared AI/human-review context
        ↓
epistemic-pipeline
claim-index@1 + evidence-envelope@2 + provider/review disclosure
        ↓
sci-render-kit
figure-claim-binding@1 + figure-evidence@2
```

Auto Doc 推荐交接字段：

```text
artifact_id
content_sha256
source_refs[]
document_status
generated_with
provenance_ref
validation_status
reproducibility_level
ai_assistance
ai_tools[]
human_review
disclosure_ref
```

不要求仓库互相 import

上游如果给出 confidence 值，必须一起携带 semantics，Auto Doc 不擅自把它改写成 probability

## 实验区重新校准

实验文件保留原名称，方便兼容已有引用，但语义已收紧：

- `template_prewarm.py`：调用者产物的有界 LRU cache
- `async_conduit.py`：有界 priority queue + concurrency scheduler，不是完整 streaming/backpressure 系统
- `memory_lattice.py`：本地 JSON node/link store + rounded numeric index，不是向量数据库或数学 lattice
- `restart_protocol.py`：只有 handler 本身可重复时 replay 才可能确定；会比对 replay result hash
- `self_observe.py`：显式事件 instrumentation + 时间统计，不是系统自主优化自己

**实验性修好 ≠ 自动升级成主链能力**

## 外部校准

标准/依赖基线继续保留 2026-08-23 观测：

- RO-Crate：1.3，2026-06-22，当前 long-term release
- SARIF：2.1.0 + Approved Errata 01
- Mistune：观察到 3.3.4，仓库安全下限仍保留 `>=3.2.1`
- Pandoc：观察到 3.10.2，仍属于可选环境依赖
- Citation File Format：1.2.0

2026-08-26 的研究校准另外吸收了 autonomous science 中对 re-openable provenance、claim-aware artifact observability、AI transparency 与 human oversight 的最新强调

这些外部信号只说明问题重要，不等于本仓被第三方认证

## 可复现性语义

共享科研契约继续使用项目内 R0–R3：

- **R0 Traceable**：记录来源/产物身份
- **R1 Replay-addressable**：输入、配置、工具修订足以定位预期重放
- **R2 Environment-bounded**：进一步记录关键运行环境和依赖假设
- **R3 Reproduced**：已经发生独立 rerun，并按声明标准完成比较

manifest、checksum、SARIF、process disclosure、RO-Crate 文件的存在都不能单独把结果提升到 R3

## 本地维护工具

需要时可以手动运行：

```bash
python -m pip install jinja2 "mistune>=3.2.1" pyyaml
make test
```

它们只是本地维护工具，**不是 GitHub 自身门禁**，仓库不新增 GitHub Actions / CI workflow / branch merge gate

本次 2026-08-26 维护不把测试套件作为完成条件

## 仓库地图

```text
auto-doc-engine/
├── core/
│   ├── renderer.py
│   ├── ast_engine.py
│   ├── incremental.py
│   ├── cross_ref.py
│   ├── frontmatter.py
│   ├── readability.py
│   ├── doctor.py
│   ├── sarif.py
│   ├── sync.py
│   ├── ro_crate.py
│   └── experimental modules
├── templates/jinja2/
├── sync/targets.yaml
├── examples/
├── tests/                  # 可选本地维护检查
├── RESEARCH_CONTRACT.md
├── PROCESS_DISCLOSURE.md
├── FRONTIER_ALIGNMENT.md
├── MANIFEST.yaml
└── CITATION.cff
```

## 科研边界

- Provenance ≠ Truth
- Digest ≠ 语义等价
- Structural Diff ≠ 自动安全合并
- AI / process disclosure ≠ 作者资格裁定或模型输出真实性证明
- Human review ≠ peer review / scientific validity
- Readability signal ≠ 科研质量
- RO-Crate metadata ≠ 已完成独立复现
- Optional dependency 缺失必须显式暴露
- Experimental source file ≠ Integrated capability

## 引用与许可

`CITATION.cff` 使用 CFF 1.2.0，许可证为 MIT
