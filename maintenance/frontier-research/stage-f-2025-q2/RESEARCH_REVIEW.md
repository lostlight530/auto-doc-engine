# Frontier Research Review — Stage F / 2025-Q2

- Review date: 2026-09-25
- Independence: `SAME_PRODUCER_REVIEW`

## Temporal integrity
- PEP 770 Final: 2025-04-11.
- Pandoc 3.7 / .0.1 / .0.2: 2025-05-14 / 17 / 28.
- RO-Crate 1.2 Recommendation: 2025-06-04.

## Boundary review
No SBOM generation/verification, package installation, Pandoc replay, tagged-PDF accessibility validation, RO-Crate generation/conformance validation or independent reproduction was performed.

## Findings
| ID | Class | Severity | Action |
|---|---|---|---|
| R1 | REVIEW_INDEPENDENCE | NON_MATERIAL | preserve SAME_PRODUCER_REVIEW |
| R2 | RUNTIME_GAP | NON_MATERIAL | keep executions NOT_EXECUTED |
| R3 | METADATA_OVERREACH | CONTROLLED | SBOM/RO-Crate presence != correctness/reproduction |
| R4 | VERSION_FIDELITY | CONTROLLED | preserve Pandoc revision-specific behavior |

Disposition: `RESEARCH_READY_FOR_STAGE_CLOSE`.
