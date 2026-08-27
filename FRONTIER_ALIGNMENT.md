# Frontier Alignment — 2026-08-27

**Repository:** `auto-doc-engine`  
**Status:** non-normative research-positioning companion to `RESEARCH_CONTRACT.md`  
**Scope:** research artifacts, process disclosure, provenance boundaries, Research Object packaging and autonomous-science interoperability

## 1. Current frontier signal

The 2026 research-agent/autonomous-science literature is converging on a useful engineering distinction:

> **a completed output is not automatically evidence, and a model-call trace is not automatically a research record.**

Several recent signals reinforce different parts of that statement:

- *Provenance grounds trust in autonomous science* (Nature Computational Science, 20 Aug 2026): trust needs complete, re-openable records that can be audited and corrected.
- *Responsible and transparent use of AI in scientific publishing* (Nature Computational Science, 20 Aug 2026): transparency, accountability and human oversight remain essential as AI enters research and communication.
- *Artifact-centered Claim-aware Observability for Autonomous Scientific Agents* (arXiv:2608.18312, 18 Aug 2026): model-call logs are insufficient; artifacts, claims and their relations need first-class audit structure.
- *EarthVerse* (arXiv:2608.23525, 24 Aug 2026): scientific agents can perform local steps while still failing to maintain a consistent chain across evidence, scale, units, calculations and interpretation.
- *From Trajectories to Evidence* (arXiv:2608.05235): a completed research-agent trajectory is not automatically evidence; consequential artifacts and later claims need bounded qualification.

These publications are neighboring research signals, not validation or endorsement of this repository.

## 2. Repository role after the four-day consolidation

`auto-doc-engine` occupies the **research-artifact / document-evidence plane**:

```text
source material
    -> structured binding
    -> typed document structure
    -> structural-change evidence
    -> metadata/reference diagnostics
    -> declared AI/human process context
    -> rendered derivatives
    -> optional artifact-record@1
    -> optional RO-Crate 1.3 package
```

The 2026-08-27 addition is important because it separates three objects that should not be conflated:

```text
frontmatter
  what the document declares about itself

artifact-record@1
  one source/derivative set with concrete identities and bounded process/diagnostic context

RO-Crate 1.3
  broader external Research Object packaging
```

## 3. Why the artifact record matters

A downstream scientific agent should not have to reconstruct artifact identity from a filename plus prose.

`artifact-record@1` gives it a compact machine-readable answer to:

- Which source bytes are being referenced?
- Which derivatives came from this production path?
- Which sources/authors/process details were declared?
- Which bounded frontmatter diagnostics were observed?
- Which config/provenance/validation refs were supplied?
- What reproducibility level is being declared?

That is lower-level infrastructure than a scientific agent, RAG system or autonomous laboratory.

## 4. Relation to RO-Crate and Workflow Run Crate work

RO-Crate 1.3 remains the repository's external Research Object packaging target.

The RO-Crate ecosystem also maintains Process Run Crate, Workflow Run Crate and Provenance Run Crate profiles for execution provenance.

The useful lesson is architectural rather than a conformance claim:

> **research data products and execution/provenance records can be linked while retaining different scopes and vocabularies.**

`auto-doc-engine` therefore does not force its project artifact record into the RO-Crate context. When both are emitted, the artifact record is merely another packageable file.

The repository does **not** claim Workflow/Process/Provenance Run Crate conformance.

## 5. Provenance-complete is not truth-complete

The repository keeps the stronger boundary:

```text
provenance != truth
metadata != evidence credibility
hash identity != semantic equivalence
artifact record completeness != experiment completeness
package completeness != scientific validity
RO-Crate != independent reproduction
```

A complete record can make a flawed result easier to inspect and correct. It cannot make the result correct merely by being complete.

## 6. Process disclosure without overreach

The current metadata plane can declare:

```text
ai_assistance
ai_tools[]
human_review
disclosure_ref
```

This aligns with the growing demand for transparent AI use, but the repository deliberately refuses stronger interpretations:

```text
AI disclosure != authorship adjudication
AI tool label != verified model provenance
human review != peer review
process metadata != publisher compliance
```

## 7. Relation to neighboring infrastructure

### Jupyter Book / MyST / publication systems

Strong at executable or structured narratives and publishing. `auto-doc-engine` does not compete on publication breadth; it focuses on artifact identity, structural evidence, diagnostics and handoff.

### RO-Crate

External packaging/interoperability target. The repository uses it rather than inventing a replacement Research Object format.

### W3C PROV / workflow-run provenance

Richer run-level lineage belongs downstream or in dedicated provenance profiles. The document repository keeps lightweight artifact references and lets `epistemic-pipeline` own run/claim evidence semantics.

### Scientific agents

Systems such as Brain Researcher, DeepEvidence, EarthVerse-style agents or domain scientific agents are potential **consumers/producers** of artifact records, not direct equivalents of this repository.

## 8. Cross-repository frontier position

```text
auto-doc-engine
  artifact-record@1
  document/process disclosure
        |
        v
epistemic-pipeline
  claim-verification@1
  evidence-envelope@2
        |
        v
sci-render-kit
  figure-claim-audit@1
  figure-evidence@2
```

The system-level idea is preservation of research semantics across transitions between **artifact**, **epistemic process** and **scientific communication**.

## 9. Research-engineering thesis

> Autonomous or AI-assisted research becomes easier to audit when research material is represented as identifiable, inspectable, process-aware artifacts before downstream reasoning begins.

This is an engineering thesis. It does not claim that document infrastructure alone creates trustworthy science.

## 10. What this frontier does not justify adding

- an LLM dependency to the canonical document path;
- automatic scientific judgment;
- automatic source-truth scores;
- provider/model registry dependence;
- autonomous authorship decisions;
- GitHub-native CI/merge governance as scientific architecture;
- a custom replacement for RO-Crate;
- fake Workflow Run Crate conformance;
- end-to-end autonomous-science compliance claims.

## 11. Primary references

Checked through 2026-08-27:

1. MacKnight R, Novitskiy IM, Radadiya R, et al. **Provenance grounds trust in autonomous science.** Nature Computational Science 6, 804–807 (2026). https://doi.org/10.1038/s43588-026-01035-4
2. **Responsible and transparent use of AI in scientific publishing.** Nature Computational Science 6, 803 (2026). https://doi.org/10.1038/s43588-026-01043-4
3. Yin X, Du M, Prince MH, Cherukara MJ. **Artifact-centered Claim-aware Observability for Autonomous Scientific Agents.** arXiv:2608.18312. https://arxiv.org/abs/2608.18312
4. **EarthVerse.** arXiv:2608.23525. https://arxiv.org/abs/2608.23525
5. Zhuang Z, Lao C, Xu P, et al. **From Trajectories to Evidence: Auditable Experimental Records for Industrial Research Agents.** arXiv:2608.05235. https://arxiv.org/abs/2608.05235
6. RO-Crate 1.3: https://www.researchobject.org/ro-crate/specification/1.3/
7. RO-Crate profiles: https://www.researchobject.org/ro-crate/profiles.html
8. W3C PROV overview: https://www.w3.org/TR/prov-overview/

## 12. Bottom line

`auto-doc-engine` is not competing to be a scientific agent. Its Day-4 role is more precise:

> **turn research documents and derivatives into inspectable artifacts with stable identity, bounded process context, diagnostics and explicit packaging boundaries before those artifacts enter agentic or human scientific reasoning.**
