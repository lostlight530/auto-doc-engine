# Research Contract — auto-doc-engine

**Calibration:** 2026-08-26  
**Status:** active repository contract for evidence, provenance, process disclosure, reproducibility and research-object claims

This contract defines what repository artifacts can and cannot establish. It is an architectural/scientific-integrity contract, not a GitHub merge policy.

## 1. Role in the three-repository toolchain

`auto-doc-engine` is the **document and evidence-packaging plane**:

```text
structured source
    -> document binding
    -> typed document structure
    -> structural-change evidence
    -> document graph / metadata diagnostics
    -> artifact process disclosure
    -> rendered artifacts
    -> optional interoperability packaging
```

It does not determine scientific truth, calibrate probabilities, adjudicate authorship, resolve arbitrary human-edit conflicts, or prove independent reproducibility.

## 2. Evidence unit

When available, a document/artifact record SHOULD preserve:

```text
artifact_id
source_refs[]
content_sha256
generated_with
configuration_ref
document_status
provenance_ref
validation_status
reproducibility_level
ai_assistance
ai_tools[]
human_review
disclosure_ref
```

A SHA-256 digest establishes byte identity under the declared algorithm. It does not establish semantic equivalence, correctness, authorship, novelty or scientific validity.

Process-disclosure fields describe the artifact's declared production/review context. They do not establish that the declaration is complete or that a named tool produced a specific sentence.

## 3. Current implemented boundary

### Integrated

- JSON / CSV / YAML data binding through Jinja2;
- Mistune-backed typed Markdown AST for the declared node subset;
- structural add/modify/delete/unchanged reporting;
- atomic bounded structural-generation history;
- document/heading reference graph and local-link diagnostics;
- bounded research frontmatter metadata;
- optional artifact-level AI-assistance / tool / human-review / disclosure metadata;
- descriptive readability metrics;
- aggregate Doctor profile with Text/JSON output;
- SARIF 2.1.0 + Approved Errata 01 result export;
- cross-platform Markdown synchronization;
- optional Pandoc-backed format conversion;
- RO-Crate 1.3 core metadata export for successful local artifact sets.

### Explicitly not established

- semantic diff / semantic equivalence;
- conflict-free collaborative merging;
- immutable or tamper-proof provenance ledger;
- SQLite / network API adapters;
- universal format availability;
- external RO-Crate validator certification;
- AI-generated-text detection;
- automatic authorship adjudication;
- automatic publisher-policy compliance;
- automatic peer review;
- automatic scientific-validity assessment;
- independent reproduction solely from generated metadata.

## 4. Document-structure semantics

The AST layer is a normalized structural representation. Parse/render behavior preserves the supported structure but is not byte-for-byte source preservation.

`ASTNode.signature` and incremental subtree identities use SHA-256 as local identity evidence. Hash equality over the selected representation does not prove semantic equivalence outside that representation.

## 5. Structural-change semantics

The incremental engine aligns sibling subtree identities and emits:

```text
add | modify | delete | unchanged
```

It is a **change detector**. It does not apply changes, negotiate ownership, resolve conflicts or provide CRDT/OT semantics.

The generation-history file is bounded and written by atomic replacement. Atomic file replacement improves interrupted-write behavior; it does not make the history append-only or tamper-proof.

## 6. Research metadata and process-disclosure semantics

`core/frontmatter.py` exposes a deliberately small metadata contract.

Research/document fields include:

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

Process-disclosure fields include:

```text
ai_assistance
ai_tools[]
human_review
disclosure_ref
```

`ai_assistance` values:

```text
none | used | not_declared
```

`human_review` values:

```text
reviewed | partial | not_reviewed | not_declared
```

Invalid field types/enums are errors. Incomplete cross-field disclosure is warning-level so historical documents can remain readable while the inconsistency is visible.

Examples:

- `ai_assistance: used` with no usable `ai_tools` entry -> warning;
- non-empty `ai_tools` while AI assistance is missing/`none`/`not_declared` -> warning.

These values are **declarations about process**, not verification outcomes.

```text
AI disclosure != authorship adjudication
AI tool identity != provenance proof
human review != peer review
human review != scientific truth
process metadata != publisher compliance
```

Detailed semantics live in `PROCESS_DISCLOSURE.md`.

## 7. Diagnostic semantics

`auto-doc-engine/doctor@1` aggregates document-set diagnostics. Error/warning severity controls the command's local status only.

A diagnostic pass can establish that implemented predicates were evaluated over the inspected files. It cannot establish:

- factual correctness of the prose;
- completeness/truth of process disclosure;
- quality of scientific reasoning;
- accessibility of a final publication;
- acceptance by a journal or reviewer.

Readability values are descriptive heuristics. Near-miss links are lexical hints.

## 8. SARIF semantics

`auto-doc-engine/sarif@1` targets OASIS SARIF 2.1.0 incorporating Approved Errata 01.

Stable finding identity uses namespaced rule IDs and `autoDocFinding/v1` partial fingerprints. A downstream tool successfully parsing the file is interoperability evidence, not certification of the repository's scientific claims.

## 9. RO-Crate 1.3 implementation profile

RO-Crate 1.3 was published on 2026-06-22 and is the current long-term release observed for this calibration.

The repository implements `auto-doc-engine/ro-crate@1` through `core/ro_crate.py`.

Current profile emits:

- `ro-crate-metadata.json` metadata descriptor as `CreativeWork`;
- `conformsTo` reference to the RO-Crate 1.3 base specification;
- `about` reference to root `./`;
- root `Dataset`;
- local payload `File` entities;
- `hasPart` relationships;
- optional `Person` author contextual entities;
- `contentSize` and `encodingFormat`;
- SHA-256 byte identity through Schema.org `PropertyValue` entities.

The project profile name is documented in repository metadata rather than injected as an undefined property into the RO-Crate JSON-LD context.

The new process-disclosure frontmatter fields are **not automatically asserted as RO-Crate standard properties by the current writer**. They remain project metadata unless a future explicit mapping is implemented.

**Not claimed:** external validator success, full coverage of every optional RO-Crate recommendation, workflow-run profile conformance, publisher compliance, or scientific reproducibility.

## 10. Reproducibility levels

These are **local project terms**, not an external standard:

- **R0 — Traceable:** source/artifact identity metadata is recorded.
- **R1 — Replay-addressable:** inputs, configuration, tool revision and intended command/path are sufficient to address the intended replay.
- **R2 — Environment-bounded:** relevant runtime/dependency/external-tool assumptions are also recorded.
- **R3 — Reproduced:** a separate rerun has actually happened and its result was compared under a declared acceptance criterion.

No manifest, checksum, SARIF report, provenance sidecar, process disclosure or RO-Crate metadata file may be used alone to label an artifact R3.

## 11. Cross-repository handoff

Preferred handoff fields to `epistemic-pipeline` or `sci-render-kit`:

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

The repositories remain loosely coupled. This contract does not require direct imports or network calls between them.

`epistemic-pipeline/evidence-envelope@2` may preserve the downstream run/provider/claim audit context; `sci-render-kit/figure-evidence@2` may preserve figure communication/process context. Auto Doc does not need to import either repository for these handoffs to remain meaningful.

If an upstream record contains a confidence value, its `confidence_semantics` must travel with it. `auto-doc-engine` must not silently reinterpret a heuristic value as calibrated probability.

## 12. Experimental-module rule

The following remain Experimental even after this refresh:

- `template_prewarm.py`
- `async_conduit.py`
- `memory_lattice.py`
- `restart_protocol.py`
- `self_observe.py`

Fixing internal bugs or clarifying semantics does not automatically promote them into the integrated architecture.

## 13. 2026-08-26 research alignment

Recent research and editorial signals strengthen the case for artifact-level audit context without defining this project's vocabulary:

- *Provenance grounds trust in autonomous science* emphasizes complete, re-openable records for correction and audit;
- *Responsible and transparent use of AI in scientific publishing* emphasizes transparency, accountability and human oversight;
- *Artifact-centered Claim-aware Observability for Autonomous Scientific Agents* argues that model-call logs alone are insufficient and that artifact/claim relations need portable audit semantics;
- *EarthVerse* evaluates package-scoped scientific investigations and highlights the gap between local answer-unit success and end-to-end consistency across evidence, calculations and interpretation.

The repository responds at its own layer: make artifact identity, source context and declared production/review metadata portable without claiming that metadata can adjudicate the science.

## 14. External observations

Standards/dependency observations retained from the 2026-08-23 calibration:

- RO-Crate 1.3 — current long-term release, published 2026-06-22;
- SARIF 2.1.0 + Approved Errata 01 — current target profile;
- Mistune 3.3.4 — observed current; repository floor remains `>=3.2.1`;
- Pandoc 3.10.2 — observed current; optional external dependency;
- Citation File Format 1.2.0 — citation metadata format.

Observation is ecosystem evidence, not compatibility proof.

## 15. Shared scientific-integrity rules

1. Provenance is not truth.
2. Hash identity is not semantic equivalence.
3. Structure is not meaning.
4. Process disclosure is not authorship adjudication.
5. Human review is not peer review or scientific validity.
6. Diagnostic success is not peer review.
7. Metadata is not independent reproduction.
8. Standard alignment is not external certification.
9. Optional dependencies must fail explicitly when unavailable.
10. Experimental code is not integrated capability merely because it exists.
11. GitHub-native CI/merge gating is not part of this repository's scientific architecture.

## 16. Primary references

Retrieved/calibrated through 2026-08-26:

- RO-Crate 1.3 specification: https://www.researchobject.org/ro-crate/specification/1.3/
- OASIS SARIF 2.1.0 + Errata 01: https://docs.oasis-open.org/sarif/sarif/v2.1.0/errata01/os/sarif-v2.1.0-errata01-os-complete.html
- FAIR R1.2 provenance principle: https://www.go-fair.org/fair-principles/r1-2-metadata-associated-detailed-provenance/
- Nature Computational Science, *Provenance grounds trust in autonomous science*: https://www.nature.com/articles/s43588-026-01035-4
- Nature Computational Science, *Responsible and transparent use of AI in scientific publishing*: https://www.nature.com/articles/s43588-026-01043-4
- *Artifact-centered Claim-aware Observability for Autonomous Scientific Agents*: https://arxiv.org/abs/2608.18312
- *EarthVerse: Benchmarking Scientific Agents Across Dynamic Earth Systems and Natural Hazards*: https://arxiv.org/abs/2608.23525
- Mistune: https://pypi.org/project/mistune/
- Pandoc releases: https://github.com/jgm/pandoc/releases
- Citation File Format 1.2.0: https://citation-file-format.github.io/
