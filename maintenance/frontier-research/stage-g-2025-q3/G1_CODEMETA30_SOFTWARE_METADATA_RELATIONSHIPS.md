# G1 — CodeMeta 3.0: Software Metadata Relationships Become More Explicit

## Question
What does the 2025-07-13 CodeMeta 3.0 release add to the representation of research-software identity and relationships?

## Object
- Research object: CodeMeta 3.0
- Event date: 2025-07-13
- Source family: CodeMeta project / GitHub release
- Authority: project release notes for the released vocabulary/context
- Accessed: 2026-09-26

## Primary source
- https://github.com/codemeta/codemeta/releases
- Stable context target: https://w3id.org/codemeta/3.0

## Observed changes
The 3.0 release records a vocabulary/context transition rather than merely a packaging bump.

Material changes include:
- rename of `codemeta:contIntegration` to `codemeta:continuousIntegration`;
- rename of `codemeta:embargoDate` to `codemeta:embargoEndDate`;
- addition of `codemeta:hasSourceCode` and `codemeta:isSourceCodeOf` to connect `SoftwareSourceCode` with `SoftwareApplication`;
- addition of Schema.org Role terms including `startDate`, `endDate`, and `roleName` for contributor-role expression;
- addition of review-related terms including `Review`, `review`, `reviewAspect`, and `reviewBody`;
- a v2→v3 crosswalk.

## Interpretation
The historical change is not "metadata became correct." It is that the metadata model became more capable of distinguishing identities and relationships that were previously easier to flatten.

For a research-artifact pipeline, this matters because:
```text
software source
!= software application
contributor identity
!= contributor role at a given time
review record
!= review outcome validity
schema relation
!= verified real-world relation
```

The release also reinforces versioned context identity: a CodeMeta document should point to a release-specific context rather than a mutable branch when stable semantics matter.

## Negative space
This Stage did not:
- validate any CodeMeta document against 3.0;
- verify that a repository's declared contributor roles are historically complete;
- establish that review metadata corresponds to peer review;
- prove that crosswalk conversion preserves every source-system meaning.

## Finding
`G1_FINDING`: Q3 2025 makes software metadata less flat: artifact identity increasingly includes typed relationships between source, application, people, roles, and review records. That improves representational precision, but it does not transfer truth from metadata into the represented world.
