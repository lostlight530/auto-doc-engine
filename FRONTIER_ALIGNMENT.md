# Frontier Alignment — 2026-08-25 / 2026-08-26 delta

**Repository:** `auto-doc-engine`  
**Status:** research-positioning snapshot; non-normative companion to `RESEARCH_CONTRACT.md`  
**Scope:** autonomous-science provenance, research-object packaging, reproducibility boundaries, process disclosure, and the role of document infrastructure in the three-repository toolchain

## 1. Why this calibration exists

Recent 2026 publications sharpen the engineering problem this repository is meant to address.

- *Provenance grounds trust in autonomous science* (Nature Computational Science, 20 Aug 2026) argues that autonomous scientific systems need a complete, re-openable record of what was reasoned, done and measured so that the record can be audited and corrected.
- *The past, present and future of self-driving laboratories* (Nature Reviews Chemistry, 31 Jul 2026) frames the next phase of self-driving laboratories around **scalability, generalizability and provenance-complete experimentation**.
- *Responsible and transparent use of AI in scientific publishing* (Nature Computational Science, 20 Aug 2026) emphasizes transparency, accountability, and human oversight as AI becomes embedded across research and communication.
- *Artifact-centered Claim-aware Observability for Autonomous Scientific Agents* (arXiv:2608.18312, 18 Aug 2026) argues that model-call logs alone are insufficient: scientific systems also need inspectable relations among artifacts, claims, evidence, runs, and verification records.
- *EarthVerse* (arXiv:2608.23525, 24 Aug 2026) evaluates scientific agents on package-scoped investigations that require heterogeneous evidence selection, transparent calculations, source reconciliation, provenance preservation, and end-to-end consistency.

These publications are external research signals, not validation or endorsement of this repository. They strengthen a design requirement already present here: scientific artifacts need durable identity, source/context links, explicit process disclosure, and provenance boundaries before downstream reasoning can be meaningfully audited.

## 2. Repository role in that frontier

`auto-doc-engine` occupies the **research-artifact and evidence-packaging plane**:

```text
source material
    -> structured binding
    -> typed document structure
    -> structural-change evidence
    -> metadata / reference diagnostics
    -> rendered artifact
    -> optional RO-Crate 1.3 packaging
```

Its job is not to make an autonomous scientist. Its job is to keep research material inspectable enough that an autonomous or human research process does not have to treat documents as opaque blobs.

The engineering value is therefore:

- stable artifact identity;
- source and document metadata preservation;
- structural-change evidence rather than silent overwrite;
- local reference-graph diagnostics;
- explicit conversion/runtime boundaries;
- portable research-object packaging through the implemented RO-Crate 1.3 profile;
- bounded process-disclosure metadata for AI assistance and declared human review.

## 3. Provenance-complete does not mean truth-complete

The current autonomous-science literature makes provenance increasingly central, but this repository keeps a stronger boundary:

```text
provenance != truth
metadata != evidence credibility
hash identity != semantic equivalence
package completeness != experiment completeness
RO-Crate != independent reproduction
AI disclosure != authorship adjudication
human review != peer review
```

A complete artifact record can make a wrong result easier to inspect and correct. It cannot make that result correct merely by being complete.

This distinction is important because provenance and disclosure can otherwise become new forms of false certainty.

## 4. Relation to neighboring infrastructure

### RO-Crate

RO-Crate 1.3 is an interoperability standard for packaging research objects and their contextual metadata. `auto-doc-engine` uses it as an external packaging target rather than inventing a competing research-object format.

The repository adds value one level earlier: typed document handling, structural change evidence, diagnostics and controlled artifact preparation before optional crate emission.

### Jupyter Book / MyST and publication systems

Executable/publication systems are strong at computational narratives, authoring and dissemination. This repository does not attempt to replace them. Its narrower concern is artifact identity, structural evidence and portable handoff semantics.

### W3C PROV and downstream provenance systems

This repository records artifact-oriented provenance references but does not attempt to become a full provenance reasoning engine. Rich run-level lineage belongs downstream, currently in `epistemic-pipeline`.

### Agent telemetry / observability

OpenTelemetry-style execution telemetry can explain when operations happened, but scientific auditability also needs to know **which artifact and which declared process context** moved between research stages. The new process-disclosure frontmatter fields are therefore an artifact-level complement to, not a replacement for, execution tracing.

## 5. 2026-08-26 engineering delta

Today the repository adds a deliberately small disclosure vocabulary to the existing frontmatter layer:

```yaml
ai_assistance: used
ai_tools:
  - provider/model or tool identifier declared by the author
human_review: reviewed
disclosure_ref: PROCESS_DISCLOSURE.md
```

The validator checks enum/type correctness and reports inconsistent combinations as warnings. The fields remain optional and are extracted through the existing research-metadata path.

This is intentionally **not** a publisher-policy engine. It gives downstream tooling a machine-readable answer to a narrower question:

> What does this artifact itself declare about AI assistance and human review?

Detailed semantics live in `PROCESS_DISCLOSURE.md`.

## 6. Cross-repository interpretation

The three repositories now form a deliberately loose chain:

```text
auto-doc-engine
Research Artifact / Evidence Packaging
        |
        v
epistemic-pipeline
Evidence-aware Research Execution / Synthesis
        |
        v
sci-render-kit
Evidence-aware Scientific Communication
```

For this repository, that means the handoff should preserve enough context for downstream systems to answer:

- Which artifact is this?
- Which sources or prior artifacts does it reference?
- What exact bytes/representation were packaged?
- Which diagnostics or transformations were applied?
- What does the artifact declare about AI assistance and human review?
- What is known about replay/reproducibility status?
- Which fields are merely metadata rather than scientific evidence?

No direct imports or runtime coupling are required to preserve this contract.

## 7. Research-engineering thesis

The repository's current thesis can be stated narrowly:

> Autonomous research becomes easier to audit when research material is represented as identifiable, inspectable, provenance-aware, and process-disclosed artifacts rather than opaque document blobs.

This is an engineering thesis, not a claim that document infrastructure alone creates trustworthy science.

## 8. What should not be added merely because the frontier is moving this way

This calibration does **not** justify adding:

- an LLM or model dependency to the canonical path;
- autonomous scientific judgment;
- source-credibility scoring presented as truth;
- authorship decisions inferred from AI disclosure fields;
- GitHub-native CI/merge governance as scientific architecture;
- a custom replacement for RO-Crate;
- claims of end-to-end autonomous-science or publisher compliance.

The repository should remain a bounded, deterministic artifact plane that other research systems can use.

## 9. Primary external references

Checked through 2026-08-26:

1. MacKnight R, Novitskiy IM, Radadiya R, et al. **Provenance grounds trust in autonomous science.** Nature Computational Science 6, 804–807 (2026). https://doi.org/10.1038/s43588-026-01035-4
2. Nature Computational Science. **Responsible and transparent use of AI in scientific publishing.** 20 Aug 2026. https://doi.org/10.1038/s43588-026-01043-4
3. Canty RB, Abolhasani M. **The past, present and future of self-driving laboratories.** Nature Reviews Chemistry 10, 523–537 (2026). https://doi.org/10.1038/s41570-026-00847-2
4. Yin X, Du M, Prince MH, Cherukara MJ. **Artifact-centered Claim-aware Observability for Autonomous Scientific Agents.** arXiv:2608.18312 (2026). https://arxiv.org/abs/2608.18312
5. Cui Z, et al. **EarthVerse: Benchmarking Scientific Agents Across Dynamic Earth Systems and Natural Hazards.** arXiv:2608.23525 (2026). https://arxiv.org/abs/2608.23525
6. RO-Crate 1.3 specification: https://www.researchobject.org/ro-crate/specification/1.3/
7. W3C PROV overview: https://www.w3.org/TR/prov-overview/

## 10. Bottom line

`auto-doc-engine` is not competing to be a scientific agent. It supplies a missing lower layer: **research artifacts that can carry identity, structure, process disclosure, provenance context and reproducibility boundaries into agentic or human scientific workflows.**
