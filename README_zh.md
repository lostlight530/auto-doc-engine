# auto-doc-engine

> AST 驱动的科研文档编译、结构差异证据、有界过程元数据、轻量 artifact record、维度化审计覆盖、SARIF 交换与可选 RO-Crate 1.3 打包

[English](README.md) · [架构](ARCHITECTURE_zh.md) · [科研契约](RESEARCH_CONTRACT.md) · [Artifact Record](ARTIFACT_RECORD.md) · [Assertion Basis & Coverage](ASSERTION_BASIS_AND_COVERAGE.md) · [过程披露](PROCESS_DISCLOSURE.md) · [五日总整合](FIVE_DAY_CONSOLIDATION.md) · [示例](examples/README_zh.md)

## 当前定位

`auto-doc-engine` 把科研文档当成**可检查、可追踪、可交接的研究产物**，而不是一段字符串或只有最终 PDF 才算产物

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
可选 RO-Crate 1.3 packaging
```

仓库优化的是：**身份、可检查性、失败显式、跨工具 handoff**

它不声称自动科学真值判断、自动无冲突合并、来源可信度裁定、作者资格裁定、同行评审、外部 RO-Crate 认证、Run Crate conformance、publisher policy 合规或仅靠 metadata 完成独立复现

## 稳定项目标识

```text
auto-doc-engine/doctor
auto-doc-engine/sarif
auto-doc-engine/artifact-record
auto-doc-engine/process-disclosure
auto-doc-engine/frontmatter-validation
auto-doc-engine/ro-crate
autoDocFinding
```

这些项目内部标识不使用装饰性的 `@1/@2` 或 `/v1` 后缀

真实外部标准和真实运行环境版本继续保留，例如 RO-Crate 1.3、SARIF 2.1.0 + Approved Errata 01、CFF 1.2.0，以及真正观测到的软件版本

## 能力矩阵

| 能力 | 状态 | 当前边界 |
|---|---|---|
| `core/renderer.py` | 已实现 | Jinja2 + JSON/CSV/YAML/YML；SQLite/网络 API 未集成 |
| `core/ast_engine.py` | 已实现 | Typed AST；规范化结构渲染，不承诺字节级 round-trip |
| `core/incremental.py` | 已实现 | add/modify/delete/unchanged 结构证据；不是 merge engine |
| `core/cross_ref.py` | 已实现 | 本地 Markdown 图与 dangling/near-miss 诊断 |
| `core/frontmatter.py` | 已实现 | 有界科研元数据 + 声明式过程披露 |
| `core/readability.py` | 已实现 | 描述性启发式，不是写作质量/peer-review 评分 |
| `core/doctor.py` | 已实现 | 文档诊断 + 本地退出状态 |
| `core/sarif.py` | 已实现 | SARIF 2.1.0 + Approved Errata 01 |
| `core/sync.py` | 已实现 / 可选转换 | Markdown copy；Pandoc 可选；HTML 可 Mistune fallback |
| `core/artifact_record.py` | 已实现项目契约 | 源/derivative 身份 + assertion basis + 维度化 audit coverage |
| `core/ro_crate.py` | 已实现核心 exporter | RO-Crate 1.3 JSON-LD；不声称外部 validator 成功 |
| experimental modules | 实验性 | 有界独立模块，不接规范主链 |

## 数据绑定

```python
from core.renderer import DataBindingEngine

engine = DataBindingEngine()
context = engine.load_data("data/research.yaml", strict=True)
markdown = engine.render("paper_summary.j2", context)
```

支持 `.json`、`.csv`、`.yaml`、`.yml`

- `strict=False`：保留历史宽松行为
- `strict=True`：缺文件、未知格式、非法顶层结构显式失败

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

仓库不会扫描正文再猜“是否由 AI 写作”，artifact record 明确记录：

```json
{"automatic_ai_detection_used": false}
```

## Assertion Basis：字段是怎么来的

第五天开始把“字段值”和“字段来源方式”分开记录

当前 artifact-record 常见 basis：

```text
document-frontmatter
runtime-observed-local-bytes
runtime-observed-local-filesystem
caller-declared
```

例如：

```text
document metadata
  -> document-frontmatter

source / derivative SHA-256
  -> runtime-observed-local-bytes

generated_with
  -> caller-declared（如果调用方提供）
```

**basis 只是“这个值如何进入记录”的 provenance，不证明这个值正确**

详见 [ASSERTION_BASIS_AND_COVERAGE.md](ASSERTION_BASIS_AND_COVERAGE.md)

## Portable Artifact Record

`auto-doc-engine/artifact-record` 填补 frontmatter 与完整 Research Object package 之间的空白

它可以保留 source/derivative byte identity、有界 metadata、声明式 source/author refs、过程披露、frontmatter diagnostics、lineage refs、execution context、assertion basis、维度化 audit coverage 与项目内 R0–R3 reproducibility declaration

```bash
python core/artifact_record.py report.md \
  --derivative html=output/report.html \
  --generated-with auto-doc-engine/sync \
  --configuration-ref sync/targets.yaml \
  --reproducibility-level R1 \
  --output output/report.artifact.json
```

也可以：

```python
from core.sync import SyncEngine

results = SyncEngine().sync_with_fallback(
    "report.md",
    targets=["markdown", "html"],
    output_dir="output",
    emit_artifact_record=True,
)
```

Artifact record 默认仍为 opt-in

## 维度化 Audit Coverage

artifact record 不输出“科研质量总分”，而是把可复核维度分开：

```text
derivative_count
declared_source_references.total / by_resolution / local_file_ratio
lineage_references.total / by_resolution / local_file_ratio
process_disclosure_declared_fields
frontmatter_error_count
frontmatter_warning_count
```

并且明确：

```json
{"aggregate_score": null}
```

解释边界：

```text
local_file_ratio != 来源可信度
reference presence != citation validity
coverage != correctness
coverage ratio != probability
frontmatter clean != scientific validity
```

## Artifact Record 与 RO-Crate

```text
auto-doc-engine/artifact-record
  = 单个 source/derivative set 的轻量项目 handoff

RO-Crate 1.3
  = 更完整 Research Object 的外部 linked-data packaging
```

如果两者同时开启，artifact record 可以作为普通 File payload 被放入 crate，但不会被伪装成 RO-Crate 自带标准 profile

## Doctor 与 SARIF

```bash
python core/doctor.py path/to/docs
python core/doctor.py path/to/docs --json
python core/sarif.py path/to/docs -o output/doctor.sarif
```

Doctor 只证明声明的结构/元数据 predicates 被执行，不证明事实正确、来源可信、peer review 或科学有效性

SARIF 是标准化 findings 容器，下游能读取不等于认证科研结论

## 多格式同步

环境边界：

- Markdown：Python stdlib copy
- HTML：Pandoc 可用时走 Pandoc，否则可 Mistune fallback
- DOCX / EPUB：Pandoc
- PDF：Pandoc + 声明的 PDF engine
- 外部 converter 可用性必须显式，不猜测

## RO-Crate 1.3

`core/ro_crate.py` 可生成保守的 core RO-Crate metadata，包括 metadata descriptor、root Dataset、File、Person、content size/media type 与 SHA-256 PropertyValue

```text
生成 RO-Crate != 外部 validator 已通过
RO-Crate metadata != 独立复现
RO-Crate packaging != 科学有效性
```

## R0–R3 可复现性语义

- **R0 Traceable**：来源/产物可关联
- **R1 Replay-addressable**：声明输入、配置、工具身份可定位预期 replay
- **R2 Environment-bounded**：关键环境/依赖边界也被记录
- **R3 Reproduced**：已经真实发生独立 rerun，并按声明标准比较

metadata 生成本身不能自封 R3

## 五日全球科研工程校准

2026-08-24 → 2026-08-28 的整合借鉴但不声称被以下工作认证：

- autonomous science 对完整、可重新打开 provenance 的要求
- scientific publishing 对透明 AI 使用、accountability、human oversight 的要求
- artifact-centered claim-aware observability
- trajectory-to-evidence conversion
- Brain Researcher 的 evidence-bounded claim review
- EarthVerse 的端到端 scientific consistency 评测
- claim-level auditability 对 provenance coverage / contradiction transparency 的强调
- 近期 AI-text detection 报道对“检测”和“主动披露”两种机制的区分
- RO-Crate 1.3 与 workflow-run provenance profiles 的互操作思路

我们只实现仓库真正能证明的结构层，不自称 provenance soundness、source credibility scoring、scientific-review authority 或 AI-content detection

详见 [FIVE_DAY_CONSOLIDATION.md](FIVE_DAY_CONSOLIDATION.md)

## 三仓 handoff

```text
auto-doc-engine/artifact-record
  assertion basis + artifact coverage
        ↓ 可选引用
epistemic-pipeline/claim-verification
epistemic-pipeline/evidence-envelope
        ↓ 可选引用
sci-render-kit/figure-claim-audit
sci-render-kit/figure-evidence
```

仓库之间不要求直接 import

## 实验区

- `template_prewarm.py`：bounded in-memory LRU
- `async_conduit.py`：bounded priority/concurrency scheduler
- `memory_lattice.py`：local node/link store + numeric bucket index
- `restart_protocol.py`：event replay + result-hash verification
- `self_observe.py`：显式 instrumentation + 描述性 timing

历史隐喻命名不等于能力事实

## 科研完整性硬边界

```text
Provenance != Truth
Digest != 语义等价
Structural diff != 冲突解决
Assertion basis != correctness
Coverage != quality
Coverage ratio != probability
Declared source != 天然可信来源
Artifact record != 外部 Research Object 标准
Process disclosure != 作者资格裁定
Human review != Peer review
RO-Crate metadata != Reproduction
Standard alignment != External certification
Experimental source != Integrated capability
```

## 本地维护

本地检查可以按需手动运行，但不是 GitHub Actions、branch protection、merge gate、peer review 或科学验证；本轮整合不把测试执行当完成证据

`CITATION.cff` 使用 CFF 1.2.0，License 为 MIT
