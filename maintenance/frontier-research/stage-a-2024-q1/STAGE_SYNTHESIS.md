# Frontier Research Stage Synthesis — Stage A / 2024-Q1

## 0. Stage identity

- **Repository:** `lostlight530/auto-doc-engine`
- **Specification version:** `2026-09-19-first-batch`
- **Stage:** `A / 2024-Q1`
- **Research window:** `2024-01-01 through 2024-03-31`
- **Record type:** `RETROSPECTIVE`
- **Research design(s):** `HISTORICAL_FRONTIER_RECONSTRUCTION + TARGETED_EVIDENCE_SYNTHESIS + COMPARATIVE_TECHNICAL_STUDY`
- **Coverage actually achieved:** `SEARCH_BOUNDED`
- **Synthesis date:** `2026-09-21`
- **Source cutoff:** `2026-09-21`
- **Status:** `COMPLETE`

## 1. Research questions revisited

| RQ | Outcome | Primary inputs | Remaining limitation |
|---|---|---|---|
| RQ1 — What Q1 changes expanded typed identity and relation semantics for research outputs/process objects? | ANSWERED within selected evidence | A1, January dossier, O1 DataCite 4.5 | adoption/usage quality not measured |
| RQ2 — What Q1 developments strengthened computational manuscript and multi-format workflows, and what did they not establish? | ANSWERED/PARTIAL | A2, Jan-Feb-Mar dossiers, O2/O4/O5/O6 | no runtime reproduction or semantic-equivalence test |
| RQ3 — How should releases, patches and proposals be represented without conflation? | ANSWERED | A3, March dossier, O1/O3/O5 | relation vocabulary remains repository-specific design choice |

## 2. Research inputs

| Input | Function | Coverage | Material unresolved issue |
|---|---|---|---|
| A1 Typed research-object identity | semantic metadata analysis | DataCite 4.5 | adoption and correctness of populated relations |
| A2 Computational manuscripts | scholarly-document workflow analysis | Quarto 1.4 line | exact patch-level feature state |
| A3 Release/proposal/lineage | governance-state analysis | DataCite + Quarto | cross-system relation vocabulary |
| January reconstruction | month-level historical reconstruction | DataCite, Quarto, Pandoc | no independent adoption evidence |
| February reconstruction | month-level historical reconstruction | Quarto, Pandoc | no rendered-output reproduction |
| March reconstruction | month-level historical reconstruction | Quarto, Typst, Pandoc, DataCite RFC | no accessibility certification/runtime comparison |
| Source/Object Register | identity/provenance control | 6 research objects, 16 sources | primary-source concentration |
| Evidence Chart | cross-object extraction | all selected objects | same-producer charting |

## 3. Method actually executed

The research began with a narrower three-object structure: DataCite 4.5, Quarto 1.4, and the March DataCite RFC. After the Human Maintainer clarified that depth and month completeness were more important than compact template completion, the research method expanded.

The executed method became:

1. recover the repository's first-batch frontier-research specification and identify `stage-a-2024-q1/` as the suggested first instantiated historical Stage;
2. establish a retrospective three-month window from 2024-01-01 through 2024-03-31;
3. define repository-specific questions around typed research objects, document lineage, multi-format scholarly records, provenance, validation, and forward correction;
4. search for high-authority primary sources tied to concrete Q1 releases/events;
5. use GitHub tag/release history when version chronology mattered;
6. separate research objects from reports and group same-origin evidence into source families;
7. add Pandoc and Typst after month-by-month reconstruction showed they materially strengthened the analysis of output validity, accessibility semantics, and cross-tool version dependence;
8. build month-level dossiers without turning them into activity logs;
9. chart evidence and negative space;
10. synthesize mechanisms across the quarter;
11. perform same-producer review with independence explicitly not established.

This was not a preregistered systematic review. Search breadth evolved during research. That evolution is recorded rather than silently presenting the final source set as if it had been fixed a priori.

## 4. Evidence coverage and selection

The Stage prioritizes direct primary evidence:

- DataCite official schema, release history, release explanation, and RFC;
- Quarto official documentation/changelog and Q1 GitHub tag commits;
- Pandoc official GitHub releases;
- Typst official changelog and release.

This source strategy provides strong evidence for **what a project released, documented, proposed, or corrected**. It is weaker for independent adoption, scientific impact, reproducibility outcomes, or comparative quality. Those stronger outcome claims are intentionally not made.

The research is English-language and search-bounded. It did not enumerate all scholarly-authoring projects active in Q1 2024. Selection was driven by whether an object exposed a mechanism central to this repository lens, not by popularity or source count.

## 5. Source-family and independence assessment

The Stage contains four producer families: DataCite, Quarto, Pandoc, and Typst. Within a family, multiple pages or releases are not counted as independent corroboration. Across families, however, the quarter shows meaningful **parallel convergence** around a shared set of engineering pressures:

- machine-readable identity is becoming more granular;
- research/document relations become more explicitly typed;
- scholarly outputs increasingly exist in multiple representations;
- output correctness depends on target-format semantics;
- accessibility properties are representation-specific;
- renderer/compiler version changes can alter output behavior;
- corrections and proposals require explicit temporal state.

This convergence is analytically useful because it arises in different project types: metadata infrastructure, computational manuscript tooling, document conversion, and document compilation. But convergence does not imply common ancestry, influence, or implementation reuse.

## 6. What changed during the Stage

### 6.1 January: identity and relations become more explicit

DataCite Metadata Schema 4.5, released 2024-01-22, is the clearest semantic event in January. It introduced `Instrument` and `StudyRegistration` as controlled resource types and the `IsCollectedBy` / `Collects` relation pair. It also added structured publisher identifiers.

These changes matter because they move research workflow objects from ambiguous prose or generic resource classes into more machine-actionable identities and relations. A research instrument can be named as a first-class object. A registration can be typed as such. A dataset can declare its collection relation to an instrument.

For an artifact-lineage system, this supports a richer graph. Yet the quarter immediately reveals why graph richness must not be confused with epistemic authority. A declared relation is only as reliable as the evidence and process behind the metadata. The graph can be structurally valid and scientifically false.

January also includes Pandoc 3.1.11.1, whose output fixes demonstrate the complementary problem: a pipeline can produce a file but still require structural, validation, or layout repair. Research documentation therefore has at least two distinct integrity planes:

```text
semantic/provenance plane
+ representation/output-validity plane
```

Neither subsumes the other.

### 6.2 February: multi-format conversion exposes representation-specific semantics

February's most informative evidence comes from Pandoc 3.1.12 and 3.1.12.1.

Pandoc 3.1.12 expanded the conversion graph by adding Djot input/output and continued changes across numerous readers and writers. The generalizable point is not the specific syntax. It is that one source representation can be transformed through a normalized document model into many outputs, each with different target semantics.

The 3.1.12.1 patch sharpened this point by correcting EPUB accessibility behavior, SVG handling, and PowerPoint math structures. These are examples where “same information” at the authoring layer requires different target-specific mechanisms.

Consequently:

```text
source-level intent
!= target-format encoding
!= assistive-technology interpretation
!= scientific meaning
```

A robust documentation engine cannot safely propagate one generic validation bit across formats. It needs to know what representation was produced, which rules applied to that representation, which checker ran, and what the check established.

This also gives concrete evidence for forward correction. The later patch repaired specific earlier behavior. Historical integrity requires keeping the earlier release state recoverable rather than silently treating the correction as if it had always been present.

### 6.3 March: dependency/version state becomes part of provenance

March adds Typst 0.11.0 and Pandoc 3.1.12.2/3.1.12.3.

Typst 0.11.0 introduced richer table structure and template packages. Both are important for durable research records. Tables are often evidence-bearing structures whose headings, spanning cells, and repeated headers carry semantics. Template packages make publication structure reusable and portable.

But reusable templates create a provenance dependency: a generated artifact may depend on a template package version in addition to source content and compiler version.

Pandoc 3.1.12.3 then provides a direct cross-project example: its Typst writer changed in response to Typst 0.11 behavior. This is strong evidence that downstream rendering is not a function of source alone.

A more realistic derivation identity is:

```text
artifact output
= f(
    source revision,
    transformation/writer revision,
    template/package revision,
    target compiler/renderer revision,
    configuration,
    environment
  )
```

The equation is conceptual, not a claim that all variables are always required or sufficient. Its value is to prevent a hash of the final file from being treated as a complete account of how the artifact came to exist.

March also includes DataCite's 2024-03-26 RFC, explicitly described as not yet a complete schema version. This creates a clean governance contrast with January's released 4.5 schema. Same producer, later date, different authority state.

The Stage therefore distinguishes:

```text
released normative version
maintained revision/patch
proposal for possible future change
documentation correction
```

Chronology alone cannot select the relation among these states.

## 7. What persisted

Several persistent problems remain visible across the entire quarter.

### 7.1 Artifact identity is easier than semantic identity

A file can be hashed. A version can be tagged. A DOI can identify an object. None of these mechanisms, alone, establishes that two artifacts mean the same thing.

This is especially acute in multi-format scholarly workflows. HTML, PDF, DOCX, EPUB, notebook output, and source text can share a project origin yet differ in hidden metadata, accessibility semantics, mathematical representation, layout, interactive behavior, or content loss.

### 7.2 Provenance records describe process; they do not validate truth

Typed lineage is useful because it makes derivation inspectable. The quarter provides multiple reasons to strengthen it. But the evidence equally supports maintaining a hard boundary:

```text
provenance != truth
lineage != scientific validation
```

A dataset's declared instrument relation can be wrong. A manuscript can expose its notebook but still fail to reproduce. A rendered PDF can validate structurally while miscommunicating a result.

### 7.3 Documentation is itself versioned evidence

Current web documentation may be easier to use than historical snapshots, but it is dangerous in retrospective research unless explicitly bounded. DataCite even notes that documentation can receive corrections between schema versions. Quarto's current manuscript page explains 1.4 semantics but is not a frozen January/February/March 2024 artifact.

This Stage therefore treats documentation access date as evidence metadata.

## 8. What weakened, failed, or disappeared

The Stage does not identify a failed grand direction; instead, it identifies **simple assumptions weakened by concrete counterexamples**.

### Assumption: “generated” means “valid”

Weakened by Pandoc fixes for DOCX validation, EPUB behavior, SVG, math, and writer regressions.

### Assumption: “same source” means “equivalent outputs”

Weakened by target-specific accessibility and writer behavior.

### Assumption: “latest state” can replace history

Weakened by patch/correction chronology and by the DataCite RFC's explicit non-final status.

### Assumption: “metadata relation” is factual verification

Not supported by the schema evidence; relation availability and relation correctness are distinct.

### Assumption: “template reuse” is reproducibility

Not established. Template/package identity is one dependency among several.

## 9. Evidence maturity

The selected objects occupy different evidence-maturity states:

| Object | Public artifact | Versioned implementation/spec | Documented execution/availability | Independent reproduction | Broader adoption |
|---|---|---|---|---|---|
| DataCite 4.5 | yes | yes | service rollout described | not studied here | not studied here |
| Quarto 1.4 | yes | yes | docs + tag history | not executed here | not studied here |
| DataCite RFC | yes | proposal only | feedback process described | n/a | n/a |
| Pandoc releases | yes | yes | release behavior described | not rerun here | not studied here |
| Typst 0.11 | yes | yes | release/changelog | not rerun here | not studied here |

This is not a universal maturity score. It is a guardrail against promoting “public artifact exists” into “independently reproduced and adopted.”

## 10. Counterevidence and competing interpretations

### Interpretation A — Q1 represents increasing reproducibility

There is partial support: computational manuscripts, explicit registrations, richer metadata, template packages, and accessible output mechanisms can all improve reproducibility infrastructure.

However, the Stage rejects the stronger claim. None of the selected evidence independently reproduces a scientific result. Several examples instead show that representations require target-specific validation and that tooling versions can change behavior.

A safer conclusion is: **Q1 expanded the infrastructure for inspectable and reproducible workflows, not proof of reproduction.**

### Interpretation B — More structured metadata means better evidence quality

DataCite 4.5 improves representation capability, but source quality and relation correctness remain external to the schema. Therefore structure improves what can be expressed and audited; it does not assign scientific authority.

### Interpretation C — Version progression implies supersession

Sometimes it may, but the quarter contains a direct counterexample: DataCite's March RFC is later than 4.5 but explicitly not a released schema version. A proposal edge is not the same as a supersession edge.

## 11. Negative space

The Stage intentionally preserves several non-findings:

- no independent corpus study of DataCite 4.5 usage;
- no local Quarto manuscript build;
- no local Pandoc conversion matrix;
- no local Typst compilation;
- no binary/document semantic-diff study;
- no accessibility conformance evaluation;
- no independent reproduction;
- no evidence that the selected external projects caused or influenced this repository;
- no evidence that current repository implementation is defective because external practice differs.

These are not failures of the Stage. They define the evidence boundary.

## 12. Cross-Part synthesis

The three thematic Parts and monthly dossiers converge on one core mechanism: **a research document is increasingly a graph of related artifacts and transformations rather than one terminal file.**

DataCite contributes explicit object and relation semantics. Quarto contributes a computational manuscript/workflow surface in which source computation and rendered publication coexist. Pandoc contributes explicit cross-format transformation and repeated evidence that target semantics matter. Typst contributes reusable template structure and a concrete dependency relation with Pandoc's writer.

This suggests a layered research-artifact model:

1. **Research object layer** — what intellectual/process object is this?
2. **Source/artifact layer** — what concrete source files/artifacts instantiate it?
3. **Relation layer** — what declared relations connect objects/artifacts?
4. **Transformation layer** — which tool/version/config transformed what into what?
5. **Representation layer** — which target format and target-specific semantics apply?
6. **Validation layer** — which checks were actually executed and what did each establish?
7. **Correction layer** — what later patch/proposal/correction changed interpretation forward?
8. **Scientific authority layer** — separate evidence about correctness, reproduction, or acceptance.

The first seven layers can improve documentation discipline. They still cannot synthesize the eighth automatically.

## 13. Repository-level interpretation

### Independent convergence

The external quarter converges strongly with existing repository principles:

- typed lineage;
- explicit artifact identity;
- process disclosure;
- multi-format research records;
- correction without history rewrite;
- checker execution distinguished from checker definition.

This is external convergence, not proof of influence.

### Deliberate divergence

The repository should resist any external pattern that encourages:

- treating metadata completeness as truth;
- treating common origin as semantic equivalence;
- treating release status as adoption;
- treating accessibility support as certification;
- treating a final file checksum as reproduction.

### Potential gaps / watch items

Research-only questions for future audit, not current defects:

- whether artifact records should explicitly carry template/package/compiler identities as separate provenance fields when relevant;
- whether representation-specific validation evidence is sufficiently first-class across all output families;
- whether proposal/released/corrected states need a richer caller-declared relation vocabulary.

These require separate current-state audit before implementation change.

### Non-gaps

The mere existence of DataCite 4.5, Quarto manuscripts, Pandoc target-specific fixes, or Typst templates does not establish a repository defect.

## 14. Repository-specific hard boundaries preserved

- `lineage != truth`
- `supersedes != predecessor invalid`
- `hash identity != semantic equivalence`
- `assertion basis != correctness`
- `coverage != quality`
- `research-object packaging != independent reproduction`

The quarter strengthens rather than weakens these boundaries.

## 15. Temporal reconciliation

What existed in Q1 2024:

- DataCite 4.5 release and March RFC;
- selected Quarto 1.4 revisions;
- Pandoc 3.1.11.1 and 3.1.12-family releases;
- Typst 0.11.0.

What was known then is represented through dated releases. Current documentation is used only with retrospective qualification.

What is known now includes later documentation and later versions, but those are not back-projected into the quarter. For example, current DataCite release history can confirm the 4.5 date; it does not make later schema values part of Q1. Current Quarto docs can identify 1.4 manuscript semantics; they do not prove a frozen patch-level state.

## 16. Previous-Stage delta

There is no prior instantiated comparable Stage. Classification: `NOT_COMPARABLE`.

Stage A establishes the initial longitudinal baseline rather than claiming a delta from an invented predecessor.

## 17. Current-repository assessment

- **Implementation drift confirmed:** `NO`
- **Active-contract drift confirmed:** `NO`
- **Documentation drift confirmed by this Stage:** `NO`
- **Separate audit/repair required:** `NO`
- **Research-only watch items:** template/compiler provenance granularity; representation-specific validation routing; typed proposal/correction relations.

```text
NO_CURRENT_REPOSITORY_DRIFT
NO_RUNTIME_CHANGE
NO_CONTRACT_CHANGE
```

This result is limited to what the Stage researched. It does not replace future maintenance audits.

## 18. Contribution and synthesis provenance

See `CONTRIBUTOR_STATEMENT.md`.

The producer and reviewer are the same AI agent. External search and GitHub retrieval were used. No local toolchain reproduction was executed.

## 19. Limitations

### Methodological

The search expanded during research and was not preregistered. Coverage is search-bounded, not systematic or exhaustive.

### Source access

The Stage relies heavily on producer-authored primary sources. This is appropriate for release status and feature semantics but weak for independent impact/adoption.

### Temporal

Some current documentation was used retrospectively. The Stage counters this by preserving Q1 release/tag anchors and explicitly marking mutable current docs.

### Runtime

No selected external tool was executed locally. No output equivalence or reproducibility experiments were run.

### Accessibility

Accessibility-related release changes were studied as evidence of target-specific semantics. No WCAG/EPUB/PDF/assistive-technology certification testing was performed.

### Repository mapping

External convergence does not prove current implementation sufficiency or deficiency.

## 20. Review readiness

Particular review attention should go to:

- the retrospective use of current Quarto documentation;
- the interpretation of Pandoc fixes as general evidence for representation-specific validation;
- the cross-tool inference drawn from Pandoc/Typst interaction;
- any future attempt to convert research watch items into implementation requirements.

## 21. Stage conclusion

`FRONTIER_STAGE_COMPLETE`

Stage A reconstructs Q1 2024 as a period in which research-document infrastructure became more explicit about object identity, relation semantics, computational publication, reusable structure, target-specific output behavior, and versioned correction.

The most important finding is not that research documents became “more reproducible” in a simple linear sense. The evidence supports a more precise interpretation: **the observable process graph became richer, while the need to keep representation, validation, provenance, correction, and scientific authority separate also became more obvious.**

DataCite 4.5 shows that research objects and process relations can become first-class metadata. Quarto 1.4 shows a document workflow in which computation sources and publication representations coexist. Pandoc shows repeatedly that conversion success is representation-specific and that accessibility/validity properties can require target-aware repair. Typst 0.11 and Pandoc's subsequent Typst-writer adjustment show that renderer/compiler state belongs to provenance when output behavior depends on it. DataCite's March RFC shows that later proposals must not be silently folded into earlier released state.

The Stage therefore strengthens a conservative but useful documentation principle:

```text
durable research documentation
= explicit identity
+ typed relations
+ transformation provenance
+ representation-specific evidence
+ forward correction
- unsupported truth transfer
```

No current repository defect is established by this research.

## 22. Correction/update triggers

Create a forward correction/reconciliation if later evidence shows:

- a Q1 release/tag date used here is wrong;
- a selected source was materially corrected/retracted;
- the historical Quarto 1.4 feature interpretation is shown inaccurate;
- a source-family independence assumption changes;
- runtime reproduction produces evidence that materially changes a Stage conclusion.

## 23. Carry-forward research questions

- When do research-document systems begin recording enough environment/template/compiler state for practical independent reproduction?
- How do scholarly infrastructures distinguish declared lineage from validated process provenance?
- Which representation-specific validators become standard across PDF/HTML/EPUB/DOCX/notebook workflows?
- How should proposal/correction/supersession relations be typed without inferring semantics from chronology?

## 24. Safe handoff set

Safe for cross-repository synthesis:

- typed identity improves auditability but not truth;
- multi-format output requires representation-specific validation;
- later corrections must move interpretation forward;
- renderer/compiler versions can be material provenance;
- proposal state must be distinct from released state.

Not safe to generalize:

- claims about broad adoption;
- claims of independent reproduction;
- claims that any specific external architecture should be copied into another repository.
