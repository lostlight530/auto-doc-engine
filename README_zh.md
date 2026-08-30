# auto-doc-engine

> AST 驱动的科研文档编译、结构差异证据、有界过程元数据、轻量 artifact record、显式 artifact lineage、维度化审计覆盖、SARIF 交换、可选 RO-Crate 1.3 打包与阶段化仓库维护

[English](README.md) · [架构](ARCHITECTURE_zh.md) · [科研契约](RESEARCH_CONTRACT.md) · [Artifact Record](ARTIFACT_RECORD.md) · [Artifact Lineage](ARTIFACT_LINEAGE_CONTRACT.md) · [Assertion Basis & Coverage](ASSERTION_BASIS_AND_COVERAGE.md) · [过程披露](PROCESS_DISCLOSURE.md) · [维护节奏](MAINTENANCE_CADENCE.md) · [文档状态](DOCUMENT_STATUS.md) · [8 月阶段收官](STAGE_2026_08_MAINTENANCE.md) · [示例](examples/README_zh.md)

## 当前定位

`auto-doc-engine` 把科研文档当成可检查、可追踪、可交接、可维护的研究产物，而不是一段字符串或只有最终 PDF 才算产物

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
可选 artifact-record
  ├─ assertion basis
  └─ dimensional audit coverage
        ↓
可选 artifact-lineage
  ├─ typed caller-declared relations
  └─ explicit non-inheritance boundaries
        ↓
可选 RO-Crate 1.3 packaging
```

仓库优化的是身份、可检查性、失败显式、跨工具 handoff 与跨代 artifact 语义保留

它不声称自动科学真值判断、自动无冲突合并、来源可信度裁定、作者资格裁定、同行评审、外部 RO-Crate 认证、Run Crate conformance、publisher policy 合规或仅靠 metadata 完成独立复现

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

项目内部标识不使用装饰性的 `@1/@2` 或 `/v1` 后缀

真实外部标准与真实运行环境版本继续保留，例如 RO-Crate 1.3、SARIF 2.1.0 + Approved Errata 01、CFF 1.2.0 以及真正观测到的软件版本

## 能力矩阵

| 能力 | 状态 | 当前边界 |
|---|---|---|
| `core/renderer.py` | 已实现 | Jinja2 + JSON/CSV/YAML/YML；SQLite/网络 API 未集成 |
| `core/ast_engine.py` | 已实现 | Typed AST；规范化结构渲染，不承诺字节级 round-trip |
| `core/incremental.py` | 已实现 | add/modify/delete/unchanged 结构证据；不是 merge engine |
| `core/cross_ref.py` | 已实现 | 本地 Markdown 图与 dangling/near-miss 诊断 |
| `core/frontmatter.py` | 已实现 | 有界科研元数据 + 声明式过程披露 |
| `core/readability.py` | 已实现 | 描述性启发式，不是写作质量或 peer-review 评分 |
| `core/doctor.py` | 已实现 | 文档诊断 + 本地退出状态 |
| `core/sarif.py` | 已实现 | SARIF 2.1.0 + Approved Errata 01 |
| `core/sync.py` | 已实现 / 可选转换 | Markdown copy；Pandoc 可选；HTML 可 Mistune fallback |
| `core/artifact_record.py` | 已实现项目契约 | source/derivative 身份 + assertion basis + audit coverage |
| `core/artifact_lineage.py` | 已实现项目契约 | typed artifact relation + non-inheritance boundary |
| `core/ro_crate.py` | 已实现核心 exporter | RO-Crate 1.3 JSON-LD；不声称外部 validator 成功 |
| `core/maintenance_cadence.py` | 已实现维护扫描器 | 只读本地 Daily / Weekly / Monthly 维护证据 |
| experimental modules | 实验性 | 有界独立模块，不接规范主链 |

## 数据绑定

```python
from core.renderer import DataBindingEngine

engine = DataBindingEngine()
context = engine.load_data("data/research.yaml", strict=True)
markdown = engine.render("paper_summary.j2", context)
```

支持 `.json`、`.csv`、`.yaml`、`.yml`

- `strict=False` 保留历史宽松行为
- `strict=True` 对缺文件、未知格式和非法顶层结构显式失败

## 科研元数据与过程披露

frontmatter 可声明 artifact ID、authors、sources、license、DOI、language、AI assistance、AI tool IDs、human review 与 disclosure reference

```text
ai_assistance: none | used | not_declared
human_review: reviewed | partial | not_reviewed | not_declared
```

未知信息保持 unknown / `not_declared`，不猜 provider、model、version、source 或 review 状态

```text
AI disclosure != 作者资格证明
AI tool label != 已验证 provider provenance
human review != peer review
过程元数据 != 科学有效性
```

仓库不会扫描正文再猜 AI 使用，artifact record 明确保留

```json
{"automatic_ai_detection_used": false}
```

## Assertion Basis

记录值与值进入记录的方式分开保存

常见 basis

```text
document-frontmatter
runtime-observed-local-bytes
runtime-observed-local-filesystem
caller-declared
```

```text
assertion basis != correctness
```

详见 [ASSERTION_BASIS_AND_COVERAGE.md](ASSERTION_BASIS_AND_COVERAGE.md)

## Portable Artifact Record

`auto-doc-engine/artifact-record` 填补 frontmatter 与更完整 Research Object package 之间的空白

它可以保留 source/derivative byte identity、有界 metadata、声明式 source/author refs、过程披露、frontmatter diagnostics、lineage refs、execution context、assertion basis、维度化 audit coverage 与项目内 R0–R3 reproducibility declaration

```bash
python core/artifact_record.py report.md \
  --derivative html=output/report.html \
  --generated-with auto-doc-engine/sync \
  --configuration-ref sync/targets.yaml \
  --reproducibility-level R1 \
  --output output/report.artifact.json
```

Artifact record 默认仍为 opt-in

## 维度化 Audit Coverage

```text
derivative_count
declared_source_references.total / by_resolution / local_file_ratio
lineage_references.total / by_resolution / local_file_ratio
process_disclosure_declared_fields
frontmatter_error_count
frontmatter_warning_count
```

并明确

```json
{"aggregate_score": null}
```

```text
local_file_ratio != 来源可信度
reference presence != citation validity
coverage != correctness
coverage ratio != probability
frontmatter clean != scientific validity
```

## Typed Artifact Lineage

`auto-doc-engine/artifact-lineage` 保存 artifact 代际之间的显式声明关系

```text
derived-from
revision-of
supersedes
uses
related-to
```

关系只允许 caller-declared，可对真实存在的本地目标计算 SHA-256

不会从文件名、时间戳、正文相似度、Git history 或模型输出中自动推断 lineage

每条 edge 都保留

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

详见 [ARTIFACT_LINEAGE_CONTRACT.md](ARTIFACT_LINEAGE_CONTRACT.md)

## Artifact Record / Lineage / RO-Crate

```text
auto-doc-engine/artifact-record
  单个 source/derivative set
        ↓ 可选关系
auto-doc-engine/artifact-lineage
  typed history/dependency handoff
        ↓ 可选打包
RO-Crate 1.3
  外部 linked-data Research Object packaging
```

项目 record 即使进入 crate，也只是普通项目 payload，不会被伪装成外部标准 profile

## R0–R3 可复现性语义

- **R0 Traceable**：来源/产物可关联
- **R1 Replay-addressable**：声明输入、配置、工具身份可定位预期 replay
- **R2 Environment-bounded**：关键环境/依赖边界被记录
- **R3 Reproduced**：真实发生独立 rerun，并按声明标准比较

metadata、hash、artifact record、lineage、RO-Crate 都不能自封 R3

## Daily / Weekly / Monthly 维护与文档权威

维护规则见 [MAINTENANCE_CADENCE.md](MAINTENANCE_CADENCE.md)

当前文档与历史快照的权威分类见 [DOCUMENT_STATUS.md](DOCUMENT_STATUS.md)

8 月阶段最终 baseline 见 [STAGE_2026_08_MAINTENANCE.md](STAGE_2026_08_MAINTENANCE.md)

```bash
python core/maintenance_cadence.py daily
python core/maintenance_cadence.py weekly
python core/maintenance_cadence.py monthly --as-of 2026-08-31
```

scanner 会根据日期和配置直接报告

```text
calendar_month: month-to-date | calendar-month-close
stage: not-started | active | closed
```

当前阶段已经正式关闭

```text
window: 2026-08-24 -> 2026-08-31
calendar_month: calendar-month-close
stage: closed
```

`FOUR_DAY_CONSOLIDATION.md`、`FIVE_DAY_CONSOLIDATION.md`、`SIX_DAY_CONSOLIDATION.md` 是 historical snapshots，不是当前 contract

## 阶段科研工程校准

2026-08-24 → 2026-08-31 阶段借鉴但不声称被以下工作认证

- autonomous science 的 re-openable provenance
- scientific publishing 的透明 AI 使用与 human oversight
- artifact-centered claim-aware observability
- trajectory-to-evidence qualification
- evidence-bounded claim review
- end-to-end scientific-agent consistency
- claim-level auditability / contradiction transparency
- long-horizon research phase behavior 与 regime-aware re-validation
- ScienceFlow-style persistent research segments / recovery
- beyond-final-score 的 long-horizon process evaluation
- Praxist solution/evidence lineage
- ReproAgent persistent implementation contracts
- reusable research-software metadata / maintenance

这些是 architecture calibration，不是仓库 validation、endorsement 或 novelty proof

详见 [FRONTIER_ALIGNMENT.md](FRONTIER_ALIGNMENT.md)

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

仓库之间不要求直接 import

## 科研完整性硬边界

```text
Provenance != Truth
Digest != 语义等价
Structural diff != 冲突解决
Assertion basis != correctness
Coverage != quality
Coverage ratio != probability
Artifact lineage != inherited validity
Declared source != 天然可信来源
Process disclosure != 作者资格裁定
Human review != Peer review
RO-Crate metadata != Reproduction
Maintenance clean != scientific validity
Calendar-month close != reproduction
Standard alignment != External certification
Experimental source != Integrated capability
```

`CITATION.cff` 使用 CFF 1.2.0，License 为 MIT
