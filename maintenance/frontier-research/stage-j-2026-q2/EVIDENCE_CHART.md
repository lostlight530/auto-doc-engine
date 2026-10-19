# Evidence and comparison chart — Stage J / 2026-Q2

## Variables and authority
Variables: object/release, date, published change, claimed capability/behavior, analytic evidence consequence, provenance/source family, independent verification state, negative space. Method: descriptive authority appraisal + chronological comparison, no quantitative meta-analysis.

| Finding | Object | Publisher-described evidence | Research interpretation | Authority/directness | Independent reproduction | Temporal scope |
|---|---|---|---|---|---|---|
| F-J1 | O3 | CycloneDX 1.7.1 adds ModelCard.property in Protobuf and modelCard properties/consideration cardinality alignments in XML and adds matching tests. | Serializations of ostensibly one evidence object have versioned schema behavior; version and format need distinct identity. | S3: direct release assertion; one origin | `UNKNOWN / NO_LOCAL_RUN` | 2026-06-02 |
| F-J2 | O4 | Pandoc 3.10 adds --typst-input to pass sys.inputs parameters and changes the default ms PDF engine to groff; ODT style emission also changes. | Transformation receipts should distinguish explicit parameters, inferred defaults and output writer/backend revision. | S4: direct release assertion; one origin | `UNKNOWN / NO_LOCAL_RUN` | 2026-06-04 |

## Comparison across research objects
The selected objects share a **provenance boundary** but not a common experimental population, success metric or runtime. Changes between releases cannot be counted as continuous improvement. Different publishers are independent origins for their own releases, not independent corroboration of one release's correctness.

## Competing interpretation and negative-space chart
- Strong alternative: object selection exposes the provenance dimensions this study prioritizes; it is not representative sampling of the whole field.
- Unsupported: release announcements => independent conformity; public documentation => successful local reproduction; same vendor sources => independent confirmation.
- Missing: measured downstream adoption, release-by-release controlled output comparison, independent specialist review, `auto-doc-engine` runtime/contract audit.
- Schema/format/SDK changes can be incompatible or source-specific; no forced equivalence judgment.
