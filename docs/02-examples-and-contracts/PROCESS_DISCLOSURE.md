> [!NOTE]
> **Current architecture interpretation — 2026-09-18**
> - **Subject class:** `CONTRACT`
> - **Role:** Current contract for explicit research-process disclosure
> - **Authority:** Current repository-native authority for the semantics explicitly owned by this file; current implementation and machine contracts remain the factual boundary for executable behavior
> - **Current meaning:** Read this subject as part of the `artifact identity → lineage/assertion basis → downstream claim/evidence handoff` architecture. It defines inspectable structure and provenance semantics without elevating generated documentation into scientific truth
> - **Evidence / implementation boundary:** Artifact identity is not semantic equivalence; lineage is caller-declared and does not inherit validity; assertion basis is not correctness; coverage is not quality or probability; process disclosure is not authorship proof; RO-Crate packaging is not reproduction
> - **Cross-document relation:** Architecture explains the integrated system; specialized contracts own their exact handoff vocabularies; current code and machine contracts bound implementation; `DOCUMENT_STATUS.md` routes current versus historical documentation
> - **Update trigger:** Update only when the owned architecture/contract semantics or implemented mechanics materially change, or when a confirmed current-authority conflict appears
> - **Preservation rule:** Existing technical explanation and stage-calibration material remains in place. Dated stage-close statements retain their historical scope and are not rewritten into current execution claims

# Research Process Disclosure — auto-doc-engine

## 中文技术对应 / Chinese technical reading

**实际对象 / Owning subject:** 模型工具、版本、输入来源、人工评审与生产披露必须如实记录，填写披露不等于同行评审或科学真实性

**English document title:** Research Process Disclosure — auto-doc-engine

**运行与证据区分 / Evidence distinction:** 需要明确 producer/consumer 的 profile、源码版本、输入/sidecar bytes、实际命令与失败状态，静态参考与交付示例不能冒充真实三仓联调或外部科学验真 / Preserve exact source revision, profile, source bytes, commands and failures, a documentary contract is not a run receipt

| Source heading / 英文拥有者章节 | 中文阅读归属 / Chinese meaning |
| --- | --- |
| Purpose | 目标 |
| Assertion basis | 当前工程合同及其具体边界 |
| Field semantics | 当前工程合同及其具体边界 |
| Validation behavior | 当前工程合同及其具体边界 |
| Cross-repository process handoff | 当前工程合同及其具体边界 |
| Maintenance and document authority | 当前工程合同及其具体边界 |
| Scientific and authorship boundaries | 当前工程合同及其具体边界 |
| External calibration | 当前工程合同及其具体边界 |
| Disclosure is a provenance statement, not an AI detector | 当前工程合同及其具体边界 |

**保留 / Preservation:** 原始英文合同字段、sample payload、历史 Stage 和运行未知状态不被本翻译改变 / Source technical semantics and dated evidence are preserved


**Calibration:** 2026-08-31  
**Status:** implemented frontmatter sub-contract; project-owned vocabulary, not an external publishing standard

## Purpose

A research artifact should be able to preserve explicit process context without pretending that metadata can decide authorship, truth, originality, peer review, or publisher compliance

Supported optional frontmatter

```yaml
ai_assistance: used
ai_tools:
  - provider/model or tool identifier declared by the author
human_review: reviewed
disclosure_ref: path-or-URI-to-a-fuller-disclosure
```

These fields are declarations. They are not inferred from document prose

## Assertion basis

When these fields enter an artifact record, their basis is

```text
document-frontmatter
```

The record also states

```json
{"automatic_ai_detection_used": false}
```

```text
explicit disclosure != AI-content detection
AI-content detection != authorship adjudication
assertion basis != truth
```

The repository does not run an AI-text detector, guess a provider/model from writing style, or infer that missing disclosure means no AI was used

## Field semantics

### `ai_assistance`

```text
none
used
not_declared
```

- `none`: the artifact explicitly declares no AI assistance for the described process
- `used`: AI assistance was declared
- `not_declared`: no claim is made either way

Absence is not converted to `none`

### `ai_tools`

Human-readable tool/model/provider identifiers supplied by the artifact author or producing system. The repository does not verify them against a vendor registry

### `human_review`

```text
reviewed
partial
not_reviewed
not_declared
```

This is declared artifact review state only

```text
reviewed != peer reviewed
reviewed != expert validation
reviewed != scientific approval
```

### `disclosure_ref`

Optional local path or URI to a fuller disclosure/methods/run record. The artifact-record layer may hash a local file; remote/opaque references are not automatically dereferenced or certified

## Validation behavior

Invalid field types/enums are errors. Cross-field incompleteness is warning-level for compatibility

- `ai_assistance: used` without usable `ai_tools` -> warning
- declared `ai_tools` while `ai_assistance` is absent/`none`/`not_declared` -> warning

A warning or clean frontmatter result is not a scientific judgment

## Cross-repository process handoff

```text
auto-doc-engine
  document-frontmatter process disclosure
        ↓
epistemic-pipeline
  provider-adapter + caller-declared process context
        ↓
sci-render-kit
  recipe-declared communication/process context
```

Each repository preserves how process metadata entered its own evidence object

None inherits authorship, peer-review, or scientific-validity claims from another

## Maintenance and document authority

This is a current authoritative specialized contract under `DOCUMENT_STATUS.md`

Daily/weekly/monthly maintenance may reconcile vocabulary and cross-repository names, but it must not infer missing disclosure or rewrite historical process declarations merely because later policy wording changes

The August stage closed on 2026-08-31. Calendar/stage closure does not convert process disclosure into authorship, peer review, or publisher compliance

## Scientific and authorship boundaries

```text
AI disclosure != authorship adjudication
AI tool identity != model provenance proof
AI disclosure != AI-text detection
human review != peer review
human review != truth
process metadata != scientific validity
process metadata != publisher compliance
maintenance clean != publisher compliance
```

## External calibration

Current scientific-publishing discussions increasingly ask for transparent disclosure and accountability. Separately, AI-content detection remains an inference/classification problem with its own uncertainty and failure modes

This repository chooses the narrower mechanism it can represent honestly: explicit declarations plus their assertion basis

Calibration signals include work on responsible/transparent AI use in scientific publishing, provenance-grounded autonomous science, artifact-centered claim-aware observability, and reporting on AI-detection limitations

These sources motivate transparency and auditability. They do not define or certify this project-owned vocabulary

## Disclosure is a provenance statement, not an AI detector

`core/artifact_record.py::_process_disclosure` sets `automatic_ai_detection_used=False` and `basis_inferred=False`. Values such as `ai_assistance`, `ai_tools`, `human_review` and `disclosure_ref` are collected from source frontmatter. They record **what the source declares**; they do not authenticate the producer, independently infer AI use, certify reviewer identity, or prove that a peer-review procedure happened.

A strong review claim therefore needs separate evidence: who reviewed, the exact source/derivative revision, scope of review, criteria and independently retained disposition. A disclosure that a human reviewed something is still compatible with an untested mathematical theorem or unverified external reference.

**Counterexample:** two artifact files declare identical `human_review` metadata, but only one has a verifiable signed/linked review record. The current artifact-record code treats their declarations equivalently at this field layer; do not infer equal real-world review strength. A later authenticated receipt can update current interpretation while keeping the original declaration traceable.
