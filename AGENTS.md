# Agent Guide — auto-doc-engine

This is the operational contract for agents modifying the repository. Keep code, machine-readable contracts and public documentation aligned.

## Canonical architecture

```text
structured data
  -> renderer
  -> typed Markdown AST
  -> structural diff / document graph / frontmatter
  -> Doctor / JSON / SARIF
  -> sync
     -> rendered derivatives
     -> optional artifact-record
          ├─ assertion basis
          └─ dimensional audit coverage
     -> optional RO-Crate 1.3
```

Integrated core: `renderer.py`, `ast_engine.py`, `incremental.py`, `cross_ref.py`, `frontmatter.py`, `readability.py`, `doctor.py`, `sarif.py`, `sync.py`, `artifact_record.py`, `ro_crate.py`.

Experimental and not integrated: `template_prewarm.py`, `async_conduit.py`, `memory_lattice.py`, `restart_protocol.py`, `self_observe.py`.

## Stable project identifiers

```text
auto-doc-engine/doctor
auto-doc-engine/sarif
auto-doc-engine/artifact-record
auto-doc-engine/process-disclosure
auto-doc-engine/frontmatter-validation
auto-doc-engine/ro-crate
autoDocFinding
```

Do not invent `@1`, `@2`, `/v1` or similar counters. Preserve real external/runtime versions when known, including RO-Crate 1.3, SARIF 2.1.0 + Approved Errata 01 and CFF 1.2.0.

## Hard rules

1. Structural Markdown changes go through the typed AST rather than regex mutation.
2. Keep SHA-256 on document/artifact identity surfaces; do not reintroduce MD5.
3. External converters use argument lists; do not introduce `shell=True`.
4. Optional dependencies and unavailable states stay explicit.
5. Normalized Markdown is not byte-preserving round-trip fidelity.
6. Structural diff is not merge or conflict resolution.
7. Near-miss/readability values are heuristics, not semantic truth.
8. Process disclosure is declarative; human review is not peer review and tool IDs are not verified model provenance.
9. The canonical path does not perform AI-text detection; do not infer AI use from prose/style.
10. `artifact-record` is project-owned, not RO-Crate/PROV/Run Crate conformance.
11. Artifact records do not embed complete document payloads by default.
12. Local files may be hashed; URI/opaque refs remain offline references unless a separate resolver is explicitly introduced.
13. Assertion basis records how a value entered the record; it never upgrades the value to truth.
14. Coverage remains dimensional. Do not create a synthetic aggregate research-quality score from presence/resolution/diagnostic counts.
15. `coverage ratio` must never be relabelled probability, evidence sufficiency or source credibility.
16. Metadata generation never self-awards R3 reproduction.
17. Standards-facing RO-Crate JSON-LD must not be polluted with invented project vocabulary.
18. Experimental modules remain Experimental until intentionally integrated.
19. Unknown provider/model/version/source/review state remains unknown; never guess.
20. Do not add GitHub Actions, CI, CodeQL, dependency bots, branch-protection assumptions or merge-gate architecture.

## Artifact-record invariants

`auto-doc-engine/artifact-record` may index source/derivative byte identities, selected metadata identity, declared sources/authors, process disclosure, bounded frontmatter validation, lineage/config refs, execution context, assertion basis, dimensional audit coverage and a local reproducibility state.

```text
hash != semantic equivalence
assertion basis != correctness
coverage != quality
coverage ratio != probability
source ref != source credibility
validation clean != factual correctness
human review != peer review
artifact record != external standard
```

If both artifact record and RO-Crate are emitted, the artifact record may be packaged as a normal File. Do not relabel it as a standard RO-Crate profile.

## Change ownership

| Goal | Primary files | Synchronize |
|---|---|---|
| data source | `core/renderer.py` | README pair + Architecture pair + Manifest |
| Markdown node | `core/ast_engine.py` | incremental/cross-ref compatibility + docs |
| diff semantics | `core/incremental.py` | Research Contract + docs |
| graph/link semantics | `core/cross_ref.py` | Doctor/SARIF semantics + docs |
| metadata/process field | `core/frontmatter.py` | Process Disclosure + Artifact Record + docs |
| assertion basis / coverage | `core/artifact_record.py` | Assertion Basis contract + Artifact Record + Manifest + examples |
| conversion target | `core/sync.py`, `sync/targets.yaml` | dependency docs + artifact record semantics |
| RO-Crate entity/relation | `core/ro_crate.py` | Research Contract + Manifest + examples |
| public capability | README / Architecture / Contracts / Manifest | update together |

## Cross-repository handoff

```text
auto-doc-engine/artifact-record
  -> epistemic-pipeline/claim-verification
  -> epistemic-pipeline/evidence-envelope
  -> sci-render-kit/figure-claim-audit
  -> sci-render-kit/figure-evidence
```

These are optional references, not direct imports or inherited scientific validity.

## Local maintenance

Local checks may be used manually when useful. Their success is not evidence of external converter availability, standards certification, peer review, scientific truth or independent reproduction.
