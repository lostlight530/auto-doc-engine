# Evidence Chart — Stage C / 2024-Q3

## Identity

- Repository: `lostlight530/auto-doc-engine`
- Coverage: `SEARCH_BOUNDED`
- Charted: `2026-09-22`

## Variables

| Variable | Meaning |
|---|---|
| environment_state | declared / resolved / synchronized / executed |
| transformation_state | converter revision + target + options/default engine |
| provenance_state | bytes/hash / build attestation / release state |
| correction_state | original / forward patch / proposal/planning |
| reproduction_state | independent execution status |

## Object chart

| Object | Q3 evidence | Provenance lesson | Reproduction |
|---|---|---|---|
| uv 0.3 | project management + lock/sync/run | resolved environment state becomes explicit | NOT_EXECUTED |
| Pandoc 3.3 | fixes 3.2.1 nested-list regression | converter revision affects derivative semantics | NOT_EXECUTED |
| Pandoc 3.4 | target caption controls + default PDF engine change | target/default engine belongs to generation context | NOT_EXECUTED |
| Matplotlib 3.9.1 | artifact attestations + behavior fixes | build origin and behavior correctness are separate | NOT_EXECUTED |
| Matplotlib 3.9.2 | later bugfix release | attested earlier artifact can remain authentic but superseded for behavior | NOT_EXECUTED |
| RO-Crate 1.2 planning | release procedure issue | process state != released specification | NOT_APPLICABLE |

## Counterexample chart

| Overclaim | Counterevidence | Resolution |
|---|---|---|
| lockfile proves reproduction | no environment/run performed | reject |
| attestation proves defect-free behavior | later Matplotlib patch exists | reject |
| same source means same derivative | Pandoc revisions/defaults change output path | reject |
| release issue means released standard | RO-Crate object is planning state | reject |
| later patch invalidates all earlier artifacts | earlier artifact remains historical state | reject |

## Independence

Four project families are represented

No family independently reproduces another family's runtime

Cross-family agreement is conceptual convergence only

## Amendments

`NONE`
