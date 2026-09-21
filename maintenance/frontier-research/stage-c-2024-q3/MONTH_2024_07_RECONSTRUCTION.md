# Stage C Month Reconstruction — 2024-07

## Scope

July 2024 / retrospective / search-bounded

## Objects

### Pandoc 3.3

Pandoc release history dates 3.3 to 2024-07-28; the announcement followed on 2024-07-29

Material evidence for this Stage:

- fix a Docx nested-list regression introduced in 3.2.1
- add `--link-images` for ODT

The first point is a direct forward-correction example

### Matplotlib 3.9.1

Release date is 2024-07-04; public announcement is 2024-07-06

Material evidence:

- GitHub artifact attestations added for sdist/wheels
- multiple backend, interactivity, scaling and serialization-related bugfixes

## July interpretation

July connects two different provenance questions

Pandoc shows that converter revision can change document structure

Matplotlib shows that build origin can be cryptographically/procedurally evidenced without proving behavioral correctness

```text
authentic build
!= defect-free behavior

later fix
!= earlier artifact never existed
```

## Limits

No local conversion, wheel verification or attestation verification executed
