# Research Contract — auto-doc-engine

**Status:** active repository contract  
**Calibrated:** 2026-08-31  
**Closed stage:** 2026-08-24 through 2026-08-31

`auto-doc-engine` is the research-artifact and document-evidence plane of the toolchain. It binds structured documents, derivatives, diagnostics, declared process context, typed artifact lineage, optional Research Object packaging, and phase-aware maintenance without claiming scientific truth.

## 1. Canonical flow

```text
structured source
  -> document binding / frontmatter
  -> typed Markdown structure
  -> structural-change evidence
  -> document graph / diagnostics
  -> rendered derivatives
  -> optional artifact-record
       ├─ assertion basis
       ├─ reference-resolution states
       └─ dimensional audit coverage
  -> optional artifact-lineage
       ├─ caller-declared typed relations
       └─ explicit non-inheritance boundaries
  -> optional RO-Crate 1.3 packaging

repository state
  -> daily / weekly / monthly maintenance
       ├─ current-document authority
       ├─ history inventory
       ├─ calendar/stage status
       └─ optional canonical SHA-256 baseline
```

## 2. Stable project identifiers

Project-owned identifiers are stable semantic names

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

Do not append decorative `@1`, `@2`, `/v1`, or similar counters unless a real compatibility/versioning regime is explicitly introduced

This rule does not remove real external versions. RO-Crate 1.3, SARIF 2.1.0 + Approved Errata 01, CFF 1.2.0, and genuinely observed software/runtime versions remain legitimate standards/provenance metadata

## 3. Document-authority contract

`DOCUMENT_STATUS.md` defines which repository documents are current authority, historical snapshots, examples, or external/citation metadata

Current contracts may evolve while historical snapshots remain time-scoped evidence

```text
historical snapshot != current contract
current contract != permission to rewrite history
```

Routine maintenance must not rewrite `FOUR_DAY_CONSOLIDATION.md`, `FIVE_DAY_CONSOLIDATION.md`, or `SIX_DAY_CONSOLIDATION.md` merely because later terminology changed

## 4. Evidence surfaces

### Frontmatter

Bounded document metadata and declared process context, including optional artifact ID, authors, sources, license/DOI/language, AI-assistance declaration, tool IDs, human-review state, and disclosure reference

### Artifact record

`auto-doc-engine/artifact-record` binds one source document to concrete source/derivative byte identities and declared context. It may preserve selected metadata identity, declared source/author references, process disclosure, validation summary, lineage references, execution context, assertion basis, dimensional audit coverage, and a local reproducibility state

### Artifact lineage

`auto-doc-engine/artifact-lineage` records typed caller-declared relationships between one artifact record and predecessor/related artifacts. It is a project handoff object, not an external provenance standard or semantic-equivalence engine

### Maintenance report

`auto-doc-engine/maintenance-report` is a read-only structural maintenance record. It may report canonical-path presence, profile-version drift, Manifest calibration age, historical snapshot inventory, optional canonical SHA-256 baselines, and temporal stage status

### RO-Crate

RO-Crate 1.3 is an external Research Object packaging standard. `core/ro_crate.py` emits a conservative core crate structure but does not claim external validator success or Run Crate conformance

These surfaces are related but not interchangeable

## 5. Assertion-basis contract

A stored value and the way that value entered the record are separate evidence dimensions

Current project bases include

```text
document-frontmatter
runtime-observed-local-bytes
runtime-observed-local-filesystem
caller-declared
not_declared
```

Typical mapping

| Surface | Basis |
|---|---|
| source / derivative byte identity | runtime-observed local bytes |
| document metadata | document frontmatter |
| authors / sources | document frontmatter |
| process disclosure | document frontmatter |
| `generated_with` | caller-declared when supplied |
| config/provenance/validation refs | caller-declared with optional local resolution |
| artifact-lineage relations | caller-declared with optional local resolution |

```text
assertion basis != correctness
```

A declaration-backed value can be false. A runtime-observed hash can identify incorrect bytes perfectly. Assertion basis improves auditability without creating a truth claim

The artifact-record path records `automatic_ai_detection_used: false`; process disclosure is declaration-backed rather than inferred from prose

## 6. Audit-coverage contract

The artifact record may expose separate descriptive coverage dimensions

- derivative count
- declared-source reference count and resolution classes
- lineage reference count and resolution classes
- local-file ratios for declared references
- process-disclosure fields actually declared
- frontmatter error/warning counts

The artifact-lineage record separately exposes relation counts, relation-vocabulary counts, resolution classes, and local-file ratio

The project deliberately does not combine these dimensions into one quality score

```json
{"aggregate_score": null}
```

```text
coverage != correctness
coverage ratio != probability
reference presence != citation validity
local-file resolution != source credibility
lineage coverage != provenance soundness
frontmatter clean != scientific validity
```

## 7. Artifact-lineage contract

Allowed relation vocabulary

```text
derived-from
revision-of
supersedes
uses
related-to
```

Relations are caller-declared and never inferred from filenames, timestamps, prose similarity, Git history, or model output

Semantics

```text
derived-from -> declared derivation; not complete provenance proof
revision-of  -> declared revision; not semantic equivalence
supersedes   -> declared replacement intent; does not erase predecessor history
uses         -> declared dependency/use; not evidence sufficiency
related-to   -> weak declared relationship with no stronger implication
```

Every relation explicitly carries

```text
scientific_validity_inherited: false
reproducibility_inherited: false
```

A successor does not inherit scientific validity, peer review, credibility, or R3 reproduction merely because it references a predecessor

## 8. Identity semantics

SHA-256 establishes identity of the recorded bytes or declared canonical mapping under the stated algorithm. It does not establish semantic equivalence, correctness, source credibility, authorship, novelty, or scientific validity

AST/incremental identities are local structural identities, not universal semantic hashes

## 9. Structural change

The incremental engine emits

```text
add | modify | delete | unchanged
```

It is a change detector, not a merge engine. It does not implement CRDT/OT semantics, negotiate ownership, resolve human conflicts, or prove semantic equivalence

## 10. Diagnostics

`auto-doc-engine/doctor` aggregates document-set diagnostics. Readability values are descriptive heuristics and near-miss links are lexical hints

A clean diagnostic run does not establish factual correctness, source trustworthiness, scientific reasoning quality, peer review, accessibility conformance, or journal acceptance

`auto-doc-engine/sarif` exports diagnostic results as SARIF 2.1.0 + Approved Errata 01. `autoDocFinding` is the stable project fingerprint namespace

## 11. Process disclosure

`auto-doc-engine/process-disclosure` records declared preparation/review context only

```text
AI assistance declaration != authorship decision
AI tool string != verified provider/model identity
human_review=reviewed != peer review
process disclosure != AI-text detection
process disclosure != scientific validation
process disclosure != publisher-policy certification
```

Missing values remain unknown/not-declared and are never guessed

## 12. Artifact-record boundary

The project record may preserve source/derivative byte identities, selected metadata identity, declared authors/sources, process disclosure, bounded frontmatter diagnostics, configuration/provenance/validation references, execution context, assertion basis, dimensional audit coverage, and local reproducibility state

It does not embed source prose by default. Existing local files may be hashed; URI/opaque references are retained without automatic dereferencing

## 13. Artifact-lineage boundary

The lineage record exists to preserve research history across generations. It does not

- infer artifact relations automatically
- decide which artifact is scientifically superior
- invalidate predecessors
- prove semantic equivalence
- certify complete provenance
- transfer reproducibility status

```text
lineage != truth
inheritance != validation
supersedes != history deletion
revision != semantic equivalence
```

## 14. Maintenance contract

`MAINTENANCE_CADENCE.md` and `maintenance/cadence.yaml` define daily, weekly, and monthly maintenance

The scanner is read-only and date-aware

For 2026-08-31 it reports

```text
calendar_month: calendar-month-close
stage: closed
```

Daily maintenance handles bounded demonstrated drift

Weekly maintenance reconciles implementation, machine contracts, current documentation, examples, cross-repository handoff names, and historical inventory

Monthly or explicit phase-close maintenance records canonical baselines and reviews document/capability status without automatic deletion or history rewrite

```text
maintenance clean != scientific validity
calendar close != reproduction
history inventory != deprecation decision
```

## 15. RO-Crate 1.3 boundary

`auto-doc-engine/ro-crate` is the repository exporter identity; RO-Crate 1.3 is the external standard target

Current exporter can emit the metadata descriptor, root Dataset, local File entities, author Person entities, `hasPart`, content size/media type, and SHA-256 PropertyValue records

Not claimed: external validator success, complete optional RO-Crate coverage, Workflow/Process/Provenance Run Crate conformance, or scientific reproducibility

## 16. Reproducibility levels

Local project terms

- **R0 — Traceable**: source/artifact association and identity are recorded
- **R1 — Replay-addressable**: inputs/configuration/tool identity address intended replay
- **R2 — Environment-bounded**: important runtime/dependency assumptions are bounded
- **R3 — Reproduced**: a separate rerun actually occurred and was compared under a declared criterion

No checksum, manifest, SARIF report, artifact record, artifact-lineage record, maintenance baseline, provenance sidecar, or RO-Crate file can independently establish R3

## 17. Cross-repository handoff

```text
auto-doc-engine/artifact-record
        ↓
auto-doc-engine/artifact-lineage
        ↓ optional reference
epistemic-pipeline/claim-verification
epistemic-pipeline/claim-transfer
epistemic-pipeline/evidence-envelope
        ↓ optional reference
sci-render-kit/figure-claim-audit
sci-render-kit/figure-evidence
sci-render-kit/communication-transfer
```

The repositories remain independently runnable. A reference or transfer is a handoff, not direct runtime coupling or inherited scientific validity

## 18. Imported-semantic rule

If an imported artifact carries a score/confidence/interval/review/lineage value, its semantic label must travel with it. Never silently reinterpret

```text
heuristic score -> probability
bounds -> confidence interval
reviewed -> peer reviewed
coverage ratio -> quality score
revision-of -> semantic equivalence
supersedes -> predecessor invalid
```

## 19. Stage-close research alignment

The closed 2026-08-24 → 2026-08-31 stage is informed by, but not certified by

- provenance-complete autonomous-science work
- transparent AI-use / human-oversight scientific-publishing guidance
- artifact-centered claim-aware observability
- trajectory-to-evidence qualification
- evidence-bounded claim review
- end-to-end scientific-agent consistency evaluation
- claim-level auditability separating provenance coverage, soundness, contradiction transparency, and audit effort
- Praxist-style solution/evidence lineage
- ReproAgent-style persistent contracts
- long-horizon phase behavior and regime-aware re-validation
- ScienceFlow-style persistent research segments and recovery
- process-level long-horizon evaluation beyond final scores
- living research-software metadata and maintenance
- RO-Crate 1.3 and related execution-provenance profiles

The repository implements only the subset it can substantiate: artifact identity, declaration provenance, dimensional coverage, typed artifact lineage, bounded diagnostics, explicit maintenance/document governance, and interoperability boundaries

## 20. Experimental modules

`template_prewarm.py`, `async_conduit.py`, `memory_lattice.py`, `restart_protocol.py`, and `self_observe.py` remain Experimental. Correctness fixes do not promote them into canonical architecture

## 21. Scientific-integrity boundaries

```text
Provenance != Truth
Hash identity != semantic equivalence
Structure != meaning
Structural change != safe merge
Assertion basis != correctness
Audit coverage != quality
Coverage ratio != probability
Artifact lineage != inherited scientific validity
Supersedes != history deletion
Declared source != credible source by definition
Process disclosure != authorship adjudication
Human review != peer review
Artifact record != external standard
RO-Crate packaging != reproduction
Maintenance clean != scientific validity
Calendar-month close != reproduction
Standard alignment != certification
```

## 22. Governance boundary

Local checks may be used manually when useful. GitHub Actions, CI, CodeQL, dependency bots, branch-protection assumptions, and merge gates are not part of the repository architecture, and test execution is not used as completion evidence for this stage-close reconciliation
