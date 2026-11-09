# Independent A1 — auto-doc-engine — 2026-11-09 Stage L source custody

## Identity and scope
- Repository: `lostlight530/auto-doc-engine`; task: `independent-maintenance/A1`.
- Logical date: 2026-11-09 Asia/Shanghai; review cut: 23:10:21 +08:00.
- A1 scope: November 01–08 inclusive. Nov09 is excluded from A1 and reserved for A2.
- Exact pre-write main: `12faa33b40ccfa2006d73d3d9b7c7cdc2b9e9891`.
- Prior A1 Nov01–07: `maintenance/frontier-research/annotations/2026-11-08_A1_STAGE_SOURCE_CONTENT.md` @ `2781b12435aa95271e0742e1d0dc9504db433de8`; inherited as a prior review, not claimed as a fresh reread of all earlier sources.
- Prior A2 Nov08: `maintenance/frontier-research/annotations/2026-11-08_A2_MONTH_RELATION.md` @ `62dc981037d3f75f066d220874bf4c42caafd795`.
- D7 Nov08: `maintenance/2026-11-08-d7-operational-continuity.md` @ `7ee067723f02f400596c49db43c3b3abcb325799`.
- Current index: `maintenance/frontier-research/LONGITUDINAL_INDEX.md` @ `8a5e12a9ad7d1d341a0b1aaf7d55b4f99ed1c47e`.
- The 2026-09-25 ten-repository SOP requires full month-start→N−1 coverage and A1 merge before fresh A2. It does not impose a universal 100-added-lines-per-PR gate.

## Exact Stage and D7 source custody
| Object | Blob SHA | Role |
|---|---|---|
| `stage-l-2026-q4/STAGE_BRIEF.md` | `188959128611ed93718425bcb558c63086075378` | Stage identity and selection boundary |
| `stage-l-2026-q4/L1_PANDOC_3121.md` | `a7ff01595bf4d3d5f69db227d0c2207b076b4829` | selected Pandoc 3.12.1 source object |
| `stage-l-2026-q4/L2_UV_0130.md` | `72884f553ece39f8f65c253f8e3f49eb26ec8fa2` | selected uv 0.13.0 source object |
| `LONGITUDINAL_INDEX.md` | `8a5e12a9ad7d1d341a0b1aaf7d55b4f99ed1c47e` | current routing/index |
| `2026-11-08-d7-operational-continuity.md` | `7ee067723f02f400596c49db43c3b3abcb325799` | D7 operational-continuity audit |

## Nov08-specific findings and decisions
1. Stage L remains a live 2026-Q4 research object, not a newly generated daily Stage-L experiment for each November date.
2. Stage L selection remains anchored to the October19 source cut; later upstream releases are candidates, not automatic replacements of the selected baseline.
3. Pandoc 3.12.1 and uv 0.13.0 are different publisher objects with separate version clocks and separate runtime responsibilities.
4. A Pandoc release note does not prove this repository executed that binary or preserved document semantics on a fixed corpus.
5. uv's interpreter default and lock/resolution metadata do not establish the interpreter actually used by a repository process.
6. YAML duplicate-key rejection and numeric-scalar parsing are distinct parser behaviors and require distinct fixtures.
7. FODT format support is not byte identity, citation fidelity or scientific semantic equivalence.
8. Citeproc/CSL, Pandoc executable, output artifact digest and rendering environment must remain separately versioned.
9. The D7 report records Nov01 as an empty prior-artifact baseline and Nov02–07 as A1/A2 maintenance objects; those are not seven Stage-L executions.
10. D7's Stage-L result is PARTIAL and records no native Pandoc/uv fixed-corpus execution.
11. The D7 report's post-merge current revision was explicitly subject to refresh; the current main index is the controlling routing object for this A1 cut.
12. The Nov08 A1 and A2 files are present on main, but the current index header still says relation-through Nov07. This is current pointer drift, not evidence that the Nov08 A2 file is absent.
13. The index's Nov08 D7 correction from Nov06 to Nov07 was valid at its author-time cut; the later Nov08 A2 is a separate successor and should not be backdated into that D7 observation.
14. The current pointer needs a forward update only after the new A1 is merged and a fresh A2 is produced; this A1 does not edit the index.
15. No current Stage L source selection, Stage Brief, MANIFEST calendar snapshot, converter implementation or runtime is changed by this A1.

## Month-to-date coverage and decision matrix
| Window | Evidence owner | Decision |
|---|---|---|
| Nov01 | Prior A1 / empty month-start baseline | INHERIT_PRIOR_A1 |
| Nov02–07 | Prior A1 source review and six dated A1/A2 pairs | INHERIT_PRIOR_A1 |
| Nov08 | D7 operational-continuity report, current index, Stage L brief and selected source objects | REVIEWED; APPEND_RELATION / CURRENT_POINTER_DRIFT |
| Nov09 | Excluded from A1 | A2_INPUT_ONLY |
| Nov10–30 | Future dates | NOT_DUE |

- Month 2026-11 remains OPEN; Stage L 2026-Q4 remains IN_PROGRESS.
- A1 covers Nov01–08 through exact predecessor review plus the Nov08 D7/index/Stage owner inspection.
- No runtime, converter, paper reproduction, publisher test or scientific artifact comparison was executed.
- Result: `A1_COVERAGE_COMPLETE_WITH_NOV08_D7_AND_INDEX_RECONCILIATION_IDENTIFIED`; the pointer repair is reserved for A2 after A1 merge.
