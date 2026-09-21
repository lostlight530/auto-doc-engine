# Frontier Research Document-Authority Reconciliation — 2026-09-21

**Repository:** `lostlight530/auto-doc-engine`  
**Status:** current dated maintenance reconciliation  
**Base revision:** `033bae57a8416f16a6f773dde0cf2d55d63d1a16`  
**Result:** `REPAIR` for document-authority routing only  
**Implementation/runtime change:** none

## Confirmed drift

The 2026-09-19 first-batch frontier-research family introduced `maintenance/frontier-research/FIRST_BATCH_SPECIFICATION.md` with status `active research-documentation specification / non-normative to repository runtime`.

The current `docs/03-maintenance-and-audit/DOCUMENT_STATUS.md` was calibrated on 2026-09-17 and did not classify `maintenance/frontier-research/` as a current authority surface.

This was a current document-router drift. It was not a runtime, capability, artifact-lineage, scientific-validity, or historical-execution defect.

## Repair

- advanced the document-router calibration date to 2026-09-21;
- added an explicit active frontier-research documentation class;
- bound the first-batch specification to documentation-method authority only;
- preserved implementation, `MANIFEST.yaml`, machine configuration, and active artifact/research contracts as higher authority for runtime/capability questions;
- preserved historical records and forward-only correction semantics.

## Deliberately unchanged

- `core/**`
- `MANIFEST.yaml`
- active artifact-lineage and artifact-record semantics
- historical FOUR/FIVE/SIX_DAY and August stage records
- GitHub Actions and scheduler surfaces

## Verification

Executed:

- fresh remote `main` recovery;
- open PR and branch overlap check;
- current first-batch specification inspection;
- current document-router inspection;
- exact-base branch creation;
- remote branch diff verification after the router update.

Not executed:

- repository-local maintenance scanner;
- tests, compile, converters, or runtime execution;
- scientific-validity or reproduction checks.

`NOT_EXECUTED` remains the correct status for those checks. No PASS is inferred from source presence.

## Final boundary

```text
frontier-research documentation method != runtime capability
structured research artifact != scientific truth
research handoff != authority transfer
correction != history rewrite
```

This repair is ready for maintainer review and must not be interpreted as a runtime capability change.
