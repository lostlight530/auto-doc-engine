# Frontier Research Stage Brief — Stage H / 2025-Q4

## Identity
- Repository: `lostlight530/auto-doc-engine`
- Stage: `H / 2025-Q4`
- Window: `2025-10-01 through 2025-12-31`
- Record type: `RETROSPECTIVE`
- Design: `HISTORICAL_FRONTIER_RECONSTRUCTION + TARGETED_EVIDENCE_SYNTHESIS`
- Coverage: `SEARCH_BOUNDED`
- Reconstruction date: `2026-09-27`
- Status: `COMPLETE`

## Rationale
Stage G separated typed metadata relations, immutable publication identity, and structural AST interchange. Stage H follows Q4 2025 as artifact evidence becomes more compositional: citations and provenance become first-class BOM relations, source integrity gains an explicit SLSA track, and document conversion broadens to additional source formats whose input identity must remain visible.

## Research questions
1. What changes when a BOM can carry citation and provenance relationships rather than only inventory facts?
2. What changes when source-management provenance becomes a first-class supply-chain track rather than an implicit prerequisite?
3. What additional identity must be retained when one converter adds spreadsheet, presentation, and AsciiDoc inputs?

## Selected objects
- CycloneDX 1.7 — released 2025-10-21.
- SLSA 1.2 — released 2025-11-24.
- Pandoc 3.8.3 — released 2025-12-01.

## Hard boundaries
```text
citation metadata != evidence sufficiency
BOM relation != verified real-world relation
SLSA source track != source truth
approved specification != local conformance
format support != semantic fidelity
converter support != local replay
broader input surface != deterministic equivalence
```
