# 架构 — auto-doc-engine

> 校准日期：2026-08-26。本文描述当前真实实现、边界和实验区，不定义 GitHub 合并政策

[English](ARCHITECTURE.md) · [README](README_zh.md) · [科研契约](RESEARCH_CONTRACT.md) · [过程披露](PROCESS_DISCLOSURE.md)

## 1. 核心判断

科研文档自动化不是“把字符串生成出来”这么简单，而是一个 **compiler + evidence packaging** 问题

规范过程可以拆成：

1. 结构化数据进入模板
2. Markdown 进入 Typed AST
3. AST 变化被记录为结构差异
4. 文档之间的引用和元数据被显式检查
5. artifact 可以显式声明 AI assistance / tool / human-review 过程上下文
6. 诊断可以转换成 Text / JSON / SARIF
7. 可选工具存在时生成其他格式
8. 成功产物可以选择性打包 RO-Crate 1.3 元数据

这套架构优化的是**可解释、可追踪、过程上下文显式、失败显式**，不是“自动化程度最大化”，也不做作者资格或科研真值裁定

## 2. 规范主链

```text
JSON / CSV / YAML
        ↓
core/renderer.py
        ↓
Markdown
        ↓
core/ast_engine.py
        ↓
Typed AST
   ┌────┼───────────────┐
   ▼    ▼               ▼
incremental       cross_ref       frontmatter
结构差异           引用图           科研 + 过程元数据
   └────┬───────────────┘
        ▼
   core/doctor.py ──> JSON
        │
        └───────────> core/sarif.py ──> SARIF

Markdown ──> core/sync.py ──> Markdown / HTML / DOCX / PDF / EPUB
                                   │
                                   ▼
                           core/ro_crate.py
                                   │
                                   ▼
                           RO-Crate 1.3 metadata
```

每个模块仍可独立调用，所以这张图表达的是**可以组合的契约**，不是强制所有模块每次全部运行

## 3. 数据绑定层

`core/renderer.py` 当前真实支持：

- JSON mapping / list
- CSV rows
- YAML / YML mapping / list
- Jinja2
- `table` / `bullet_list` Markdown filter

两种加载语义：

- `strict=False`：保留历史宽松行为
- `strict=True`：缺文件、未知 suffix、非法顶层结构显式失败

当前未集成：SQLite、数据库、网络 API、自动 schema 推断

## 4. AST 层

`core/ast_engine.py` 是当前集成模块共享的 Markdown 结构入口

已声明支持：

- heading / paragraph / text
- fenced code / inline code
- ordered / unordered list
- table
- blockquote / thematic break
- strong / emphasis / strikethrough
- link / image
- softbreak / linebreak

`ASTNode.signature` 使用 SHA-256，但仍然只是**浅层本地身份辅助**，不是语义哈希

Parse → Render 输出 normalized Markdown，不承诺源文件字节级 round-trip

## 5. Structural Diff 层

`core/incremental.py`：

```text
normalized subtree text
        ↓
SHA-256
        ↓
sibling SequenceMatcher
        ↓
add / modify / delete / unchanged
```

Generation history 使用原子替换写入并保持有界

它能证明“结构变化被怎样记录”，不能证明：

- patch 自动安全应用
- 所有人类修改都能保留
- 多人冲突自动解决
- 两段文本语义相同

## 6. Cross-reference 层

`core/cross_ref.py` 当前负责：

- document node / heading node
- 本地 `.md` link
- aliases
- near-miss / dangling
- recurring missing target backlog
- directed document graph

当前路径处理支持 URL parser、percent-decoding、文档集 root-relative Markdown path，heading text 使用递归抽取

`near_miss` 只是 lexical hint，不等于推断作者真正意图

## 7. Frontmatter 科研元数据与过程披露层

科研/文档字段：

```text
title
description
aliases
status
updated
tags
authors
sources
license
doi
language
artifact_id
```

2026-08-26 新增过程披露字段：

```text
ai_assistance
ai_tools[]
human_review
disclosure_ref
```

允许值：

```text
ai_assistance: none | used | not_declared
human_review: reviewed | partial | not_reviewed | not_declared
```

校验规则：

- 非法 type / enum → error
- `ai_assistance: used` 但没有有效 `ai_tools` → warning
- 已存在 `ai_tools`，但 assistance 缺失 / none / not_declared → warning

warning 是**不一致信号**，不是自动通过认证

这些字段只描述 artifact 自己声明的生产/复核过程：

```text
AI disclosure ≠ authorship adjudication
AI tool identity ≠ provenance proof
human review ≠ peer review
human review ≠ scientific validity
process metadata ≠ publisher compliance
```

这是 portable metadata layer，不是完整出版物 ontology，也不是期刊 AI-policy engine

详细语义见 `PROCESS_DISCLOSURE.md`

## 8. Doctor

`core/doctor.py` 当前 profile：`auto-doc-engine/doctor@1`

聚合：

- unresolved links
- orphan docs
- selected directed cycles
- frontmatter issues，包括过程披露类型/枚举问题
- readability signals
- graph statistics

退出码是**调用方运行时信号**，不是 GitHub 自身门禁，也不是科研结论或 publisher compliance 判定

## 9. SARIF

`core/sarif.py` → `auto-doc-engine/sarif@1`

标准目标：SARIF 2.1.0 + Approved Errata 01

稳定互操作身份：

- namespaced `ruleId`
- `autoDocFinding/v1` partial fingerprint
- `sourceProfile = auto-doc-engine/doctor@1`

SARIF 在这里是 findings interchange，不代表任何下游平台已经替仓库做兼容性认证或科研评审

## 10. Sync

`core/sync.py` 明确区分内建能力和外部工具：

- Markdown：Python `shutil.copy2`
- HTML：Pandoc；缺失时可 Mistune fallback
- DOCX / EPUB：Pandoc
- PDF：Pandoc + 当前声明的 XeLaTeX engine

`sync/targets.yaml.custom.pandoc_path` 是真实运行时设置

所有 subprocess 使用 argv list，不使用 `shell=True`

## 11. RO-Crate 1.3

`core/ro_crate.py` 是当前真实 research-object metadata writer

标准面对外 JSON-LD 只写 RO-Crate / Schema.org 语义，不把项目自己的 profile 字段硬塞进 RO-Crate context

```text
ro-crate-metadata.json : CreativeWork
        │ about
        ▼
./ : Dataset
        │ hasPart
        ├── File A ──> SHA-256 PropertyValue
        └── File B ──> SHA-256 PropertyValue

Dataset ── author ──> Person
```

可以 CLI 独立运行，也可以由 SyncEngine 对成功输出进行可选打包

今天新增的 process-disclosure frontmatter 仍是**项目字段**；当前 `ro_crate.py` 不会擅自把它们写成 RO-Crate 标准属性

**生成文件 ≠ 外部 validator 已验证**

## 12. 实验区

| 模块 | 当前真实语义 |
|---|---|
| `template_prewarm.py` | 调用者产物的 in-memory LRU cache |
| `async_conduit.py` | 有界 priority queue + concurrency scheduler |
| `memory_lattice.py` | local node/link JSON store + numeric bucket index |
| `restart_protocol.py` | event replay + result hash verification；确定性依赖 handler 本身 |
| `self_observe.py` | explicit instrumentation + timing summaries |

保留历史文件名是兼容性，不代表名字里的隐喻就是功能事实

## 13. 三仓 handoff

与 `epistemic-pipeline` / `sci-render-kit` 保持低耦合，推荐通过结构数据交接：

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

概念链：

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

不要求仓库互相 import

上游如果给出 confidence 值，必须一起携带 semantics，Auto Doc 不擅自把它改写成 probability

## 14. 2026-08-26 更新的研究意义

最新 autonomous-science 研究把普通 operation telemetry 与 artifact/claim auditability 区分开，同时 AI scientific publishing 也越来越强调 transparency / accountability / human oversight

Auto Doc 所在的最下层不需要因此增加一个 LLM 或“自动真值判断器”

更合理的工程增量是：

> **让 artifact 自己声明生产/人工复核过程，并让这段上下文能跟 identity / source / structure 一起进入后续科研链**

下游 Epistemic 可以继续增加 run/provider/claim audit；Sci Render 可以继续增加 figure/claim communication audit

## 15. R0–R3

- R0 Traceable
- R1 Replay-addressable
- R2 Environment-bounded
- R3 Reproduced

R3 必须真的发生独立 rerun + declared comparison，metadata / checksum / process disclosure / RO-Crate 文件不能单独证明它

## 16. 外部基线

标准/依赖观测继续保留 2026-08-23：

- RO-Crate 1.3：2026-06-22，当前 long-term release
- SARIF 2.1.0 + Approved Errata 01
- Mistune：观察到 3.3.4，仓库 floor `>=3.2.1`
- Pandoc：观察到 3.10.2，仍为可选外部环境
- CFF：1.2.0

“观察到最新版本”与“仓库已经验证全部兼容”严格分开

## 17. 非目标

- GitHub Actions / merge gating 作为架构层
- 自动同行评审
- 自动作者资格裁定
- publisher AI-policy compliance 认证
- 科学真值推断
- 网络数据抓取
- universal Markdown byte fidelity
- universal converter availability
- external RO-Crate certification
- 因为实验文件存在就自动晋升主链
