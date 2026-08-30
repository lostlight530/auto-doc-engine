# 架构 — auto-doc-engine

> 校准日期：2026-08-31。本文描述当前真实实现、维护面、边界和实验区，不定义 GitHub 合并政策

## 核心判断

科研文档自动化是一个 **compiler + artifact evidence + lineage + Research Object packaging + maintenance** 问题

```text
structured data
  -> renderer / Jinja2
  -> normalized Markdown
  -> typed Markdown AST
  -> structural-change evidence
  -> document graph + frontmatter + readability
  -> Doctor / JSON / SARIF
  -> sync / rendered derivatives
  -> optional artifact-record
       ├─ assertion basis
       ├─ reference-resolution states
       └─ dimensional audit coverage
  -> optional artifact-lineage
       ├─ typed caller-declared relations
       └─ non-inheritance boundaries
  -> optional RO-Crate 1.3

repository state
  -> daily / weekly / monthly maintenance scanner
       ├─ canonical document/path inventory
       ├─ stable-profile checks
       ├─ calendar/stage status
       └─ optional SHA-256 baseline
```

架构优化的是可检查性、稳定身份、失败显式、可移植 handoff 和跨代研究语义保留，不把文档自动化或仓库维护包装成科学真值推理

## 稳定项目标识

```text
auto-doc-engine/doctor
auto-doc-engine/sarif
auto-doc-engine/artifact-record
auto-doc-engine/artifact-lineage
auto-doc-engine/process-disclosure
auto-doc-engine/frontmatter-validation
auto-doc-engine/ro-crate
auto-doc-engine/maintenance-cadence
auto-doc-engine/maintenance-report
autoDocFinding
```

项目内部 profile 不使用装饰性的 `@1/@2` 或 `/v1` 后缀

真实外部标准与真实运行环境版本继续保留，例如 RO-Crate 1.3、SARIF 2.1.0 + Approved Errata 01、CFF 1.2.0

## 数据绑定边界

`core/renderer.py` 支持 JSON、CSV、YAML/YML + Jinja2

- `strict=False` 保留历史宽松加载
- `strict=True` 对缺失输入、未知格式、非法顶层结构显式失败

未集成 SQLite/数据库连接、网络数据获取、凭证管理与自动 schema inference

## Typed Markdown 边界

`core/ast_engine.py` 提供规范化 Markdown 结构

AST/subtree 的 SHA-256 是当前表示的身份，不是通用语义 hash

parse/render 会规范化受支持 Markdown，不承诺字节级 round-trip

## 结构差异层

`core/incremental.py` 输出

```text
add / modify / delete / unchanged
```

它是 change detector，不是自动 patch、冲突解决、ownership negotiation、CRDT/OT merge 或语义等价证明

## 文档图与 metadata

`core/cross_ref.py` 负责本地文档/标题引用与 dangling/near-miss/recurring diagnostics

near-miss 只是词法提示

`core/frontmatter.py` 提供有界科研 metadata 和声明式过程披露

缺失 provider/model/version/review 信息保持 unknown / `not_declared`

```text
process disclosure != authorship proof
human review != peer review
source ref != source credibility
```

规范主链不进行 automatic AI-text detection

## Doctor 与 SARIF

`core/doctor.py` 输出 `auto-doc-engine/doctor`

`core/sarif.py` 输出 `auto-doc-engine/sarif`，外部标准目标是 SARIF 2.1.0 + Approved Errata 01

`autoDocFinding` 是稳定项目 fingerprint namespace

SARIF 被下游读取只是 interoperability，不是科研认证

## 同步层

`core/sync.py`

- Markdown：Python `shutil.copy2`
- HTML：Pandoc 可用时走 Pandoc，否则 Mistune fallback
- DOCX / EPUB：Pandoc
- PDF：Pandoc + 声明的 PDF engine

外部进程使用参数列表，不依赖 `shell=True`

artifact record 与 RO-Crate 输出均为 opt-in

## Artifact Record 层

`core/artifact_record.py` 输出 `auto-doc-engine/artifact-record`

它可以记录

- source/derivative SHA-256
- 有界 metadata identity
- 声明式 source/author refs
- process disclosure
- frontmatter validation
- lineage/configuration/validation refs
- execution context
- 项目内 R0–R3 state
- assertion basis
- 维度化 audit coverage

默认不复制源文档 prose

本地文件可 hash，URI/opaque refs 保持显式未解析

## Assertion Basis 层

```text
document-frontmatter
runtime-observed-local-bytes
runtime-observed-local-filesystem
caller-declared
```

例如

| 字段 | Basis |
|---|---|
| source / derivative SHA-256 | runtime-observed local bytes |
| bounded document metadata | document frontmatter |
| authors / sources | document frontmatter |
| process disclosure | document frontmatter |
| `generated_with` | caller-declared，如果提供 |
| lineage refs | caller-declared + 可选本地解析 |

```text
assertion basis != truth
```

一个字段可以有精确 provenance，但内容仍然可能错

## Audit Coverage 层

artifact record 只计算真正可证明的描述性维度

```text
derivative_count
declared-source resolution counts + local_file_ratio
lineage-reference resolution counts + local_file_ratio
process-disclosure declared fields
frontmatter error/warning counts
```

不计算总质量分

```text
coverage != correctness
coverage ratio != probability
local-file resolution != source credibility
reference presence != evidence sufficiency
```

当前不声称 provenance soundness 或 scientific evidence verification

## Artifact Lineage 层

`core/artifact_lineage.py` 输出 `auto-doc-engine/artifact-lineage`

关系词表

```text
derived-from
revision-of
supersedes
uses
related-to
```

关系只允许 caller-declared

本地目标可 hash，URI/opaque reference 保持离线

不会从文件名、时间戳、正文相似度、Git history 或模型输出自动推断 lineage

每条关系都明确

```text
scientific_validity_inherited: false
reproducibility_inherited: false
```

```text
lineage != truth
revision-of != semantic equivalence
supersedes != history deletion
uses != evidence sufficiency
```

## RO-Crate 层

`core/ro_crate.py` 面向真实外部标准 RO-Crate 1.3

`auto-doc-engine/ro-crate` 只是稳定项目 exporter 标识，不是外部 RO-Crate 版本 profile

当前不声称外部 validator 成功、Workflow/Process/Provenance Run Crate conformance 或独立科学复现

## Artifact Record / Lineage / RO-Crate 分层

```text
auto-doc-engine/artifact-record
  单个 artifact handoff
        ↓ 可选关系
auto-doc-engine/artifact-lineage
  项目 history/dependency relation layer
        ↓ 可选打包
RO-Crate 1.3
  外部 Research Object packaging
```

它们可以关联，但不能混成同一 vocabulary 或科学声明

## 可复现性语义

- R0 Traceable
- R1 Replay-addressable
- R2 Environment-bounded
- R3 只有真实独立 rerun + 声明比较标准后才成立

checksum、SARIF、artifact record、lineage record、maintenance baseline 或 crate 都不能自封 R3

## Maintenance 层

`core/maintenance_cadence.py` 输出 `auto-doc-engine/maintenance-report`

`maintenance/cadence.yaml` 定义 canonical paths、scan paths、当前 stage、cadence 行为和治理排除项

Daily / Weekly / Monthly 规则见 `MAINTENANCE_CADENCE.md`

当前文档与历史快照权威分类见 `DOCUMENT_STATUS.md`

scanner 可报告

```text
canonical path presence
decorative project profile versions
Manifest calibration age
historical snapshot inventory
canonical SHA-256 baseline
calendar month status
configured stage status
```

当前 2026-08-31

```text
calendar_month: calendar-month-close
stage: closed
```

scanner 是只读维护证据，不运行测试、不调用 GitHub、不远程解引用、不删除历史、不证明科学有效性

## 文档治理层

`DOCUMENT_STATUS.md` 把 current contracts、examples、external metadata 与 historical snapshots 显式分类

历史文件

```text
FOUR_DAY_CONSOLIDATION.md
FIVE_DAY_CONSOLIDATION.md
SIX_DAY_CONSOLIDATION.md
```

保留为时间限定的研究快照，不再作为 current architecture contract

```text
historical snapshot != current contract
current contract != permission to rewrite history
```

## 三仓 handoff

```text
auto-doc-engine/artifact-record
auto-doc-engine/artifact-lineage
        ↓ 可选引用
epistemic-pipeline/claim-verification
epistemic-pipeline/claim-transfer
epistemic-pipeline/evidence-envelope
        ↓ 可选引用
sci-render-kit/figure-claim-audit
sci-render-kit/figure-evidence
sci-render-kit/communication-transfer
```

引用不等于隐藏 import，也不继承 scientific validity

## 阶段全球校准

2026-08-24 → 2026-08-31 阶段借鉴

- autonomous-science provenance 的 complete / re-openable corrective record
- scientific publishing 的 transparent AI use / human oversight
- artifact-centered claim-aware observability
- trajectory-to-evidence qualification
- evidence-bounded claim review
- end-to-end scientific-agent consistency
- claim-level auditability / contradiction transparency
- long-horizon phase behavior / regime-aware re-validation
- ScienceFlow-style persistent research segments / recovery
- beyond-final-score 的 long-horizon process evaluation
- Praxist solution/evidence lineage
- ReproAgent persistent contracts
- living research-software metadata / maintenance

这些只是 design signals，不是 validation、endorsement、novelty proof 或 conformance evidence

## 实验区

- `template_prewarm.py`：bounded in-memory LRU
- `async_conduit.py`：bounded priority scheduler
- `memory_lattice.py`：local node/link store + numeric bucket index
- `restart_protocol.py`：event replay + result-hash verification
- `self_observe.py`：显式 instrumentation + 描述性 timing

历史隐喻文件名不等于能力声明

## 硬边界

```text
Provenance != Truth
Hash identity != semantic equivalence
Structure != meaning
Structural change != conflict resolution
Assertion basis != correctness
Audit coverage != quality
Coverage ratio != probability
Artifact lineage != inherited scientific validity
Declared source != source credibility
Process disclosure != authorship proof
Human review != peer review
Artifact record != external standard
RO-Crate packaging != reproduction
Maintenance clean != scientific validation
Calendar-month close != reproduction
Local diagnostics != scientific validation
```

GitHub Actions、CI、CodeQL、dependency bots、branch protection 与 merge-gate architecture 不属于本仓库科研架构
