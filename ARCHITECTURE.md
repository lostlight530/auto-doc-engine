# Architecture Design & Research Boundaries

[简体中文](ARCHITECTURE_zh.md) | [English](ARCHITECTURE.md)

> Current architecture calibration: 2026-08-23. This document describes implemented repository behavior and explicit boundaries. Aspirational interoperability is labeled `proposed`.

## 1. Positioning

`auto-doc-engine` is an AST-driven toolkit for inspectable document generation, structural change detection, cross-document health checks, and optional format conversion.

Its architectural priority is not maximum automation. It is **evidence-preserving automation with explicit failure semantics**: document structure, transformations, references, optional dependencies, and output status should remain inspectable instead of being hidden behind a single success flag.

The repository is not a semantic truth engine, collaborative merge system, immutable provenance ledger, or fully integrated production publishing pipeline.

## 2. Canonical data flow

```text
JSON / CSV source
      |
      v
Jinja2 binding + Markdown text
      |
      v
Mistune Markdown AST
      |
      +--> structural diff records
      |
      +--> cross-document reference / health analysis
      |
      v
Markdown rendering
      |
      v
optional format synchronization
      |
      v
artifact + explicit result / error state
```

The current modules are independently callable. This diagram is an architectural composition of their contracts, not a claim that every stage is wired into one validated production facade.

## 3. Core invariants

### 3.1 AST-first, not string-replacement-first

`core/ast_engine.py` parses supported Markdown constructs into typed nodes using Mistune. Structural operations should target the parsed representation whenever the repository has an AST contract for the content.

Unsupported nodes must fail explicitly instead of being silently reinterpreted. Parse/render behavior is structural, not byte-for-byte lossless formatting preservation.

### 3.2 Structural diff is a detector, not a merge engine

`core/incremental.py` renders nodes, computes SHA-256 digests (shortened for the stored/matching signature), and uses `difflib.SequenceMatcher` over sibling-node signatures to classify `add`, `modify`, `delete`, and `unchanged` records.

This corrects two older architectural overclaims:

- the implementation uses SHA-256, not MD5;
- computing a structural delta does **not** guarantee automatic preservation of arbitrary human edits.

The repository currently does not provide a general patch application, conflict-resolution, ownership, or CRDT/merge layer. Human-edit preservation remains an upper-layer workflow property until there is an executable contract for it.

### 3.3 Data binding is intentionally bounded

`core/renderer.py` currently binds JSON and CSV data into Jinja2 templates. SQLite and network/API bindings are not integrated. "Data-source independent" is therefore an architectural direction, not a current universal capability.

### 3.4 Cross-document structure is a diagnosable graph

`core/cross_ref.py` builds document/heading references from parsed Markdown links. It distinguishes:

- valid indexed targets;
- `near_miss` broken links with candidate suggestions;
- `dangling` references to missing/planned documents;
- recurring missing targets that can be surfaced as backlog.

This graph is a documentation structure. It does not imply a semantic knowledge graph or semantic equivalence between linked documents.

### 3.5 Document health is evidence about document structure

`core/frontmatter.py`, `core/readability.py`, and `core/doctor.py` form a health layer that can report schema violations, broken references, orphans, cycles, readability heuristics, and graph statistics.

A passing doctor report means that the implemented predicates passed. It does not establish factual correctness, scientific validity, translation quality, or peer-review readiness.

### 3.6 Format synchronization is capability- and environment-bounded

`core/sync.py` invokes external tools with argument lists and does not use `shell=True`.

Current target semantics are explicit:

| Target | Normal path | Boundary |
| --- | --- | --- |
| Markdown | platform `cp` command | current implementation is not a portable Python copy abstraction |
| HTML | Pandoc | `sync_with_fallback()` can use Mistune when Pandoc is unavailable |
| DOCX | Pandoc | fallback does not fabricate DOCX; it reports Markdown-only availability |
| PDF | Pandoc + configured XeLaTeX engine | depends on the local toolchain |
| EPUB | Pandoc | depends on the local toolchain |

A missing converter or failed subprocess is an explicit failure/unsupported state, not successful multi-format delivery.

## 4. Provenance and research-object boundary

The repository now has a root [Research Contract](RESEARCH_CONTRACT.md). It defines the shared evidence vocabulary used to reason about this repository together with `epistemic-pipeline` and `sci-render-kit`.

The core distinction is:

```text
artifact identity != semantic truth
provenance != independent reproduction
structural diff != safe merge
health check != scientific validation
```

RO-Crate 1.3 (published 2026-06-22) is recorded as a **proposed interoperability target**. No current output, manifest, or history file is claimed to be an RO-Crate. A conforming exporter/validator plus executable tests would be required before that status can change.

## 5. Reproducibility doctrine

The local project vocabulary is defined in `RESEARCH_CONTRACT.md`:

- `R0 Traceable`: metadata/source references exist;
- `R1 Replay-addressable`: input/config/revision/digests and commands address a replay;
- `R2 Environment-bounded`: runtime/dependency/tool assumptions are also captured;
- `R3 Reproduced`: a separate rerun has actually been performed and compared.

These labels are local doctrine, not an external standard. A metadata file alone must never be promoted to `R3`.

## 6. Dependency evidence as of 2026-08-23

External ecosystem facts are kept separate from repository verification:

- Mistune `>=3.2.1` remains the repository's documented security floor. PyPI lists 3.3.4 as the latest observed release on 2026-08-23. Recording that release does not claim that this repository has verified every 3.3.x behavior.
- Pandoc 3.10.2 is the latest observed release (2026-08-11). Pandoc remains an optional local dependency and this repository does not claim validation against 3.10.2 merely because the version is current.

This distinction prevents "latest upstream" from being silently converted into "tested here".

## 7. Architecture doctrine

1. **Implemented behavior outranks prose.** If code and documentation disagree, documentation must be corrected or the implementation must receive an executable contract.
2. **No fabricated success.** Optional dependencies, unsupported nodes, broken references, and failed conversions remain visible failures or bounded fallbacks.
3. **No semantic inflation.** Hashes, ASTs, links, and readability metrics are structural evidence, not semantic truth.
4. **No integration by wording.** Experimental modules and cross-repository contracts remain non-integrated until the canonical execution path and tests prove otherwise.
5. **Version external standards.** A standard, dependency, or research-object profile is cited with a date/version and a local implementation status.

## 8. Primary architecture references

Retrieved 2026-08-23:

- [RO-Crate 1.3 Specification](https://www.researchobject.org/ro-crate/1.3/)
- [FAIR Principle R1.2](https://www.go-fair.org/fair-principles/r1-2-metadata-associated-detailed-provenance/)
- [Mistune on PyPI](https://pypi.org/project/mistune/)
- [Pandoc releases](https://github.com/jgm/pandoc/releases)
