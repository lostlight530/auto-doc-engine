# Architecture & Philosophy

[简体中文](ARCHITECTURE_zh.md) | [README](README.md)

## 1. Design thesis: document automation is a compiler problem

`auto-doc-engine` treats a document set as three things at once:

1. a **typed syntax tree** that can be parsed and rendered,
2. a **versioned structure** whose changes can be described explicitly,
3. a **knowledge graph** whose references and metadata can become unhealthy.

The architecture therefore follows compiler discipline rather than free-form text mutation. Every higher layer reuses evidence produced by a lower layer instead of inventing a second parser or hidden success condition.

## 2. Six-layer architecture

```text
[Data binding]
      ↓
[Markdown AST]
      ↓
[Structural diff]
      ↓
[Cross-document graph]
      ↓
[Health diagnostics]
      ↓
[Diagnostic interchange] ──> Text / JSON / SARIF
      ↓
[Optional format sync] ─────> Markdown / HTML / DOCX / PDF / EPUB
```

### 2.1 Data binding — `core/renderer.py`

`DataBindingEngine` loads the currently implemented JSON/CSV sources and renders Jinja2 templates. SQLite and network API adapters are deliberately marked Not Integrated until an adapter, failure contract, and tests exist.

### 2.2 AST contract — `core/ast_engine.py`

Mistune is the single Markdown parsing boundary. Supported Mistune nodes map to typed `ASTNode` values; unsupported structure raises an explicit error rather than silently flattening content. The recommended Mistune floor is 3.2.1 because later 3.x releases include the security fixes behind that baseline.

### 2.3 Structural change — `core/incremental.py`

`DiffTracker` aligns sibling AST nodes and reports `add`, `modify`, `delete`, and `unchanged` records. The important boundary is semantic: this layer **describes change**. It does not claim to resolve concurrent human/agent edits or apply conflict-free patches automatically.

### 2.4 Document graph — `core/cross_ref.py`

`EntanglementIndex` reuses the same Markdown parser to build a document/heading index and directed document-level link graph. Missing targets are classified as `near_miss` or `dangling`; repeatedly referenced missing targets become an explicit backlog signal.

### 2.5 Health model — `core/doctor.py`, `core/frontmatter.py`, `core/readability.py`

`doctor` composes existing evidence into one health report:

- unresolved links are errors,
- frontmatter type/enum violations are errors,
- orphans, selected cycles, unknown frontmatter fields, and readability signals are warnings,
- `--strict` promotes warnings into the exit-code gate,
- `--json` exposes the project-native machine-readable model.

Readability and link suggestions remain heuristics. A warning is evidence for review, not proof that prose is bad or a suggested target is intended.

### 2.6 Diagnostic interchange — `core/sarif.py`

The 2026-08-23 calibration adds a standards boundary above the native doctor model. `core/sarif.py` maps the same findings into a conservative OASIS SARIF 2.1.0 + Approved Errata 01 result set.

The mapping deliberately uses:

- stable namespaced `ruleId` values (`doc.link.*`, `doc.frontmatter.*`, `doc.graph.*`, `doc.readability.*`),
- SARIF `level` values that preserve the doctor error/warning distinction,
- physical artifact locations using document-relative URIs,
- a versioned `autoDocFinding/v1` partial fingerprint built from stable finding identity rather than timestamps,
- run properties containing document and graph counts.

This is an **interchange profile**, not a claim that Markdown health analysis is source-code static analysis or that every optional SARIF feature is implemented.

## 3. Output and synchronization boundary

`core/sync.py` is intentionally downstream of document semantics. External commands are invoked with argument arrays rather than `shell=True`. Missing tools remain visible failures. HTML may use the local Mistune fallback; other conversion targets retain their documented external dependencies.

The sync layer is optional because document correctness should be auditable even on a machine with no publishing toolchain installed.

## 4. Verification architecture

The repository now has two complementary gates:

- **repository contract:** `make test` executes deterministic Python-level tests, including living documentation and SARIF mapping;
- **continuous contract:** `.github/workflows/ci.yml` runs that same command with Python 3.12 for pull requests and `main` pushes.

CI does not magically prove environment-dependent converters. Its job is narrower: prevent code, declared capability, examples, and diagnostic semantics from drifting apart.

## 5. Architecture rules

1. **One parser contract.** New structural Markdown behavior must extend the AST layer, not introduce ad-hoc regex mutation.
2. **No success by declaration.** A MANIFEST/README claim follows implementation evidence, never the reverse.
3. **Stable diagnostic identity.** SARIF `ruleId` and fingerprint versions are public interoperability contracts; breaking them requires a new version.
4. **Explicit severity.** Findings must be intentionally classified as errors or warnings.
5. **No hidden shell.** External tools use argument arrays; no `shell=True` escape hatch.
6. **Environment honesty.** Optional publishing tools stay optional and their absence remains observable.
7. **Experimental means unwired.** A standalone module is not promoted because it imports successfully.

## 6. Standards and inspirations

- Compiler pipelines: source → AST → analysis → diagnostics → targets.
- Virtual-DOM-style reconciliation: structural sibling alignment for change description.
- Knowledge-base health tools: graph-level broken-link/orphan/cycle reasoning.
- OASIS SARIF 2.1.0 + Errata 01: interoperable analysis-result transport.
- Citation File Format 1.2.0: machine-readable software citation metadata.
- Executable-documentation culture: examples are part of the repository contract rather than decorative prose.

## 7. Non-goals

The repository does not currently claim a universal document database, real-time collaborative editor, arbitrary byte-preserving Markdown transformer, or end-to-end production conversion service. Those are separate systems with different correctness contracts.
