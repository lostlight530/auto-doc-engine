# E1 — Converter Revision and Derivative Identity

## Research question
Can one stable source document be treated as producing one stable derivative meaning when the converter revision changes?

## Selected evidence
Pandoc official release history records:
- 3.6.2 — 2025-01-12: adds the `pod` input format and reader-level behavior changes.
- 3.6.3 — 2025-02-09: changes wikilink representation from a `title` marker to class `wikilink`, affecting readers/writers that support wikilinks.
- 3.6.4 — 2025-03-16: changes citation handling when `--citeproc` is used and fixes additional reader behavior.

Source: https://pandoc.org/releases.html

## Analysis
The Q1 sequence is not merely "new formats added." It demonstrates that converter revision is part of derivative provenance because representation, parsing and citation behavior can change while the source bytes remain unchanged.

```text
same source bytes
+ different converter revision/config
!= same derivative identity
!= semantic equivalence
```

This supports recording converter revision/configuration alongside derivative hashes rather than treating a hash or output filename as a complete explanation.

## Limits
No local Pandoc conversion matrix was run. The official changelog establishes project-declared release behavior, not independent reproduction.

## Outcome
`SUPPORTED_OBSERVATION / NO_CURRENT_REPOSITORY_DRIFT`
