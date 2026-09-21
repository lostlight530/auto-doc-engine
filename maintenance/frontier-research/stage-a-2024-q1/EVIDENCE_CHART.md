# Evidence Chart — Stage A / 2024-Q1

## 0. Chart identity

- **Repository:** `lostlight530/auto-doc-engine`
- **Stage:** `A / 2024-Q1`
- **Charting date:** `2026-09-21`
- **Charting method:** single-producer structured extraction; same-producer review
- **Coverage:** `SEARCH_BOUNDED`

## 1. Research questions served

- RQ1: typed research-object identity and relation semantics.
- RQ2: computational manuscripts and multi-format publication.
- RQ3: release/proposal/correction/lineage state.

## 2. Predeclared chart variables

| Variable | Definition | Coding |
|---|---|---|
| authority_state | source/object governance state | RELEASED / REVISION / PATCH / PROPOSAL / CURRENT_DOC |
| temporal_anchor | date relevant to historical Stage | explicit event/release/tag date |
| relation_semantics | machine-readable object relation present? | explicit / implicit / none |
| representation_surface | document/output representations involved | named formats/workflows |
| validation_scope | validation actually evidenced | format-specific / structural / none observed |
| correction_mode | how later change relates to earlier state | forward patch / proposal / unknown |
| source_family | evidence-producing actor/project | SF1-SF4 |
| reproduction_state | independent execution/reproduction | EXECUTED / NOT_EXECUTED / UNKNOWN |

## 3. Object-level chart

| Object | Problem addressed | Method/architecture | Observed evidence | Validation/reproduction | Known limits |
|---|---|---|---|---|---|
| O1 DataCite 4.5 | richer identity and relation graph | controlled resource types + typed relations | official released schema | version/release verified; no corpus study | metadata != truth |
| O2 Quarto 1.4 | computational manuscript + multiple publication forms | source notebooks/qmd + manuscript outputs | current official docs + Q1 tag anchors | no runtime reproduction | current docs != frozen Q1 snapshot |
| O3 DataCite March RFC | future metadata change governance | explicit RFC/proposal | official proposal text | proposal status verified | not normative |
| O4 Pandoc 3.1.11.1 | output structural/layout correctness | multi-format conversion fixes | official release notes | release evidence only | no local conversion run |
| O5 Pandoc 3.1.12 family | expanding formats + target-specific accessibility/compatibility | readers/writers + patches | release/patch notes | some upstream project validation described; not rerun here | generated != semantically equivalent |
| O6 Typst 0.11.0 | richer structured authoring + reusable templates | document compiler + package templates | official changelog/release | no local compile | structure != accessibility/scientific correctness |

## 4. Finding/evidence chart

| ID | Claim/observation | Object(s) | Sources | Evidence class | Authority/directness | Independence | Time |
|---|---|---|---|---|---|---|---|
| F1 | DataCite 4.5 released 2024-01-22 | O1 | S1,S3 | released specification | direct | same-family | Jan |
| F2 | Instrument, StudyRegistration and IsCollectedBy/Collects added | O1 | S1,S2 | schema semantics | direct | same-family | Jan |
| F3 | Publisher identifiers added | O1 | S1,S2 | schema semantics | direct | same-family | Jan |
| F4 | Quarto 1.4 has selected revisions in Jan/Feb/Mar | O2 | S6-S8 | repository tag history | direct | same-family | Q1 |
| F5 | Manuscripts connect computation sources with multiple publication representations | O2 | S4,S5 | official docs | direct but retrospective | same-family | 1.4 semantics |
| F6 | Pandoc January fixes show generated outputs can still require structural/layout repair | O4 | S10 | release evidence | direct | single-family | Jan |
| F7 | Pandoc 3.1.12 expands conversion surface with Djot I/O | O5 | S11 | release evidence | direct | single-family | Feb |
| F8 | Pandoc 3.1.12.1 distinguishes target accessibility/validation behavior | O5 | S12 | patch evidence | direct | single-family | Feb |
| F9 | Pandoc 3.1.12.2 maps SVG alt text into ARIA semantics | O5 | S13 | patch evidence | direct | single-family | Mar |
| F10 | Typst 0.11 adds richer table structure and template packages | O6 | S15,S16 | release evidence | direct | same-family | Mar |
| F11 | Pandoc 3.1.12.3 adapts Typst writer to Typst 0.11 behavior | O5,O6 | S14,S15 | cross-project compatibility observation | direct within each family | cross-family convergence | Mar |
| F12 | DataCite March RFC is explicitly not a complete schema version | O3 | S9 | proposal-status evidence | direct | same-family | Mar |
| F13 | authority state must distinguish released/revision/patch/proposal | O1-O6 | Stage synthesis | analytic | derived | cross-family | Q1 |
| F14 | multi-format lineage needs representation-specific validation and version provenance | O2,O4-O6 | Stage synthesis | analytic | derived | cross-family | Q1 |

## 5. Comparative dimensions

| Object | Authority state | Structured identity/lineage | Multi-format concern | Correction/version concern | Scientific validation |
|---|---|---|---|---|---|
| O1 | RELEASED | explicit typed metadata relations | docs web/PDF | mutable docs under stable schema version | not established |
| O2 | REVISION_LINE | project/source/output lineage | strong | patch-level state unresolved | not established |
| O3 | PROPOSAL | candidate future relation to schema | n/a | must not rewrite O1 | n/a |
| O4 | RELEASE/PATCH | conversion derivation | strong | output validity fixes | not established |
| O5 | RELEASE+PATCHES | conversion derivation + target semantics | strong | forward corrections | not established |
| O6 | RELEASED | template/package/source derivation | compiler output | compiler behavior matters downstream | not established |

## 6. Counterevidence / competing interpretation matrix

| Issue | Initial/simple interpretation | Narrowing evidence | Resolution |
|---|---|---|---|
| richer metadata means better truth | typed relation seems authoritative | DataCite defines representation, not scientific verification | unsupported inference |
| common project/source means outputs equivalent | Quarto/Pandoc derive multiple outputs | target-specific fixes show format semantics differ | rejected |
| a successful render is enough | file exists | Pandoc structural/accessibility fixes show successful generation can still be deficient | rejected |
| later patch means earlier release was “really” fixed | patch corrects regression | dated releases preserve earlier behavior | rejected; forward correction |
| March RFC supersedes January schema | same producer + later date | RFC explicitly non-final | rejected |
| template reuse guarantees reproducibility | template pins presentation logic | compiler/template versions and environment still matter | not established |

## 7. Negative-space chart

| Expected/claimed element | Evidence checked | Result | Interpretation boundary |
|---|---|---|---|
| DataCite 4.5 adoption in Q1 | official release material | no independent adoption study in declared set | no non-adoption inference |
| Quarto manuscript reproduction | docs + tag history | `NOT_EXECUTED` | no reproducibility claim |
| cross-format semantic equivalence | Pandoc/Quarto release/docs | not established | common source lineage insufficient |
| WCAG conformance | target accessibility fixes | not evaluated | accessibility support != certification |
| deterministic reproduction across Typst/Pandoc versions | release notes | not executed | compatibility change is evidence of risk, not failure rate |
| scientific correctness of documents | all selected tooling sources | outside evidence scope | structured documentation != scientific validity |

## 8. Appraisal

Primary sources are authoritative for their own releases/specifications. Source-family independence is low within each object, but cross-family convergence is meaningful for the general mechanism: independent projects expose similar needs for version identity, target-specific semantics, correction lineage, and machine-readable structure.

## 9. Charting amendments

The initial chart included DataCite and Quarto only. During month-by-month reconstruction, Pandoc and Typst were added because they directly exposed target-format validation and cross-renderer compatibility, materially strengthening RQ2/RQ3. This expansion increases coverage but means the Stage remains `SEARCH_BOUNDED`, not pre-registered exhaustive research.

## 10. Chart limitations

No local executables were run; no output files were generated and compared; no archival snapshots of mutable docs were independently fetched; no adoption telemetry or corpus analysis was conducted.

## 11. Analytic notes

The strongest cross-month pattern is a transition from **representation richness** in January toward **representation-specific validation and correction** in February and **dependency/version governance** in March. The Stage therefore treats provenance as a layered record: object identity + source identity + tool/template/compiler version + output identity + validation event + later correction state.
