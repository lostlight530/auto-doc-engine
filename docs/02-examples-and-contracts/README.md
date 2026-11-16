# 02 — Examples and Contracts

## 中文技术对应 / Chinese technical reading

**实际对象 / Owning subject:** 本目录集中记录合同与案例及交付边界，不将 profile 名称或 schema 通过视为已经完成科学验证

**English document title:** 02 — Examples and Contracts

**运行与证据区分 / Evidence distinction:** 需要明确 producer/consumer 的 profile、源码版本、输入/sidecar bytes、实际命令与失败状态，静态参考与交付示例不能冒充真实三仓联调或外部科学验真 / Preserve exact source revision, profile, source bytes, commands and failures, a documentary contract is not a run receipt

| Source heading / 英文拥有者章节 | 中文阅读归属 / Chinese meaning |
| --- | --- |
| Machine and capability surfaces | 机器与能力表面 |
| Active contracts | 现行合同 |
| Cross-repository handoff | 当前工程合同及其具体边界 |
| Operator and contribution guidance | 当前工程合同及其具体边界 |
| Scholarly metadata | 当前工程合同及其具体边界 |
| Reading path | 当前工程合同及其具体边界 |

**保留 / Preservation:** 原始英文合同字段、sample payload、历史 Stage 和运行未知状态不被本翻译改变 / Source technical semantics and dated evidence are preserved


This class answers: **how are auto-doc-engine outputs represented, constrained, interpreted, and handed to other research-infrastructure layers?**

## Machine and capability surfaces

- root `MANIFEST.yaml` — machine-readable capability map; it describes declared current capability, not execution success.
- `sync/targets.yaml` — declared synchronization targets/configuration.
- `examples/` — worked examples of supported shapes and workflows; examples do not create capability absent from implementation or active contracts.

## Active contracts

### [`RESEARCH_CONTRACT.md`](./RESEARCH_CONTRACT.md)

Repository-level research/integrity semantics and the strongest claims the current implementation can support. Start here when a field or artifact is being interpreted scientifically rather than merely parsed.

### [`ARTIFACT_RECORD.md`](./ARTIFACT_RECORD.md)

Defines the repository-owned artifact-record object: identity, declared fields, references, digests, and bounded provenance. An artifact record describes an artifact; it is not peer review or truth certification.

### [`ARTIFACT_LINEAGE_CONTRACT.md`](./ARTIFACT_LINEAGE_CONTRACT.md)

Defines explicit lineage relations such as `derived-from`, `revision-of`, `supersedes`, `uses`, and `related-to`.

Lineage must be declared or otherwise supported by the owning contract. It must not be inferred merely from filenames, timestamps, Git adjacency, prose similarity, or model output.

```text
lineage relation
!= semantic equivalence
!= inherited scientific validity
```

### [`ASSERTION_BASIS_AND_COVERAGE.md`](./ASSERTION_BASIS_AND_COVERAGE.md)

Separates the value of a field from **how that value entered the record**, and separates dimensional coverage from correctness or evidence sufficiency.

```text
assertion basis != correctness
coverage != quality
coverage ratio != probability
```

### [`PROCESS_DISCLOSURE.md`](./PROCESS_DISCLOSURE.md)

Defines bounded disclosure of how an artifact/process was produced or reviewed. Process metadata supports inspectability; it does not adjudicate authorship, prove semantic correctness, or convert human review into peer review.

### [ARTIFACT_IDENTITY_NEGATIVE_CASES.md](./ARTIFACT_IDENTITY_NEGATIVE_CASES.md)

Source-grounded counterexamples for caller-declared R3, byte-versus-metadata identity, typed lineage relations and RO-Crate packaging, with unexecuted fixture boundaries

**This is a durable research-method casebook, not an executed test log or historical maintenance account**

## Cross-repository handoff

auto-doc-engine is the document/artifact identity layer in the three-repository research-infrastructure chain:

```text
artifact record / lineage / assertion basis
        ↓
epistemic-pipeline claim/evidence processing
        ↓
sci-render-kit scientific communication
```

Downstream consumers must not silently strengthen an upstream reference. A digest, lineage edge, source reference, or process disclosure remains bounded by the semantics defined here.

## Operator and contribution guidance

- root `AGENTS.md` — repository-owned operational guidance.
- root `CONTRIBUTING.md` — public contribution contract.
- `examples/` — inspectable examples for current supported formats.

These help users operate the repository but do not outrank implementation, `MANIFEST.yaml`, or the active subject-specific contract.


### [INTEROPERABILITY_VERIFICATION.md](./INTEROPERABILITY_VERIFICATION.md)

Current producer/consumer fixture scope, Python environment pins, CodeMeta 4 migration boundaries, and (where applicable) failure injection or offline renderer verification — evidence of a test is separate from its execution

## Scholarly metadata

- root `CITATION.cff`
- root `codemeta.json`
- root `RELEASE_POLICY.md`
- root `LICENSE`

The repository DOI identifies an archived software publication. It does not self-award artifact validity, semantic equivalence, scientific truth, or R3 independent reproduction.

## Reading path

For a new integration or research object:

1. identify the owning implementation/capability in source and `MANIFEST.yaml`;
2. read `RESEARCH_CONTRACT.md` for repository-wide scientific/integrity boundaries;
3. read the specialized contract for the object being produced;
4. inspect `examples/` for supported representation;
5. retain revision-matched execution evidence when claiming that generation/validation actually ran.

Current explanatory architecture lives under [`../01-source-and-explanation/`](../01-source-and-explanation/). Maintenance/audit material under class 03 is a separate operational/history layer, not the primary artifact semantics.
