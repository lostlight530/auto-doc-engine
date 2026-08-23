# Auto Doc Engine Scientific Closure Design — Historical Record

**Original date:** 2026-08-05  
**Current status:** **SUPERSEDED on 2026-08-23**  
**Current authority:** `README.md`, `README_zh.md`, `ARCHITECTURE.md`, `ARCHITECTURE_zh.md`, `RESEARCH_CONTRACT.md`, `MANIFEST.yaml`

## Why this file remains

This document records the August 5 transition away from unsupported capability claims and from an unreviewed local V2 reference pack. That historical correction was useful, but several implementation/governance recommendations in the original plan are no longer active.

In particular, the original proposal to add cloud verification, CodeQL, dependency-maintenance automation, or other GitHub-native gating **must not be treated as current repository instructions**. The 2026-08-23 architecture keeps local maintenance checks optional and separates GitHub governance from the research-software architecture.

## Historical problem that this design correctly identified

At the time, repository documentation overclaimed capabilities such as:

- universal API/SQLite binding;
- complete multi-format delivery;
- automatic preservation of arbitrary human edits;
- immutable provenance;
- local files being treated as cloud/main evidence.

The correct durable lesson is still active:

> Repository claims must follow current code and explicit dependency boundaries; unmerged local material is not repository implementation evidence.

## What changed after August 5

By the 2026-08-23 full refresh, the repository has a different implemented baseline:

```text
JSON / CSV / YAML binding
        ↓
typed Markdown AST
        ↓
structural change evidence
        ↓
document graph + bounded research metadata
        ↓
Doctor -> JSON / SARIF
        ↓
cross-platform sync + optional Pandoc
        ↓
optional RO-Crate 1.3 metadata packaging
```

Important concrete changes include:

- SHA-256 AST/diff identity rather than legacy MD5 surfaces;
- YAML data binding;
- research frontmatter fields;
- corrected cross-reference path/heading semantics;
- descriptive readability boundaries;
- versioned Doctor/SARIF profiles;
- cross-platform Markdown copy;
- configurable Pandoc executable;
- concrete RO-Crate 1.3 core metadata writer;
- experimental modules corrected without being promoted into the main chain.

## Current governance boundary

The following August 5 ideas are explicitly **retired as repository defaults**:

- GitHub Actions as a required verification layer;
- CodeQL workflow installation as part of this research refresh;
- dependency-bot automation as a completion criterion;
- “merge only after automated checks pass” as a repository rule;
- treating local test execution as cloud evidence.

Current rule:

> Local checks may exist as optional maintenance tools. They are not GitHub merge gates and are not the scientific architecture.

## Current scientific-closure rule

The repository now uses the stronger distinction:

```text
Provenance != Truth
Digest != Semantic Equivalence
Structure != Meaning
Diagnostic Pass != Peer Review
Metadata != Independent Reproduction
Standard Alignment != External Certification
```

See `RESEARCH_CONTRACT.md` for R0–R3 reproducibility semantics and `ARCHITECTURE.md` for the current module composition.

## Historical local-reference-pack note

The original document referred to a local Windows path (`D:\Agent-farm\work\mit3-analysis`) and local V2 files. Those remain historical context only. They are not a source of truth for the current repository unless specific behavior is deliberately reviewed and committed to `main` through a later change.

## Archive rule

Do not execute this historical design task-by-task. Use it only to understand why earlier capability claims were recalibrated. For current changes, follow the 2026-08-23 authority files listed at the top of this document.
