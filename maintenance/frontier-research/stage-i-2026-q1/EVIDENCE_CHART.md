# Evidence and comparison chart — Stage I / 2026-Q1

## Variables and authority
Variables: object/release, date, published change, claimed capability/behavior, analytic evidence consequence, provenance/source family, independent verification state, negative space. Method: descriptive authority appraisal + chronological comparison, no quantitative meta-analysis.

| Finding | Object | Publisher-described evidence | Research interpretation | Authority/directness | Independent reproduction | Temporal scope |
|---|---|---|---|---|---|---|
| F-I1 | O1 | Pandoc 3.9 announces a WASM build and browser application, JSON/YAML defaults with variable interpolation, and media-archive output options. | Execution host (browser versus native binary), defaults-file version and configuration become distinct transformation provenance; browser availability does not prove identical results. | S1: direct release assertion; one origin | `UNKNOWN / NO_LOCAL_RUN` | 2026-02-04 |
| F-I2 | O2 | Pandoc 3.9.0.2 is explicitly a fix for a regression in the Typst template introduced in an earlier 3.9 patch sequence. | A patch-release boundary can affect the rendered derivative even when source content is unchanged. | S2: direct release assertion; one origin | `UNKNOWN / NO_LOCAL_RUN` | 2026-03-19 |

## Comparison across research objects
The selected objects share a **provenance boundary** but not a common experimental population, success metric or runtime. Changes between releases cannot be counted as continuous improvement. Different publishers are independent origins for their own releases, not independent corroboration of one release's correctness.

## Competing interpretation and negative-space chart
- Strong alternative: object selection exposes the provenance dimensions this study prioritizes; it is not representative sampling of the whole field.
- Unsupported: release announcements => independent conformity; public documentation => successful local reproduction; same vendor sources => independent confirmation.
- Missing: measured downstream adoption, release-by-release controlled output comparison, independent specialist review, `auto-doc-engine` runtime/contract audit.
- Schema/format/SDK changes can be incompatible or source-specific; no forced equivalence judgment.
