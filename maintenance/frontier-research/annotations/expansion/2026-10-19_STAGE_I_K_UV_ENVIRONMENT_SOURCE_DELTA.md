# 2026-10-19 source-selection expansion — uv environment lineage (Stages I–K)

## Change class, source cutoff and ownership
- Repository: `lostlight530/auto-doc-engine`; authoring/source-access date: **2026-10-19**.
- Type: `ADDITIVE_SOURCE_SELECTION_EXPANSION / FORWARD_RECONCILIATION`.
- This note is **not** a retroactive amendment of the Stage I/J/K study designs, source-object registers, month files, reviews or completion claims. Those records remain authoritative for the exact sources they selected.
- Stage I–K were recently instantiated retrospectively on 2026-10-19, using `SOURCE_BOUNDED` official releases; the originally selected set mostly focused on Pandoc/CycloneDX. This supplement studies a **different upstream family** from the same year: `astral-sh/uv`.
- Read method executed: GitHub `/repos/astral-sh/uv/releases?per_page=100` and exact tagged release descriptions on 2026-10-19. This is targeted release navigation, **not** an exhaustive search or security audit.

## Newly selected candidate objects (not renumbered into original Stage registers)
| Supplemental object ID | Historical month / native owner | Original source and release date | Issuer-described observation | Bounded implication |
|---|---|---|---|---|
| UX1 | [2026-03 / I](../../stage-i-2026-q1/MONTH_2026_03_RECONSTRUCTION.md) | [uv 0.11.0](https://github.com/astral-sh/uv/releases/tag/0.11.0), 2026-03-23 | Networking/TLS verifier changes, documented as potentially breaking | Reproducibility depends on certificate/host trust and installer revision; does not establish which environment our repository used |
| UX2 | [2026-04 / J](../../stage-j-2026-q2/MONTH_2026_04_RECONSTRUCTION.md) | [uv 0.11.6](https://github.com/astral-sh/uv/releases/tag/0.11.6), 2026-04-09 | Wheel RECORD validation and uninstall path safety fixes | Package file lists and uninstall scope are real environment/provenance questions |
| UX3 | [2026-05 / J](../../stage-j-2026-q2/MONTH_2026_05_RECONSTRUCTION.md) | [uv 0.11.15](https://github.com/astral-sh/uv/releases/tag/0.11.15), 2026-05-18 | Fixes for TAR parser differential and script entry-point escape | Archive parsing and executable path controls are separate from document correctness |
| UX4 | [2026-07 / K](../../stage-k-2026-q3/MONTH_2026_07_RECONSTRUCTION.md) | [uv 0.12.0](https://github.com/astral-sh/uv/releases/tag/0.12.0), 2026-07-28 | Newly initialized uv projects define a build system by default; release describes compatibility changes | An artifact's realized build environment can depend on project-init defaults and uv version |

## What this changes — and what it does not
**Added research question:** Existing Stage I–K analysis correctly distinguishes source conversion, parser settings, schema serialization and artifact identity. The uv release series adds another distinct evidence boundary: `declared project -> installer/network/archive behavior -> realized environment -> converter -> derivative artifact`. A release's security fix or changed default does **not** prove our repository was vulnerable, patched, reproducible or deployed with that release.

**Preserve historical negative space:** J's April/May `NO_SELECTED_OBJECT_IN_DECLARED_SOURCE_SET` remains true **for its originally declared selected set**. UX2/UX3 do not falsify that scoped result; they show what a later expanded selection can recover. No original month file is rewritten. These are additional **source objects for potential Stage amendments**, not an automatic change to its register's object counts.

**Source-independence boundary:** Four tagged uv releases originate from one upstream issuer family. They do not independently corroborate each other, and uv notes do not independently verify Pandoc/CycloneDX behavior. Actual package install/uninstall, certificate validation, project creation and derivative reproduction were **not run**.

## Review and next gate
- Internal source/date/quarter check performed against tagged GitHub Releases metadata; no independent technical or security review, no local CI/runtime test.
- `NO_CURRENT_REPOSITORY_DRIFT_ESTABLISHED / NO_RUNTIME_CHANGE / NO_CONTRACT_CHANGE`.
- To elevate UX1–UX4 into native Stage research, first record an explicit selection amendment, source IDs and Part-level re-analysis, then a same- or independently produced Stage review and forward correction. A future A1/A2 index owner should route that amendment by date without erasing the original Stage snapshots.

