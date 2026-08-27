# Contributing to auto-doc-engine

Contributions should make the document/artifact evidence architecture more truthful, portable or inspectable. Module count and automation volume are not goals by themselves.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
python -m pip install jinja2 "mistune>=3.2.1" pyyaml
```

`make test` remains an optional local maintenance tool. Do not add GitHub Actions, CI/CodeQL workflows, dependency bots or merge-gate requirements as routine maintenance architecture.

## Development principles

- **AST first:** structural Markdown behavior goes through `core/ast_engine.py`.
- **SHA-256 identity:** document/artifact identity surfaces use SHA-256.
- **No `shell=True`:** external tools use argument lists and explicit failures.
- **Portable core path:** use stdlib behavior for built-in operations; keep Pandoc/PDF engines optional.
- **Diff is not merge:** structural changes do not promise conflict-free edit preservation.
- **Diagnostics are bounded:** Doctor/SARIF findings establish only implemented predicates.
- **Research metadata stays bounded:** new frontmatter fields require clear type/semantics.
- **Process disclosure is not authorship:** AI/human-review fields are declarations, not role adjudication or peer review.
- **Artifact records are project-owned:** `auto-doc-engine/artifact-record@1` must not be described as RO-Crate/PROV/Workflow Run Crate conformance.
- **Artifact records stay payload-minimal:** index identities/context rather than duplicating full documents.
- **Offline reference handling:** local files may be hashed; opaque URI/reference values are not automatically fetched.
- **RO-Crate honesty:** `core/ro_crate.py` targets the implemented `auto-doc-engine/ro-crate@1` profile; external validator success is not implied.
- **R3 discipline:** no metadata/checksum/package self-awards independent reproduction.
- **Experimental stays Experimental:** fixes do not automatically integrate experimental modules.
- **Bilingual architecture:** README and Architecture language pairs describe the same implemented boundary.

## Change consistency

| Change | Also inspect |
|---|---|
| renderer/data source | README pair, Architecture pair, MANIFEST, templates/examples |
| AST node/rendering | incremental, cross-ref, executable documentation |
| structural diff | Research Contract, history semantics |
| cross-ref/frontmatter | Doctor, SARIF, templates, Artifact Record |
| process-disclosure field | PROCESS_DISCLOSURE, ARTIFACT_RECORD, README pair, MANIFEST |
| Doctor diagnostic | SARIF mapping |
| sync target | `sync/targets.yaml`, dependency docs, Artifact Record behavior |
| artifact-record field | ARTIFACT_RECORD, Research Contract, MANIFEST, examples |
| RO-Crate entity/relation | Research Contract, MANIFEST, examples |
| experimental behavior | module docstring + public Experimental description |

External version observations should remain separate from compatibility or conformance claims.

## Cross-repository compatibility

The current handoff uses project artifacts/references, not imports:

```text
auto-doc-engine/artifact-record@1
  -> epistemic-pipeline/evidence-envelope@2
  -> sci-render-kit/figure-evidence@2
```

Do not strengthen an imported field's meaning silently. Examples:

```text
heuristic score -> probability      # prohibited without evidence
bounds -> confidence interval       # prohibited without semantics
reviewed -> peer reviewed           # prohibited
source ref -> trusted source        # prohibited
```

## Historical documents

Older design/plan material remains historical. When it conflicts with the 2026-08-27 authority set, current README / Architecture / Research Contract / Artifact Record / Process Disclosure / Manifest take precedence.

## Scientific-integrity reminders

```text
provenance != truth
digest != semantic equivalence
structure != meaning
artifact record != external standard
process disclosure != authorship proof
human review != peer review
RO-Crate metadata != reproduced result
standard alignment != external certification
```

## License

Contributions are licensed under the MIT License.
