# January 2024 Reconstruction — Stage A

## Purpose

This dossier reconstructs January 2024 as a month inside Stage A. It is a research artifact, not a maintenance or activity log. It records selected external developments relevant to `auto-doc-engine`'s lens and preserves the distinction between event date, source publication date, later access date, and current repository interpretation.

Coverage is `SEARCH_BOUNDED`. The research did not attempt an exhaustive inventory of every documentation or scholarly-authoring release.

## Month frame

January establishes the quarter's strongest evidence for **research-object typing and explicit relation semantics**, while also showing that routine document-tool revisions can change output validity and metadata placement without changing a research object's scientific meaning.

### Objects/events included

- **J1 / O1 — DataCite Metadata Schema 4.5**, released 2024-01-22.
- **J2 / O2 — Quarto 1.4 release-line revision v1.4.549**, tag commit dated 2024-01-24.
- **J3 / O4 — Pandoc 3.1.11.1**, released 2024-01-06.

## J1 — DataCite 4.5: typed research objects enter a richer relation graph

Primary sources:

- DataCite Metadata Schema 4.5: https://schema.datacite.org/meta/kernel-4.5/
- DataCite release explanation, 2024-01-24: https://datacite.org/blog/introducing-datacite-metadata-schema-4-5/
- DataCite release history: https://schema.datacite.org/versions.html

### Observed change

Schema 4.5 added `Instrument` and `StudyRegistration` as controlled `resourceTypeGeneral` values and added `IsCollectedBy` / `Collects` relations. Publisher identifiers also became structured sub-properties.

The important research-engineering shift is that previously prose-heavy or generic objects can now be represented as typed nodes and typed edges in a research-output graph. An instrument can be a first-class research resource, and a dataset can explicitly declare that it was collected by that instrument.

### Why this matters for documentation systems

A documentation engine that preserves only filenames or human prose can lose these distinctions. A durable research artifact needs at least object identity, object type, declared relation, relation direction, version/effective date, and evidence basis for the declaration.

But none of those fields validate the underlying science. A metadata edge can be syntactically valid and scientifically wrong.

```text
lineage != truth
declared relation != verified causal/process fact
metadata completeness != scientific completeness
```

### Process-disclosure significance

The new `StudyRegistration` type is especially relevant because it makes a planning/protocol-like object more directly identifiable in the metadata graph. That does not prove adherence to a registration, but it makes the existence and identity of the registration easier to route, cite, and compare with later outputs.

### Mutability and version-awareness

DataCite's January release communication also explains a documentation-format shift toward Read the Docs with PDF export and notes that small documentation corrections can occur between schema versions.

```text
schema release date != documentation last-updated date
same schema version != frozen wording at every later access time
```

A robust lineage record should capture both the normative schema version and the accessed documentation revision/date when exact language matters.

## J2 — Quarto 1.4.549: release-line continuity as temporal evidence

Source: https://github.com/quarto-dev/quarto-cli/commit/8fa73d2233a0309ca089a888bad96d7e2a9224a4

The tag is narrow but valuable evidence. It establishes that the Quarto 1.4 line had a concrete January revision. It does **not** establish that all current Quarto 1.4 documentation text was already present on that exact date, nor does it establish adoption.

For the Stage, January's Quarto evidence is therefore used as a **temporal anchor**, not as a claim that every manuscript feature can be backdated to the tag without additional historical evidence.

## J3 — Pandoc 3.1.11.1: output validity and representation-specific repair

Primary source: https://github.com/jgm/pandoc/releases/tag/3.1.11.1

The release included fixes such as ensuring generated DOCX output validates, correcting OpenDocument highlighting-style placement, improving table caption/identifier handling, and ensuring LaTeX rerun warnings are detected to avoid incorrect layout states.

These are not “frontier scientific discoveries,” but they matter for research-artifact durability because they show that a document pipeline can successfully generate a file while still producing structurally invalid, misplaced, or visually incorrect content.

```text
file generated != output valid
output valid != semantically equivalent to source
layout completed != scientific communication preserved
```

A multi-format research record therefore needs format-specific validation evidence rather than one generic “render succeeded” status propagated across all outputs.

## January synthesis

January contains two complementary movements:

1. metadata representation becomes more expressive through DataCite 4.5;
2. document conversion remains representation-sensitive through routine Pandoc fixes.

Together they suggest that durable research documentation requires both a richer semantic graph and format-specific validation. Adding relations without validating outputs is insufficient; validating file structure without preserving research-object identity is also insufficient.

## January negative space

Not established in this month's declared search:

- independent measurement of DataCite 4.5 adoption during January;
- independent scientific validation of `Instrument` or `StudyRegistration` metadata;
- semantic-equivalence testing across Pandoc output formats;
- reproduction of Quarto 1.4 manuscript workflows on the January tag.

These remain `NOT_FOUND_IN_DECLARED_SEARCH` or `NOT_EXECUTED`, not evidence of absence or failure.

## Carry-forward to February

February should test whether multi-format conversion and accessibility semantics become more explicit, and whether the Quarto release line remains temporally active.
