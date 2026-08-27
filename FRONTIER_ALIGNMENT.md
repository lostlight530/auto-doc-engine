# Frontier Alignment — auto-doc-engine

**Status:** non-normative research-positioning snapshot  
**Calibrated:** 2026-08-27

`auto-doc-engine` occupies the research-artifact / document-evidence plane. It is not a scientific agent and does not infer scientific truth.

## Current engineering thesis

A completed document or model-call trace is not automatically a durable research record. Before downstream reasoning, research material benefits from explicit identity, declared process context, diagnostics and portable handoff.

```text
source material
  -> structured binding
  -> typed document structure
  -> structural-change evidence
  -> metadata/reference diagnostics
  -> declared process context
  -> rendered derivatives
  -> optional artifact-record
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

## Why artifact identity matters

A downstream research process should not have to reconstruct identity from a filename plus prose. The artifact record can preserve concrete source/derivative hashes, declared source/process metadata, bounded validation and lineage references.

This is infrastructure for auditability, not proof of scientific correctness.

## Stable project vocabulary

```text
doctor
sarif
artifact-record
process-disclosure
frontmatter-validation
ro-crate
```

Project-owned identifiers have no decorative `@1/@2` or `/v1` suffixes. Real external standards and observed runtime versions remain provenance.

## Relation to neighboring infrastructure

- Jupyter Book / MyST / publication systems: broader executable/structured publishing; this repository focuses on artifact identity, structural evidence, diagnostics and handoff.
- RO-Crate: external packaging/interoperability target rather than something to replace.
- W3C PROV / Run Crate profiles: richer execution lineage belongs in dedicated provenance/run layers; this repository does not claim conformance it does not implement.
- Scientific agents: potential producers/consumers of artifact records, not direct equivalents.

## Cross-repository position

```text
auto-doc-engine/artifact-record
        ↓ optional reference
epistemic-pipeline/claim-verification
epistemic-pipeline/evidence-envelope
        ↓ optional reference
sci-render-kit/figure-claim-audit
sci-render-kit/figure-evidence
```

The system-level idea is preserving research semantics across artifact, epistemic process and scientific communication layers.

## External direction boundary

Recent autonomous-science, provenance, claim-observability and Research Object work motivates durable/re-openable artifact records and human oversight. These sources are design signals, not validation, endorsement, novelty proof or standards certification for this repository.

## Hard boundaries

```text
provenance != truth
metadata != evidence credibility
hash identity != semantic equivalence
artifact completeness != experiment completeness
package completeness != scientific validity
RO-Crate != independent reproduction
AI disclosure != authorship adjudication
human review != peer review
```

## What this frontier does not justify

- LLM dependence in the canonical document path;
- automatic scientific judgment or source-truth scoring;
- provider/model registry dependence;
- autonomous authorship decisions;
- GitHub-native CI/merge governance as scientific architecture;
- a custom replacement for RO-Crate;
- fake Run Crate conformance.

> The repository's research-engineering value is turning documents and derivatives into identifiable, inspectable, process-aware artifacts before they enter human or agentic scientific reasoning.
