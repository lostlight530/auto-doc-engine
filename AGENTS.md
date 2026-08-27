# Agent Guide — auto-doc-engine

This is the operational contract for agents modifying the repository. Current capability authority is shared by:

- `README.md` / `README_zh.md`
- `ARCHITECTURE.md` / `ARCHITECTURE_zh.md`
- `RESEARCH_CONTRACT.md`
- `ARTIFACT_RECORD.md`
- `PROCESS_DISCLOSURE.md`
- `FOUR_DAY_CONSOLIDATION.md`
- `MANIFEST.yaml`

## 1. Canonical architecture

```text
structured data
  -> renderer
  -> typed Markdown AST
  -> structural diff / document graph / frontmatter
  -> Doctor / JSON / SARIF
  -> sync
     -> rendered derivatives
     -> optional artifact-record@1
     -> optional RO-Crate 1.3
```

Integrated core files:

```text
core/renderer.py
core/ast_engine.py
core/incremental.py
core/cross_ref.py
core/frontmatter.py
core/readability.py
core/doctor.py
core/sarif.py
core/sync.py
core/artifact_record.py
core/ro_crate.py
```

Experimental and **not integrated**:

```text
template_prewarm.py
async_conduit.py
memory_lattice.py
restart_protocol.py
self_observe.py
```

## 2. Repository-governance boundary

Do **not** add GitHub Actions, CI/CodeQL workflows, dependency-update bots, branch-protection assumptions, or merge-gate language as normal research-maintenance architecture.

Local commands such as `make test` may remain optional maintenance aids. They are not scientific validation or repository architecture.

## 3. Hard implementation rules

1. **AST first.** Structural Markdown changes go through the typed AST rather than regex mutation.
2. **SHA-256 identity.** Do not reintroduce MD5 on document/artifact identity surfaces.
3. **No `shell=True`.** External converters use argument lists.
4. **Built-in core before shell utility.** Markdown copy remains Python stdlib.
5. **External dependencies stay explicit.** Pandoc/PDF engines are optional and unavailable states remain visible.
6. **Normalized Markdown is not byte preservation.** Never claim arbitrary source round-trip fidelity.
7. **Structural diff is not merge.** `incremental.py` reports changes; it does not resolve ownership/conflicts.
8. **Hints are not semantics.** Near-miss and readability values remain heuristics.
9. **Process disclosure is declarative.** Never convert `human_review=reviewed` into peer review or `ai_tools` into verified model provenance.
10. **Artifact record is project-owned.** `artifact-record@1` is not RO-Crate/PROV/Workflow Run Crate conformance.
11. **Artifact payload minimization.** Do not embed complete document payloads in the artifact record by default.
12. **Reference handling remains offline.** Local files may be hashed; URI/opaque refs are retained without network dereferencing.
13. **R3 discipline.** Metadata generation never self-awards reproduction.
14. **RO-Crate standards-facing JSON-LD stays standards-facing.** Project profile names belong in project metadata/docs, not invented context terms.
15. **Experimental stays Experimental.** Correcting a module does not wire it into the canonical chain.

## 4. Artifact-record invariants

Current project profile:

```text
auto-doc-engine/artifact-record@1
```

The record can index:

```text
source byte identity
derivative byte identities
selected metadata identity
declared sources/authors
process disclosure
frontmatter validation
lineage/config references
execution context
local reproducibility declaration
```

Interpretation boundaries:

```text
hash != semantic equivalence
source ref != source credibility
validation clean != factual correctness
human review != peer review
artifact record != external standard
```

If SyncEngine emits both artifact record and RO-Crate, the artifact record may be packaged as a normal file. Do not relabel it as a standard RO-Crate profile.

## 5. Where to change what

| Goal | Primary files | Synchronize |
|---|---|---|
| data source | `core/renderer.py` | README pair, Architecture pair, MANIFEST |
| Markdown node | `core/ast_engine.py` | incremental/cross-ref compatibility + docs |
| diff semantics | `core/incremental.py` | Research Contract + docs |
| graph/link semantics | `core/cross_ref.py` | Doctor/SARIF semantics + docs |
| metadata/process field | `core/frontmatter.py` | Process Disclosure + Artifact Record + docs |
| Doctor finding | `core/doctor.py` | SARIF mapping when exportable |
| conversion target | `core/sync.py`, `sync/targets.yaml` | dependency docs + artifact record semantics |
| artifact record field | `core/artifact_record.py` | ARTIFACT_RECORD + Contract + MANIFEST + examples |
| RO-Crate entity/relation | `core/ro_crate.py` | Research Contract + MANIFEST + examples |
| public architecture | README / Architecture / Contract / MANIFEST | update together |

## 6. Cross-repository handoff

Current conceptual interface:

```text
auto-doc-engine/artifact-record@1
        -> epistemic-pipeline/evidence-envelope@2
           + claim-verification@1
        -> sci-render-kit/figure-evidence@2
```

No direct imports are required.

Never silently reinterpret an imported score/interval/review field into a stronger scientific meaning.

## 7. Global research calibration rule

External papers/standards may justify a design principle but do not automatically establish compatibility or correctness.

Current Day-4 signals are summarized in `FOUR_DAY_CONSOLIDATION.md` and `FRONTIER_ALIGNMENT.md`.

When adding a new external reference, distinguish:

```text
observed direction
implemented repository behavior
external standard conformance
scientific validation
```

## 8. Local maintenance

Optional:

```bash
python -m pip install jinja2 "mistune>=3.2.1" pyyaml
make test
```

Do not describe local check success as evidence of external converter availability, RO-Crate certification, peer review, scientific truth or independent reproduction.
