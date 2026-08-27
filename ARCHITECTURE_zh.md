# 架构 — auto-doc-engine

> 校准日期：2026-08-27。本文描述当前真实实现、边界和实验区，不定义 GitHub 合并政策

[English](ARCHITECTURE.md) · [README](README_zh.md) · [科研契约](RESEARCH_CONTRACT.md) · [Artifact Record](ARTIFACT_RECORD.md) · [过程披露](PROCESS_DISCLOSURE.md) · [四日总整合](FOUR_DAY_CONSOLIDATION.md)

## 1. 核心判断

科研文档自动化不是“把字符串生成出来”这么简单，而是一个：

> **compiler + artifact evidence + research-object packaging** 问题

仓库把容易混成“生成报告”的动作拆成 9 层：

1. 结构化数据绑定
2. typed document structure
3. structural-change evidence
4. 文档/引用诊断
5. 有界科研 metadata 与过程披露
6. findings interchange
7. 带显式外部依赖边界的格式转换
8. 轻量 artifact handoff record
9. 可选外部 Research Object packaging

目标是**可检查、可追踪、失败显式**，不是最大化自动化、作者裁定、来源真值判断或自动同行评审

## 2. 规范架构

```text
JSON / CSV / YAML
        ↓
core/renderer.py + Jinja2
        ↓
normalized Markdown
        ↓
core/ast_engine.py
        │
        ├── core/incremental.py
        │      structural change evidence
        ├── core/cross_ref.py
        │      document / heading graph
        └── core/frontmatter.py
               metadata + process disclosure
        ↓
core/doctor.py + core/readability.py
        │
        ├── JSON
        └── core/sarif.py
               SARIF 2.1.0 + Errata 01

Markdown
   ↓
core/sync.py
   ├── Markdown / optional HTML/DOCX/PDF/EPUB
   ├── optional core/artifact_record.py
   │      artifact-record@1
   └── optional core/ro_crate.py
          RO-Crate 1.3
```

每个模块仍可独立调用，这张图表达的是可组合契约，不是每次必须全跑

## 3. 数据绑定层

`core/renderer.py` 当前支持：

- JSON mapping/list
- CSV rows
- YAML/YML mapping/list
- Jinja2
- 仓库 Markdown helper filters

两种加载语义：

- `strict=False`：保留历史宽松行为
- `strict=True`：缺文件、未知 suffix、非法顶层结构显式失败

未集成：SQLite、数据库连接、网络抓取、credential 管理、自动 schema inference

## 4. Typed Markdown 层

`core/ast_engine.py` 是集成模块共享的结构入口

支持：

- heading / paragraph / text
- fenced / inline code
- ordered / unordered list
- table
- blockquote / thematic break
- strong / emphasis / strikethrough
- link / image
- softbreak / linebreak

`ASTNode.signature` 与 incremental subtree identity 使用 SHA-256，但只是声明表示层的身份辅助，不是普适 semantic hash

Parse → Render 输出 normalized Markdown，不承诺原始字节 round-trip

## 5. Structural Change 层

```text
normalized subtree
      ↓
SHA-256
      ↓
sibling SequenceMatcher
      ↓
add / modify / delete / unchanged
```

generation history 有界并使用原子替换写入

能说明：结构变化如何被记录

不能说明：

- patch 自动安全应用
- conflict ownership
- CRDT/OT merge
- 语义等价
- 任意并发人类编辑都能保留

## 6. Cross-reference 与诊断

`core/cross_ref.py` 当前包括：

- document / heading nodes
- local Markdown links
- percent-decoding
- URL 先解析再区分本地路径
- root-relative `.md` path
- recursive heading text
- aliases
- near-miss / dangling / recurring-target
- directed document graph

`near_miss` 是 lexical hint，不是作者真实意图推断

## 7. Metadata 与 Process Disclosure

`core/frontmatter.py` 当前有界字段：

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
ai_assistance
ai_tools
human_review
disclosure_ref
```

过程枚举：

```text
ai_assistance: none | used | not_declared
human_review: reviewed | partial | not_reviewed | not_declared
```

类型/枚举错误是 error；交叉字段过程不一致是 warning；未知字段 warning 保留 forward compatibility

这层不是：

- 完整 bibliographic ontology
- 作者资格决策系统
- provider/model identity registry
- peer review
- publisher-policy validator

## 8. Doctor 与 SARIF

`core/doctor.py`：`auto-doc-engine/doctor@1`

聚合：

- unresolved links
- orphan docs
- selected directed cycles
- frontmatter/process-disclosure issues
- readability signals
- graph statistics

退出状态只是 caller-facing local runtime signal

`core/sarif.py`：`auto-doc-engine/sarif@1`

目标：OASIS SARIF 2.1.0 + Approved Errata 01

SARIF 是 findings interchange，不是科学或兼容性认证

## 9. Sync 层

`core/sync.py` 明确区分内建能力与外部工具：

- Markdown：Python `shutil.copy2`
- HTML：Pandoc；不可用时 Mistune fallback
- DOCX / EPUB：Pandoc
- PDF：Pandoc + 声明 PDF engine

外部 subprocess 使用 argv list，不依赖 `shell=True`

两个可选证据/package 输出：

```text
artifact_record.emit
research_object.emit_ro_crate
```

默认都关闭

## 10. Artifact Record 层

2026-08-27 新增：

```text
auto-doc-engine/artifact-record@1
```

它位于“文档 metadata”和“完整 Research Object packaging”之间

可以记录：

- source document SHA-256
- 成功 derivative SHA-256
- selected metadata canonical identity
- declared authors / source refs
- process disclosure
- frontmatter validation summary
- configuration / provenance / validation refs
- execution context
- caller-declared R0–R3 level
- scientific/authorship/peer-review 等边界 flag

默认不复制 payload text

### 引用处理

```text
存在的本地文件
  -> 记录 file hash

URI
  -> 原样作为 opaque URI 保留，不联网解引用

其他未解析字符串
  -> 保留为 unresolved/opaque reference
```

所以 artifact record 不引入隐藏网络依赖

### Validation 语义

嵌入的 validation 只来自当前 bounded frontmatter validator

```text
frontmatter clean != factual correctness
frontmatter clean != scientific validity
frontmatter clean != peer review
```

## 11. RO-Crate 1.3 层

`core/ro_crate.py` 是真实 RO-Crate 1.3 writer

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

如果先生成 `artifact-record@1`，后续 RO-Crate 可以把 `.artifact.json` 当作普通 `File` payload package

这**不表示** artifact record 自动变成 RO-Crate 标准 profile

当前 canonical path 不运行外部 RO-Crate validator

## 12. 为什么 Artifact Record 和 RO-Crate 分层

```text
artifact-record@1
  项目自有轻量 interoperability object

RO-Crate 1.3
  外部 Research Object packaging
```

借鉴的是 Research Object / Workflow Run Crate 的 separation of concerns：资源、annotation、execution/provenance record 可以关联，但保持各自 scope/vocabulary/provenance

当前不声称：

- Process Run Crate conformance
- Workflow Run Crate conformance
- Provenance Run Crate conformance

## 13. R0–R3

- **R0 Traceable**：source/artifact association 存在
- **R1 Replay-addressable**：声明 input/config/tool identity 可定位预期 replay
- **R2 Environment-bounded**：关键 runtime/dependency 边界也被记录
- **R3 Reproduced**：真实发生 separate rerun + declared comparison

checksum、artifact record、SARIF、RO-Crate 都不能自己把结果升级成 R3

## 14. 三仓 Day-4 handoff

```text
auto-doc-engine
artifact-record@1
        ↓
epistemic-pipeline
upstream artifact refs
claim-verification@1
evidence-envelope@2
        ↓
sci-render-kit
claim_audit_ref
figure-claim-audit@1
figure-evidence@2
```

互操作通过文件/引用表达，不通过 hidden imports

## 15. 实验区

| 模块 | 当前真实语义 |
|---|---|
| `template_prewarm.py` | in-memory LRU cache |
| `async_conduit.py` | bounded priority scheduling |
| `memory_lattice.py` | local node/link JSON store + numeric index |
| `restart_protocol.py` | event replay + result hash；确定性依赖 handler |
| `self_observe.py` | instrumentation + descriptive timing |

历史命名只为兼容，不是能力证明

## 16. 2026-08-27 全球校准

当前设计借鉴：

- autonomous science 中 re-openable provenance 的纠错价值
- AI scientific publishing 的透明度、责任与 human oversight
- artifact-centered claim-aware observability
- EarthVerse 暴露的端到端 evidence-chain consistency 问题
- RO-Crate / Workflow Run Crate 对 research product 与 execution/provenance record 的分层

这些是设计信号，不是外部 endorsement / conformance 证明

详见 `FOUR_DAY_CONSOLIDATION.md` 与 `FRONTIER_ALIGNMENT.md`

## 17. 非目标

- GitHub Actions / CI / CodeQL / merge gate 作为架构层
- 自动 peer review
- scientific truth inference
- source credibility adjudication
- canonical network data acquisition
- universal Markdown byte fidelity
- universal converter availability
- external RO-Crate certification
- fake Workflow Run Crate conformance
- 实验模块自动晋升主链

## 18. 硬边界

```text
Provenance != Truth
Hash identity != semantic equivalence
Structure != meaning
Structural change != conflict resolution
Declared source != source credibility
Process disclosure != authorship proof
Human review != peer review
Artifact record != external standard
RO-Crate packaging != reproduction
Local diagnostics != scientific validation
```
