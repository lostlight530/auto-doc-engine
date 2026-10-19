# Evidence and comparison chart — Stage K / 2026-Q3

## Variables and authority
Variables: object/release, date, published change, claimed capability/behavior, analytic evidence consequence, provenance/source family, independent verification state, negative space. Method: descriptive authority appraisal + chronological comparison, no quantitative meta-analysis.

| Finding | Object | Publisher-described evidence | Research interpretation | Authority/directness | Independent reproduction | Temporal scope |
|---|---|---|---|---|---|---|
| F-K1 | O5 | Pandoc 3.10.1 is a follow-up release with incremental improvements and bug fixes after 3.10. | Patch chronology is provenance: a durable artifact record should name the revision rather than only 'Pandoc 3.10'. | S5: direct release assertion; one origin | `UNKNOWN / NO_LOCAL_RUN` | 2026-07-22 |
| F-K2 | O6 | Pandoc 3.11 introduces --math-method, changes the default to mathml, retains deprecated aliases and reports a security-related template-fetch fix. | Math rendering policy, config aliases and fetching/source trust can change independently of source text. | S6: direct release assertion; one origin | `UNKNOWN / NO_LOCAL_RUN` | 2026-08-29 |
| F-K3 | O7 | CycloneDX 1.7.2 adds an optional repeated XML node for relatedCryptographicAsset and introduces schema tests. | Evidence portability depends on schema revision and serialization-specific relations; a BOM can encode claims without verifying them. | S7: direct release assertion; one origin | `UNKNOWN / NO_LOCAL_RUN` | 2026-09-17 |
| F-K4 | O8 | Pandoc 3.12 reports performance-oriented changes and makes -t xml respect --standalone, emitting a fragment when absent. | Latency claims and output framing are separate transformation evidence; an output structure change can affect derivative identity. | S8: direct release assertion; one origin | `UNKNOWN / NO_LOCAL_RUN` | 2026-09-29 |

## Comparison across research objects
The selected objects share a **provenance boundary** but not a common experimental population, success metric or runtime. Changes between releases cannot be counted as continuous improvement. Different publishers are independent origins for their own releases, not independent corroboration of one release's correctness.

## Competing interpretation and negative-space chart
- Strong alternative: object selection exposes the provenance dimensions this study prioritizes; it is not representative sampling of the whole field.
- Unsupported: release announcements => independent conformity; public documentation => successful local reproduction; same vendor sources => independent confirmation.
- Missing: measured downstream adoption, release-by-release controlled output comparison, independent specialist review, `auto-doc-engine` runtime/contract audit.
- Schema/format/SDK changes can be incompatible or source-specific; no forced equivalence judgment.
