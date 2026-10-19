# Evidence Chart — I/2026-Q1

- Extraction date 2026-10-19. Variables: `tagged_object`, `release_publication_date`, `upstream_observation`, `analysis`, `independence`, `local_verification`, `unresolved`.
- Units: unique upstream versions; multiple observations of the same release would not add independent objects.

| Finding ID | Object/source | Claimed/observed upstream release change | Bounded analytic inference | Independence | Current local evidence |
|---|---|---|---|---|---|
| F1 | O1 / S1 | SBOM synthetic-root dependency fixes and portable installed RECORD paths | A machine-readable inventory's dependency graph and installed-file portability are different evidence objects; a corrected exported SBOM must not retroactively certify older inventory output. | Same-origin publisher release | NOT_RUN / NOT_AUDITED |
| F2 | O2 / S2 | WASM/browser compilation, JSON/YAML defaults, media ZIP extraction and citation-state controls | Document transformation gained a browser-capable deployment route and more configuration forms. Record the execution host, defaults-file semantics, embedded asset packaging and citeproc state separately. | Same-origin publisher release | NOT_RUN / NOT_AUDITED |
| F3 | O3 / S3 | Typst-template regression correction | A patch-level repair following the 3.9 family changes means a stable looking conversion command is not a stable derivative contract unless release revision and template are recorded. | Same-origin publisher release | NOT_RUN / NOT_AUDITED |

## Counterevidence matrix
- Official upstream change descriptions do not demonstrate local compatibility, scientific/benchmark truth or downstream correctness.
- A later patch/version may correct earlier behavior without proving that all older artifacts were wrong.
- No executed independent disconfirmation search or cross-version reproduction; **absence of observed contradiction is not corroboration**.

## Negative space
- No native instrumented run, precise dependency lock replay, benchmark execution or cross-version output-comparison performed for this research.
- No source-family census, systematic-scoping coverage or quantitative adoption inference.
