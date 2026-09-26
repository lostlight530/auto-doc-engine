# Frontier Research Review — Stage G / 2025-Q3

- Review date: 2026-09-26
- Independence: `SAME_PRODUCER_REVIEW`

## Temporal integrity
- CodeMeta 3.0 release: 2025-07-13.
- GitHub immutable releases public preview: 2025-08-26.
- Pandoc 3.8: 2025-09-06.
- Pandoc 3.8.1: 2025-09-29.

Dates are treated as event/release dates for their respective objects. Reconstruction occurred later and is not backdated.

## Source/object integrity
CodeMeta, GitHub release infrastructure, and Pandoc are separate research objects. Pandoc 3.8 and 3.8.1 are one source/project lineage.

## Boundary review
No CodeMeta migration/validation, immutable-release configuration, release-attestation verification, Pandoc 3.8 installation, AST round-trip, converter regression replay, or independent reproduction was executed.

## Findings
| ID | Class | Severity | Action |
|---|---|---|---|
| R1 | REVIEW_INDEPENDENCE | NON_MATERIAL | retain SAME_PRODUCER_REVIEW |
| R2 | METADATA_OVERREACH | CONTROLLED | relation declaration != verified relation |
| R3 | IMMUTABILITY_OVERREACH | CONTROLLED | immutable/signed != correct/secure/scientifically valid |
| R4 | EXECUTION_GAP | NON_MATERIAL | keep local validation/replay NOT_EXECUTED |
| R5 | SAME_LINEAGE | CONTROLLED | Pandoc 3.8.1 is later same-lineage evidence |

Disposition: `RESEARCH_READY_FOR_STAGE_CLOSE`.
