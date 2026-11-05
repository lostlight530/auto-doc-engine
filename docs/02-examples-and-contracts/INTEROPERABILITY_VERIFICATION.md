# Interoperability and Verification — auto-doc-engine

**Status:** current source/contract-based verification, not a historical-stage record

## Owned producer and consumers

`core/artifact_record.py` produces `auto-doc-engine/artifact-record`. `core/artifact_lineage.py` reads this exact profile and produces `auto-doc-engine/artifact-lineage`, hashing the source sidecar and retaining explicit caller-declared relations. `core/ro_crate.py` separately produces a RO-Crate 1.3 JSON-LD structure

`epistemic-pipeline` may carry the artifact-record **path/reference** in `upstream_artifact_refs`; it does not thereby validate the document or infer the artifact's lineage. `sci-render-kit` can carry declared upstream references into figure evidence without truth inheritance

`tests/test_cross_repo_contract.py` invokes the actual local artifact-record, lineage and RO-Crate producers on ephemeral files. It checks profile identity, sidecar byte hash, declared relation semantics and no scientific-validity/reproduction inheritance. This is **consumer-oriented shape verification**, not an installed three-repository integration run or external RO-Crate Validator conformance

## Verification scope and environment

Python verification baseline: **Python 3.13** and `requirements-python313.txt`, with both direct and observed transitive distribution versions pinned

```bash
python3.13 -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements-python313.txt
python scripts/check_python_environment.py
make test
```

The version checker emits a JSON result and a nonzero exit code on mismatch. This is a bounded **version-set snapshot**, not a PEP 751 `pylock.toml`, a wheel-hash lock, a cross-platform guarantee, a validated new installation, or scientific reproduction. Reconcile a fresh Python 3.13 resolver output and archive package hashes/environment provenance when stronger byte-level replay is needed

The pre-existing optional `.github/workflows/tool-cli-agent-smoke.yml` runs the same bounded checks when matching PR paths trigger it. Workflow definition is not run evidence; inspect the workflow run and commit SHA before claiming execution success

## Scholarly metadata migration

`codemeta.json` uses the official CodeMeta 4.0 context `https://w3id.org/codemeta/4.0` (released 2026-09-29) rather than 3.1. Existing publication DOI, author, license and repository metadata are not rewritten. CodeMeta 4 changes the CodeMeta namespace and schema.org's HTTP/HTTPS mapping, and removes `relatedSoftware` (unused here). The local contract test verifies syntax and CITATION.cff field identity, **not** a remotely expanded JSON-LD graph, external repository index, or citation resolver

Official release: https://github.com/codemeta/codemeta/releases/tag/4.0

## Protocol boundaries

No MCP server, A2A agent service, OTel exporter, independently authenticated approval workflow, publisher certification, scientific truth verification, or R3 independent reproduction is created by these tests

