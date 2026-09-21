# March 2024 Reconstruction — Stage A

## Purpose

This dossier reconstructs March 2024 as the close of Stage A. March contains both concrete releases and an explicit proposal state, allowing the Stage to compare released implementation, maintained conversion behavior, and future-change governance.

Coverage is `SEARCH_BOUNDED`.

## Objects/events included

- **M1 / O2 — Quarto 1.4.551**, 2024-03-05 tag commit.
- **M2 / O6 — Typst 0.11.0**, released 2024-03-15.
- **M3 / O5 — Pandoc 3.1.12.2 / 3.1.12.3**, released 2024-03-01 / 2024-03-18.
- **M4 / O3 — DataCite metadata schema RFC**, 2024-03-26.

## M1 — Quarto 1.4.551

Source: https://github.com/quarto-dev/quarto-cli/commit/d7a62ccf866a2b749ecb12d2810b31eba90fa021

Together with January and February tags, this creates a three-month revision trace for the 1.4 line. The trace is useful for chronology, but it still does not prove semantic equivalence between tags.

## M2 — Typst 0.11.0: reusable templates and richer table structure

Sources:

- https://typst.app/docs/changelog/0.11.0/
- https://github.com/typst/typst/releases/tag/v0.11.0

Typst 0.11.0 added richer table structure, including configurable cells, row/column spanning, repeated headers/footers, and line controls. It also introduced template packages and `typst init <template>` workflows.

The table changes matter because scientific documents often carry evidence through tables whose structure—not just pixels—communicates hierarchy and grouping. Repeated headers and explicit cells make that structure easier to author consistently, but they do not guarantee accessible reading order or correct scientific interpretation.

Template packages separate reusable presentation/process logic from individual document content. That can improve consistency, but it can also create hidden coupling if a template version changes without the generated artifact recording the template identity.

A durable document record therefore benefits from template/package identity and version, source revision, renderer/compiler version, output identity, declared derivation relation, and validation status.

## M3 — Pandoc 3.1.12.2 and 3.1.12.3

Primary sources:

- https://github.com/jgm/pandoc/releases/tag/3.1.12.2
- https://github.com/jgm/pandoc/releases/tag/3.1.12.3

### 3.1.12.2

The release added `role="img"` to SVGs and `aria-label` when SVG alt text is present, explicitly because screen readers do not treat SVG `alt` attributes like image alt text. It also fixed EPUB metadata/validation and multiple writer regressions.

This is direct evidence that “alt text exists in source” and “assistive technology receives equivalent accessible semantics in target output” are different claims.

### 3.1.12.3

The release adjusted the Typst writer in response to Typst 0.11 behavior, including image sizing and table handling. This is a concrete cross-tool dependency event:

```text
writer success at t1
!= guaranteed writer success after target-runtime change at t2
```

A reproducibility record that omits the target renderer/compiler version can be materially incomplete.

## M4 — DataCite March RFC: explicit proposal status prevents history collapse

Primary source: https://datacite.org/blog/metadata-schema-rfc-march_2024/

DataCite explicitly states that the March RFC was not yet a complete schema version and that proposed items might be distributed across future versions depending on complexity, compatibility, and roadmap.

The Stage therefore rejects a naive chronology model such as “March changes superseded January 4.5.” They did not. The RFC was a candidate future change set.

## March synthesis

March brings the quarter's three strands together:

1. versioned release-line continuity — Quarto;
2. reusable document structure and renderer evolution — Typst + Pandoc;
3. explicit change-governance state — DataCite RFC.

The shared problem is not merely file generation. It is maintaining enough provenance to answer what source produced an artifact, which template/package affected presentation, which renderer/compiler interpreted it, which target semantics applied, whether the change was released/proposed/corrected, which validations ran, and which claims remain representation-only rather than scientifically verified.

## March negative space

Not established:

- WCAG conformance of Typst/Pandoc outputs;
- semantic equivalence of Quarto/Pandoc/Typst output representations;
- adoption rates of template packages or DataCite proposals during Q1;
- deterministic reproduction across renderer versions;
- scientific validity of content carried by the systems.

## Quarter-close implication

March supports closing Stage A because the quarter now contains enough evidence to identify a coherent mechanism: **research-document systems were becoming more structured, composable, typed, and multi-format, while the cost of version/provenance ambiguity also became more visible.**

The appropriate repository response is research interpretation, not an automatic implementation change.
