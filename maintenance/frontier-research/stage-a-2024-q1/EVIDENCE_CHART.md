# Evidence Chart — Stage A / 2024-Q1

## 0. Chart identity

- **Repository:** `lostlight530/auto-doc-engine`
- **Stage:** `A / 2024-Q1`
- **Charting date:** `2026-09-21`
- **Method:** single-producer structured extraction; same-producer review
- **Coverage:** `SEARCH_BOUNDED`

## 1. Research questions served

RQ1 typed identity/relations; RQ2 computational manuscripts/multi-format records; RQ3 release/proposal/lineage boundaries.

## 2. Predeclared variables

| Variable | Definition |
|---|---|
| authority_state | released / revision / proposal / explanatory-doc |
| object_identity | distinct research object/event |
| temporal_anchor | event/release/tag date |
| machine_semantics | typed objects/relations or structured workflow semantics |
| representation_count | one vs multi-format outputs |
| validation_state | what was actually validated/reproduced |
| source_family | producer lineage |

## 3. Object-level chart

| Object | Problem | Method/architecture | Observed evidence | Validation/reproduction | Limits |
|---|---|---|---|---|---|
| O1 DataCite 4.5 | richer research-resource identity/relations | controlled types + relation vocabulary | official released schema | schema existence verified; no corpus validation | metadata != truth |
| O2 Quarto 1.4 | computational scholarly publication across formats | notebook/qmd source + manuscript site + alternate formats | official docs + Q1 tag commits | no runtime reproduction | common origin != semantic equivalence |
| O3 DataCite March RFC | future metadata evolution | public proposal/RFC | official RFC explicitly non-final | proposal status verified | not normative release |

## 4. Finding/evidence chart

| ID | Claim/observation | Sources | Authority | Independence | Time |
|---|---|---|---|---|---|
| F1 | Schema 4.5 released 2024-01-22 | S1,S3 | direct | same-family | Q1 |
| F2 | Added Instrument, StudyRegistration, IsCollectedBy/Collects | S1,S2 | direct | same-family | Q1 |
| F3 | Publisher identifiers added | S1,S2 | direct | same-family | Q1 |
| F4 | Quarto 1.4 revisions anchored Jan/Feb/Mar | S6-S8 | direct repo history | same-family | Q1 |
| F5 | Manuscripts link computation sources and multiple publication formats | S4,S5 | direct docs, retrospective | same-family | 1.4 semantics |
| F6 | March RFC was not a complete schema release | S9 | direct | same-family | 2024-03-26 |
| F7 | Release/proposal/revision require distinct authority states | S1,S6-S9 | synthesis | cross-family | Stage interpretation |

## 5. Comparative dimensions

| Object | Version state | Structured lineage | Multi-format | Normative status |
|---|---|---|---|---|
| O1 | released schema | explicit relations | docs in web/PDF forms | released |
| O2 | release line | source/project/render derivation implied by workflow | yes | software/docs release |
| O3 | proposal event | proposes future change | n/a | non-final proposal |

## 6. Counterevidence / contradiction matrix

| Issue | Supporting | Narrowing evidence | State |
|---|---|---|---|
| richer metadata means better truth | none required | schema sources do not claim truth validation | resolved: unsupported inference |
| multi-format means reproducible | S4 shows linked computations | no execution/reproduction evidence | unresolved/not established |
| March RFC modifies 4.5 | chronological proximity | S9 explicitly says not complete version | resolved: false conflation |

## 7. Negative space

| Expected element | Checked | Result | Boundary |
|---|---|---|---|
| adoption evidence | selected official sources | not found | do not infer non-adoption |
| independent reproduction | selected Quarto sources | not executed | do not infer failure |
| semantic equivalence across formats/tags | docs/tag history | not established | same origin/version line is insufficient |

## 8. Appraisal

Primary-source authority high for release/feature status; independence low within each project family; adoption/reproducibility evidence absent by design.

## 9. Amendments

`NONE`.

## 10. Chart limitations

No frozen 2024 Quarto documentation snapshot was independently archived in this run. Current docs are temporally qualified.

## 11. Analytic notes

Across objects, Q1 evidence is strongest for **structured identity and inspectable derivation**, not for scientific correctness. The key longitudinal variable for future Stages should be whether systems move from representing lineage to validating or reproducing the processes that lineage points to.
