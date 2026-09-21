# Frontier Research Part A2 — Computational Manuscripts and Multi-Format Scholarly Records

## 0. Part identity

- **Repository:** `lostlight530/auto-doc-engine`
- **Stage:** `A / 2024-Q1`
- **Part ID:** `A2`
- **Research design:** `HISTORICAL_FRONTIER_RECONSTRUCTION + COMPARATIVE_TECHNICAL_STUDY`
- **Window:** `2024-01-01 through 2024-03-31`
- **Reconstructed:** `2026-09-21`
- **Coverage:** `SEARCH_BOUNDED`
- **Status:** `COMPLETE`

## 1. Research question

> What Q1 2024 developments strengthened computational manuscript and multi-format publication workflows, and what did those workflows not establish about durability or reproduction?

## 2. Scope and unit of analysis

Object O2 is the Quarto 1.4 release line as it existed across Q1 2024. Patch/tag revisions `v1.4.549`, `v1.4.550`, and `v1.4.551` are temporal anchors within one release-line object.

## 3. Eligibility

Include official Quarto documentation and direct GitHub tag commits. Exclude current features not tied to 1.4 semantics. Current Quarto docs are used retrospectively only where they explicitly identify a feature as belonging to 1.4.

## 4. Discovery/search method

| ID | Surface | Exact method | Executed | Limitation |
|---|---|---|---|---|
| Q1 | web | `"Quarto 1.4" manuscripts 2024 release stable` | 2026-09-21 | current pages may have evolved |
| Q2 | web | `"Quarto Manuscripts" 1.4 2024` | 2026-09-21 | explanatory, not frozen snapshot |
| Q3 | GitHub | fetch commits for tags `v1.4.549`, `v1.4.550`, `v1.4.551` | 2026-09-21 | anchors existence/date, not adoption |

## 5. Object/source selection

O2 INCLUDE. No adoption studies were added because the Stage question is about workflow capability and record structure.

## 6. Source authority and provenance

- **S4:** Quarto Manuscripts documentation: https://quarto.org/docs/manuscripts/
- **S5:** Quarto 1.4 changelog: https://github.com/quarto-dev/quarto-cli/blob/main/news/changelog-1.4.md
- **S6:** `v1.4.549` tag commit, 2024-01-24: https://github.com/quarto-dev/quarto-cli/commit/8fa73d2233a0309ca089a888bad96d7e2a9224a4
- **S7:** `v1.4.550` tag commit, 2024-02-15: https://github.com/quarto-dev/quarto-cli/commit/69168152ee3532fa7c14149b95512f0e3653f646
- **S8:** `v1.4.551` tag commit, 2024-03-05: https://github.com/quarto-dev/quarto-cli/commit/d7a62ccf866a2b749ecb12d2810b31eba90fa021

S4/S5/S6-S8 are one project/source family.

## 7. Evidence extraction

| Finding | Sources | Evidence class | Time boundary |
|---|---|---|---|
| F4 Quarto 1.4 was an active release line in each month of Q1 | S6,S7,S8 | repository tag/commit evidence | Q1 2024 |
| F5 Manuscripts are identified by Quarto as a 1.4 feature | S4,S5 | official documentation | retrospective explanation of 1.4 |
| F6 Manuscript projects link source computations/notebooks with article and multiple output formats | S4 | official documentation | feature semantics; accessed 2026 |

## 8. Observations

### O1 — A computational manuscript could make source computation part of the publication surface

Quarto documents manuscript projects as allowing notebooks or `.qmd` documents to be source material while also exposing computations alongside the article.

### O2 — One project could emit and route multiple representations

The manuscript workflow exposes an article website plus formats such as PDF and Word, and can link notebook representations and supporting artifacts.

### O3 — Q1 tag history anchors the 1.4 line without proving every current detail existed at every patch

The Q1 tags establish that the 1.4 line was actively versioned through January, February, and March 2024. They do not make the current manuscript documentation a bit-for-bit historical snapshot.

## 9. Counterevidence / alternative interpretation

A single source project controls the docs and release tags, so this evidence is not independent validation. Multi-format publication can increase inspectability while also increasing equivalence risk: HTML, PDF, DOCX, notebook output, and source code may diverge in rendering or execution semantics.

## 10. Negative space

- Independent reproduction of manuscript computations: `NOT_EXECUTED`
- Equivalence testing across emitted formats: `NOT_EXECUTED`
- Evidence that a notebook link guarantees environment reconstruction: `NOT_FOUND_IN_DECLARED_SEARCH`
- Broad publisher acceptance of all output forms: not established.

## 11. Critical appraisal

High authority for feature/release identity; weak for adoption and reproducibility outcomes.

## 12. Analysis

Quarto 1.4 is significant to auto-doc-engine because it narrows the distance between “document” and “research process record.” A notebook can be both an authoring/execution source and part of the publication surface; the same project can route readers toward multiple rendered forms and computation artifacts.

That creates richer process disclosure but also a lineage challenge. A PDF, HTML article, source notebook, and downloadable archive may share a project origin without being semantically interchangeable. A durable documentation engine therefore needs explicit artifact identity and derivation rather than assuming “same project” means “same meaning.”

## 13. Interpretation

**Observed:** Q1 tags exist; current official docs identify manuscripts as a 1.4 feature and describe source/notebook + multi-format publication.  
**Inference:** this is a strong external convergence toward multi-format research-record bundles.  
**Unknown:** exact feature behavior at each Q1 patch without frozen historical docs/runtime execution.

## 14. Relation to repository

`PARALLEL_CONVERGENCE` for multi-format research records and process disclosure.  
`DELIBERATE_BOUNDARY`: this repository should not equate common source lineage with semantic equivalence or independent reproduction.

## 15. Current-repository implication

No implementation/contract change is justified by this Part alone.

## 16. Method deviations

Current documentation was used as a retrospective explanatory source; temporal overreach is mitigated by Q1 tag anchors and explicit uncertainty about patch-level feature completeness.

## 17. Contribution/provenance

No Quarto runtime was installed or executed. No manuscript was rendered.

## 18. Part conclusion

`SUPPORTED_OBSERVATION / PARALLEL_CONVERGENCE`

Q1 2024 Quarto 1.4 provides a concrete example of scholarly documents becoming multi-representation computational research records. The correct boundary is **shared source/project lineage != semantic equivalence != independent reproduction**.

## 19. Unresolved questions

- Which manuscript subfeatures were stable at each Q1 patch?
- How often do downstream publisher conversions preserve computation-linked context?

## 20. Inputs to synthesis

Carry forward multi-format convergence, the need for derivation identity, and the retrospective-doc limitation.
