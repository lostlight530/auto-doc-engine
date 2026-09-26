# G2 — Immutable Releases: Publication Identity After the Tag Is Cut

## Question
What changes when a repository release can become immutable after publication?

## Object
- Research object: GitHub immutable releases public preview
- Event date: 2025-08-26
- Source family: GitHub product changelog/documentation
- Authority: platform-described feature semantics
- Accessed: 2026-09-26

## Primary sources
- https://github.blog/changelog/2025-08-26-releases-now-support-immutability-in-public-preview/
- https://docs.github.com/en/actions/concepts/security/artifact-attestations

## Observed feature state
The announcement describes immutable releases as protecting:
- release assets from addition, modification, or deletion after publication;
- the associated tag from deletion or movement;
- release assets with signed attestations intended to support authenticity/integrity verification.

GitHub's attestation documentation separately states that attestations link artifacts to build provenance and can also carry SBOM predicates, while warning that an attestation is not a guarantee that the artifact is secure.

## Interpretation
Earlier artifact narratives often treat a tag/release name as if it were a stable object by convention. Immutable release semantics make that stability an explicit platform state.

That yields a more precise publication chain:

```text
source revision
-> build workflow identity
-> release tag
-> release asset bytes
-> signed attestation
-> immutable publication state
```

But the chain is not a truth ladder:

```text
immutable
!= correct
signed
!= scientifically valid
attested provenance
!= safe artifact
release identity
!= semantic equivalence
```

For research software and derivative research artifacts, the important historical shift is that "what was published" and "can the published object later be mutated in place" become separately inspectable questions.

## Lifecycle nuance
The feature was a public preview. The Stage records the platform state announced in Q3 2025, not a universal guarantee that every GitHub release was immutable or that every repository enabled the feature.

## Finding
`G2_FINDING`: Q3 2025 strengthens the publication-identity layer. A release can be modeled not only by tag/name and asset hashes, but by whether the publication surface itself is mutable, protected, and linked to a signed provenance statement.
