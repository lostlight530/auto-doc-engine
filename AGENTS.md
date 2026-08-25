# Agent Guide — auto-doc-engine

This is the operational guide for agents modifying the repository. Current capability authority is `README.md` / `README_zh.md`, `ARCHITECTURE.md` / `ARCHITECTURE_zh.md`, `RESEARCH_CONTRACT.md`, `PROCESS_DISCLOSURE.md`, and `MANIFEST.yaml`.

## 1. Current system identity

The integrated architecture is:

```text
structured data
  -> renderer
  -> typed Markdown AST
  -> structural diff / document graph / research metadata
  -> artifact process disclosure metadata
  -> Doctor
  -> JSON / SARIF
  -> sync
  -> optional RO-Crate 1.3 metadata
```

Core files:

```text
core/renderer.py      JSON / CSV / YAML -> Jinja2 Markdown
core/ast_engine.py    typed Markdown AST + normalized renderer
core/incremental.py   structural change reports + bounded atomic history
core/cross_ref.py     local Markdown reference graph + diagnostics
core/frontmatter.py   bounded research metadata + process disclosure
core/readability.py   descriptive Latin/CJK heuristics
core/doctor.py        auto-doc-engine/doctor@1
core/sarif.py         auto-doc-engine/sarif@1
core/sync.py          cross-platform copy + optional Pandoc conversions
core/ro_crate.py      auto-doc-engine/ro-crate@1
```

Experimental, **not integrated**:

```text
template_prewarm.py
async_conduit.py
memory_lattice.py
restart_protocol.py
self_observe.py
```

Fixing an Experimental module does not promote it automatically.

## 2. Repository-governance boundary

Do **not** add GitHub Actions, CI workflows, CodeQL workflows, dependency-update bots, branch-protection assumptions, or merge-gate language as part of normal repository maintenance.

Local commands such as `make test` may remain available as optional maintenance tools, but they are not repository architecture and are not a prerequisite encoded by GitHub.

The historical 2026-08-05 Superpowers plans/specs are retained as history and are superseded where they conflict with this 2026-08-26 baseline.

## 3. Local inspection tools

When useful:

```bash
python -m pip install jinja2 "mistune>=3.2.1" pyyaml
make test
```

Operational examples:

```bash
python core/doctor.py <docs_dir> --json
python core/sarif.py <docs_dir> -o output/doctor.sarif
python core/ro_crate.py output report.md \
  --name "Research artifact set" \
  --description "Rendered artifacts" \
  --author lostlight530
```

These commands produce local evidence. They do not establish external compatibility, peer review, publisher-policy compliance, or independent reproduction.

## 4. Hard implementation rules

1. **AST first.** Structural Markdown changes go through `ASTNode`, not regex mutation.
2. **SHA-256 identity.** Do not reintroduce MD5 for document/artifact identity surfaces.
3. **No `shell=True`.** External commands use argument arrays.
4. **Built-in before platform-specific.** Core Markdown copy uses Python stdlib, not `cp` / `copy` shell commands.
5. **Explicit dependency boundary.** Pandoc/XeLaTeX remain optional and missing tools remain observable.
6. **Normalized Markdown is not byte preservation.** Do not claim source-format round-trip fidelity.
7. **Diff is not merge.** `incremental.py` reports structural change only.
8. **Hints are not semantics.** cross-ref near-miss and readability signals are heuristics.
9. **Process disclosure is declared, not inferred.** Missing AI/human-review fields stay absent/unknown; do not convert them to `none` or `reviewed`.
10. **AI/tool disclosure is not authorship or validity.** `ai_tools` names are human-readable declarations, not vendor-verified provenance proof.
11. **Human review is not peer review.** `human_review: reviewed` must never be described as scientific validation.
12. **Confidence semantics travel with values.** Never rewrite an upstream score as calibrated probability without evidence.
13. **Experimental names are not claims.** Historical metaphorical class/module names may remain for compatibility, but docs describe actual implementation semantics.

## 5. Frontmatter/process-disclosure boundaries

Current bounded process fields:

```text
ai_assistance: none | used | not_declared
ai_tools[]
human_review: reviewed | partial | not_reviewed | not_declared
disclosure_ref
```

Type/enum violations are errors. Cross-field incompleteness is warning-level.

Do not add a field whose meaning silently requires this repository to adjudicate:

```text
authorship
AI-generated-text detection
model authenticity
peer review
source credibility
publisher AI-policy compliance
scientific validity
```

unless a separate explicit architecture is designed and documented.

Detailed semantics are in `PROCESS_DISCLOSURE.md`.

## 6. Standards boundaries

### SARIF

Target: OASIS SARIF 2.1.0 + Approved Errata 01.

Keep:

- stable namespaced `ruleId`;
- `autoDocFinding/v1` logical fingerprints;
- source-profile linkage to Doctor.

Do not imply that a SARIF consumer certifies the repository.

### RO-Crate

Target: RO-Crate 1.3.

The standards-facing JSON-LD emitted by `core/ro_crate.py` must use terms supported by the selected context. Keep project-internal profile names in repository metadata/docs rather than inventing undefined context terms.

Implemented profile currently covers metadata descriptor, root Dataset, File payloads, authors, content size/media type and SHA-256 PropertyValue identity.

Current process-disclosure frontmatter fields remain project metadata; do not emit them as RO-Crate standard properties without an explicit standards-valid mapping.

Do not claim external validator success unless one was actually run and recorded.

## 7. Where to change what

| Goal | Primary files | Synchronize |
|---|---|---|
| data source | `core/renderer.py` | README pair, Architecture pair, MANIFEST |
| Markdown node | `core/ast_engine.py` | diff/cross-ref compatibility + docs |
| diff semantics | `core/incremental.py` | Research Contract + docs |
| graph/link semantics | `core/cross_ref.py` | Doctor/SARIF semantics + docs |
| metadata field | `core/frontmatter.py` | templates + docs + MANIFEST |
| process-disclosure field | `core/frontmatter.py` | Process Disclosure + README/Architecture/Research Contract/MANIFEST |
| readability metric | `core/readability.py` | Doctor/SARIF descriptions |
| Doctor finding | `core/doctor.py` | `core/sarif.py` when exportable |
| SARIF rule | `core/sarif.py` | preserve identity/version semantics |
| conversion target | `core/sync.py`, `sync/targets.yaml` | dependency docs |
| RO-Crate entity/relationship | `core/ro_crate.py` | Research Contract + MANIFEST + examples |
| template semantics | `templates/jinja2/` | evidence/frontmatter schema |
| public architecture | README/Architecture/Research Contract/Process Disclosure/MANIFEST | update together |

## 8. Research-object invariants

A generated/handoff artifact may record:

```text
artifact_id
source_refs
content_sha256
generated_with
provenance_ref
validation_status
reproducibility_level
ai_assistance
ai_tools[]
human_review
disclosure_ref
```

Interpretation boundaries:

- hash = byte identity, not truth;
- process disclosure = declared workflow context, not authorship/peer review;
- RO-Crate = interoperable contextual metadata, not independent reproduction;
- diagnostic success = implemented predicates evaluated, not peer review;
- R3 = an actual separate rerun + declared comparison criterion.

Preferred downstream audit profiles currently include `epistemic-pipeline/evidence-envelope@2` and `sci-render-kit/figure-evidence@2`; these are handoff targets, not import dependencies.

## 9. Experimental-module rules

When touching Experimental modules:

- improve correctness if a real bug is visible;
- preserve the `[EXPERIMENTAL]` boundary in documentation;
- do not wire them into the canonical chain just because they are improved;
- describe the concrete data structure/algorithm rather than metaphorical names;
- record determinism/performance claims only when the implementation actually establishes them.

## 10. Documentation consistency

Keep English/Chinese README and Architecture files conceptually synchronized. Examples and templates must use the same evidence/process semantics as the root docs. Historical design documents must clearly identify when a newer baseline supersedes them.
