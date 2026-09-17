# Contributing to auto-doc-engine

Contributions should improve the document/artifact evidence architecture, portability, diagnostics, reproducibility, or public metadata without strengthening scientific claims beyond what the implementation can support.

## Start from the owning surface

Use the current repository contracts to locate ownership:

- `core/`, `templates/`, `sync/`, and `tests/` own executable behavior;
- `MANIFEST.yaml` owns the machine-readable capability map;
- `docs/02-examples-and-contracts/` owns research/artifact semantics;
- `docs/01-source-and-explanation/` and README files explain current behavior;
- `docs/03-maintenance-and-audit/DOCUMENT_STATUS.md` routes current documents and historical evidence;
- `maintenance/cadence.yaml` and maintenance documentation own repository-maintenance semantics;
- `.github/`, security, citation, CodeMeta, and release files are repository infrastructure.

## Development principles

- Structural Markdown behavior belongs in the implemented AST/document pipeline.
- SHA-256 identifies recorded bytes; it does not establish semantic equivalence or scientific validity.
- Structural diff is not merge/conflict resolution.
- Doctor/SARIF findings establish only their implemented predicates.
- Assertion basis describes how a value entered a record, not whether it is correct.
- Audit coverage remains dimensional; do not turn coverage ratios into probability or quality scores.
- Artifact lineage is declared lineage, not inherited scientific authority.
- `supersedes` does not erase predecessor history.
- RO-Crate packaging is an interoperability/export surface, not reproduction by itself.
- Unknown provider/model/version/source/review state remains unknown.
- Experimental modules remain experimental until intentionally integrated.

## Implementation and contract changes

For executable behavior:

1. define or reproduce the behavior at a named revision;
2. update proportionate regression tests;
3. update `MANIFEST.yaml` and active contracts only when their semantics actually change;
4. keep examples and explanatory documentation synchronized with the implemented contract;
5. preserve compatibility and migration expectations where applicable.

External tools should use argument arrays rather than shell interpolation. New dependencies or external runtimes require an explicit reason, portability impact, failure model, and rollback.

## Evidence and lineage changes

When adding an evidence or lineage field, identify separately:

```text
value
assertion / observation basis
what the repository can actually observe
resolution / coverage state
limitations and non-inheritance semantics
```

Do not infer lineage from filenames, timestamps, prose similarity, Git history, or model output.

## Verification

Run checks relevant to the changed surface and supported by the repository. Record exact commands, revision/environment where material, and observed results in the pull request.

Do not report an unrun test, scanner, exporter, or external validator as passed. Structural validation is engineering evidence for the tested surface, not scientific validation.

## Documentation and historical evidence

Use `DOCUMENT_STATUS.md` to distinguish current contracts from dated maintenance and historical snapshots. Do not rewrite FOUR/FIVE/SIX_DAY or other historical bodies merely to match later terminology; correct current interpretation forward.

## Publication and citation metadata

`CITATION.cff`, `codemeta.json`, and `RELEASE_POLICY.md` describe public software identity. A DOI identifies an archived publication; it does not establish R3 reproduction, semantic equivalence with later `main`, or scientific validity.

## Pull requests

Use the repository pull-request template and include:

- the problem and bounded change;
- affected implementation, Manifest/contracts, examples, documentation, or metadata;
- evidence/rationale;
- verification actually performed;
- relevant checks or environments not exercised;
- compatibility and historical impact;
- security/privacy impact;
- a practical rollback.

## Security, privacy, license, and attribution

Follow `SECURITY.md` for sensitive reports. Do not publish credentials, private data, or exploit details requiring coordinated disclosure.

Contributions to repository-owned work are licensed under the MIT License. Third-party material retains its original attribution and licensing, and Git/PR history remains the source of contribution attribution.
