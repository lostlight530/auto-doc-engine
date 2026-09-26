# Frontier Research Stage Brief — Stage G / 2025-Q3

## Identity
- Repository: `lostlight530/auto-doc-engine`
- Specification: `2026-09-19-first-batch`
- Stage: `G / 2025-Q3`
- Window: `2025-07-01 through 2025-09-30`
- Record type: `RETROSPECTIVE`
- Design: `HISTORICAL_FRONTIER_RECONSTRUCTION + TARGETED_EVIDENCE_SYNTHESIS + COMPARATIVE_TECHNICAL_STUDY`
- Coverage: `SEARCH_BOUNDED`
- Reconstruction date: `2026-09-26`
- Status: `COMPLETE`

## Rationale
Stage F widened the artifact evidence envelope from dependency selection into package composition, converter revision, and Research Object packaging. Stage G follows the next quarter as three different forms of identity become more explicit: software metadata relationships, publication immutability, and a converter-native structural interchange representation.

The research question is not whether these projects make artifacts "trustworthy" in one step. It is how they sharpen the answer to three narrower questions: what object is being described, whether a published release can later change, and whether a document transform has a portable structural representation that is distinct from its rendered bytes.

## Research questions
1. What changes when CodeMeta 3.0 adds richer software/application, contributor-role, and review relationships?
2. What changes when a release can be marked immutable and receive signed attestations over release assets?
3. What does Pandoc 3.8's XML representation of the Pandoc AST add to transformation identity and inspectability?

## Selected objects
- CodeMeta 3.0 — released 2025-07-13.
- GitHub immutable releases public preview — announced 2025-08-26.
- Pandoc 3.8 — released 2025-09-06; 3.8.1 followed on 2025-09-29 as a same-lineage corrective/feature release.

## Hard boundaries
```text
metadata relation != verified real-world relation
review metadata != review validity
immutable release != secure software
attestation != scientific truth
signed identity != semantic equivalence
Pandoc XML AST != byte-for-byte round trip
converter format support != local replay
release note != independent reproduction
```
