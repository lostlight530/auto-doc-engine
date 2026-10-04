# Open-research routing reconciliation — 2026-10-05

Status: READY_FOR_MAINTAINER_REVIEW  
Repository: `lostlight530/auto-doc-engine`  
Exact base revision: `ecf74a3b085502a1de78ddc2e6b3fac2917415ef`  
Branch: `maintenance/2026-10-05-open-research-routing`

## Confirmed current drift

Current `main` contains `OPEN_RESEARCH.md` as a durable repository-level open-research production guide and `RESEARCH_TEMPLATE.md` as prospective bounded-record scaffolding. README and CONTRIBUTING already route contributors to them.

At the observed base revision, the current document-governance router, agent recovery guide, and machine cadence path inventory did not enumerate either file. This created a current-governance gap: a durable current research-method surface could exist outside the explicit authority router and deterministic maintenance scan inventory.

## Bounded repair

This repair only:
- adds `OPEN_RESEARCH.md` and `RESEARCH_TEMPLATE.md` to the current document router with explicit lower-than-implementation/contract authority;
- routes agents to the open-research guide while preserving more specific native contracts;
- adds both files to maintenance canonical/scan paths.

It does not change implementation, `MANIFEST.yaml`, capability semantics, artifact/lineage contracts, scientific-validity claims, historical FOUR_DAY/FIVE_DAY/SIX_DAY records, frontier-research Stage/Part records, or `LONGITUDINAL_INDEX` semantics.

## Preserved boundaries

```text
Provenance != Truth
Hash != semantic equivalence
maintenance clean != scientific validation
frontier-research documentation != runtime authority
RESEARCH_TEMPLATE != historical rewrite instruction
```

## Evidence state

Executed in this producer pass:
- fresh exact-main recovery;
- open-PR overlap check;
- exact-file inspection of current authority and maintenance surfaces;
- static source/contract reconciliation.

NOT_EXECUTED in this producer pass:
- maintenance scanner execution;
- test suite;
- runtime/exporter execution;
- scientific validation;
- independent reproduction.

Source presence and static inspection are not reported as execution PASS.
