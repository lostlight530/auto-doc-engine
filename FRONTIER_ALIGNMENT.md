# Frontier Alignment — 2026-08-25

**Repository:** `auto-doc-engine`  
**Status:** research-positioning snapshot; non-normative companion to `RESEARCH_CONTRACT.md`  
**Scope:** autonomous-science provenance, research-object packaging, reproducibility boundaries, and the role of document infrastructure in the three-repository toolchain

## 1. Why this calibration exists

Two recent 2026 publications sharpen the engineering problem this repository is meant to address.

- *Provenance grounds trust in autonomous science* (Nature Computational Science, 20 Aug 2026) argues that autonomous scientific systems need a complete, re-openable record of what was reasoned, done and measured so that the record can be audited and corrected.
- *The past, present and future of self-driving laboratories* (Nature Reviews Chemistry, 31 Jul 2026) frames the next phase of self-driving laboratories around **scalability, generalizability and provenance-complete experimentation**.

These publications are external research signals, not validation or endorsement of this repository. They strengthen a design requirement already present here: scientific artifacts need durable identity, source/context links and explicit provenance boundaries before downstream reasoning can be meaningfully audited.

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
- portable research-object packaging through the implemented RO-Crate 1.3 profile.

## 3. Provenance-complete does not mean truth-complete

The current autonomous-science literature makes provenance increasingly central, but this repository keeps a stronger boundary:

```text
provenance != truth
metadata != evidence credibility
hash identity != semantic equivalence
package completeness != experiment completeness
RO-Crate != independent reproduction
```

A complete artifact record can make a wrong result easier to inspect and correct. It cannot make that result correct merely by being complete.

This distinction is important because provenance can otherwise become a new form of false certainty.

## 4. Relation to neighboring infrastructure

### RO-Crate

RO-Crate 1.3 is an interoperability standard for packaging research objects and their contextual metadata. `auto-doc-engine` uses it as an external packaging target rather than inventing a competing research-object format.

The repository adds value one level earlier: typed document handling, structural change evidence, diagnostics and controlled artifact preparation before optional crate emission.

### Jupyter Book / MyST and publication systems

Executable/publication systems are strong at computational narratives, authoring and dissemination. This repository does not attempt to replace them. Its narrower concern is artifact identity, structural evidence and portable handoff semantics.

### W3C PROV and downstream provenance systems

This repository records artifact-oriented provenance references but does not attempt to become a full provenance reasoning engine. Rich run-level lineage belongs downstream, currently in `epistemic-pipeline`.

## 5. Cross-repository interpretation

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
- What is known about replay/reproducibility status?
- Which fields are merely metadata rather than scientific evidence?

No direct imports or runtime coupling are required to preserve this contract.

## 6. Research-engineering thesis

The repository's current thesis can be stated narrowly:

> Autonomous research becomes easier to audit when research material is represented as identifiable, inspectable and provenance-aware artifacts rather than opaque document blobs.

This is an engineering thesis, not a claim that document infrastructure alone creates trustworthy science.

## 7. What should not be added merely because the frontier is moving this way

This calibration does **not** justify adding:

- an LLM or model dependency to the canonical path;
- autonomous scientific judgment;
- source-credibility scoring presented as truth;
- GitHub-native CI/merge governance as scientific architecture;
- a custom replacement for RO-Crate;
- claims of end-to-end autonomous-science compliance.

The repository should remain a bounded, deterministic artifact plane that other research systems can use.

## 8. Primary external references

Checked 2026-08-25:

1. MacKnight R, Novitskiy IM, Radadiya R, et al. **Provenance grounds trust in autonomous science.** Nature Computational Science 6, 804–807 (2026). DOI: https://doi.org/10.1038/s43588-026-01035-4
2. Canty RB, Abolhasani M. **The past, present and future of self-driving laboratories.** Nature Reviews Chemistry 10, 523–537 (2026). DOI: https://doi.org/10.1038/s41570-026-00847-2
3. RO-Crate 1.3 specification: https://www.researchobject.org/ro-crate/specification/1.3/
4. W3C PROV overview: https://www.w3.org/TR/prov-overview/

## 9. Bottom line

`auto-doc-engine` is not competing to be a scientific agent. It supplies a missing lower layer: **research artifacts that can carry identity, structure, provenance context and reproducibility boundaries into agentic or human scientific workflows.**
