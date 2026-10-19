# Evidence and comparison chart — Stage L / 2026-Q4

## Variables and authority
Variables: object/release, date, published change, claimed capability/behavior, analytic evidence consequence, provenance/source family, independent verification state, negative space. Method: descriptive authority appraisal + chronological comparison, no quantitative meta-analysis.

| Finding | Object | Publisher-described evidence | Research interpretation | Authority/directness | Independent reproduction | Temporal scope |
|---|---|---|---|---|---|---|
| F-L1 | O9 | Pandoc 3.12.1 adds FODT input/output and changes citeproc interpretation of structured surname particles, alongside several regression fixes. | A citation-provenance path depends on a named converter revision and reference semantics; apparently identical data may yield different derivative citations. | S9: direct release assertion; one origin | `UNKNOWN / NO_LOCAL_RUN` | 2026-10-08 |
| F-L2 | O10 | uv 0.13.0 announces Python 3.15 as its default stable Python, together with correctness and compatibility changes. | Environment resolution defaults are another independent clock for reproducible document generation; lock representation does not establish the realized interpreter. | S10: direct release assertion; one origin | `UNKNOWN / NO_LOCAL_RUN` | 2026-10-09 |

## Comparison across research objects
The selected objects share a **provenance boundary** but not a common experimental population, success metric or runtime. Changes between releases cannot be counted as continuous improvement. Different publishers are independent origins for their own releases, not independent corroboration of one release's correctness.

## Competing interpretation and negative-space chart
- Strong alternative: object selection exposes the provenance dimensions this study prioritizes; it is not representative sampling of the whole field.
- Unsupported: release announcements => independent conformity; public documentation => successful local reproduction; same vendor sources => independent confirmation.
- Missing: measured downstream adoption, release-by-release controlled output comparison, independent specialist review, `auto-doc-engine` runtime/contract audit.
- Schema/format/SDK changes can be incompatible or source-specific; no forced equivalence judgment.
