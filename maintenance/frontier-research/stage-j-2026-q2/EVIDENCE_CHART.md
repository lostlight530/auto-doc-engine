# Evidence Chart — J/2026-Q2

- Extraction date 2026-10-19. Variables: `tagged_object`, `release_publication_date`, `upstream_observation`, `analysis`, `independence`, `local_verification`, `unresolved`.
- Units: unique upstream versions; multiple observations of the same release would not add independent objects.

| Finding ID | Object/source | Claimed/observed upstream release change | Bounded analytic inference | Independence | Current local evidence |
|---|---|---|---|---|---|
| F1 | O1 / S1 | direct-URL hash matching and merged archive hashes | Package-source hash checking is an input-selection guard; matching algorithms constrain declared integrity but do not certify installed artifact semantics. | Same-origin publisher release | NOT_RUN / NOT_AUDITED |
| F2 | O2 / S2 | manual GitHub release publication after registry timeout with GitHub attestations unavailable | A released binary and its accompanying provenance attestation have separate availability states. The maintainer explicitly disclosed a release without GitHub attestations, making missing evidence meaningful rather than assumed present. | Same-origin publisher release | NOT_RUN / NOT_AUDITED |
| F3 | O3 / S3 | Protobuf/XML model-card schema alignment | Representation parity is revision-specific: a model-card relation encoded in one serialization does not guarantee another schema supports it without the alignment change. | Same-origin publisher release | NOT_RUN / NOT_AUDITED |
| F4 | O4 / S4 | Typst sys.inputs parameters and ODT style-generation changes | A conversion output depends on passed evaluation parameters and writer style strategy as well as source bytes and converter revision; reference ODT style compatibility remains a test question. | Same-origin publisher release | NOT_RUN / NOT_AUDITED |

## Counterevidence matrix
- Official upstream change descriptions do not demonstrate local compatibility, scientific/benchmark truth or downstream correctness.
- A later patch/version may correct earlier behavior without proving that all older artifacts were wrong.
- No executed independent disconfirmation search or cross-version reproduction; **absence of observed contradiction is not corroboration**.

## Negative space
- No native instrumented run, precise dependency lock replay, benchmark execution or cross-version output-comparison performed for this research.
- No source-family census, systematic-scoping coverage or quantitative adoption inference.
