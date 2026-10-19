# Quarterly Frontier Research Synthesis — Stage J / 2026-Q2

- Repository: `lostlight530/auto-doc-engine`
- Source window: `2026-04-01 through 2026-06-30`; research and source access `2026-10-19` (RETROSPECTIVE)
- Design: `HISTORICAL_FRONTIER_RECONSTRUCTION + TARGETED_EVIDENCE_SYNTHESIS`; coverage `SOURCE_BOUNDED`
- Native specification: `2026-09-19-first-batch`
- Status `COMPLETE` only for selected `SOURCE_BOUNDED` documentary scope; synthesis date 2026-10-19.
- Independence: `SAME_PRODUCER_REVIEW`, independent result validation not established.

## Quarter research question and answered scope
Q2: uv lock/workspace/source metadata, Pandoc Typst and ODT configuration and CycloneDX schema alignment show that artifact identity extends beyond files.

Within the 4 selected versioned upstream release objects, the research distinguishes **a publisher-observable version event** from **a conceptual evidentiary consequence** and **a missing local validation**. It answers what should be recorded for future work; it does not answer whether the user's repository runs the relevant tools or whether such tool claims are scientifically true.

## Monthly and Part inputs
- [2026-04](MONTH_2026_04_RECONSTRUCTION.md)
- [2026-05](MONTH_2026_05_RECONSTRUCTION.md)
- [2026-06](MONTH_2026_06_RECONSTRUCTION.md)
- [J1_LOCK_WORKSPACE.md](J1_LOCK_WORKSPACE.md): Workspace metadata now includes lock dependency information; Lock descriptions and realized runtime remain separate
- [J2_GIT_SOURCE_URL.md](J2_GIT_SOURCE_URL.md): Fixes Git archive lock handling and preserves repository URLs in direct URL metadata; Source location and archive resolution are evidence separate from content identity
- [J3_SCHEMA_MODEL_CARD.md](J3_SCHEMA_MODEL_CARD.md): Aligns model-card properties in XML/Protobuf and adds schema tests; Schema revision and serialization must be identified
- [J4_TYPST_ODT_CONFIG.md](J4_TYPST_ODT_CONFIG.md): Adds --typst-input and changes ODT styles and ms PDF engine default; Writer parameters, default engine and output style are transform identity

## Substantive change and previous quarter
Q2: uv lock/workspace/source metadata, Pandoc Typst and ODT configuration and CycloneDX schema alignment show that artifact identity extends beyond files.

Compared with prior Stage I, the new source class shifts the versioned evidence question: Q1: uv missing-lock diagnostics, Pandoc WASM/browser sandbox and a Typst regression distinguish lock presence, host capabilities and revision-sensitive outputs.

- **2026-04-01 / astral-sh/uv 0.11.3**: Workspace metadata now includes lock dependency information. Analytical delta: Lock descriptions and realized runtime remain separate.
- **2026-05-28 / astral-sh/uv 0.11.17**: Fixes Git archive lock handling and preserves repository URLs in direct URL metadata. Analytical delta: Source location and archive resolution are evidence separate from content identity.
- **2026-06-02 / CycloneDX/specification 1.7.1**: Aligns model-card properties in XML/Protobuf and adds schema tests. Analytical delta: Schema revision and serialization must be identified.
- **2026-06-04 / jgm/pandoc 3.10**: Adds --typst-input and changes ODT styles and ms PDF engine default. Analytical delta: Writer parameters, default engine and output style are transform identity.

## Persistent structures, competing explanations, non-comparability
Persistent boundaries: lineage != truth; hash != semantic equivalence; release != local execution. The apparent progression may reflect source selection and the repository's established lens rather than ecosystem-wide improvement. Publisher claims are authoritative for their released text; distinct source families address different objects, not replicated measurements. Patch fixes can narrow a prior fault without proving broad correctness, and newer versions do not retroactively invalidate old research artifacts.

## Evidence maturity and negative space
Maturity observed: publication of official tagged release artifacts. No independent execution, benchmark replication, user evaluation, security audit, source-family triangulation, systematic searching or local contract audit. No negative-result search was performed; missing corroboration remains `UNKNOWN` rather than `DOES_NOT_EXIST`. Temporal differences between upstream publication and 2026-10-19 reconstruction are not collapsed.

## Repository conclusion and handoff
No current repository defect established; drift `UNKNOWN / NOT_AUDITED`; no runtime or contract modification. Source files, monthly periods and previous stages remain unchanged; later corrections are additive. [Research review](RESEARCH_REVIEW.md) records same-producer independence and material scope limitations; [handoff](STAGE_HANDOFF.md) exports questions only.

`FRONTIER_STAGE_COMPLETE — SOURCE_BOUNDED RETROSPECTIVE STUDY`, **not independently scientifically validated**.
