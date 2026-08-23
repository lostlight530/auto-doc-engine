# Contributing to auto-doc-engine

## Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
python -m pip install jinja2 "mistune>=3.2.1" pyyaml
```

`make test` is available as an optional local maintenance check. It is not a GitHub merge gate.

## Development principles

- **AST first:** structural Markdown behavior goes through the shared AST layer rather than regex/string mutation.
- **No `shell=True`:** external format tools use argument lists and explicit failure paths.
- **Diff is not merge:** `DiffTracker` describes structural change; do not claim automatic conflict-free preservation of arbitrary human/agent edits.
- **Doctor severity is intentional:** new findings must be classified as error or warning and reflected in the SARIF mapping.
- **Stable SARIF identity:** `ruleId` and `autoDocFinding/v1` fingerprint semantics are interoperability contracts; breaking identity requires a new profile/fingerprint version.
- **Research-object honesty:** follow `RESEARCH_CONTRACT.md`; provenance/digests establish traceability or identity under declared rules, not scientific truth.
- **RO-Crate boundary:** RO-Crate 1.3 is a proposed mapping target only until a conforming writer/validator exists.
- **Honest status:** public capabilities are labelled Implemented / Optional / Experimental / Not Integrated from current code and evidence.
- **Bilingual architecture:** README and ARCHITECTURE language pairs change together.
- **Executable docs:** Python-fenced blocks in README/ARCHITECTURE should remain runnable when used as executable examples.
- **Dependency discipline:** runtime Python dependencies remain `jinja2`, `mistune>=3.2.1`, and `pyyaml` unless a change explicitly justifies and documents more.

See `AGENTS.md` for the operational module map and `RESEARCH_CONTRACT.md` for research-artifact/evidence semantics.

## Change consistency

When public behavior changes, keep implementation, capability claims, SARIF mappings, bilingual docs, and MANIFEST aligned. Optional dependencies and Experimental modules must remain explicit.

## License

Contributions are licensed under the MIT License.
