# Research Contract — auto-doc-engine

**Calibration:** 2026-08-23  
**Status:** active repository contract for evidence, provenance, reproducibility and research-object claims

This contract defines what repository artifacts can and cannot establish. It is an architectural/scientific-integrity contract, not a GitHub merge policy.

## 1. Role in the three-repository toolchain

`auto-doc-engine` is the **document and evidence-packaging plane**:

```text
structured source
    -> document binding
    -> typed document structure
    -> structural-change evidence
    -> document graph / metadata diagnostics
    -> rendered artifacts
    -> optional interoperability packaging
```

It does not determine scientific truth, calibrate probabilities, resolve arbitrary human-edit conflicts, or prove independent reproducibility.

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
```

A SHA-256 digest establishes byte identity under the declared algorithm. It does not establish semantic equivalence, correctness, authorship, novelty or scientific validity.

## 3. Current implemented boundary

### Integrated

- JSON / CSV / YAML data binding through Jinja2;
- Mistune-backed typed Markdown AST for the declared node subset;
- structural add/modify/delete/unchanged reporting;
- atomic bounded structural-generation history;
- document/heading reference graph and local-link diagnostics;
- bounded research frontmatter metadata;
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

## 6. Diagnostic semantics

`auto-doc-engine/doctor@1` aggregates document-set diagnostics. Error/warning severity controls the command's local status only.

A diagnostic pass can establish that implemented predicates were evaluated over the inspected files. It cannot establish:

- factual correctness of the prose;
- quality of scientific reasoning;
- accessibility of a final publication;
- acceptance by a journal or reviewer.

Readability values are descriptive heuristics. Near-miss links are lexical hints.

## 7. SARIF semantics

`auto-doc-engine/sarif@1` targets OASIS SARIF 2.1.0 incorporating Approved Errata 01.

Stable finding identity uses namespaced rule IDs and `autoDocFinding/v1` partial fingerprints. A downstream tool successfully parsing the file is interoperability evidence, not certification of the repository's scientific claims.

## 8. RO-Crate 1.3 implementation profile

RO-Crate 1.3 was published on 2026-06-22 and is the current long-term release observed for this calibration.

The repository now implements `auto-doc-engine/ro-crate@1` through `core/ro_crate.py`.

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

**Not claimed:** external validator success, full coverage of every optional RO-Crate recommendation, workflow-run profile conformance, or scientific reproducibility.

## 9. Reproducibility levels

These are **local project terms**, not an external standard:

- **R0 — Traceable:** source/artifact identity metadata is recorded.
- **R1 — Replay-addressable:** inputs, configuration, tool revision and intended command/path are sufficient to address the intended replay.
- **R2 — Environment-bounded:** relevant runtime/dependency/external-tool assumptions are also recorded.
- **R3 — Reproduced:** a separate rerun has actually happened and its result was compared under a declared acceptance criterion.

No manifest, checksum, SARIF report, provenance sidecar or RO-Crate metadata file may be used alone to label an artifact R3.

## 10. Cross-repository handoff

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
```

The repositories remain loosely coupled. This contract does not require direct imports or network calls between them.

If an upstream record contains a confidence value, its `confidence_semantics` must travel with it. `auto-doc-engine` must not silently reinterpret a heuristic value as calibrated probability.

## 11. Experimental-module rule

The following remain Experimental even after this refresh:

- `template_prewarm.py`
- `async_conduit.py`
- `memory_lattice.py`
- `restart_protocol.py`
- `self_observe.py`

Fixing internal bugs or clarifying semantics does not automatically promote them into the integrated architecture.

## 12. External observations — 2026-08-23

Observations are ecosystem evidence, not compatibility proof:

- RO-Crate 1.3 — current long-term release, published 2026-06-22;
- SARIF 2.1.0 + Approved Errata 01 — current target profile;
- Mistune 3.3.4 — observed current; repository floor remains `>=3.2.1`;
- Pandoc 3.10.2 — observed current; optional external dependency;
- Citation File Format 1.2.0 — citation metadata format.

## 13. Shared scientific-integrity rules

1. Provenance is not truth.
2. Hash identity is not semantic equivalence.
3. Structure is not meaning.
4. Diagnostic success is not peer review.
5. Metadata is not independent reproduction.
6. Standard alignment is not external certification.
7. Optional dependencies must fail explicitly when unavailable.
8. Experimental code is not integrated capability merely because it exists.
9. GitHub-native CI/merge gating is not part of this repository's scientific architecture.

## 14. Primary references

Retrieved/calibrated 2026-08-23:

- RO-Crate 1.3 specification: https://www.researchobject.org/ro-crate/specification/1.3/
- OASIS SARIF 2.1.0 + Errata 01: https://docs.oasis-open.org/sarif/sarif/v2.1.0/errata01/os/sarif-v2.1.0-errata01-os-complete.html
- FAIR R1.2 provenance principle: https://www.go-fair.org/fair-principles/r1-2-metadata-associated-detailed-provenance/
- Mistune: https://pypi.org/project/mistune/
- Pandoc releases: https://github.com/jgm/pandoc/releases
- Citation File Format 1.2.0: https://citation-file-format.github.io/
