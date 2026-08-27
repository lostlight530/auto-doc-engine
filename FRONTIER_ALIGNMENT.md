# Frontier Alignment — auto-doc-engine

**Status:** non-normative research-positioning snapshot  
**Calibrated:** 2026-08-28

`auto-doc-engine` occupies the research-artifact / document-evidence plane. It is not a scientific agent and does not infer scientific truth.

## Current engineering thesis

A completed document or model-call trace is not automatically a durable research record. Before downstream reasoning, research material benefits from explicit identity, declared process context, **assertion basis**, dimensional audit coverage, diagnostics and portable handoff.

```text
source material
  -> structured binding
  -> typed document structure
  -> structural-change evidence
  -> metadata/reference diagnostics
  -> declared process context
  -> rendered derivatives
  -> artifact-record
       ├─ assertion basis
       └─ dimensional audit coverage
  -> optional RO-Crate 1.3 package
```

## Three distinct objects

```text
frontmatter
  what the document declares about itself

auto-doc-engine/artifact-record
  bounded project handoff for one source/derivative set

RO-Crate 1.3
  external Research Object packaging
```

These layers are related but intentionally not collapsed.

## Day-5: basis before interpretation

A metadata value such as a provider/tool name, review state or source reference is easier to audit when the record also says how that value was obtained.

Current artifact-side bases include:

```text
document-frontmatter
caller-declared
runtime-observed-local-bytes
runtime-observed-local-filesystem
```

The repository does not infer AI use from text and explicitly records `automatic_ai_detection_used: false` in the artifact-record process disclosure.

```text
assertion basis != truth
explicit disclosure != AI detection
AI detection != authorship adjudication
```

## Day-5: coverage without fake quality scores

Claim-level auditability research increasingly separates dimensions such as provenance coverage, soundness, contradiction transparency and audit effort. This repository only implements the narrow part it can compute from its own artifacts: **coverage**.

Examples include declared-source resolution counts, local-file ratios, lineage-reference resolution and process-disclosure field presence.

It does not claim provenance soundness.

```text
coverage != correctness
coverage ratio != probability
local resolution != source credibility
```

No aggregate research-quality score is produced.

## Global signals used for calibration

### Provenance-complete autonomous science

Nature Computational Science's August 2026 provenance discussion emphasizes complete, re-openable records that make autonomous-science actions auditable and correctable.

Borrowed principle: durable identity/context matter.

Not borrowed claim: provenance makes the science correct.

### Transparent AI use and human oversight

Scientific-publishing guidance emphasizes transparency, accountability and human oversight.

Borrowed principle: process declarations should be explicit and portable.

Not borrowed claim: a metadata declaration automatically satisfies publisher policy.

### Artifact-centered claim-aware observability

Current scientific-agent observability work argues that model-call traces alone are insufficient; artifacts, claims and their relations should be first-class audit objects.

Borrowed principle: downstream reasoning should receive identifiable artifacts rather than reconstruct identity from prose.

### From trajectories to evidence

Trajectory-to-evidence work distinguishes completed execution from auditable evidence and post-execution claim qualification.

Borrowed principle: finished output is not automatically evidence.

### Brain Researcher

Brain Researcher emphasizes evidence-bounded claims and explicit review outcomes.

Borrowed principle: evidence and review state should remain explicit.

Not borrowed: scientific accepted/rejected statuses, because this repository has no scientific-review authority.

### EarthVerse

EarthVerse shows that strong local task performance can coexist with poor strict end-to-end consistency across evidence, units, computation and interpretation.

Borrowed principle: preserve transition boundaries and artifact identities rather than assuming final-output consistency.

### Claim-level auditability

*From Fluent to Verifiable* frames provenance coverage, provenance soundness, contradiction transparency and audit effort as separate auditability concerns.

Borrowed today: structural coverage dimensions.

Not implemented: provenance soundness or scientific evidence adjudication.

### AI detection versus disclosure

Recent Nature reporting on AI-detection tools reinforces that automatic detection is a separate inference problem from explicit process disclosure.

This repository uses explicit disclosure and basis metadata; it does not silently add AI-text classification to the canonical path.

## Relation to neighboring infrastructure

- Jupyter Book / MyST / publication systems: broader executable/structured publishing; this repository focuses on artifact identity, structural evidence, diagnostics and handoff.
- RO-Crate: external packaging/interoperability target rather than something to replace.
- W3C PROV / Run Crate profiles: richer execution lineage belongs in dedicated provenance/run layers; this repository does not claim conformance it does not implement.
- Scientific agents: potential producers/consumers of artifact records, not direct equivalents.

## Cross-repository position

```text
auto-doc-engine/artifact-record
  assertion basis + artifact coverage
        ↓ optional reference
epistemic-pipeline/claim-verification
epistemic-pipeline/evidence-envelope
        ↓ optional reference
sci-render-kit/figure-claim-audit
sci-render-kit/figure-evidence
```

The system-level idea is preserving research semantics across artifact, epistemic process and scientific communication layers.

## External direction boundary

The sources above are design signals, not validation, endorsement, novelty proof or standards certification for this repository.

## Hard boundaries

```text
provenance != truth
metadata != evidence credibility
hash identity != semantic equivalence
assertion basis != correctness
coverage != quality
coverage ratio != probability
artifact completeness != experiment completeness
package completeness != scientific validity
RO-Crate != independent reproduction
AI disclosure != AI detection
AI disclosure != authorship adjudication
human review != peer review
```

> Day 5 makes the artifact plane more auditable by recording not only artifact identity and declared process context, but also the basis and coverage of those records without manufacturing a scientific-quality score.
