# Contributing to auto-doc-engine

Contributions should make the document/artifact evidence architecture more truthful, portable or inspectable. Module count and automation volume are not goals by themselves.

## Development principles

- Structural Markdown behavior goes through `core/ast_engine.py`.
- Document/artifact identity surfaces use SHA-256.
- External tools use argument lists; do not introduce `shell=True`.
- Built-in operations prefer portable stdlib behavior; Pandoc/PDF engines remain optional.
- Structural diff is not merge or conflict resolution.
- Doctor/SARIF findings establish only implemented predicates.
- New frontmatter fields need explicit type and semantics.
- AI/human-review fields are declarations, not authorship adjudication or peer review.
- `auto-doc-engine/artifact-record` is project-owned, not RO-Crate/PROV/Run Crate conformance.
- `auto-doc-engine/ro-crate` is the project exporter identity; RO-Crate 1.3 is the external standard target.
- Artifact records stay payload-minimal; local files may be hashed while URI/opaque refs are not automatically fetched.
- Metadata/checksums/packages never self-award R3 reproduction.
- Experimental modules remain Experimental until intentionally integrated.
- Unknown provider/model/version/source/review state remains unknown; never guess.

## Stable project identifiers

```text
auto-doc-engine/doctor
auto-doc-engine/sarif
auto-doc-engine/artifact-record
auto-doc-engine/process-disclosure
auto-doc-engine/frontmatter-validation
auto-doc-engine/ro-crate
autoDocFinding
```

Do not append decorative `@1/@2` or `/v1` suffixes. Real external standard/runtime versions remain legitimate evidence when actually known.

## Cross-repository handoff

```text
auto-doc-engine/artifact-record
  -> epistemic-pipeline/claim-verification
  -> epistemic-pipeline/evidence-envelope
  -> sci-render-kit/figure-evidence
```

Do not silently strengthen imported semantics:

```text
heuristic score -> probability      # prohibited without calibration evidence
bounds -> confidence interval       # prohibited without declared semantics
reviewed -> peer reviewed           # prohibited
source ref -> trusted source        # prohibited
```

## Repository governance boundary

Local checks may be used manually. Do not add GitHub Actions, CI/CodeQL workflows, dependency bots, branch-protection assumptions or merge-gate architecture as routine maintenance.

## License

Contributions are licensed under the MIT License.
