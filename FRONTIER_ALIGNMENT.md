# Frontier Alignment — auto-doc-engine

**Status:** non-normative research-positioning snapshot  
**Calibrated:** 2026-08-29

`auto-doc-engine` occupies the research-artifact / document-evidence plane. It is not a scientific agent and does not infer scientific truth.

## Current engineering thesis

A completed document or model-call trace is not automatically a durable research record. Before downstream reasoning, research material benefits from explicit identity, declared process context, assertion basis, dimensional audit coverage, diagnostics, portable handoff and explicit artifact lineage.

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
  -> artifact-lineage
       ├─ typed declared relations
       └─ non-inheritance boundaries
  -> optional RO-Crate 1.3 package
```

## Distinct objects

```text
frontmatter
  what the document declares about itself

auto-doc-engine/artifact-record
  bounded project handoff for one source/derivative set

auto-doc-engine/artifact-lineage
  typed relationship layer across artifact generations

RO-Crate 1.3
  external Research Object packaging
```

These layers are related but intentionally not collapsed.

## Basis before interpretation

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

## Coverage without fake quality scores

Claim-level auditability research increasingly separates dimensions such as provenance coverage, soundness, contradiction transparency and audit effort. This repository only implements the narrow parts it can compute from its own artifacts: descriptive coverage and local reference resolution.

It does not claim provenance soundness.

```text
coverage != correctness
coverage ratio != probability
local resolution != source credibility
```

No aggregate research-quality score is produced.

## Day-6: lineage without inherited authority

Long-running research loses meaning when a successor artifact arrives without an inspectable relation to predecessors. `core/artifact_lineage.py` therefore supports a bounded relation vocabulary:

```text
derived-from
revision-of
supersedes
uses
related-to
```

Relations are caller-declared and may resolve/hash local targets. They are never inferred from filenames, timestamps, prose similarity, Git history or model output.

Every relation keeps:

```text
scientific_validity_inherited: false
reproducibility_inherited: false
```

```text
supersedes != history deletion
revision-of != semantic equivalence
uses != evidence sufficiency
lineage != truth
```

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

Borrowed: structural coverage dimensions.

Not implemented: provenance soundness or scientific evidence adjudication.

### Praxist — solution lineages

**Praxist: From Experimental Artifacts to Solution Lineages** (arXiv:2608.25955, 26 Aug 2026) argues that isolated attempts and logs are insufficient for sustained autonomous R&D, and materializes typed evidence/solution lineage across generations.

Borrowed principle: improvement/history relationships should be inspectable and inheritable as explicit records.

Not borrowed: Praxist's complete generational research runtime, evaluator assumptions or benchmark claims.

### ReproAgent — persistent implementation contracts

**ReproAgent: Contract-Guided Paper-to-Code Reproduction** (arXiv:2608.24291, 25 Aug 2026) preserves implementation requirements and reference evidence across planning, generation and repair.

Borrowed principle: constraints and reference context should survive long agent trajectories rather than be reconstructed later.

Not borrowed: its paper-to-code task formulation or performance claims.

## Relation to neighboring infrastructure

- Jupyter Book / MyST / publication systems: broader executable/structured publishing; this repository focuses on artifact identity, structural evidence, diagnostics and handoff.
- RO-Crate: external packaging/interoperability target rather than something to replace.
- W3C PROV / Run Crate profiles: richer execution lineage belongs in dedicated provenance/run layers; this repository does not claim conformance it does not implement.
- Scientific agents: potential producers/consumers of artifact records and lineage records, not direct equivalents.

## Cross-repository position

```text
auto-doc-engine/artifact-record
  assertion basis + artifact coverage
        ↓
auto-doc-engine/artifact-lineage
        ↓ optional reference
epistemic-pipeline/claim-verification
epistemic-pipeline/claim-transfer
epistemic-pipeline/evidence-envelope
        ↓ optional reference
sci-render-kit/figure-claim-audit
sci-render-kit/figure-evidence
sci-render-kit/communication-transfer
```

The system-level idea is preserving research semantics across artifact, epistemic process and scientific communication layers while preventing unsupported authority from propagating with the references.

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
lineage != inherited scientific validity
supersedes != history deletion
artifact completeness != experiment completeness
package completeness != scientific validity
RO-Crate != independent reproduction
AI disclosure != AI detection
AI disclosure != authorship adjudication
human review != peer review
```

> Day 6 extends the artifact plane from identifiable records to inspectable artifact generations: lineage is explicit, but scientific authority never propagates automatically through the lineage edge.
