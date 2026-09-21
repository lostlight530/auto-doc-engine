# Document Status — auto-doc-engine

**Status:** active document-governance router  
**Calibrated:** 2026-09-21  
**Stage note:** the August 2026 research-infrastructure phase closed on 2026-08-31

This file classifies current repository surfaces by role and authority. It is a router, not an independent source of runtime behavior or scientific truth.

See `docs/README.md` for the repository documentation taxonomy.

## Class 01 — implementation and explanation

Primary implementation and explanatory surfaces:

```text
core/
templates/
sync/
tests/
Makefile
README.md
README_zh.md
docs/01-source-and-explanation/ARCHITECTURE.md
docs/01-source-and-explanation/ARCHITECTURE_zh.md
```

Implementation determines actual behavior. README and Architecture explain current behavior and must remain bounded by implementation and active contracts.

`core/maintenance_cadence.py` is executable source. Source presence is not execution evidence.

## Class 02 — machine contracts, research contracts, examples, and scholarly metadata

Current capability and usage constraints include:

```text
MANIFEST.yaml
docs/02-examples-and-contracts/RESEARCH_CONTRACT.md
docs/02-examples-and-contracts/ARTIFACT_RECORD.md
docs/02-examples-and-contracts/ARTIFACT_LINEAGE_CONTRACT.md
docs/02-examples-and-contracts/ASSERTION_BASIS_AND_COVERAGE.md
docs/02-examples-and-contracts/PROCESS_DISCLOSURE.md
sync/targets.yaml
examples/
AGENTS.md
CONTRIBUTING.md
CITATION.cff
codemeta.json
RELEASE_POLICY.md
LICENSE
```

`MANIFEST.yaml` is the machine-readable capability map. Active research and artifact contracts define the semantics of their named evidence surfaces. Examples demonstrate supported use but do not create capabilities absent from implementation or active contracts.

`CITATION.cff`, `codemeta.json`, and `RELEASE_POLICY.md` describe public discovery, citation, release, and archival identity. They do not establish runtime success, scientific validity, semantic equivalence, or reproduction.

```text
publication identity != current implementation state
DOI != R3 reproduction
citation metadata != capability evidence
```

## Class 03 — current maintenance and repository governance

Current maintenance surfaces include:

```text
docs/03-maintenance-and-audit/DOCUMENT_STATUS.md
docs/03-maintenance-and-audit/MAINTENANCE_CADENCE.md
docs/03-maintenance-and-audit/README.md
docs/03-maintenance-and-audit/independent-gpt/README.md
maintenance/cadence.yaml
.github/pull_request_template.md
.github/ISSUE_TEMPLATE/
```

These files govern maintenance, recovery, contribution, and delivery behavior. They do not outrank implementation, machine contracts, or subject-specific research contracts for capability or scientific semantics.

## Class 04 — active frontier-research documentation

The current longitudinal frontier-research documentation surface is:

```text
maintenance/frontier-research/
```

`maintenance/frontier-research/FIRST_BATCH_SPECIFICATION.md` is the active documentation-method authority for this surface. Its templates and instantiated stages govern research framing, source/object discrimination, evidence charting, synthesis, review, correction/reconciliation, longitudinal routing, handoff, and contributor responsibility within the frontier-research documentation family.

This surface is explicitly non-normative to repository runtime and capability state. It does not outrank current implementation, `MANIFEST.yaml`, machine-readable configuration, or active subject-specific artifact/research contracts.

```text
frontier-research documentation method != runtime capability
structured research artifact != scientific truth
research handoff != authority transfer
later template revision != earlier stage rewrite
```

Instantiated Stage and Part records remain bounded by their declared evidence window and executed method. Later corrections move interpretation forward without silently rewriting earlier research artifacts.

## Historical and dated evidence

Dated maintenance records and files under `docs/03-maintenance-and-audit/history/` remain point-in-time evidence. This includes the closed August stage, frontier alignment, FOUR/FIVE/SIX_DAY consolidations, correction records, demonstrations, and later dated reconciliations.

Historical records remain useful for reconstructing what was observed, believed, or repaired at a specific time. They are not silently rewritten to match current terminology or behavior.

```text
historical snapshot != current contract
later success != earlier success
correction != history rewrite
current path presence != earlier execution
```

## Current authority by question

### Implementation or capability question

```text
current implementation
> current machine-readable contract/configuration for the subject
> active subject-specific contract
> revision-matched executable/operational evidence
> current explanatory documentation
> current maintenance/document router
> historical records
```

### Publication or citation question

```text
CITATION.cff / codemeta.json / RELEASE_POLICY.md / DOI record
```

These surfaces identify the software publication and how to cite it. They do not replace the implementation/evidence chain above.

### Maintenance/document-routing question

Use the current maintenance contract, this document router, cadence configuration, and current repository state. Historical maintenance records can inform the decision but remain time-scoped.

## Scientific-integrity boundaries

```text
lineage != truth
supersedes != predecessor invalid
hash identity != semantic equivalence
assertion basis != correctness
coverage != quality
RO-Crate packaging != reproduction
maintenance clean != scientific validity
checker definition != checker execution
```

Unknown or unexecuted evidence remains unknown or unexecuted. A current document should not promote a structural or metadata observation into a stronger scientific claim.

## Current stage interpretation

The 2026-08-24 through 2026-08-31 research-infrastructure phase is closed. Later maintenance and publication updates do not reopen that historical phase.

Current September state must be recovered from current repository truth and current dated records rather than inferred from the August closure.
