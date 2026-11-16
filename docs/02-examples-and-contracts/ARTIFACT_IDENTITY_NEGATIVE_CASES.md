# Artifact identity and lineage — source-derived negative cases

## 中文技术对应 / Chinese technical reading

**实际对象 / Owning subject:** 反例区分相同字节与不同 metadata、原始 sidecar 与哈希、lineage 关系与 R3 复现，文档案例不等于已执行测试

**English document title:** Artifact identity and lineage — source-derived negative cases

**运行与证据区分 / Evidence distinction:** 需要明确 producer/consumer 的 profile、源码版本、输入/sidecar bytes、实际命令与失败状态，静态参考与交付示例不能冒充真实三仓联调或外部科学验真 / Preserve exact source revision, profile, source bytes, commands and failures, a documentary contract is not a run receipt

| Source heading / 英文拥有者章节 | 中文阅读归属 / Chinese meaning |
| --- | --- |
| Unit of analysis | 当前工程合同及其具体边界 |
| Falsification cases | 当前工程合同及其具体边界 |
| Evidence collection protocol | 当前工程合同及其具体边界 |

**保留 / Preservation:** 原始英文合同字段、sample payload、历史 Stage 和运行未知状态不被本翻译改变 / Source technical semantics and dated evidence are preserved


**Document class:** durable specialized research method, not a status report  
**Source baseline:** `main@bb21be87f0ccc62245a01fbacb05cc70a53340f9`, inspected 2026-11-15  
**Owners:** [Artifact Record](./ARTIFACT_RECORD.md), [Artifact Lineage](./ARTIFACT_LINEAGE_CONTRACT.md), [Assertion Basis and Coverage](./ASSERTION_BASIS_AND_COVERAGE.md)  
**Implementation:** `core/artifact_record.py`, `core/artifact_lineage.py`, `core/ro_crate.py`

## Unit of analysis

The local code builds one source-artifact record from concrete file bytes, document-declared frontmatter, optional caller-supplied reference fields, and selected generated derivatives

```text
local source bytes --------> file_sha256                      [locally observed bytes]
frontmatter ---------------> metadata_canonical_sha256       [selected declared fields]
caller-supplied links -----> declared lineage and disclosure [declarations, not truth]
artifact record + links ---> lineage sidecar                 [typed relation graph]
payload files -------------> RO-Crate JSON-LD               [packaging, not certification]
```

Neither one local hash nor an external reference string proves the referenced proposition, authorship, peer review, independent reproduction or the semantics of a derived document

## Falsification cases

| ID | Controlled input and change | Source owner | Supportable outcome / excluded inference |
| --- | --- | --- | --- |
| A-1 | Pass `reproducibility_level="R3"` without a rerun | `artifact_record.py::build_artifact_record` | The function accepts caller-declared R3 metadata, but performs no independent reproduction |
| A-2 | Modify document body but keep selected frontmatter values unchanged | `file_sha256` and `canonical_sha256(core_metadata)` | Source-byte hash changes, metadata hash can remain identical |
| A-3 | Declare an opaque HTTP reference | `artifact_record.py::_reference` | External location may be recorded, but this call does not fetch and verify its claim |
| A-4 | Supply duplicate `("uses","x")` twice and `("supersedes","x")` once | `artifact_lineage.py::build_artifact_lineage` | Deduplication is by exact relation–target tuple, not target alone |
| A-5 | Reference the lineage record's source artifact-record sidecar itself | local `Path.resolve()` self-target check | Self-reference is rejected, but general cycles/transitive validity are not checked |
| A-6 | Export files using `ro_crate.py::build_ro_crate` | RO-Crate exporter | JSON-LD packaging and digest representation, not external certification or scientific validity |

## Evidence collection protocol

Use a temporary fixture directory and retain source Git SHA, Python environment, source bytes, frontmatter, arguments, sidecar digests, actual return values, exceptions, and unchanged inputs after rejected writes

Compare `source_artifact.file_sha256` against `record_identity.metadata_canonical_sha256` as different objects and require a separate rerun receipt before interpreting any R3 declaration as reproduced

**Execution status:** source pathways and existing regression test definitions read, new fixtures `NOT_EXECUTED`, external scientific adjudication `NOT_PERFORMED`

This companion adds no new code behavior, record fields, implicit lineage, or revised historical execution status
