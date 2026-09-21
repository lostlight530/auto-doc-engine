# Source and Research-Object Register — Stage C / 2024-Q3

## Identity

- Repository: `lostlight530/auto-doc-engine`
- Stage: `C / 2024-Q3`
- Specification: `2026-09-19-first-batch`
- Register date: `2026-09-22`
- Coverage: `SEARCH_BOUNDED`

## Identity rules

```text
dependency declaration != resolved lock state
lock state != executed environment
converter version != target semantic equivalence
artifact attestation != scientific validity
release planning != released specification
later patch != rewrite of earlier artifact
```

## Research objects

| ID | Object | Type | Q3 event/state | Identity basis |
|---|---|---|---|---|
| O1 | uv 0.3 project interface | package/project manager release line | announced 2024-08-20 | Astral announcement + changelog |
| O2 | Pandoc 3.3 | converter release | 2024-07-28/29 | official release history/announcement |
| O3 | Pandoc 3.4 | converter release | 2024-09-10 | official announcement |
| O4 | Matplotlib 3.9.1 | plotting-library release | 2024-07-04, announcement 2024-07-06 | official release documentation |
| O5 | Matplotlib 3.9.2 | plotting-library patch release | 2024-08-12 | official release statistics/docs |
| O6 | RO-Crate 1.2 release-planning issue | release-process event | opened 2024-09-09 | project issue/milestone state |

## Evidence sources

| ID | Source | Family | Date/state | Authority | Limitation |
|---|---|---|---|---|---|
| S1 | https://astral.sh/blog/uv-unified-python-packaging | Astral uv | 2024-08-20 | release/interface announcement | producer source |
| S2 | https://github.com/astral-sh/uv/blob/main/changelogs/0.3.x.md | Astral uv | versioned changelog | 0.3 behavior/change inventory | mutable current branch |
| S3 | https://docs.astral.sh/uv/concepts/projects/layout/ | Astral uv | current docs | lockfile conceptual explanation | contains later features; retrospective use bounded |
| S4 | https://pandoc.org/releases.html | Pandoc | 3.3 dated 2024-07-28 | official release history | producer source |
| S5 | https://github.com/jgm/pandoc/discussions/10167 | Pandoc | 2024-09-10 | 3.4 announcement | producer source |
| S6 | https://discourse.matplotlib.org/t/matplotlib-announce-ann-matplotlib-3-9-1/24539 | Matplotlib | 2024-07-06 announcement | 3.9.1 release/fix summary | producer source |
| S7 | https://matplotlib.org/3.9.2/users/github_stats.html | Matplotlib | 2024-08-12 | 3.9.2 release chronology | no independent behavior reproduction |
| S8 | https://github.com/ResearchObject/ro-crate/issues/353 | RO-Crate | opened 2024-09-09 | release-process/milestone state | not release proof |

## Source-family map

- SF1: S1-S3 — Astral uv
- SF2: S4-S5 — Pandoc
- SF3: S6-S7 — Matplotlib
- SF4: S8 — RO-Crate community/project

Cross-family convergence supports a broader provenance interpretation but does not prove causal influence

## State/correction register

| Object | Earlier state | Q3 state | Treatment |
|---|---|---|---|
| O2 Pandoc 3.3 | 3.2.1 regression exists | nested-list regression fixed | forward correction; earlier state preserved |
| O4/O5 Matplotlib | 3.9.1 attested artifacts + fixes | 3.9.2 later bugfix state | provenance validity does not erase behavior revision |
| O6 RO-Crate | release procedure opened | planning/milestone state | do not classify as released 1.2 in Q3 |

## Limitations

No local uv environment recreation, Pandoc conversion matrix, attestation verification, Matplotlib execution or RO-Crate packaging run was executed
