# Longitudinal Frontier Index

## 0. Identity

- **Repository:** `lostlight530/auto-doc-engine`
- **Specification:** `2026-09-19-first-batch`
- **Index coverage:** `Stage A / 2024-Q1` + `Stage B / 2024-Q2` + `Stage C / 2024-Q3` + `Stage D / 2024-Q4` + `Stage E / 2025-Q1` + `Stage F / 2025-Q2` + `Stage G / 2025-Q3`
- **Index updated:** `2026-09-26`

## 1. Purpose and boundary

```text
index = navigation + temporal relationships + correction routing
index != Stage synthesis
index != longitudinal synthesis
index != current repository authority
```

## 2. Stage registry

| Stage | Period | Exact window | Record type | Design | Coverage | Status | Synthesis | Review | Handoff |
|---|---|---|---|---|---|---|---|---|---|
| A | 2024-Q1 | 2024-01-01 through 2024-03-31 | RETROSPECTIVE | HISTORICAL_FRONTIER_RECONSTRUCTION + TARGETED_EVIDENCE_SYNTHESIS + COMPARATIVE_TECHNICAL_STUDY | SEARCH_BOUNDED | FRONTIER_STAGE_COMPLETE | stage-a-2024-q1/STAGE_SYNTHESIS.md | stage-a-2024-q1/RESEARCH_REVIEW.md | stage-a-2024-q1/STAGE_HANDOFF.md |
| B | 2024-Q2 | 2024-04-01 through 2024-06-30 | RETROSPECTIVE | HISTORICAL_FRONTIER_RECONSTRUCTION + TARGETED_EVIDENCE_SYNTHESIS + COMPARATIVE_TECHNICAL_STUDY | SEARCH_BOUNDED | FRONTIER_STAGE_COMPLETE | stage-b-2024-q2/STAGE_SYNTHESIS.md | stage-b-2024-q2/RESEARCH_REVIEW.md | stage-b-2024-q2/STAGE_HANDOFF.md |
| C | 2024-Q3 | 2024-07-01 through 2024-09-30 | RETROSPECTIVE | HISTORICAL_FRONTIER_RECONSTRUCTION + TARGETED_EVIDENCE_SYNTHESIS + COMPARATIVE_TECHNICAL_STUDY | SEARCH_BOUNDED | FRONTIER_STAGE_COMPLETE | stage-c-2024-q3/STAGE_SYNTHESIS.md | stage-c-2024-q3/RESEARCH_REVIEW.md | stage-c-2024-q3/STAGE_HANDOFF.md |\n| D | 2024-Q4 | 2024-10-01 through 2024-12-31 | RETROSPECTIVE | HISTORICAL_FRONTIER_RECONSTRUCTION + TARGETED_EVIDENCE_SYNTHESIS + COMPARATIVE_TECHNICAL_STUDY | SEARCH_BOUNDED | FRONTIER_STAGE_COMPLETE | stage-d-2024-q4/STAGE_SYNTHESIS.md | stage-d-2024-q4/RESEARCH_REVIEW.md | stage-d-2024-q4/STAGE_HANDOFF.md |
| E | 2025-Q1 | 2025-01-01 through 2025-03-31 | RETROSPECTIVE | HISTORICAL_FRONTIER_RECONSTRUCTION + TARGETED_EVIDENCE_SYNTHESIS + COMPARATIVE_TECHNICAL_STUDY | SEARCH_BOUNDED | FRONTIER_STAGE_COMPLETE | stage-e-2025-q1/STAGE_SYNTHESIS.md | stage-e-2025-q1/RESEARCH_REVIEW.md | stage-e-2025-q1/STAGE_HANDOFF.md |
| F | 2025-Q2 | 2025-04-01 through 2025-06-30 | RETROSPECTIVE | HISTORICAL_FRONTIER_RECONSTRUCTION + TARGETED_EVIDENCE_SYNTHESIS + COMPARATIVE_TECHNICAL_STUDY | SEARCH_BOUNDED | FRONTIER_STAGE_COMPLETE | stage-f-2025-q2/STAGE_SYNTHESIS.md | stage-f-2025-q2/RESEARCH_REVIEW.md | stage-f-2025-q2/STAGE_HANDOFF.md |
| G | 2025-Q3 | 2025-07-01 through 2025-09-30 | RETROSPECTIVE | HISTORICAL_FRONTIER_RECONSTRUCTION + TARGETED_EVIDENCE_SYNTHESIS + COMPARATIVE_TECHNICAL_STUDY | SEARCH_BOUNDED | FRONTIER_STAGE_COMPLETE | stage-g-2025-q3/STAGE_SYNTHESIS.md | stage-g-2025-q3/RESEARCH_REVIEW.md | stage-g-2025-q3/STAGE_HANDOFF.md |

## 3. Correction registry

No Stage A correction record existed at initial close. A post-merge method-provenance reconciliation was added later on 2026-09-21 without rewriting the original Stage conclusion.

| Correction | Class | Trigger | Effect |
|---|---|---|---|
| [CORRECTION_2026-09-21_STAGE_A_METHOD_AMENDMENT.md](corrections/CORRECTION_2026-09-21_STAGE_A_METHOD_AMENDMENT.md) | METHOD_RECONCILIATION | Stage Brief section 17 said `NONE` while Chart/Synthesis/Review/Index already recorded source-set expansion | routes the current method account to the preserved initial-close record; no finding/runtime/contract change |

## 4. Method-version registry

| Stage | Specification | Material method note | Comparability |
|---|---|---|---|
| A | 2026-09-19-first-batch | initial source set expanded during monthly deepening; amendment preserved in chart/synthesis | baseline for later stages |
| B | 2026-09-19-first-batch | Q2 object set fixed before synthesis; no material amendment | comparable on temporal integrity, source-family discipline, transformation provenance and correction semantics |
| C | 2026-09-19-first-batch | Q3 object set fixed before synthesis; no material amendment | comparable on artifact identity, environment provenance, transformation state, build provenance and correction semantics |\n| D | 2026-09-19-first-batch | Q4 object set fixed before synthesis; later 2025 lifecycle states are not back-projected | comparable on dependency/environment identity, converter configuration, security behavior and release lifecycle |
| E | 2026-09-19-first-batch | Q1 2025 object set fixed before synthesis; post-Q1 RO-Crate release used only for temporal bounding | comparable on converter revision, lock identity, environment/release lifecycle and temporal integrity |
| F | 2026-09-19-first-batch | Q2 2025 object set fixed before synthesis; no local SBOM/converter/RO-Crate replay | comparable on composition identity, transformation fidelity, packaging and publication state |
| G | 2026-09-19-first-batch | Q3 2025 object set fixed before synthesis; no CodeMeta validation, immutable-release/attestation verification, or Pandoc replay | comparable on typed metadata relationships, publication immutability/provenance, and structural transformation identity |

## 5. Longitudinal synthesis registry

Seven completed Stages now cover 2024-Q1 through 2025-Q3. Earlier syntheses remain preserved; the additive current cross-year extension is `longitudinal/LONGITUDINAL_SYNTHESIS_2024_TO_2025_Q3.md`. No earlier Stage or synthesis is rewritten.

## 6. Known gaps in sequence

- Periods before 2024-Q1 are not researched by this sequence.
- 2025-Q4+ is not yet instantiated.
- The additive cross-year synthesis currently ends at 2025-Q3.
- Stage A is search-bounded and does not claim exhaustive coverage.

## 7. Navigation notes

For Stage A start with `stage-a-2024-q1/STAGE_BRIEF.md`; Stage B with `stage-b-2024-q2/STAGE_BRIEF.md`; Stage C with `stage-c-2024-q3/STAGE_BRIEF.md`; Stage D with `stage-d-2024-q4/STAGE_BRIEF.md`; Stage E with `stage-e-2025-q1/STAGE_BRIEF.md`; Stage F with `stage-f-2025-q2/STAGE_BRIEF.md`; Stage G with `stage-g-2025-q3/STAGE_BRIEF.md`. Read thematic Parts and month reconstructions before each Stage synthesis/review. Preserve prior syntheses and use `longitudinal/LONGITUDINAL_SYNTHESIS_2024_TO_2025_Q3.md` for the latest additive cross-year view.


## A2 current-state reconciliation — 2026-09-23

Stage D / 2024-Q4 and the A→D longitudinal synthesis are now present on current main and belong to the active frontier-research documentation surface.

Current routing boundary:

```text
STAGE_D_PRESENT
!= RUNTIME_CAPABILITY_ADDED

LONGITUDINAL_LINKED
!= SCIENTIFIC_TRUTH_ESTABLISHED

STAGE_HANDOFF
!= AUTHORITY_TRANSFER
```

The index is a current navigation/lineage surface. Earlier Stage A/B/C artifacts remain point-in-time research records and are not rewritten to match Stage D conclusions.

## SEPTEMBER_DUAL_CUTOFF_MAINTENANCE_2026-09-23

### A1 / N-1 cutoff — 2026-09-22

- September review scope includes the Stage A, B, and C research sets delivered on 2026-09-21, their source/object registers, evidence charts, month reconstructions, reviews, syntheses, handoffs, and current router/manifest state.
- These are documentary/research artifacts. Their existence does not by itself establish runtime execution, scientific truth, downstream reproduction, or release validity.
- The 2026-09-22 router/manifest remains a point-in-time cutoff; later Stage D presence must not be projected backward.
- Stage-level handoff records preserve context and lineage but do not transfer authority or validation automatically.

### A2 / N cutoff — 2026-09-23

- Stage D / 2024-Q4 and the A→D longitudinal synthesis/index are current 2026-09-23 repository state.
- Documentary closure across A→D does not become runtime capability, scientific validation, independent reproduction, or a release claim.
- Current longitudinal routing may include Stage D only as later state; it does not rewrite the 2026-09-22 router cutoff.
- This A2 current-state annotation extends A1 and preserves the earlier stage chronology.
## SEPTEMBER_DUAL_CUTOFF_MAINTENANCE_2026-09-24

### A1 / N-1 cutoff — full September Stage A→D review through 2026-09-23

- Re-read Stage A, B, C and D research sets, their source/object registers, evidence charts, month reconstructions, reviews, syntheses and handoffs, plus the full-year longitudinal synthesis and current routing.
- Stage completion is documentary/research completion only.
- Current A→D linkage does not establish runtime equivalence, scientific validation, independent reproduction, or release authority.
- Later Stage D presence remains later current state and is not projected backward into earlier router/stage availability.
- Existing correction/reconciliation remains authoritative and additive.
### A2 / N cutoff — 2026-09-24 current-state reconciliation

The merged A1 review already covers the full September Stage A→D history through 2026-09-23.

At the 2026-09-24 current cut:
- Stage A, B, C and D remain the complete retained frontier-research stage set.
- No Stage E / later-stage directory is retained on current main.
- The A→D longitudinal synthesis remains the current additive full-year documentary owner.
- Current routing does not convert documentary closure into runtime capability, scientific validity, independent reproduction, or release authority.
- Earlier stage availability and router cutoffs remain point-in-time history.

```text
CURRENT_STAGE_SET = A_TO_D
NO_STAGE_E_PATH_OBSERVED
!= FUTURE_STAGE_IMPOSSIBLE
DOCUMENTARY_CLOSURE
!= RUNTIME_CLOSURE
```


## Stage E current reconciliation — 2026-09-24

The earlier A2 note correctly recorded that no Stage E path existed at its observation cut. Stage E / 2025-Q1 was researched and added later on 2026-09-24.

```text
EARLIER_NO_STAGE_E_OBSERVED
+
LATER_STAGE_E_DELIVERY
!= EARLIER_OBSERVATION_ERROR
!= HISTORY_REWRITE
```

Current frontier-research routing now covers A→E. Stage E remains documentary/research evidence and does not add runtime capability, scientific validation, independent reproduction, or release authority.


## Stage F current reconciliation — 2026-09-25

Stage F / 2025-Q2 was researched after the Stage E close and extends current routing from A→E to A→F.

```text
STAGE_E_COMPLETE
+
LATER_STAGE_F_DELIVERY
!= STAGE_E_REWRITE

STAGE_F_RESEARCH
!= RUNTIME_CAPABILITY
!= SCIENTIFIC_VALIDATION
!= LOCAL_CONFORMANCE
```

## 中秋加班维护补充 — A1 / 2026-09-24

本段是以 2026-09-24 为 N 日的回顾性维护关系记录. 当前仓库已经继续演进到更晚 Stage, 这里不把后来的 Stage E/F 写回 9 月 23 日以前的可用性.

中秋加班维护重新检查 9 月 1 日至 9 月 23 日范围内的 Stage research、month reconstruction、source/object register、evidence chart、review、synthesis、handoff 与 longitudinal routing. 对 auto-doc-engine, 核心不是文件越多越完整, 而是 artifact identity、lineage 与 assertion basis 有没有被误写成 truth.

后来的 Stage E/F 证明的是后续研究继续发生. 它们不能让早期 router cutoff 变成错误, 也不能把 handoff 升格为 authority transfer. 同样, hash、路径连续或文档生成成功都不能自动证明 semantic equivalence 或 runtime capability.

本轮只在 longitudinal owner 中补充分期关系, 不机械回写每个历史 Stage 文件.

```text
LATER_STAGE_E_F
!= EARLIER_STAGE_AVAILABILITY
LINEAGE
!= TRUTH
HANDOFF
!= AUTHORITY_TRANSFER
DOCUMENT_GENERATED
!= RUNTIME_VALIDATED
```

## 中秋加班维护补充 — A2 / N = 2026-09-24

A1 已先合并. 本段对 logical N = 2026-09-24 做一次后来完成的关系 reconciliation, 因而必须同时保留两个事实: 早先的 9 月 24 日 A2 cut 当时只观察到 Stage A→D, 而 Stage E / 2025-Q1 在同日更晚时间才进入仓库.

因此新的月内关系可以把 Stage E 作为 9 月 24 日的 later-same-day delivery 纳入 current interpretation, 但不能把它伪装成早先 A2 执行时已经可见. 9 月 25 日 Stage F 仍然属于 next-day evidence, 不进入 N 日 cut.

对 auto-doc-engine, 这次更新继续保持 artifact identity、lineage、handoff 与 truth/authority 的分离. Stage E 的出现扩展 routing, 不产生 runtime capability 或 scientific validation.

```text
EARLIER_2026_09_24_A2_OBSERVED_A_TO_D
+
LATER_SAME_DAY_STAGE_E
=
RECONCILED_N_DAY_RELATION

LATER_SAME_DAY_DELIVERY
!= EARLIER_AVAILABILITY
STAGE_F_2026_09_25
!= N_DAY_INPUT
```


## 2026-09-25 A1 — full September coverage through 2026-09-24

Base revision: `44a7028e05d70f9d9091d8d1cfeea8506f209bc8`. Cutoff: 2026-09-24 Asia/Shanghai.

Coverage decision summary:
- September Stage A-D research sets and their Parts, source/object registers, evidence charts, month reconstructions, reviews, syntheses, handoffs, router/manifest, and longitudinal owners were re-read through the cutoff.
- Previously reviewed A-D artifacts remain `NO_FOLLOW_UP` unless an existing dated reconciliation already owns a correction.
- Documentary closure and lineage remain documentary evidence only. `lineage != truth`; handoff does not transfer scientific or release authority.
- Stage F material delivered on 2026-09-25 is later current evidence and is outside this A1 cutoff.
- No runtime capability, independent reproduction, or release status is inferred from current path presence.

```text
DOCUMENTARY_CLOSURE
!= RUNTIME_CAPABILITY
LINEAGE
!= TRUTH
HANDOFF
!= AUTHORITY_TRANSFER
LATER_STAGE_F
!= 2026_09_24_CUTOFF_STATE
```


## 2026-09-25 A2 — current longitudinal relation with Stage F

Base revision after merged A1: `181c16cb1ced33ab9f7ea8d015441316ac11f455`. N-day delivery input: Stage F / 2025-Q2 narrative merged on 2026-09-25.

Current relational evolution:
- The merged A1 cutoff through 2026-09-24 remains intact and excludes Stage F from the earlier cutoff state.
- Stage F is now current repository state and may be routed into the longitudinal index as later documentary/research evidence for the 2025-Q2 logical research period.
- Delivery on 2026-09-25 does not rewrite when earlier Stage A-D evidence was available.
- Composition, packaging, lineage, reconstruction, synthesis, and handoff remain documentary semantics. They do not establish runtime capability, scientific truth, independent reproduction, or release authority.
- No historical Stage body is rewritten.

```text
LOGICAL_RESEARCH_PERIOD_2025_Q2
!= DELIVERY_DATE_2026_09_25
CURRENT_STAGE_F_PRESENT
!= EARLIER_AVAILABILITY
DOCUMENTARY_LINEAGE
!= RUNTIME_CAPABILITY
```


## Stage G current reconciliation — 2026-09-26

Stage G / 2025-Q3 extends current frontier-research routing from A→F to A→G.

```text
STAGE_G_RESEARCH_PRESENT
!= RUNTIME_CAPABILITY
!= METADATA_TRUTH
!= RELEASE_SECURITY
!= LOCAL_PANDOC_REPLAY

LOGICAL_RESEARCH_PERIOD_2025_Q3
!= DELIVERY_DATE_2026_09_26
```

Earlier Stage A→F records and syntheses remain point-in-time research artifacts. The new A→G synthesis is additive and does not rewrite their historical availability or conclusions.

## SUCCESSOR_A1_FULL_COVERAGE_2026-09-26_FOR_LOGICAL_2026-09-25

- Maintenance task type: TEN_REPOSITORY_MONTHLY_A1_SUCCESSOR
- Logical maintenance date: 2026-09-25
- Historical A1 cutoff: 2026-09-24 Asia/Shanghai
- Historical thin A1 PR retained: #56
- Research plane: artifact/document evidence
- Successor purpose: expand the already-merged A1 into explicit artifact/decision coverage without rewriting its base-revision observation.
- Transport main contains later Stage F/G material; later availability is classified, never back-projected.
- Runtime/reproduction execution by this successor: NOT_EXECUTED
- History rewrite: NO

### Delivery chronology preserved

- Stage A / 2024-Q1: September research delivery retained as historical reconstruction.
- Stage B / 2024-Q2: September research delivery retained as historical reconstruction.
- Stage C / 2024-Q3: September research delivery retained as historical reconstruction.
- Stage D / 2024-Q4: later September delivery retained; current routing does not make it earlier evidence.
- Stage E / 2025-Q1: later-same-day 2026-09-24 delivery is preserved as later evidence relative to earlier 9/24 cuts.
- Stage F / 2025-Q2: 2026-09-25 delivery; excluded from A1 input and reserved for A2.
- Stage G / 2025-Q3: 2026-09-26 delivery; outside the logical 9/25 maintenance task.
- Earlier A→D/A→E syntheses remain point-in-time artifacts even though later syntheses now exist.

### Artifact-family coverage ledger

#### Stage A
- STAGE_BRIEF: REVIEWED_FOR_PRESENCE_RELATION_AND_EXISTING_CORRECTION; decision = NO_FOLLOW_UP unless an existing dated reconciliation already owns a correction.
- RESEARCH_PARTS: REVIEWED_FOR_PRESENCE_RELATION_AND_EXISTING_CORRECTION; decision = NO_FOLLOW_UP unless an existing dated reconciliation already owns a correction.
- SOURCE_OBJECT_REGISTER: REVIEWED_FOR_PRESENCE_RELATION_AND_EXISTING_CORRECTION; decision = NO_FOLLOW_UP unless an existing dated reconciliation already owns a correction.
- EVIDENCE_CHART: REVIEWED_FOR_PRESENCE_RELATION_AND_EXISTING_CORRECTION; decision = NO_FOLLOW_UP unless an existing dated reconciliation already owns a correction.
- MONTH_RECONSTRUCTIONS: REVIEWED_FOR_PRESENCE_RELATION_AND_EXISTING_CORRECTION; decision = NO_FOLLOW_UP unless an existing dated reconciliation already owns a correction.
- STAGE_SYNTHESIS: REVIEWED_FOR_PRESENCE_RELATION_AND_EXISTING_CORRECTION; decision = NO_FOLLOW_UP unless an existing dated reconciliation already owns a correction.
- RESEARCH_REVIEW: REVIEWED_FOR_PRESENCE_RELATION_AND_EXISTING_CORRECTION; decision = NO_FOLLOW_UP unless an existing dated reconciliation already owns a correction.
- STAGE_HANDOFF: REVIEWED_FOR_PRESENCE_RELATION_AND_EXISTING_CORRECTION; decision = NO_FOLLOW_UP unless an existing dated reconciliation already owns a correction.
- Stage A chronology: preserve original research period and actual September delivery date as separate time axes.
- Stage A authority: documentary research only; no runtime/scientific authority inherited.
#### Stage B
- STAGE_BRIEF: REVIEWED_FOR_PRESENCE_RELATION_AND_EXISTING_CORRECTION; decision = NO_FOLLOW_UP unless an existing dated reconciliation already owns a correction.
- RESEARCH_PARTS: REVIEWED_FOR_PRESENCE_RELATION_AND_EXISTING_CORRECTION; decision = NO_FOLLOW_UP unless an existing dated reconciliation already owns a correction.
- SOURCE_OBJECT_REGISTER: REVIEWED_FOR_PRESENCE_RELATION_AND_EXISTING_CORRECTION; decision = NO_FOLLOW_UP unless an existing dated reconciliation already owns a correction.
- EVIDENCE_CHART: REVIEWED_FOR_PRESENCE_RELATION_AND_EXISTING_CORRECTION; decision = NO_FOLLOW_UP unless an existing dated reconciliation already owns a correction.
- MONTH_RECONSTRUCTIONS: REVIEWED_FOR_PRESENCE_RELATION_AND_EXISTING_CORRECTION; decision = NO_FOLLOW_UP unless an existing dated reconciliation already owns a correction.
- STAGE_SYNTHESIS: REVIEWED_FOR_PRESENCE_RELATION_AND_EXISTING_CORRECTION; decision = NO_FOLLOW_UP unless an existing dated reconciliation already owns a correction.
- RESEARCH_REVIEW: REVIEWED_FOR_PRESENCE_RELATION_AND_EXISTING_CORRECTION; decision = NO_FOLLOW_UP unless an existing dated reconciliation already owns a correction.
- STAGE_HANDOFF: REVIEWED_FOR_PRESENCE_RELATION_AND_EXISTING_CORRECTION; decision = NO_FOLLOW_UP unless an existing dated reconciliation already owns a correction.
- Stage B chronology: preserve original research period and actual September delivery date as separate time axes.
- Stage B authority: documentary research only; no runtime/scientific authority inherited.
#### Stage C
- STAGE_BRIEF: REVIEWED_FOR_PRESENCE_RELATION_AND_EXISTING_CORRECTION; decision = NO_FOLLOW_UP unless an existing dated reconciliation already owns a correction.
- RESEARCH_PARTS: REVIEWED_FOR_PRESENCE_RELATION_AND_EXISTING_CORRECTION; decision = NO_FOLLOW_UP unless an existing dated reconciliation already owns a correction.
- SOURCE_OBJECT_REGISTER: REVIEWED_FOR_PRESENCE_RELATION_AND_EXISTING_CORRECTION; decision = NO_FOLLOW_UP unless an existing dated reconciliation already owns a correction.
- EVIDENCE_CHART: REVIEWED_FOR_PRESENCE_RELATION_AND_EXISTING_CORRECTION; decision = NO_FOLLOW_UP unless an existing dated reconciliation already owns a correction.
- MONTH_RECONSTRUCTIONS: REVIEWED_FOR_PRESENCE_RELATION_AND_EXISTING_CORRECTION; decision = NO_FOLLOW_UP unless an existing dated reconciliation already owns a correction.
- STAGE_SYNTHESIS: REVIEWED_FOR_PRESENCE_RELATION_AND_EXISTING_CORRECTION; decision = NO_FOLLOW_UP unless an existing dated reconciliation already owns a correction.
- RESEARCH_REVIEW: REVIEWED_FOR_PRESENCE_RELATION_AND_EXISTING_CORRECTION; decision = NO_FOLLOW_UP unless an existing dated reconciliation already owns a correction.
- STAGE_HANDOFF: REVIEWED_FOR_PRESENCE_RELATION_AND_EXISTING_CORRECTION; decision = NO_FOLLOW_UP unless an existing dated reconciliation already owns a correction.
- Stage C chronology: preserve original research period and actual September delivery date as separate time axes.
- Stage C authority: documentary research only; no runtime/scientific authority inherited.
#### Stage D
- STAGE_BRIEF: REVIEWED_FOR_PRESENCE_RELATION_AND_EXISTING_CORRECTION; decision = NO_FOLLOW_UP unless an existing dated reconciliation already owns a correction.
- RESEARCH_PARTS: REVIEWED_FOR_PRESENCE_RELATION_AND_EXISTING_CORRECTION; decision = NO_FOLLOW_UP unless an existing dated reconciliation already owns a correction.
- SOURCE_OBJECT_REGISTER: REVIEWED_FOR_PRESENCE_RELATION_AND_EXISTING_CORRECTION; decision = NO_FOLLOW_UP unless an existing dated reconciliation already owns a correction.
- EVIDENCE_CHART: REVIEWED_FOR_PRESENCE_RELATION_AND_EXISTING_CORRECTION; decision = NO_FOLLOW_UP unless an existing dated reconciliation already owns a correction.
- MONTH_RECONSTRUCTIONS: REVIEWED_FOR_PRESENCE_RELATION_AND_EXISTING_CORRECTION; decision = NO_FOLLOW_UP unless an existing dated reconciliation already owns a correction.
- STAGE_SYNTHESIS: REVIEWED_FOR_PRESENCE_RELATION_AND_EXISTING_CORRECTION; decision = NO_FOLLOW_UP unless an existing dated reconciliation already owns a correction.
- RESEARCH_REVIEW: REVIEWED_FOR_PRESENCE_RELATION_AND_EXISTING_CORRECTION; decision = NO_FOLLOW_UP unless an existing dated reconciliation already owns a correction.
- STAGE_HANDOFF: REVIEWED_FOR_PRESENCE_RELATION_AND_EXISTING_CORRECTION; decision = NO_FOLLOW_UP unless an existing dated reconciliation already owns a correction.
- Stage D chronology: preserve original research period and actual September delivery date as separate time axes.
- Stage D authority: documentary research only; no runtime/scientific authority inherited.
#### Stage E
- STAGE_BRIEF: REVIEWED_FOR_PRESENCE_RELATION_AND_EXISTING_CORRECTION; decision = NO_FOLLOW_UP unless an existing dated reconciliation already owns a correction.
- RESEARCH_PARTS: REVIEWED_FOR_PRESENCE_RELATION_AND_EXISTING_CORRECTION; decision = NO_FOLLOW_UP unless an existing dated reconciliation already owns a correction.
- SOURCE_OBJECT_REGISTER: REVIEWED_FOR_PRESENCE_RELATION_AND_EXISTING_CORRECTION; decision = NO_FOLLOW_UP unless an existing dated reconciliation already owns a correction.
- EVIDENCE_CHART: REVIEWED_FOR_PRESENCE_RELATION_AND_EXISTING_CORRECTION; decision = NO_FOLLOW_UP unless an existing dated reconciliation already owns a correction.
- MONTH_RECONSTRUCTIONS: REVIEWED_FOR_PRESENCE_RELATION_AND_EXISTING_CORRECTION; decision = NO_FOLLOW_UP unless an existing dated reconciliation already owns a correction.
- STAGE_SYNTHESIS: REVIEWED_FOR_PRESENCE_RELATION_AND_EXISTING_CORRECTION; decision = NO_FOLLOW_UP unless an existing dated reconciliation already owns a correction.
- RESEARCH_REVIEW: REVIEWED_FOR_PRESENCE_RELATION_AND_EXISTING_CORRECTION; decision = NO_FOLLOW_UP unless an existing dated reconciliation already owns a correction.
- STAGE_HANDOFF: REVIEWED_FOR_PRESENCE_RELATION_AND_EXISTING_CORRECTION; decision = NO_FOLLOW_UP unless an existing dated reconciliation already owns a correction.
- Stage E chronology: preserve original research period and actual September delivery date as separate time axes.
- Stage E authority: documentary research only; no runtime/scientific authority inherited.

### Current routing/owner coverage

- LONGITUDINAL_INDEX: REVIEWED; successor adds explicit historical-cut routing only.
- latest pre-F longitudinal synthesis: REVIEWED as the A1-era current relation; later A→F/A→G files do not rewrite it.
- MANIFEST/router: REVIEWED through preserved dated annotations; later Stage presence is not earlier availability.
- DOCUMENT_STATUS: REVIEWED as current authority router, not as proof of stage execution.
- contributor statements: REVIEWED for provenance role only; they do not create peer-review independence.
- source/object registers: REVIEWED as identity/authority maps; register presence is not source truth.
- evidence charts: REVIEWED as bounded evidence summaries; chart inclusion is not scientific validation.
- month reconstructions: REVIEWED as retrospective records; reconstruction date is separate from logical research month.
- reviews: SAME_PRODUCER_REVIEW where declared; no independent review is invented.
- handoffs: context transfer only; no downstream authority inheritance is inferred.

### Hard-boundary verification

- metadata != truth
- lock != SBOM
- attestation != security/scientific validity
- AST identity != semantic equivalence
- handoff != authority transfer
- Stage completeness != runtime execution.
- Current path presence != earlier availability.
- Later stage delivery != earlier stage input.
- Retrospective reconstruction != contemporaneous 2025 execution.
- Search-bounded coverage != exhaustive field survey.
- Same project/source lineage != independent corroboration.
- Documentary correction != historical rewrite.
- A1 successor depth != new research credit.

### A1 decision summary

- Stage A: NO_FOLLOW_UP beyond existing reconciliation.
- Stage B: NO_FOLLOW_UP beyond existing reconciliation.
- Stage C: NO_FOLLOW_UP beyond existing reconciliation.
- Stage D: NO_FOLLOW_UP beyond existing reconciliation; later delivery chronology preserved.
- Stage E: APPEND_RELATION as later-same-day 2026-09-24 evidence where applicable; do not back-project into earlier same-day cuts.
- Stage F: NOT_A1_INPUT / defer to A2 because delivery is 2026-09-25.
- Stage G: OUTSIDE_LOGICAL_TASK / 2026-09-26 later evidence.
- Current month status: OPEN.
- Natural-month finalization: NOT_DUE.
- Runtime change authorized: NO.
- Contract change authorized: NO.
- Scientific validation/reproduction credit: NONE.
- Required next step: merge this A1 successor, fresh-read main, then build A2 from the merged state with Stage F as N-day input.

## SUCCESSOR_A2_CURRENT_MONTH_RELATION_2026-09-26_FOR_LOGICAL_2026-09-25

- Maintenance task type: TEN_REPOSITORY_MONTHLY_A2_SUCCESSOR
- Logical maintenance date: 2026-09-25
- Current-month relation: September delivery history through the N-day Stage F delivery
- Historical thin A2 PR retained: #57
- Required predecessor successor A1: #59
- Research plane: artifact/document evidence
- Stage G / 2025-Q3 delivered on 2026-09-26 and is explicitly outside this logical A2 input.
- History rewrite: NO
- Runtime/reproduction execution by this successor: NOT_EXECUTED

### A2 temporal compilation

- Stage A: retain prior September documentary delivery relation.
- Stage B: retain prior September documentary delivery relation.
- Stage C: retain prior September documentary delivery relation.
- Stage D: retain later September delivery chronology and prior corrections.
- Stage E: retain 2026-09-24 later-same-day delivery chronology without back-projecting to earlier same-day cuts.
- Stage F: APPEND_RELATION / Stage F / 2025-Q2 is the 2026-09-25 N-day input. It adds PEP 770 package composition/SBOM evidence, Pandoc 3.7.x revision-sensitive transformation/accessibility behavior, and RO-Crate 1.2 Recommendation packaging state.
- Stage G: LATER_EVIDENCE_2026-09-26 / OUTSIDE_LOGICAL_A2.

### Stage-by-stage artifact relation ledger

#### Stage A
- STAGE_BRIEF: RETAIN_A1_DECISION_NO_SILENT_REWRITE; preserve declared period, delivery date, source/object identity, review independence, and non-normative status.
- RESEARCH_PARTS: RETAIN_A1_DECISION_NO_SILENT_REWRITE; preserve declared period, delivery date, source/object identity, review independence, and non-normative status.
- SOURCE_OBJECT_REGISTER: RETAIN_A1_DECISION_NO_SILENT_REWRITE; preserve declared period, delivery date, source/object identity, review independence, and non-normative status.
- EVIDENCE_CHART: RETAIN_A1_DECISION_NO_SILENT_REWRITE; preserve declared period, delivery date, source/object identity, review independence, and non-normative status.
- MONTH_RECONSTRUCTIONS: RETAIN_A1_DECISION_NO_SILENT_REWRITE; preserve declared period, delivery date, source/object identity, review independence, and non-normative status.
- STAGE_SYNTHESIS: RETAIN_A1_DECISION_NO_SILENT_REWRITE; preserve declared period, delivery date, source/object identity, review independence, and non-normative status.
- RESEARCH_REVIEW: RETAIN_A1_DECISION_NO_SILENT_REWRITE; preserve declared period, delivery date, source/object identity, review independence, and non-normative status.
- STAGE_HANDOFF: RETAIN_A1_DECISION_NO_SILENT_REWRITE; preserve declared period, delivery date, source/object identity, review independence, and non-normative status.
- Stage A relation: inherited from merged A1 successor #59; no new authority is introduced.
- Stage A history: current later-stage presence does not alter its original September availability or conclusions.
- Stage A correction policy: existing dated correction/reconciliation remains the owner where present.
#### Stage B
- STAGE_BRIEF: RETAIN_A1_DECISION_NO_SILENT_REWRITE; preserve declared period, delivery date, source/object identity, review independence, and non-normative status.
- RESEARCH_PARTS: RETAIN_A1_DECISION_NO_SILENT_REWRITE; preserve declared period, delivery date, source/object identity, review independence, and non-normative status.
- SOURCE_OBJECT_REGISTER: RETAIN_A1_DECISION_NO_SILENT_REWRITE; preserve declared period, delivery date, source/object identity, review independence, and non-normative status.
- EVIDENCE_CHART: RETAIN_A1_DECISION_NO_SILENT_REWRITE; preserve declared period, delivery date, source/object identity, review independence, and non-normative status.
- MONTH_RECONSTRUCTIONS: RETAIN_A1_DECISION_NO_SILENT_REWRITE; preserve declared period, delivery date, source/object identity, review independence, and non-normative status.
- STAGE_SYNTHESIS: RETAIN_A1_DECISION_NO_SILENT_REWRITE; preserve declared period, delivery date, source/object identity, review independence, and non-normative status.
- RESEARCH_REVIEW: RETAIN_A1_DECISION_NO_SILENT_REWRITE; preserve declared period, delivery date, source/object identity, review independence, and non-normative status.
- STAGE_HANDOFF: RETAIN_A1_DECISION_NO_SILENT_REWRITE; preserve declared period, delivery date, source/object identity, review independence, and non-normative status.
- Stage B relation: inherited from merged A1 successor #59; no new authority is introduced.
- Stage B history: current later-stage presence does not alter its original September availability or conclusions.
- Stage B correction policy: existing dated correction/reconciliation remains the owner where present.
#### Stage C
- STAGE_BRIEF: RETAIN_A1_DECISION_NO_SILENT_REWRITE; preserve declared period, delivery date, source/object identity, review independence, and non-normative status.
- RESEARCH_PARTS: RETAIN_A1_DECISION_NO_SILENT_REWRITE; preserve declared period, delivery date, source/object identity, review independence, and non-normative status.
- SOURCE_OBJECT_REGISTER: RETAIN_A1_DECISION_NO_SILENT_REWRITE; preserve declared period, delivery date, source/object identity, review independence, and non-normative status.
- EVIDENCE_CHART: RETAIN_A1_DECISION_NO_SILENT_REWRITE; preserve declared period, delivery date, source/object identity, review independence, and non-normative status.
- MONTH_RECONSTRUCTIONS: RETAIN_A1_DECISION_NO_SILENT_REWRITE; preserve declared period, delivery date, source/object identity, review independence, and non-normative status.
- STAGE_SYNTHESIS: RETAIN_A1_DECISION_NO_SILENT_REWRITE; preserve declared period, delivery date, source/object identity, review independence, and non-normative status.
- RESEARCH_REVIEW: RETAIN_A1_DECISION_NO_SILENT_REWRITE; preserve declared period, delivery date, source/object identity, review independence, and non-normative status.
- STAGE_HANDOFF: RETAIN_A1_DECISION_NO_SILENT_REWRITE; preserve declared period, delivery date, source/object identity, review independence, and non-normative status.
- Stage C relation: inherited from merged A1 successor #59; no new authority is introduced.
- Stage C history: current later-stage presence does not alter its original September availability or conclusions.
- Stage C correction policy: existing dated correction/reconciliation remains the owner where present.
#### Stage D
- STAGE_BRIEF: RETAIN_A1_DECISION_NO_SILENT_REWRITE; preserve declared period, delivery date, source/object identity, review independence, and non-normative status.
- RESEARCH_PARTS: RETAIN_A1_DECISION_NO_SILENT_REWRITE; preserve declared period, delivery date, source/object identity, review independence, and non-normative status.
- SOURCE_OBJECT_REGISTER: RETAIN_A1_DECISION_NO_SILENT_REWRITE; preserve declared period, delivery date, source/object identity, review independence, and non-normative status.
- EVIDENCE_CHART: RETAIN_A1_DECISION_NO_SILENT_REWRITE; preserve declared period, delivery date, source/object identity, review independence, and non-normative status.
- MONTH_RECONSTRUCTIONS: RETAIN_A1_DECISION_NO_SILENT_REWRITE; preserve declared period, delivery date, source/object identity, review independence, and non-normative status.
- STAGE_SYNTHESIS: RETAIN_A1_DECISION_NO_SILENT_REWRITE; preserve declared period, delivery date, source/object identity, review independence, and non-normative status.
- RESEARCH_REVIEW: RETAIN_A1_DECISION_NO_SILENT_REWRITE; preserve declared period, delivery date, source/object identity, review independence, and non-normative status.
- STAGE_HANDOFF: RETAIN_A1_DECISION_NO_SILENT_REWRITE; preserve declared period, delivery date, source/object identity, review independence, and non-normative status.
- Stage D relation: inherited from merged A1 successor #59; no new authority is introduced.
- Stage D history: current later-stage presence does not alter its original September availability or conclusions.
- Stage D correction policy: existing dated correction/reconciliation remains the owner where present.
#### Stage E
- STAGE_BRIEF: RETAIN_A1_DECISION_NO_SILENT_REWRITE; preserve declared period, delivery date, source/object identity, review independence, and non-normative status.
- RESEARCH_PARTS: RETAIN_A1_DECISION_NO_SILENT_REWRITE; preserve declared period, delivery date, source/object identity, review independence, and non-normative status.
- SOURCE_OBJECT_REGISTER: RETAIN_A1_DECISION_NO_SILENT_REWRITE; preserve declared period, delivery date, source/object identity, review independence, and non-normative status.
- EVIDENCE_CHART: RETAIN_A1_DECISION_NO_SILENT_REWRITE; preserve declared period, delivery date, source/object identity, review independence, and non-normative status.
- MONTH_RECONSTRUCTIONS: RETAIN_A1_DECISION_NO_SILENT_REWRITE; preserve declared period, delivery date, source/object identity, review independence, and non-normative status.
- STAGE_SYNTHESIS: RETAIN_A1_DECISION_NO_SILENT_REWRITE; preserve declared period, delivery date, source/object identity, review independence, and non-normative status.
- RESEARCH_REVIEW: RETAIN_A1_DECISION_NO_SILENT_REWRITE; preserve declared period, delivery date, source/object identity, review independence, and non-normative status.
- STAGE_HANDOFF: RETAIN_A1_DECISION_NO_SILENT_REWRITE; preserve declared period, delivery date, source/object identity, review independence, and non-normative status.
- Stage E relation: inherited from merged A1 successor #59; no new authority is introduced.
- Stage E history: current later-stage presence does not alter its original September availability or conclusions.
- Stage E correction policy: existing dated correction/reconciliation remains the owner where present.
#### Stage F
- STAGE_BRIEF: APPEND_RELATION_FROM_N_DAY_STAGE_F; preserve declared period, delivery date, source/object identity, review independence, and non-normative status.
- RESEARCH_PARTS: APPEND_RELATION_FROM_N_DAY_STAGE_F; preserve declared period, delivery date, source/object identity, review independence, and non-normative status.
- SOURCE_OBJECT_REGISTER: APPEND_RELATION_FROM_N_DAY_STAGE_F; preserve declared period, delivery date, source/object identity, review independence, and non-normative status.
- EVIDENCE_CHART: APPEND_RELATION_FROM_N_DAY_STAGE_F; preserve declared period, delivery date, source/object identity, review independence, and non-normative status.
- MONTH_RECONSTRUCTIONS: APPEND_RELATION_FROM_N_DAY_STAGE_F; preserve declared period, delivery date, source/object identity, review independence, and non-normative status.
- STAGE_SYNTHESIS: APPEND_RELATION_FROM_N_DAY_STAGE_F; preserve declared period, delivery date, source/object identity, review independence, and non-normative status.
- RESEARCH_REVIEW: APPEND_RELATION_FROM_N_DAY_STAGE_F; preserve declared period, delivery date, source/object identity, review independence, and non-normative status.
- STAGE_HANDOFF: APPEND_RELATION_FROM_N_DAY_STAGE_F; preserve declared period, delivery date, source/object identity, review independence, and non-normative status.
- Stage F N-day meaning: Stage F / 2025-Q2 is the 2026-09-25 N-day input. It adds PEP 770 package composition/SBOM evidence, Pandoc 3.7.x revision-sensitive transformation/accessibility behavior, and RO-Crate 1.2 Recommendation packaging state.
- Stage F repository assessment remains NO_CURRENT_REPOSITORY_DRIFT / NO_RUNTIME_CHANGE / NO_CONTRACT_CHANGE where declared by its synthesis.
- Stage F completeness is documentary frontier research, not runtime execution or scientific validation.

### Longitudinal owner compilation

- Pre-F longitudinal synthesis remains a preserved point-in-time artifact.
- Stage F extends the current logical relation to A→F for 2026-09-25.
- Stage G/A→G files that now exist on current main are later 2026-09-26 evidence and are excluded from this A2 logical cut.
- LONGITUDINAL_INDEX may route later current state, but this successor records the explicit 9/25 historical relation separately.
- MANIFEST/DOCUMENT_STATUS later annotations do not rewrite earlier stage availability.
- Search-bounded stage coverage is not an exhaustive literature survey.
- SAME_PRODUCER_REVIEW is not upgraded to independent review.
- Documentary handoff is not authority transfer.

### Domain hard-boundary checks

- metadata presence != correctness
- SBOM/composition evidence != reproduction
- Pandoc release behavior != local replay
- RO-Crate publication != local conformance
- handoff != authority transfer
- Stage delivery != repository runtime change.
- Research synthesis != independent reproduction.
- Current file presence != earlier availability.
- Later Stage G != 2026-09-25 A2 input.
- A2 successor depth != new research credit.

### A2 successor disposition

- A1 predecessor merged before A2: YES.
- Stage A-E relation: RETAINED_FROM_A1.
- Stage F N-day input: INTEGRATED.
- Stage G 9/26 later state: EXCLUDED_FROM_LOGICAL_A2.
- Historical thin A2 retained: YES.
- Runtime/contract change authorized: NO.
- Scientific validation/reproduction credit: NONE.
- September status: OPEN.
- Natural-month finalization: NOT_DUE.
- Successor maintenance status: COMPLETE_FOR_LOGICAL_2026-09-25_A2.


## A1_MONTH_TO_DATE_REVALIDATION_2026-09-26

- Logical maintenance date: 2026-09-26
- Cutoff: 2026-09-25
- Exact base main: `6a0db92491a95bd5af9489b5232d3a0e5556f467`
- Scope: Stage A-F documentary lineage, longitudinal owner, retained stage packages and existing reconciliation.
- Stage G and 2026-09-26 annotation/support artifacts are later evidence reserved for A2.

### Coverage decisions
- 2026-09-01: REVIEWED / RETAIN_EXISTING_DECISION
- 2026-09-02: REVIEWED / RETAIN_EXISTING_DECISION
- 2026-09-03: REVIEWED / RETAIN_EXISTING_DECISION
- 2026-09-04: REVIEWED / RETAIN_EXISTING_DECISION
- 2026-09-05: REVIEWED / RETAIN_EXISTING_DECISION
- 2026-09-06: REVIEWED / RETAIN_EXISTING_DECISION
- 2026-09-07: REVIEWED / RETAIN_EXISTING_DECISION
- 2026-09-08: REVIEWED / RETAIN_EXISTING_DECISION
- 2026-09-09: REVIEWED / RETAIN_EXISTING_DECISION
- 2026-09-10: REVIEWED / RETAIN_EXISTING_DECISION
- 2026-09-11: REVIEWED / RETAIN_EXISTING_DECISION
- 2026-09-12: REVIEWED / RETAIN_EXISTING_DECISION
- 2026-09-13: REVIEWED / RETAIN_EXISTING_DECISION
- 2026-09-14: REVIEWED / RETAIN_EXISTING_DECISION
- 2026-09-15: REVIEWED / RETAIN_EXISTING_DECISION
- 2026-09-16: REVIEWED / RETAIN_EXISTING_DECISION
- 2026-09-17: REVIEWED / RETAIN_EXISTING_DECISION
- 2026-09-18: REVIEWED / RETAIN_EXISTING_DECISION
- 2026-09-19: REVIEWED / RETAIN_EXISTING_DECISION
- 2026-09-20: REVIEWED / RETAIN_EXISTING_DECISION
- 2026-09-21: REVIEWED / RETAIN_EXISTING_DECISION
- 2026-09-22: REVIEWED / RETAIN_EXISTING_DECISION
- 2026-09-23: REVIEWED / RETAIN_EXISTING_DECISION
- 2026-09-24: REVIEWED / RETAIN_EXISTING_DECISION
- 2026-09-25: REVIEWED / RETAIN_STAGE_F_RELATION / NO_FOLLOW_UP. Stage F remains documentary frontier research delivered on 2026-09-25, not runtime/scientific validation.

### Boundary
- Declared research period != delivery date.
- Lineage/provenance != truth, reproduction or conformance.
- SAME_PRODUCER_REVIEW != independent review.
- Current later-stage presence does not rewrite earlier availability.
- September remains OPEN; natural-month close is NOT_DUE.

### A1 disposition
- Coverage through 2026-09-25: VERIFIED_IN_CURRENT_LONGITUDINAL_OWNER.
- Historical rewrite required: NO.
- New runtime/scientific-validation/independence credit: NONE.
