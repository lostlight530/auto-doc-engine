# Source and Research-Object Register — Stage A / 2024-Q1

## 0. Register identity

- **Repository:** `lostlight530/auto-doc-engine`
- **Stage:** `A / 2024-Q1`
- **Specification:** `2026-09-19-first-batch`
- **Register date:** `2026-09-21`
- **Source cutoff:** `2026-09-21`
- **Coverage:** `SEARCH_BOUNDED`

## 1. Identity rules

```text
object != report
source != object unless explicitly dual-role
multiple sources may describe one object
same-origin restatement != independent corroboration
proposal != released version
patch progression != semantic equivalence
current documentation != frozen historical snapshot
later correction != rewrite of earlier release
```

## 2. Research-object register

| ID | Canonical name | Type | Version/revision | Q1 event date(s) | Identity basis | Notes |
|---|---|---|---|---|---|---|
| O1 | DataCite Metadata Schema | released schema | 4.5 | 2024-01-22 | official schema + release history | Q1 normative release |
| O2 | Quarto 1.4 release line | computational-document release line | 1.4.x | 2024-01-24, 2024-02-15, 2024-03-05 selected tag anchors | GitHub tags + official docs | grouped release-line object |
| O3 | DataCite Metadata Schema RFC | proposal event | 2024-03-26 RFC | 2024-03-26 | official RFC post | explicitly not a complete schema version |
| O4 | Pandoc January maintenance release | document converter release | 3.1.11.1 | 2024-01-06 | official GitHub release | output validation/layout fixes |
| O5 | Pandoc 3.1.12 release family | document converter release line | 3.1.12–3.1.12.3 | 2024-02-15 through 2024-03-18 | official GitHub releases | includes forward corrections and accessibility/writer changes |
| O6 | Typst | document compiler release | 0.11.0 | 2024-03-15 | official changelog + GitHub release | table structure + template packages |

## 3. Evidence-source register

| ID | Source | Type | Family | Publication/event date | Access date | Authority | Limitations |
|---|---|---|---|---|---|---|---|
| S1 | https://schema.datacite.org/meta/kernel-4.5/ | official schema | DataCite | 2024-01-22 | 2026-09-21 | normative released schema | producer source |
| S2 | https://datacite.org/blog/introducing-datacite-metadata-schema-4-5/ | official release explanation | DataCite | 2024-01-24 | 2026-09-21 | release semantics/rollout | same family as S1 |
| S3 | https://schema.datacite.org/versions.html | release history | DataCite | mutable | 2026-09-21 | version chronology | later mutable page |
| S4 | https://quarto.org/docs/manuscripts/ | official docs | Quarto | current; identifies manuscripts as 1.4 feature | 2026-09-21 | feature semantics | not frozen Q1 snapshot |
| S5 | https://github.com/quarto-dev/quarto-cli/blob/main/news/changelog-1.4.md | changelog | Quarto | mutable branch view | 2026-09-21 | 1.4 feature/change inventory | current branch view |
| S6 | https://github.com/quarto-dev/quarto-cli/commit/8fa73d2233a0309ca089a888bad96d7e2a9224a4 | tag commit | Quarto | 2024-01-24 | 2026-09-21 | January version anchor | not feature/adoption proof |
| S7 | https://github.com/quarto-dev/quarto-cli/commit/69168152ee3532fa7c14149b95512f0e3653f646 | tag commit | Quarto | 2024-02-15 | 2026-09-21 | February version anchor | not semantic-equivalence proof |
| S8 | https://github.com/quarto-dev/quarto-cli/commit/d7a62ccf866a2b749ecb12d2810b31eba90fa021 | tag commit | Quarto | 2024-03-05 | 2026-09-21 | March version anchor | not semantic-equivalence proof |
| S9 | https://datacite.org/blog/metadata-schema-rfc-march_2024/ | official RFC | DataCite | 2024-03-26 | 2026-09-21 | proposal status/scope | non-normative proposal |
| S10 | https://github.com/jgm/pandoc/releases/tag/3.1.11.1 | official release | Pandoc | 2024-01-06 | 2026-09-21 | release behavior/fixes | project source |
| S11 | https://github.com/jgm/pandoc/releases/tag/3.1.12 | official release | Pandoc | 2024-02-15 | 2026-09-21 | release behavior/fixes | project source |
| S12 | https://github.com/jgm/pandoc/releases/tag/3.1.12.1 | official patch release | Pandoc | 2024-02-18 | 2026-09-21 | forward correction | project source |
| S13 | https://github.com/jgm/pandoc/releases/tag/3.1.12.2 | official patch release | Pandoc | 2024-03-01 | 2026-09-21 | accessibility/writer corrections | project source |
| S14 | https://github.com/jgm/pandoc/releases/tag/3.1.12.3 | official patch release | Pandoc | 2024-03-18 | 2026-09-21 | writer/renderer compatibility | project source |
| S15 | https://typst.app/docs/changelog/0.11.0/ | official changelog | Typst | 2024-03-15 | 2026-09-21 | 0.11 feature semantics | producer source |
| S16 | https://github.com/typst/typst/releases/tag/v0.11.0 | official release | Typst | 2024-03-15 | 2026-09-21 | release anchor | same family as S15 |

## 4. Source-to-object mapping

| Object | Source(s) | Relation | Directness | Independence |
|---|---|---|---|---|
| O1 | S1,S2,S3 | defines/announces/records | direct | same-family |
| O2 | S4,S5 | documents | direct, retrospective | same-family |
| O2 | S6,S7,S8 | anchors revisions | direct | same-family |
| O3 | S9 | defines proposal status | direct | same-family with O1 |
| O4 | S10 | records release/fixes | direct | single-family |
| O5 | S11-S14 | records release + forward corrections | direct | single-family |
| O6 | S15,S16 | defines/records release | direct | same-family |

## 5. Source-family / independence map

| Family | Members | Common origin | Independence limitation |
|---|---|---|---|
| SF1 | S1,S2,S3,S9 | DataCite | same producer; multiple pages are not independent corroboration |
| SF2 | S4,S5,S6,S7,S8 | Quarto | docs/tags from same project |
| SF3 | S10-S14 | Pandoc | release notes from same project |
| SF4 | S15,S16 | Typst | changelog/release from same project |

Cross-family convergence can support a broader research-engineering interpretation, but does not prove causal influence among projects.

## 6. Corrections, retractions, supersession

| Object | Change | Date | Treatment | Research effect |
|---|---|---|---|---|
| O5 | 3.1.12.1 corrects regressions in 3.1.12 | 2024-02-18 | forward patch | earlier release remains historical |
| O5 | 3.1.12.2 adds/fixes target accessibility and writer behavior | 2024-03-01 | forward patch | target-specific semantics become clearer |
| O5 | 3.1.12.3 adjusts Typst writer after Typst 0.11 behavior | 2024-03-18 | compatibility correction | renderer/compiler version becomes material |
| O3 | RFC proposes future DataCite changes | 2024-03-26 | proposal event, not supersession | no rewrite of 4.5 state |

## 7. Identity conflicts / unresolved temporal questions

- Exact first-stable Quarto 1.4 release date was not established in the declared research. Treatment: `UNKNOWN`; selected Q1 tag commits only establish active revisions.
- Current Quarto manuscript documentation is not treated as a frozen 2024 snapshot.
- No claim is made that Pandoc patch-level outputs are semantically equivalent.

## 8. Register limitations

Primary-source-heavy, English-language, search-bounded reconstruction. No exhaustive package-index survey, adoption study, artifact corpus analysis, or runtime reproduction was executed.
