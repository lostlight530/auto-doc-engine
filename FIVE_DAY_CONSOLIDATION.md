# Five-Day Consolidation — auto-doc-engine

**Window:** 2026-08-24 → 2026-08-28  
**Repository role:** research-artifact / document-evidence plane  
**Status:** implementation and architecture consolidation snapshot

## 1. Five-day trajectory

### Day 1 — implementation truth

The repository was tightened around typed Markdown structure, SHA-256 identity, explicit structural-change reports, bounded frontmatter validation, cross-document diagnostics, SARIF interchange, optional conversion dependencies and a real RO-Crate 1.3 writer.

### Day 2 — autonomous-science calibration

The architecture was positioned as a lower research-infrastructure layer rather than an autonomous scientist. Provenance and inspectability were treated as corrective infrastructure, not scientific truth.

### Day 3 — process disclosure

Document frontmatter gained bounded declarations for AI assistance, tool identifiers, human review and disclosure references. The repository explicitly refused to infer authorship, peer review or scientific validity from those fields.

### Day 4 — portable artifact record

`auto-doc-engine/artifact-record` became the lightweight machine handoff between in-document metadata and broader RO-Crate packaging. It binds source/derivative byte identity, metadata, process disclosure, diagnostics, lineage refs and local reproducibility semantics.

### Day 5 — assertion basis + dimensional coverage

The artifact record now records **how fields were obtained**, not only their values:

```text
document-frontmatter
runtime-observed-local-bytes
caller-declared
runtime-observed-local-filesystem
```

It also emits dimensional `audit_coverage` instead of a synthetic total quality score.

## 2. Current canonical chain

```text
structured source
    ↓
Jinja2 binding
    ↓
typed Markdown AST
    ↓
structural-change evidence
    ↓
document/reference/frontmatter diagnostics
    ↓
process disclosure
    ↓
rendered derivatives
    ↓
artifact-record
  ├─ concrete byte identities
  ├─ assertion basis
  ├─ reference-resolution states
  ├─ dimensional audit coverage
  ├─ validation summary
  └─ R0–R3 declaration boundary
    ↓
optional RO-Crate 1.3 packaging
```

## 3. Why Day 5 matters

A provenance field without a basis can be ambiguous. For example:

```text
model: X
```

could mean a user typed the name, an SDK reported it, a log recorded it, or a classifier guessed it. Those are not equivalent evidence.

The Day-5 contract therefore makes the acquisition basis explicit wherever this repository can do so honestly.

Similarly, “coverage” is decomposed instead of converted into a single score. The repository may know how many declared source refs are local files, but it does not know whether those sources are credible or sufficient.

## 4. External signals used for calibration

The five-day architecture is informed by, but not certified by:

- Nature Computational Science, *Provenance grounds trust in autonomous science* (20 Aug 2026);
- Nature Computational Science, *Responsible and transparent use of AI in scientific publishing* (20 Aug 2026);
- *Artifact-centered Claim-aware Observability for Autonomous Scientific Agents* (18 Aug 2026);
- *From Trajectories to Evidence: Auditable Experimental Records for Industrial Research Agents* (5 Aug 2026);
- *Bringing analytic rigor to agentic AI for science: The Brain Researcher platform for neuroimaging data analysis* (20 Aug 2026);
- *EarthVerse* (24 Aug 2026);
- *From Fluent to Verifiable: Claim-Level Auditability for Deep Research Agents* (14 Feb 2026);
- Nature reporting on AI-text detection (25 Aug 2026), which reinforces that detection and transparent disclosure are different mechanisms;
- RO-Crate 1.3 and the Workflow/Process/Provenance Run Crate family as external Research Object / execution-provenance references.

## 5. What was borrowed — and what was not

Borrowed design ideas:

- portable artifact identity;
- claim/artifact auditability;
- explicit provenance and applicability boundaries;
- dimensional coverage rather than opaque success claims;
- explicit human/AI process context;
- separation between research products and execution records.

Not borrowed as unsupported claims:

- provenance soundness;
- scientific acceptance/rejection states;
- source credibility scoring;
- model-authenticity detection;
- automatic AI-content detection;
- peer-review status;
- independent reproduction;
- external standards conformance that has not actually been validated.

## 6. Cross-repository role after Day 5

```text
auto-doc-engine
  artifact-record
  assertion basis
  artifact audit coverage
        ↓
epistemic-pipeline
  claim-verification
  claim audit coverage
  evidence-envelope
        ↓
sci-render-kit
  figure-claim-audit
  communication coverage
  figure-evidence
```

The three repositories communicate through files and explicit references. They do not inherit truth claims from one another.

## 7. Hard boundaries

```text
Provenance != Truth
Hash identity != semantic equivalence
Assertion basis != correctness
Declaration != external verification
Coverage != quality
Coverage ratio != probability
Human review != peer review
Artifact record != RO-Crate standard profile
RO-Crate package != independent reproduction
```

## 8. Maintenance boundary

This consolidation does not add GitHub Actions, CI, CodeQL, dependency bots, branch-protection assumptions or merge gates as research architecture.

Local checks remain optional maintenance aids. The Day-5 completion criterion is code/config/document contract consistency plus final branch-vs-main diff auditing, not a claim of scientific validation.
