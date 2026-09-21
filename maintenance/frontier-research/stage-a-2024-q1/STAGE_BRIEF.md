# Frontier Research Stage Brief — Stage A / 2024-Q1

## 0. Identity

- **Repository:** `lostlight530/auto-doc-engine`
- **Specification version:** `2026-09-19-first-batch`
- **Stage ID:** `A`
- **Canonical period:** `2024-Q1`
- **Research window:** `2024-01-01 through 2024-03-31`
- **Record type:** `RETROSPECTIVE`
- **Research design class(es):** `HISTORICAL_FRONTIER_RECONSTRUCTION + TARGETED_EVIDENCE_SYNTHESIS + COMPARATIVE_TECHNICAL_STUDY`
- **Coverage class intended:** `SEARCH_BOUNDED`
- **Protocol/reconstruction date:** `2026-09-21`
- **Research cutoff:** `2026-09-21`
- **Status:** `COMPLETE`

## 1. Rationale

This is the first historical Stage instantiated from the first-batch frontier-research specification. The specification itself uses `stage-a-2024-q1/` as the suggested first instantiated directory, so this reconstruction treats 2024-Q1 as the canonical starting window rather than deriving a different quarter from later repository history.

The Stage asks what changed in Q1 2024 around machine-actionable research-object identity, relation semantics, computational manuscripts, multi-format scholarly records, and versioned documentation. It is not a reconstruction of this repository's own 2024 state; the repository did not yet exist in its present form. It is an external frontier reconstruction through the repository's current research lens.

## 2. Repository lens and non-claims

Lens: **research artifacts, document evidence, provenance, process disclosure, typed lineage, research objects, artifact durability, and multi-format research records.**

Hard boundaries:

- `lineage != truth`
- `supersedes != predecessor invalid`
- `hash identity != semantic equivalence`
- `assertion basis != correctness`
- `coverage != quality`
- `research-object packaging != independent reproduction`

Additional Stage non-claims:

- a metadata relation does not establish scientific causality or truth;
- a manuscript bundle does not establish reproducibility;
- a release tag does not establish adoption;
- a proposal/RFC does not equal a released normative schema;
- current documentation used retrospectively does not prove all described details were available on every Q1 date.

## 3. Objectives and research questions

### Objective

Reconstruct bounded Q1 2024 developments that materially changed or clarified how research outputs, process objects, computational manuscripts, and versioned documentation could be represented and carried across scholarly workflows.

### Research questions

1. **RQ1:** What Q1 2024 changes expanded typed identity and relation semantics for research outputs and research-process objects?
2. **RQ2:** What Q1 2024 developments strengthened computational manuscript and multi-format publication workflows, and what did those workflows not establish about durability or reproduction?
3. **RQ3:** How should released specifications, patch/release lines, and forward proposals be represented without conflating proposal, supersession, or semantic equivalence?

## 4. Conceptual scope

Included: persistent-identifier metadata, typed research resources, explicit relations, computational manuscript structure, notebook/source linkage, multi-format outputs, release/version evidence, proposal-versus-release status, and documentation mutability.

Excluded: broad bibliometrics, general publishing economics, journal acceptance rates, scientific validity of content carried by these formats, and adoption claims not directly supported by selected evidence.

## 5. Temporal scope

- Event window: 2024-01-01 through 2024-03-31.
- Later sources may be used only to reconstruct or explain Q1 objects.
- Q1 release/tag dates are separated from 2026 access dates.
- Later documentation changes are not projected backward as if known in Q1.

## 6. Eligibility and selection logic

### Inclusion

- primary specification/release material with a Q1 event date;
- official project documentation tied to a Q1 release line;
- official release/tag history sufficient to anchor temporal existence;
- proposals published in Q1 when proposal status is explicit and analytically relevant.

### Exclusion

- secondary summaries when a primary source is available;
- sources whose only material event falls outside Q1 unless used as retrospective context;
- generic tooling changes with no relation to the repository lens.

### Hold / unresolved

- exact first-stable Quarto 1.4 release boundary is not inferred from current docs alone; Q1 tag commits are used as temporal anchors.
- current Quarto manuscript documentation is treated as retrospective explanatory material, not a frozen Q1 snapshot.

Multiple reports of one release/specification are grouped to one research object.

## 7. Source classes and authority plan

| Source class | Intended use | What it can establish | What it cannot establish |
|---|---|---|---|
| Official schema/specification | released metadata semantics | versioned terms, relations, release date | adoption, scientific correctness |
| Official project docs | feature semantics | documented workflow/feature behavior | exact historical availability unless version-anchored |
| GitHub tag/commit | temporal/version anchor | existence of tagged revisions at dates | adoption or semantic equivalence |
| Official RFC/blog | proposal/event status | proposal scope and date | released normative state |

## 8. Discovery and search design

| ID | Surface | Exact query/navigation method | Limits | RQ |
|---|---|---|---|---|
| Q1 | Web search | `"DataCite Metadata Schema 4.5" 2024` | official DataCite preferred | RQ1,RQ3 |
| Q2 | Web search | `"DataCite Schema 4.5" StudyRegistration Instrument January 2024` | official DataCite | RQ1 |
| Q3 | Web search | `"Quarto 1.4" manuscripts 2024 release stable` | Quarto/GitHub preferred | RQ2 |
| Q4 | Web search | `"Quarto Manuscripts" 1.4 2024` | Quarto official docs | RQ2 |
| Q5 | Direct GitHub history | Quarto tags `v1.4.549`, `v1.4.550`, `v1.4.551` | tag commit dates only | RQ2,RQ3 |
| Q6 | Web search | DataCite 2024-03-26 metadata schema RFC | official DataCite | RQ3 |

No exhaustive literature-search claim is made.

## 9. Research-object model

A released schema version is one object. A later RFC is a separate event object even when produced by the same organization. Quarto 1.4 Q1 patch/tag revisions are grouped into one release-line object because the Stage question concerns the evolving 1.4 manuscript/multi-format surface rather than patch-level bug genealogy.

## 10. Planned research Parts

| Part | Title | Question |
|---|---|---|
| A1 | Typed research-object identity and relation expansion | RQ1 |
| A2 | Computational manuscripts and multi-format scholarly records | RQ2 |
| A3 | Release, proposal, and lineage boundaries | RQ3 |

## 11. Planned extraction / charting

Object/version, event date, resource/relation semantics, source-vs-output structure, multi-format behavior, provenance/process disclosure, normative status, mutability, source-family independence, and explicit non-claims.

## 12. Critical appraisal plan

`DESCRIPTIVE SOURCE-AUTHORITY APPRAISAL`. Primary official sources are used for what they directly define or report. No universal quality score is used.

## 13. Analysis and synthesis plan

Chronological + comparative analysis. Distinguish released state from proposal, object identity from source count, and documented workflow from validated reproduction.

## 14. Longitudinal comparability plan

Future Stages should retain: exact quarter window, object/source separation, release-vs-proposal status, source-family map, and the same repository hard boundaries. Topic mix may evolve.

## 15. Review plan

- Research review required: **YES**
- Desired independence: `INDEPENDENT_REVIEW preferred`
- Review actually available in this run: `SAME_PRODUCER_REVIEW`
- Search-method review: **YES**
- Domain specialist review: **CONDITIONAL**

## 16. Contributor responsibility and instrument provenance plan

Human Maintainer retains final governance responsibility. The ChatGPT agent performs bounded discovery, evidence curation, analysis, drafting, and same-producer review. Web search and GitHub connectors are instruments, not authors.

## 17. Amendment / deviation record

`NONE`.

## 18. Completion and stopping criteria

Stage can close when all three Parts are complete, shared sources/objects are registered, structured evidence is charted, synthesis preserves unresolved boundaries, review is completed with independence status explicit, contribution provenance is recorded, and safe handoff is bounded.

## 19. Update / correction triggers

A dated correction is required if a historical release date, version identity, source status, or a material interpretation is later shown incorrect; later adoption evidence belongs to a later Stage or longitudinal synthesis.

## 20. Expected outputs

- `STAGE_BRIEF.md`
- `A1_TYPED_RESEARCH_OBJECTS.md`
- `A2_COMPUTATIONAL_MANUSCRIPTS.md`
- `A3_RELEASE_PROPOSAL_LINEAGE.md`
- `SOURCE_OBJECT_REGISTER.md`
- `EVIDENCE_CHART.md`
- `CONTRIBUTOR_STATEMENT.md`
- `STAGE_SYNTHESIS.md`
- `RESEARCH_REVIEW.md`
- `STAGE_HANDOFF.md`
- repository-level `LONGITUDINAL_INDEX.md`
