# auto-doc-engine

> AST 驱动的科研文档编译、结构差异证据、过程披露元数据、轻量 artifact record、跨文档诊断、SARIF 交换与可选 RO-Crate 1.3 研究对象打包

[English](README.md) · [架构](ARCHITECTURE_zh.md) · [科研契约](RESEARCH_CONTRACT.md) · [Artifact Record](ARTIFACT_RECORD.md) · [过程披露](PROCESS_DISCLOSURE.md) · [四日总整合](FOUR_DAY_CONSOLIDATION.md) · [前沿校准](FRONTIER_ALIGNMENT.md) · [示例](examples/README_zh.md)

## 当前定位

`auto-doc-engine` 把科研文档当成**可检查、可追踪、可交接的研究产物**，而不是一段等待字符串替换的文本，也不是只有最后一个 PDF 才算产物

当前规范主链：

```text
JSON / CSV / YAML
        ↓
Jinja2 数据绑定
        ↓
Typed Markdown AST
        ↓
结构差异证据
        ↓
跨文档图 + 有界元数据诊断
        ↓
声明式 AI / 人工复核过程上下文
        ↓
Text / JSON / SARIF findings
        ↓
Markdown / 可选 Pandoc 格式
        ↓
可选 artifact-record@1
        ↓
可选 RO-Crate 1.3 packaging
```

仓库优化的是：**身份、可检查性、失败显式、跨工具 handoff**

仓库不声称：

- 自动科学真值判断
- 自动无冲突合并
- 来源可信度裁定
- 作者资格裁定
- 自动同行评审
- universal 格式转换
- 外部 RO-Crate validator 已认证
- Workflow Run Crate conformance
- publisher AI policy 合规认证
- 仅靠 metadata 完成独立复现

## 能力矩阵

| 能力 | 状态 | 当前边界 |
|---|---|---|
| `core/renderer.py` | **已实现** | Jinja2 + JSON / CSV / YAML/YML；SQLite 与网络 API 未集成 |
| `core/ast_engine.py` | **已实现** | Mistune 3.x Typed AST；规范化结构渲染，不承诺字节级 round-trip |
| `core/incremental.py` | **已实现** | SHA-256 + sibling sequence alignment，输出 add/modify/delete/unchanged；不是 merge engine |
| `core/cross_ref.py` | **已实现** | 本地 Markdown 文档/标题图、aliases、dangling/near-miss 与 recurring-target 诊断 |
| `core/frontmatter.py` | **已实现** | 有界科研元数据 + AI assistance / tool / human-review disclosure |
| `core/readability.py` | **已实现** | 拉丁/CJK 描述性启发式；不是写作质量或 peer review 评分 |
| `core/doctor.py` | **已实现** | 本地文档诊断 Text/JSON + 显式退出状态；不是 GitHub merge policy |
| `core/sarif.py` | **已实现** | SARIF 2.1.0 + Approved Errata 01 findings profile |
| `core/sync.py` | **已实现 / 可选转换** | Python 原生 Markdown copy；Pandoc 可选；HTML 可 Mistune fallback |
| `core/artifact_record.py` | **已实现 profile** | `auto-doc-engine/artifact-record@1`：单个源文档 + derivative 身份 + metadata/process/diagnostic context；项目自有，不是外部标准 |
| `core/ro_crate.py` | **已实现 profile** | 本地 artifact set 的 RO-Crate 1.3 核心 JSON-LD；不声称外部 validator 成功 |
| `template_prewarm` / `async_conduit` / `memory_lattice` / `restart_protocol` / `self_observe` | **实验性** | 有界独立模块，不接规范主链 |

## 数据绑定

```python
from core.renderer import DataBindingEngine

engine = DataBindingEngine()
context = engine.load_data("data/research.yaml", strict=True)
markdown = engine.render("paper_summary.j2", context)
assert markdown
```

当前支持：

```text
.json
.csv
.yaml
.yml
```

- `strict=False`：保留历史宽松行为
- `strict=True`：缺文件、未知格式、非法顶层结构显式失败

## 科研 frontmatter 与过程披露

```yaml
---
title: Evidence synthesis
description: Structured summary of declared sources
status: draft
updated: 2026-08-27
authors: [lostlight530]
sources:
  - https://www.researchobject.org/ro-crate/specification/1.3/
license: MIT
language: zh-CN
artifact_id: summary-2026-08-27
ai_assistance: used
ai_tools:
  - 人工声明的 provider/model/tool 标识
human_review: reviewed
disclosure_ref: PROCESS_DISCLOSURE.md
---
```

有界枚举：

```text
ai_assistance: none | used | not_declared
human_review: reviewed | partial | not_reviewed | not_declared
```

交叉字段不一致保留为 warning，例如 `ai_assistance: used` 却没有有效 `ai_tools`

硬边界：

```text
AI disclosure != 作者资格证明
AI tool label != provider provenance proof
human_review=reviewed != peer review
过程元数据 != 科学有效性
```

详见 [PROCESS_DISCLOSURE.md](PROCESS_DISCLOSURE.md)

## 新增：Portable Artifact Record

2026-08-27 四日总整合新增：

```text
auto-doc-engine/artifact-record@1
```

它填补了 frontmatter 和完整 Research Object package 之间的空白

一个 record 可以保留：

- 源 Markdown 的 byte identity
- 成功 derivative 的 byte identity
- 选定的有界 metadata
- 声明的 authors / source refs
- AI / human-review process disclosure
- frontmatter/schema diagnostics
- configuration / provenance / validation refs
- execution context
- 项目内 R0–R3 reproducibility declaration
- scientific/authorship/peer-review 等边界 flag

独立 CLI：

```bash
python core/artifact_record.py report.md \
  --derivative html=output/report.html \
  --generated-with auto-doc-engine/sync@1 \
  --configuration-ref sync/targets.yaml \
  --reproducibility-level R1 \
  --output output/report.artifact.json
```

SyncEngine：

```python
from core.sync import SyncEngine

results = SyncEngine().sync_with_fallback(
    "report.md",
    targets=["markdown", "html"],
    output_dir="output",
    emit_artifact_record=True,
)
```

也可以在 `sync/targets.yaml` 开启：

```yaml
artifact_record:
  emit: true
  reproducibility_level: R1
```

默认 `emit: false`，避免旧调用突然多出新文件

详见 [ARTIFACT_RECORD.md](ARTIFACT_RECORD.md)

## Artifact Record 和 RO-Crate 为什么分开

两者是互补层：

```text
artifact-record@1
  = 一个 source/derivative set 的轻量项目 handoff

RO-Crate 1.3
  = 更完整 Research Object 的外部 linked-data packaging
```

如果两者同时开启：

1. SyncEngine 先生成 `.artifact.json`
2. RO-Crate 再把它作为普通 payload 一起 package

仓库不会把 `artifact-record@1` 伪装成 RO-Crate 标准属性，也不声称 Workflow / Process / Provenance Run Crate conformance

这借鉴了 Research Object / Workflow Run Crate 很重要的 separation of concerns：

> **数据产物和描述其执行/溯源过程的记录彼此相关，但不是同一个语义对象**

## Doctor 与 SARIF

```bash
python core/doctor.py path/to/docs
python core/doctor.py path/to/docs --json
python core/doctor.py path/to/docs --strict
python core/sarif.py path/to/docs -o output/doctor.sarif
```

Doctor 当前覆盖：

- unresolved local Markdown links
- orphan documents
- 选定有向引用环
- frontmatter / process-disclosure 问题
- readability 描述性信号
- 文档图统计

`--strict` 只影响当前命令退出状态，不是 GitHub merge gate，也不是 scientific validity check

SARIF 是 findings interchange；下游平台能读 SARIF 不代表它替我们认证科研结论

## 多格式同步

```python
results = SyncEngine().sync_with_fallback(
    "report.md",
    targets=["markdown", "html", "docx"],
    output_dir="output",
)
```

环境边界：

- Markdown：Python stdlib copy
- HTML：Pandoc 可用时走 Pandoc，否则可 Mistune fallback
- DOCX / EPUB：Pandoc
- PDF：Pandoc + 声明的 PDF engine
- 外部 converter 缺失必须显式报告
- 不依赖 `shell=True`

## RO-Crate 1.3

```bash
python core/ro_crate.py output report.md report.html \
  --name "Research artifact set" \
  --description "Rendered report and interoperable metadata" \
  --author lostlight530 \
  --license MIT
```

当前实现：

- `ro-crate-metadata.json` → `CreativeWork` metadata descriptor
- `./` → root `Dataset`
- payload → `File`
- `contentSize` / `encodingFormat`
- 作者 → contextual `Person`
- SHA-256 → Schema.org `PropertyValue`

边界：

```text
生成 RO-Crate != 外部 validator 已通过
RO-Crate metadata != 独立复现
RO-Crate packaging != 科学有效性
```

## R0–R3 可复现性语义

项目内术语：

- **R0 Traceable**：来源/产物可关联并有身份记录
- **R1 Replay-addressable**：声明输入、配置、工具身份足以定位预期 replay
- **R2 Environment-bounded**：关键运行环境/依赖边界也被记录
- **R3 Reproduced**：已经真实发生独立 rerun，并按声明标准完成比较

`artifact_record.py` 可以携带调用者声明的 level，但 metadata 生成本身不会执行 rerun，也不能自封 R3

## 三仓 Day-4 handoff

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

仓库之间通过文件/引用交接，不要求直接 import

## 2026-08-27 全球前沿校准

当前设计借鉴但不声称被这些工作认证：

- Nature Computational Science：**Provenance grounds trust in autonomous science**（2026-08-20）——完整、可重新打开的 provenance 是纠错基础设施
- Nature Computational Science：**Responsible and transparent use of AI in scientific publishing**（2026-08-20）——强调 transparency、accountability、human oversight
- **Artifact-centered Claim-aware Observability for Autonomous Scientific Agents**（arXiv:2608.18312）——仅记录 model call 不够，artifact / claim / relation 需要一等审计结构
- **EarthVerse**（arXiv:2608.23525）——局部任务能力不等于端到端 evidence / scale / unit / calculation / interpretation 链一致
- RO-Crate 1.3 与 Workflow Run Crate family——data products 与 execution/provenance descriptions 应显式关联但保持语义分离

详见 [FOUR_DAY_CONSOLIDATION.md](FOUR_DAY_CONSOLIDATION.md) 与 [FRONTIER_ALIGNMENT.md](FRONTIER_ALIGNMENT.md)

## 实验区

仍不接规范主链：

- `template_prewarm.py`：bounded in-memory LRU cache
- `async_conduit.py`：bounded priority/concurrency scheduler
- `memory_lattice.py`：local node/link store + rounded numeric index
- `restart_protocol.py`：event replay + result-hash check；确定性取决于 caller handler
- `self_observe.py`：显式 instrumentation + 描述性 timing

历史隐喻命名不等于能力事实

## 本地维护

可选：

```bash
python -m pip install jinja2 "mistune>=3.2.1" pyyaml
make test
```

这些只是本地维护工具，不是 GitHub Actions、branch protection、merge gate、peer review 或科学验证

2026-08-27 四日总整合**不把测试执行当完成证据**；完成依据是静态接口、profile、文档一致性与 branch diff 审计

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
│   ├── artifact_record.py
│   ├── ro_crate.py
│   └── experimental modules
├── templates/jinja2/
├── sync/targets.yaml
├── examples/
├── tests/                  # 可选本地维护检查
├── RESEARCH_CONTRACT.md
├── ARTIFACT_RECORD.md
├── PROCESS_DISCLOSURE.md
├── FOUR_DAY_CONSOLIDATION.md
├── FRONTIER_ALIGNMENT.md
├── MANIFEST.yaml
└── CITATION.cff
```

## 科研完整性硬边界

```text
Provenance != Truth
Digest != 语义等价
Structural diff != 冲突解决
Declared source != 天然可信来源
Artifact record != 外部 Research Object 标准
Process disclosure != 作者资格裁定
Human review != Peer review
RO-Crate metadata != Reproduction
Standard alignment != External certification
Experimental source != Integrated capability
```

## 引用与许可

`CITATION.cff`：CFF 1.2.0  
License：MIT
