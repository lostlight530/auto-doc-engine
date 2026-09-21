# February 2024 Reconstruction — Stage A

## Purpose

This dossier reconstructs February 2024 through the repository lens of multi-format research records, format-specific validity, accessibility metadata, and versioned scholarly-document conversion.

Coverage is `SEARCH_BOUNDED`.

## Objects/events included

- **F1 / O2 — Quarto 1.4.550**, tag commit dated 2024-02-15.
- **F2 / O5 — Pandoc 3.1.12**, released 2024-02-15.
- **F3 / O5 — Pandoc 3.1.12.1**, released 2024-02-18.
- **F4 / O5 — Pandoc 3.1.12.2**, released 2024-03-01 but includes fixes to regressions introduced in the February release; treated as a March correction that changes interpretation forward, not as a February event.

## F1 — Quarto 1.4.550

Source: https://github.com/quarto-dev/quarto-cli/commit/69168152ee3532fa7c14149b95512f0e3653f646

This revision provides a February temporal anchor for the 1.4 line. Alongside current official manuscript documentation and the 1.4 changelog, it supports a bounded conclusion that the manuscript/multi-format release family was actively maintained through the quarter. It does not by itself prove exact manuscript feature state or publisher adoption.

## F2 — Pandoc 3.1.12: conversion surface expands

Primary source: https://github.com/jgm/pandoc/releases/tag/3.1.12

Pandoc 3.1.12 added Djot as both an input and output format and changed multiple readers/writers. From an artifact-lineage perspective, every new conversion edge increases the number of representations that may share origin without sharing exact semantics.

```text
source artifact
  -> normalized document AST
  -> output A
  -> output B
  -> output C
```

That graph does not establish that A, B, and C communicate the same content with the same affordances. Each writer may preserve, transform, drop, or reinterpret features.

## F3 — Pandoc 3.1.12.1: accessibility and self-contained graphics expose output-specific semantics

Primary source: https://github.com/jgm/pandoc/releases/tag/3.1.12.1

The patch included omitting EPUB3-specific accessibility features on EPUB2 to fix a regression, additional SVG ID handling for self-contained output, proper math handling in PowerPoint headings/tables using alternate-content structures, and validation of EPUB2 output as part of the build target.

```text
same source content
!= same target accessibility mechanism
!= same validation rule
```

A documentation system should therefore record **which validator/checker applies to which representation**, and whether that checker was actually executed.

## Cross-version correction discipline

The 3.1.12.1 patch corrected regressions from 3.1.12. The correct historical model is additive:

```text
3.1.12 released with behavior X
3.1.12.1 later corrected specific behavior
```

It would be historically false to rewrite the 3.1.12 record as if the fix had always existed.

## February synthesis

February deepens the quarter's central problem from “can we identify research artifacts?” to “can we preserve semantics across representations?”

The evidence shows:

- conversion surfaces expand;
- target formats carry distinct constraints;
- accessibility handling can be version- and format-specific;
- later patch releases can correct output validity without invalidating the historical existence of the earlier release.

The repository-level implication is not a new runtime requirement by itself. It is a stronger research basis for maintaining explicit artifact identity, target format, validator identity, execution state, and correction lineage.

## February negative space

Not established:

- cross-format semantic equivalence for any selected Pandoc conversion;
- successful accessibility conformance of arbitrary converted research documents;
- reproducibility of computation merely because a manuscript links source notebooks;
- independent adoption evidence for Quarto manuscripts.

## Carry-forward to March

March should test whether authoring/rendering systems add more reusable structure and whether standards producers distinguish clearly between released state and proposed future change.
