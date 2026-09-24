# Frontier Research Stage Brief — Stage E / 2025-Q1

## 0. Identity
- Repository: `lostlight530/auto-doc-engine`
- Specification version: `2026-09-19-first-batch`
- Stage ID: `E`
- Canonical period: `2025-Q1`
- Research window: `2025-01-01 through 2025-03-31`
- Record type: `RETROSPECTIVE`
- Design: `HISTORICAL_FRONTIER_RECONSTRUCTION + TARGETED_EVIDENCE_SYNTHESIS + COMPARATIVE_TECHNICAL_STUDY`
- Coverage: `SEARCH_BOUNDED`
- Reconstruction date: `2026-09-24`
- Status: `COMPLETE`

## 1. Rationale
Stage D ended with a lifecycle model separating dependency declaration, lock/environment state, converter configuration, generated artifact and release/publication state. Stage E asks what happens when Q1 2025 turns some of those previously provisional surfaces into finalized standards while converter behavior continues to drift revision by revision.

## 2. Repository lens and non-claims
Lens: research artifacts, document evidence, provenance, process disclosure, typed lineage, research objects, artifact durability, multi-format records.

Hard boundaries:
```text
lineage != truth
lock format != reproduced environment
converter version != semantic equivalence
release process != release
later release != earlier availability
```

## 3. Research questions
1. How did Pandoc Q1 releases change representational behavior relevant to derivative identity?
2. What changed when PEP 751 became Final on 2025-03-31?
3. What does RO-Crate 1.2's later Q2 release establish about Q1 publication state without back-projection?

## 4. Source plan
Primary/official surfaces only for the selected objects:
- Pandoc release history: https://pandoc.org/releases.html
- PEP 751: https://peps.python.org/pep-0751/
- RO-Crate official release history: https://github.com/ResearchObject/ro-crate/releases

## 5. Planned Parts
- E1 — converter revision and derivative identity.
- E2 — standardized lock representation and installation provenance.
- E3 — release-process state versus actual publication.

## 6. Completion criteria
Each Part must preserve event/publication/reconstruction dates, same-project source-family limits, no runtime execution claim, and no current-repository defect claim without repository evidence.
