# Source and Research-Object Register — Stage A / 2024-Q1

## 0. Register identity

- **Repository:** `lostlight530/auto-doc-engine`
- **Stage:** `A / 2024-Q1`
- **Specification:** `2026-09-19-first-batch`
- **Register date:** `2026-09-21`
- **Source cutoff:** `2026-09-21`

## 1. Identity rules

```text
object != report
source != object unless explicitly dual-role
multiple sources may describe one object
same-origin restatement != independent corroboration
proposal != released version
patch progression != semantic equivalence
```

## 2. Research-object register

| ID | Canonical name | Type | Version | Event/start date | Identity basis | Notes |
|---|---|---|---|---|---|---|
| O1 | DataCite Metadata Schema | released schema | 4.5 | 2024-01-22 | official release history/schema | Q1 normative release |
| O2 | Quarto 1.4 release line | software/document workflow release line | 1.4.x | Q1 2024 | Q1 tag commits + official docs | grouped across selected Q1 patches |
| O3 | DataCite Metadata Schema RFC | proposal event | 2024-03-26 RFC | 2024-03-26 | official RFC post | not a complete released schema version |

## 3. Evidence-source register

| ID | Source | Type | Family | Date | Authority | Limitations |
|---|---|---|---|---|---|---|
| S1 | https://schema.datacite.org/meta/kernel-4.5/ | official schema | DataCite | 2024-01-22 | released schema | producer source |
| S2 | https://datacite.org/blog/introducing-datacite-metadata-schema-4-5/ | official release post | DataCite | 2024-01-24 | release interpretation/rollout | same family as S1 |
| S3 | https://schema.datacite.org/versions.html | official release history | DataCite | mutable page | version chronology | current page accessed retrospectively |
| S4 | https://quarto.org/docs/manuscripts/ | official docs | Quarto | current; identifies manuscripts as 1.4 feature | feature semantics | not frozen Q1 snapshot |
| S5 | https://github.com/quarto-dev/quarto-cli/blob/main/news/changelog-1.4.md | changelog | Quarto | mutable branch view | 1.4 feature/change inventory | current branch view |
| S6 | https://github.com/quarto-dev/quarto-cli/commit/8fa73d2233a0309ca089a888bad96d7e2a9224a4 | tag commit | Quarto | 2024-01-24 | Q1 version anchor | not adoption evidence |
| S7 | https://github.com/quarto-dev/quarto-cli/commit/69168152ee3532fa7c14149b95512f0e3653f646 | tag commit | Quarto | 2024-02-15 | Q1 version anchor | not semantic-equivalence evidence |
| S8 | https://github.com/quarto-dev/quarto-cli/commit/d7a62ccf866a2b749ecb12d2810b31eba90fa021 | tag commit | Quarto | 2024-03-05 | Q1 version anchor | not semantic-equivalence evidence |
| S9 | https://datacite.org/blog/metadata-schema-rfc-march_2024/ | official RFC post | DataCite | 2024-03-26 | proposal status/scope | proposal, not normative release |

## 4. Source-to-object mapping

| Object | Source | Relation | Directness | Independence |
|---|---|---|---|---|
| O1 | S1 | defines | direct | same-family |
| O1 | S2 | announces/explains | direct | same-family |
| O1 | S3 | records release | direct | same-family |
| O2 | S4 | documents feature | direct, retrospective | same-family |
| O2 | S5 | records release-line changes | direct | same-family |
| O2 | S6,S7,S8 | anchors revisions | direct | same-family |
| O3 | S9 | defines proposal event/status | direct | same-family with O1 sources |

## 5. Source-family map

| Family | Members | Common origin | Limitation |
|---|---|---|---|
| SF1 | S1,S2,S3,S9 | DataCite | repeated statements are not independent corroboration |
| SF2 | S4,S5,S6,S7,S8 | Quarto project | docs/tags originate from same project |

## 6. Corrections / supersession

No Q1 correction/retraction identified for O1 in the declared search. O3 is not treated as a correction to O1; it is a proposal event.

## 7. Identity conflicts

Exact “first stable” Quarto 1.4 release date was not established from the selected evidence. Treatment: `UNKNOWN`; Q1 tag commits are used only to establish active 1.4 revisions during the quarter.

## 8. Limitations

Search-bounded, English-language, primary-source-heavy reconstruction. No exhaustive adoption or archival snapshot study.
