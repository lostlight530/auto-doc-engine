# Four-Day Consolidation — auto-doc-engine

**Window:** 2026-08-24 → 2026-08-27  
**Repository role:** research-artifact / document-evidence plane  
**Status:** implementation and architecture consolidation snapshot

## 1. What changed over these four days

The repository moved from “document automation with diagnostics” toward a more
explicit **research-artifact infrastructure** without turning into an AI agent or
workflow engine.

### 24 Aug — implementation truth and external standards

The canonical path was tightened around:

- typed Markdown AST rather than regex mutation;
- SHA-256 structural identity;
- explicit add/modify/delete/unchanged structural evidence;
- document graph and frontmatter diagnostics;
- SARIF 2.1.0 + Approved Errata 01 findings interchange;
- cross-platform sync and explicit optional Pandoc boundaries;
- real RO-Crate 1.3 output instead of a documentation-only proposal;
- R0–R3 reproducibility language with R3 reserved for an actual separate rerun.

### 25 Aug — autonomous-science frontier calibration

The repository was positioned against the emerging 2026 autonomous-science
literature: provenance-complete science needs durable artifact identity and
inspectable research material, but provenance itself does not establish truth.

### 26 Aug — process disclosure

Frontmatter gained bounded declarations for:

```text
ai_assistance
ai_tools[]
human_review
disclosure_ref
```

This made AI/human production context portable while explicitly refusing to
infer authorship, peer review, scientific validity or publisher-policy
compliance.

### 27 Aug — artifact record

The missing middle layer is now implemented:

```text
frontmatter
    ↓
auto-doc-engine/artifact-record@1
    ↓
optional downstream evidence processing
    ↓
optional RO-Crate 1.3 packaging
```

`artifact-record@1` binds one source document to concrete derivative hashes,
frontmatter diagnostics, declared source refs, process disclosure,
configuration/provenance refs and local reproducibility semantics.

## 2. Why the artifact record is separate from RO-Crate

RO-Crate is the external Research Object packaging target. The artifact record
is a small project-owned handoff record.

That separation is intentional:

```text
artifact record
  = one bounded production/handoff record

RO-Crate
  = broader linked Research Object packaging
```

If both are enabled, the artifact record can itself be packaged as an ordinary
RO-Crate payload. The repository does not invent an undefined RO-Crate property
for the project record and does not claim Workflow/Process/Provenance Run Crate
conformance.

## 3. Global signals borrowed, not copied

### Provenance as corrective infrastructure

*Provenance grounds trust in autonomous science* (Nature Computational Science,
20 Aug 2026) argues for complete, re-openable records of what autonomous systems
reasoned, did and measured so errors can be audited and corrected.

Borrowed design principle:

> research artifacts should carry enough stable identity and context that a
> later process can reopen how they were produced.

Not borrowed as a claim:

> provenance makes the artifact scientifically correct.

### Responsible AI scientific publishing

The 20 Aug 2026 Nature Computational Science editorial on responsible and
transparent use of AI in scientific publishing emphasizes transparency,
accountability and human oversight.

Borrowed design principle:

> production/review context should be representable explicitly rather than
> inferred from prose or omitted.

Not borrowed as a claim:

> a metadata field satisfies a publisher policy.

### Artifact-centered claim-aware observability

Yin et al., *Artifact-centered Claim-aware Observability for Autonomous
Scientific Agents* (arXiv:2608.18312), argues that model-call logs are not
enough: artifacts, claims and their relations need portable audit structure.

Borrowed design principle:

> an artifact should be independently addressable before downstream claim
> reasoning tries to use it.

### EarthVerse

EarthVerse (arXiv:2608.23525, 24 Aug 2026) shows a broader scientific-agent
problem: strong local task performance does not guarantee a consistent chain
across evidence, scales, units, computation and physical interpretation.

Borrowed design principle:

> preserve boundaries and identities at transitions; do not assume downstream
> consistency can be reconstructed from a final answer.

### RO-Crate 1.3 and Workflow Run Crate family

RO-Crate 1.3 remains the repository's external packaging target. The RO-Crate
community also maintains Process Run Crate, Workflow Run Crate and Provenance
Run Crate profiles for execution provenance.

Borrowed design principle:

> data products and execution/provenance records are related but distinct
> objects.

The repository deliberately does **not** claim conformance to those workflow-run
profiles.

## 4. Current canonical architecture

```text
Structured source
      ↓
Jinja2 binding
      ↓
Typed Markdown AST
      ├── structural change evidence
      ├── cross-document reference graph
      ├── frontmatter + process disclosure
      └── readability diagnostics
      ↓
Doctor / JSON / SARIF
      ↓
SyncEngine
      ├── Markdown / HTML / DOCX / PDF / EPUB as available
      ├── optional artifact-record@1
      └── optional RO-Crate 1.3
```

## 5. Cross-repository contract after Day 4

```text
auto-doc-engine
  artifact-record@1
  document/process disclosure
        ↓
epistemic-pipeline
  upstream artifact refs
  claim-verification@1
  evidence-envelope@2
        ↓
sci-render-kit
  upstream claim audit ref
  figure-claim-audit@1
  figure-evidence@2
```

The contract travels through files/references, not hidden imports.

## 6. What remains deliberately out of scope

- automatic source-credibility adjudication;
- scientific truth inference;
- semantic diff or automatic conflict-free merge;
- autonomous peer review;
- provider/model identity verification;
- automatic authorship decisions;
- publisher-policy certification;
- Workflow Run Crate / PROV-O conformance claims that are not implemented;
- GitHub Actions / CI / CodeQL / merge gates as research architecture.

## 7. Primary references

Checked through 2026-08-27:

1. MacKnight R, Novitskiy IM, Radadiya R, et al. **Provenance grounds trust in autonomous science.** Nature Computational Science 6, 804–807 (2026). https://doi.org/10.1038/s43588-026-01035-4
2. **Responsible and transparent use of AI in scientific publishing.** Nature Computational Science 6, 803 (2026). https://doi.org/10.1038/s43588-026-01043-4
3. Yin X, Du M, Prince MH, Cherukara MJ. **Artifact-centered Claim-aware Observability for Autonomous Scientific Agents.** arXiv:2608.18312. https://arxiv.org/abs/2608.18312
4. **EarthVerse: Benchmarking and Advancing AI Agents for Global Earth Science.** arXiv:2608.23525. https://arxiv.org/abs/2608.23525
5. RO-Crate 1.3 specification: https://www.researchobject.org/ro-crate/specification/1.3/
6. RO-Crate profiles, including Workflow Run Crate family: https://www.researchobject.org/ro-crate/profiles.html

## 8. Bottom line

The four-day change is not “more automation”. It is a stronger boundary between:

```text
document content
artifact identity
production context
diagnostic evidence
research-object packaging
```

That boundary is the repository's research-engineering value.
