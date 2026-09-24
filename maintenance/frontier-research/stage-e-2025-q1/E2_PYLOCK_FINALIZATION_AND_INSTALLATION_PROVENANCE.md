# E2 — PEP 751 Finalization and Installation Provenance

## Research question
What does a standardized lock-file format add to reproducibility evidence, and what does it still not prove?

## Evidence
PEP 751 is a Standards Track Packaging PEP with status `Final` and resolution date `2025-03-31`. It specifies `pylock.toml`, requires `lock-version`, records creator identity via `created-by`, supports environment markers and package source forms, and is designed so installers can determine what to install without dependency resolution at install time.

Source: https://peps.python.org/pep-0751/

## Analysis
Stage D observed dependency intent and lock representation as distinct lifecycle states. Stage E adds a standards-level representation for the lock artifact itself.

```text
dependency intent
-> standardized lock representation
-> installer interpretation
-> realized environment
-> execution
```

The arrows remain evidence transitions, not automatic inheritance.

A compliant `pylock.toml` improves portability and auditability of dependency selection, but it does not by itself prove:
- the installer actually consumed that file;
- the environment matched every intended external condition;
- the resulting program executed successfully;
- the produced scientific artifact is correct or reproduced independently.

## Outcome
`SUPPORTED_OBSERVATION / DESIGN_CONVERGENCE_WITH_EXISTING_BOUNDARY`
