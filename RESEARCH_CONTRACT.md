# Research Contract — auto-doc-engine

**Status:** active repository contract  
**Calibrated:** 2026-08-27

`auto-doc-engine` is the research-artifact and document-evidence plane of the toolchain. It binds structured documents, derivatives, diagnostics, declared process context and optional Research Object packaging without claiming scientific truth.

## 1. Canonical flow

```text
structured source
  -> document binding / frontmatter
  -> typed Markdown structure
  -> structural-change evidence
  -> document graph / diagnostics
  -> rendered derivatives
  -> optional artifact-record
  -> optional RO-Crate 1.3 packaging
```

## 2. Stable project identifiers

Project-owned identifiers are stable semantic names:

```text
auto-doc-engine/doctor
auto-doc-engine/sarif
auto-doc-engine/artifact-record
auto-doc-engine/process-disclosure
auto-doc-engine/frontmatter-validation
auto-doc-engine/ro-crate
autoDocFinding
```

Do not append decorative `@1`, `@2`, `/v1` or similar counters unless a real compatibility/versioning regime is explicitly introduced.

This rule does not remove real external versions. RO-Crate 1.3, SARIF 2.1.0 + Approved Errata 01, CFF 1.2.0 and genuinely observed software/runtime versions remain legitimate standards/provenance metadata.

## 3. Evidence surfaces

### Frontmatter

Bounded document metadata and declared process context, including optional artifact ID, authors, sources, license/DOI/language, AI-assistance declaration, tool IDs, human-review state and disclosure reference.

### Artifact record

`auto-doc-engine/artifact-record` binds one source document to concrete source/derivative byte identities and declared context. It may preserve selected metadata identity, declared source/author references, process disclosure, validation summary, lineage references, execution context and a local reproducibility state.

### RO-Crate

RO-Crate 1.3 is an external Research Object packaging standard. `core/ro_crate.py` emits a conservative core crate structure but does not claim external validator success or Run Crate conformance.

These three surfaces are related but not interchangeable.

## 4. Identity semantics

SHA-256 establishes identity of the recorded bytes or declared canonical mapping under the stated algorithm. It does not establish semantic equivalence, correctness, source credibility, authorship, novelty or scientific validity.

AST/incremental identities are local structural identities, not universal semantic hashes.

## 5. Structural change

The incremental engine emits:

```text
add | modify | delete | unchanged
```

It is a change detector, not a merge engine. It does not implement CRDT/OT semantics, negotiate ownership, resolve human conflicts or prove semantic equivalence.

## 6. Diagnostics

`auto-doc-engine/doctor` aggregates document-set diagnostics. Readability values are descriptive heuristics and near-miss links are lexical hints.

A clean diagnostic run does not establish factual correctness, source trustworthiness, scientific reasoning quality, peer review, accessibility conformance or journal acceptance.

`auto-doc-engine/sarif` exports diagnostic results as SARIF 2.1.0 + Approved Errata 01. `autoDocFinding` is the stable project fingerprint namespace.

## 7. Process disclosure

`auto-doc-engine/process-disclosure` records declared preparation/review context only.

```text
AI assistance declaration != authorship decision
AI tool string != verified provider/model identity
human_review=reviewed != peer review
process disclosure != scientific validation
process disclosure != publisher-policy certification
```

Missing values remain unknown/not-declared and are never guessed.

## 8. Artifact-record boundary

The project record may preserve:

- source and derivative byte identities;
- selected metadata identity;
- declared authors/sources;
- process disclosure;
- bounded frontmatter diagnostics;
- configuration/provenance/validation references;
- execution context;
- local reproducibility state.

It does not embed source prose by default. Existing local files may be hashed; URI/opaque references are retained without automatic dereferencing.

```text
frontmatter clean != factual correctness
frontmatter clean != source credibility
frontmatter clean != scientific validity
```

## 9. RO-Crate 1.3 boundary

`auto-doc-engine/ro-crate` is the repository's exporter identity; RO-Crate **1.3** is the external standard target.

Current exporter can emit the metadata descriptor, root Dataset, local File entities, author Person entities, `hasPart`, content size/media type and SHA-256 PropertyValue records.

Not claimed:

- external RO-Crate validator success;
- complete optional RO-Crate coverage;
- Workflow/Process/Provenance Run Crate conformance;
- scientific reproducibility.

## 10. Artifact record versus RO-Crate

```text
auto-doc-engine/artifact-record
  lightweight project handoff

RO-Crate 1.3
  external Research Object packaging
```

If both exist, an artifact record can be packaged as an ordinary crate file. Packaging does not transform the project record into an external standard profile.

## 11. Reproducibility levels

Local project terms:

- **R0 — Traceable**: source/artifact association and identity are recorded;
- **R1 — Replay-addressable**: inputs/configuration/tool identity address intended replay;
- **R2 — Environment-bounded**: important runtime/dependency assumptions are bounded;
- **R3 — Reproduced**: a separate rerun actually occurred and was compared under a declared criterion.

No checksum, manifest, SARIF report, artifact record, provenance sidecar or RO-Crate file can independently establish R3.

## 12. Cross-repository handoff

```text
auto-doc-engine/artifact-record
        ↓ optional reference
epistemic-pipeline/claim-verification
epistemic-pipeline/evidence-envelope
        ↓ optional reference
sci-render-kit/figure-claim-audit
sci-render-kit/figure-evidence
```

The repositories remain independently runnable. A reference is a handoff, not direct runtime coupling or inherited scientific validity.

## 13. Imported-score rule

If an imported artifact carries a score/confidence/interval/review value, its semantic label must travel with it. Never silently reinterpret:

```text
heuristic score -> probability
bounds -> confidence interval
reviewed -> peer reviewed
```

## 14. Experimental modules

`template_prewarm.py`, `async_conduit.py`, `memory_lattice.py`, `restart_protocol.py` and `self_observe.py` remain Experimental. Correctness fixes do not promote them into canonical architecture.

## 15. Scientific-integrity boundaries

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

## 16. Maintenance boundary

Local checks may be used manually when useful. GitHub Actions, CI, CodeQL, dependency bots, branch-protection assumptions and merge gates are not part of the repository architecture, and test execution is not used as completion evidence for this consolidation.
