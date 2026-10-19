# Frontier Research Stage L / 2026-Q4 — 2026-10 monthly research reconstruction
- Source period: 2026-10; retrospective reconstruction/record 2026-10-19; cutoff 2026-10-19; coverage `SOURCE_BOUNDED`.
- Research question owner: Citation semantics and interpreter drift — OPEN. Evidence-object count: 2; **not** a measure of field-wide activity.
## 2026-10-08 — Citation family-name treatment (`L-O1`)
**Publisher source:** [jgm/pandoc 3.12.1](https://github.com/jgm/pandoc/releases/tag/3.12.1) (`L-S1`).
**Observed release note:** Pandoc reports FODT input/output and changes in citeproc family-name particle handling, alongside regression fixes.
**Analysis:** Attributed name rendering is part of documentary evidence and bibliography transformation, not just display formatting.
**Alternative / caution:** No family-name citation replay, FODT conversion or local defect confirmed.

## 2026-10-09 — Interpreter default migration (`L-O2`)
**Publisher source:** [astral-sh/uv 0.13.0](https://github.com/astral-sh/uv/releases/tag/0.13.0) (`L-S2`).
**Observed release note:** uv reports Python 3.15 as default stable version for unpinned selection and a changed cache format.
**Analysis:** Unpinned interpreter selection and cache realization can drift even if document source bytes do not.
**Alternative / caution:** Pinned and already-installed interpreters may be unaffected; local state uninspected.

## Month-level disposition
`SELECTED_SOURCE_BOUNDED`; publisher change != local execution, scientific verification or repo drift. The quarter's Parts own deeper analysis; this file owns the event time boundary.
