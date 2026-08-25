# Contributing to auto-doc-engine

Contributions should make the document/evidence architecture more truthful, portable or inspectable. Module count and automation volume are not goals by themselves.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
python -m pip install jinja2 "mistune>=3.2.1" pyyaml
```

`make test` remains an optional local maintenance tool. Do not add GitHub Actions, CI workflows, CodeQL workflows, dependency bots or merge-gate requirements as part of routine maintenance.

## Development principles

- **AST first:** structural Markdown behavior goes through `core/ast_engine.py`.
- **SHA-256 identity:** document/artifact identity surfaces use SHA-256; do not reintroduce weaker legacy hashes for those contracts.
- **No `shell=True`:** external format tools use argument lists and explicit failure paths.
- **Portable core path:** prefer stdlib operations for built-in behavior; keep Pandoc/XeLaTeX clearly optional.
- **Diff is not merge:** `DiffTracker` reports structure change and does not promise conflict-free edit preservation.
- **Diagnostic severity is local runtime semantics:** error/warning classification belongs to Doctor/SARIF behavior, not repository merge policy.
- **Stable SARIF identity:** changing `ruleId` or `autoDocFinding/v1` identity semantics requires deliberate versioning.
- **Research metadata stays bounded:** add frontmatter fields only when their type and research-object meaning are clear.
- **Process disclosure stays declarative:** `ai_assistance`, `ai_tools`, `human_review`, and `disclosure_ref` describe recorded process context only.
- **Do not infer missing disclosure:** absent fields do not mean `none`, `reviewed`, or “no AI used”.
- **AI/tool names are not provenance proof:** a declared model/tool identifier does not prove authorship, authenticity, capability or output validity.
- **Human review is not peer review:** never describe `human_review: reviewed` as expert validation or scientific correctness.
- **RO-Crate honesty:** `core/ro_crate.py` implements the current `auto-doc-engine/ro-crate@1` core profile. Do not claim external validator success unless it actually occurred.
- **No fake RO-Crate mapping:** process-disclosure fields remain project metadata unless an explicit standards-valid mapping is implemented.
- **Research-object honesty:** provenance, digests and metadata improve traceability; they do not establish scientific truth or independent reproduction.
- **Experimental stays Experimental:** internal fixes do not automatically integrate `template_prewarm`, `async_conduit`, `memory_lattice`, `restart_protocol`, or `self_observe`.
- **Bilingual architecture:** README and Architecture language pairs describe the same implemented boundary.
- **Evidence-aware templates:** generated confidence/evidence fields must preserve their declared semantics rather than silently upgrading a score into probability.

## Change consistency

When behavior changes, review the nearest connected surfaces:

| Change | Also inspect |
|---|---|
| renderer/data source | README pair, Architecture pair, MANIFEST, templates/examples |
| AST node/rendering | incremental, cross-ref, executable documentation |
| structural diff | Research Contract, history semantics |
| cross-ref/frontmatter | Doctor, SARIF, templates |
| process-disclosure field | PROCESS_DISCLOSURE, README pair, Architecture pair, Research Contract, MANIFEST, examples |
| Doctor diagnostic | SARIF mapping |
| sync target | `sync/targets.yaml`, dependency docs |
| RO-Crate entity/relationship | Research Contract, MANIFEST, examples |
| experimental behavior | module docstring + public Experimental description |

External version observations should be recorded separately from compatibility claims.

## Historical documents

The 2026-08-05 Superpowers plan/spec files remain as historical records. Their GitHub CI/CodeQL/cloud-verification recommendations are superseded by the 2026-08-26 architecture and must not be treated as active repository instructions.

## Scientific-integrity reminders

- provenance ≠ truth
- digest ≠ semantic equivalence
- structure ≠ meaning
- AI/process disclosure ≠ authorship adjudication
- human review ≠ peer review or scientific validity
- local diagnostic success ≠ peer review
- RO-Crate metadata ≠ reproduced result
- standard alignment ≠ external certification

## License

Contributions are licensed under the MIT License.
