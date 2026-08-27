# Research Contract — auto-doc-engine

**Calibration:** 2026-08-27  
**Status:** active repository contract for document evidence, artifact records, process disclosure, provenance, reproducibility and Research Object packaging

This contract defines what repository artifacts can and cannot establish. It is an architectural/scientific-integrity contract, not GitHub merge policy.

## 1. Role in the three-repository toolchain

`auto-doc-engine` is the **research-artifact / document-evidence plane**:

```text
structured source
    -> document binding
    -> typed document structure
    -> structural-change evidence
    -> document graph / metadata diagnostics
    -> process disclosure
    -> rendered derivatives
    -> optional artifact-record@1
    -> optional RO-Crate 1.3 packaging
```

It does not determine scientific truth, source credibility, authorship, peer-review status, calibrated probability, journal acceptance, or independent reproducibility.

## 2. Evidence-unit model

The repository now has three different metadata/evidence surfaces.

### 2.1 In-document frontmatter

Frontmatter describes the document's own bounded metadata and declared process context.

Typical fields:

```text
artifact_id
authors[]
sources[]
status
license
doi
language
ai_assistance
ai_tools[]
human_review
disclosure_ref
```

### 2.2 Portable artifact record

`auto-doc-engine/artifact-record@1` binds one source document to concrete bytes, derivatives and declared context.

Preferred fields include:

```text
artifact_id
source_artifact.file_sha256
derivatives[].file_sha256
declared_sources[]
process_disclosure
validation
lineage
reproducibility
```

### 2.3 RO-Crate package

RO-Crate 1.3 describes a broader Research Object through external linked-data conventions.

These three surfaces are related but intentionally not interchangeable.

## 3. Identity semantics

### 3.1 File identity

SHA-256 over local file bytes establishes byte identity under the declared algorithm.

It does **not** establish:

- semantic equivalence;
- correctness;
- source credibility;
- authorship;
- novelty;
- scientific validity.

### 3.2 Structured identity

The artifact record may compute a canonical SHA-256 over selected bounded metadata.

That hash identifies the selected normalized mapping, not the entire meaning of the document.

### 3.3 Structural identity

AST/incremental identities operate over declared structural representations. They are not universal semantic hashes.

## 4. Current implemented boundary

### Integrated

- JSON / CSV / YAML data binding through Jinja2;
- typed Markdown AST for the declared node subset;
- structural add/modify/delete/unchanged reporting;
- bounded atomic structural history;
- document/heading graph and local-link diagnostics;
- bounded research frontmatter metadata;
- AI-assistance / tool / human-review process disclosure;
- descriptive readability signals;
- aggregate Doctor profile with Text/JSON output;
- SARIF 2.1.0 + Approved Errata 01 export;
- cross-platform Markdown synchronization;
- optional Pandoc-backed formats;
- `artifact-record@1` project handoff records;
- RO-Crate 1.3 core metadata export.

### Explicitly not established

- semantic diff or semantic equivalence;
- automatic conflict-free collaborative merge;
- immutable/tamper-proof provenance ledger;
- source credibility;
- SQLite/network API source adapters;
- universal converter availability;
- external RO-Crate validator certification;
- Workflow/Process/Provenance Run Crate conformance;
- authorship adjudication;
- peer review;
- publisher-policy compliance;
- scientific validity;
- independent reproduction solely from generated metadata.

## 5. Document-structure semantics

The AST layer is a normalized structural representation. Parse/render preserves the supported structure but not source bytes.

`ASTNode.signature` and incremental subtree identities use SHA-256 for local identity evidence.

Hash equality over the selected representation does not establish semantic equivalence outside that representation.

## 6. Structural-change semantics

The incremental engine emits:

```text
add | modify | delete | unchanged
```

It is a **change detector**, not a merge engine.

It does not:

- apply patches;
- negotiate ownership;
- resolve human conflicts;
- implement CRDT/OT semantics;
- prove two text versions have identical meaning.

Atomic history replacement improves interrupted-write behavior but does not make the history append-only or tamper-proof.

## 7. Diagnostic semantics

`auto-doc-engine/doctor@1` aggregates document-set diagnostics.

A diagnostic pass may establish only that implemented predicates were evaluated over the inspected files.

It cannot establish:

- factual correctness;
- source trustworthiness;
- scientific reasoning quality;
- peer review;
- whole-publication accessibility;
- journal acceptance.

Readability values are descriptive heuristics. Near-miss links are lexical hints.

## 8. Process-disclosure semantics

Project profile:

```text
auto-doc-engine/process-disclosure@1
```

Bounded vocabulary:

```text
ai_assistance: none | used | not_declared
human_review: reviewed | partial | not_reviewed | not_declared
ai_tools[]
disclosure_ref
```

Hard boundaries:

```text
AI assistance declaration != authorship decision
AI tool string != verified provider/model identity
human_review=reviewed != peer review
process disclosure != scientific validation
process disclosure != publisher-policy certification
```

The repository does not dereference external disclosure references by default.

## 9. Artifact-record profile

Implemented profile:

```text
auto-doc-engine/artifact-record@1
```

The record is a project-owned interoperability object for one source document plus declared/generated derivatives.

It may include:

- source byte identity;
- derivative byte identities;
- selected metadata identity;
- declared author/source refs;
- process disclosure;
- frontmatter validation summary;
- configuration/provenance/validation references;
- execution context;
- local reproducibility level;
- explicit negative scientific/authorship/peer-review claims.

### 9.1 Payload rule

The record indexes artifacts and context. It does not embed source document prose by default.

### 9.2 Reference rule

- existing local files may be hashed;
- URIs are retained as opaque references and not dereferenced;
- unresolved strings remain explicitly unresolved/opaque.

Network availability is therefore not hidden inside record generation.

### 9.3 Validation rule

The embedded validation summary is bounded to the frontmatter validator.

```text
frontmatter clean != factual correctness
frontmatter clean != source credibility
frontmatter clean != scientific validity
```

## 10. SARIF semantics

`auto-doc-engine/sarif@1` targets SARIF 2.1.0 incorporating Approved Errata 01.

Stable finding identity uses namespaced rule IDs and `autoDocFinding/v1` fingerprints.

A downstream consumer parsing SARIF is interoperability evidence, not certification of the findings or science.

## 11. RO-Crate 1.3 implementation profile

`core/ro_crate.py` implements:

```text
auto-doc-engine/ro-crate@1
```

targeting RO-Crate 1.3.

Current profile emits:

- `ro-crate-metadata.json` metadata descriptor;
- root `Dataset`;
- local payload `File` entities;
- `hasPart` relationships;
- optional author `Person` entities;
- `contentSize` / `encodingFormat`;
- SHA-256 identities through Schema.org `PropertyValue`.

Project profile names remain in project documentation rather than being injected as undefined JSON-LD properties.

Not claimed:

- external validator success;
- full optional RO-Crate coverage;
- Workflow Run Crate conformance;
- Process Run Crate conformance;
- Provenance Run Crate conformance;
- scientific reproducibility.

## 12. Artifact record versus RO-Crate

The architecture intentionally separates:

```text
artifact-record@1
  project-owned, lightweight artifact/process handoff

RO-Crate 1.3
  external Research Object packaging
```

If both are emitted, the artifact record may be included as an ordinary File payload in the crate.

That packaging relationship does not convert the project record into a standard RO-Crate profile.

This separation is consistent with a wider Research Object practice in which resources and annotations/provenance records remain linked while keeping distinct vocabularies and scope.

## 13. Reproducibility levels

These are local project terms, not an external standard:

- **R0 — Traceable:** source/artifact association and identity are recorded.
- **R1 — Replay-addressable:** inputs/configuration/tool identity address the intended replay.
- **R2 — Environment-bounded:** important runtime/dependency assumptions are also bounded.
- **R3 — Reproduced:** a separate rerun actually occurred and its result was compared under a declared criterion.

The artifact record can carry a caller-declared level but does not itself execute a rerun.

No manifest, checksum, SARIF report, artifact record, provenance sidecar or RO-Crate file can independently establish R3.

## 14. Cross-repository handoff

Current preferred chain:

```text
auto-doc-engine/artifact-record@1
        ↓
epistemic-pipeline
  upstream artifact/evidence refs
  claim-verification@1
  evidence-envelope@2
        ↓
sci-render-kit
  claim_audit_ref
  figure-claim-audit@1
  figure-evidence@2
```

A downstream repository may consume the reference but owns the interpretation of its own fields.

No direct import/network coupling is required.

## 15. Confidence/score transport rule

If any imported artifact contains a confidence/score value, its semantic label must travel with it.

`auto-doc-engine` must not silently reinterpret:

```text
heuristic score -> probability
interval -> confidence interval
reviewed -> peer reviewed
```

## 16. Experimental-module rule

The following remain Experimental:

- `template_prewarm.py`
- `async_conduit.py`
- `memory_lattice.py`
- `restart_protocol.py`
- `self_observe.py`

Correctness fixes do not promote them into the canonical architecture.

## 17. Global research-engineering calibration

The 2026-08-27 architecture takes design signals from:

- re-openable provenance for autonomous science;
- transparent AI use and human oversight in scientific publishing;
- artifact-centered claim-aware observability;
- EarthVerse-style end-to-end scientific-chain consistency failures;
- RO-Crate and Workflow Run Crate separation of research resources and execution/provenance descriptions.

These are external research signals, not validation, endorsement or standards conformance of this repository.

See `FOUR_DAY_CONSOLIDATION.md` and `FRONTIER_ALIGNMENT.md`.

## 18. Shared hard rules

```text
Provenance != Truth
Hash identity != semantic equivalence
Structure != meaning
Structural change != safe merge
Declared source != credible source by definition
Process disclosure != authorship adjudication
Human review != peer review
Artifact record != external standard
RO-Crate packaging != reproduction
Standard alignment != certification
```

## 19. Maintenance model

Local checks may be run manually when useful. They are not GitHub merge policy and do not establish scientific validity.

The repository architecture does not require GitHub Actions, CI, CodeQL, dependency bots, branch protection or merge gates.

The 2026-08-27 consolidation does not use test execution as completion evidence.

## 20. Primary references

Checked through 2026-08-27:

- RO-Crate 1.3: https://www.researchobject.org/ro-crate/specification/1.3/
- RO-Crate profiles / Workflow Run Crate family: https://www.researchobject.org/ro-crate/profiles.html
- OASIS SARIF 2.1.0 + Errata 01: https://docs.oasis-open.org/sarif/sarif/v2.1.0/errata01/os/sarif-v2.1.0-errata01-os-complete.html
- Nature Computational Science, *Provenance grounds trust in autonomous science*: https://doi.org/10.1038/s43588-026-01035-4
- Nature Computational Science, *Responsible and transparent use of AI in scientific publishing*: https://doi.org/10.1038/s43588-026-01043-4
- *Artifact-centered Claim-aware Observability for Autonomous Scientific Agents*: https://arxiv.org/abs/2608.18312
- *EarthVerse*: https://arxiv.org/abs/2608.23525
