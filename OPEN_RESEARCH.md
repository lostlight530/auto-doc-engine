# Open Research / 开放科研

Status: durable open-research production guide
Scope: repository-level research positioning, independent research-production method, scholarly-metadata boundaries, and semantic-drift governance

## Authority

This guide complements rather than replaces implementation, `MANIFEST.yaml`, architecture, research/artifact contracts, maintenance contracts, release policy, or historical evidence.

```text
current repository truth
→ implementation / MANIFEST / research contracts
→ OPEN_RESEARCH.md
→ RESEARCH_TEMPLATE.md
→ prospective research records
→ scholarly metadata / downstream indexes
```

A stricter repository-native contract wins.

## Canonical positioning

**Canonical Type:** Research-document compilation and research-object infrastructure

**One-line positioning:** Research-document compilation and research-object infrastructure for typed Markdown transformation, structural-change evidence, artifact records, lineage, process disclosure, and bounded packaging

**Primary domains:** research software; document processing; abstract syntax trees; provenance; research objects; reproducibility

**Non-goals:** generic word processor; semantic truth engine; peer-review system; AI-text detector; automatic source-credibility adjudicator

```text
External Classification != Repository Identity
Inferred Topic != Canonical Research Domain
Keyword Match != Project Purpose
Scholarly Graph Representation != Repository Self-Definition
```

## Independent research-production layer

This repository's maintenance contracts and engineering contracts are strong, but maintenance evidence is not automatically an independent research result. New research units should explicitly capture question, falsifiability, evidence identity, fixed artifact/revision/environment identity, procedure, raw observation, counterexample, bounded conclusion, research increment, and retest condition.

A successful render, package, checker, or exporter establishes only the implemented predicate actually observed.

## Repository-specific method

Record when relevant
- input document and data identity
- template or renderer identity
- typed AST and structural-diff surface
- artifact-record assertion basis and coverage
- artifact-lineage relation
- generated derivative identity
- optional RO-Crate packaging surface
- transformation/reproducibility boundary

`rendered successfully != scientifically correct`
`lineage relation != inherited validity`
`coverage != research quality`

Research records should distinguish document/source identity, transformation identity, derivative identity, assertion basis, lineage relation, audit coverage, and packaging surface.

## Evidence and execution discipline

```text
render success != scientific truth
lineage relation != inherited validity
coverage != research quality
RO-Crate package != reproduction
process metadata != authorship proof
```

Unknown or unexecuted states stay explicit.

## Open-science file responsibilities

- `README.md` — public orientation.
- `OPEN_RESEARCH.md` — durable open-research method and positioning.
- `RESEARCH_TEMPLATE.md` — prospective bounded research-record template.
- `AUTHORS`, `LICENSE`, `CITATION.cff`, `codemeta.json` — authorship, reuse, citation/software metadata.
- `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `SECURITY.md` — contribution/community/security governance.
- `RELEASE_POLICY.md` — release/archive semantics.
- `.github/ISSUE_TEMPLATE/**` and pull-request template — reviewable intake.

These surfaces support open research; they do not establish scientific validity.

## Scholarly metadata discipline

Preserve Canonical Type, One-line Positioning, Primary Domains, Non-goals, accurate structured subjects where supported, and 5–7 defining keywords before future metadata publication. Do not rewrite precise descriptions for a classifier or use keyword stuffing.

## Shadow classification

Candidate title + abstract/description may be checked against downstream topic/keyword inference.

```text
ALIGNED
PARTIALLY_ALIGNED
MISCLASSIFIED
CLASSIFIER_NOISE
```

Execution state is separately `RUN` or `NOT_RUN`. Repair owning metadata only for genuine upstream ambiguity; otherwise record downstream classifier noise.

## Semantic drift audit

Compare canonical positioning with `CITATION.cff`, CodeMeta, archive/DOI metadata, OpenAIRE, and OpenAlex.

- **CANONICAL_DRIFT**
- **TRANSPORT_DRIFT**
- **DERIVATION_DRIFT**
- **VERSION_SKEW**

`DERIVATION_DRIFT != REPOSITORY_DEFECT`.

## History and correction

```text
CURRENT_STATE != TASK_TIME_STATE
LATER_SUCCESS != EARLIER_SUCCESS
PUBLICATION_IDENTITY != CURRENT_MAIN
RESEARCH_PRODUCTION != MAINTENANCE != PERIODIC_AUDIT
```

Preserve historical Stage/maintenance records. Correct current interpretation forward through correction, reconciliation, or a new timepoint record.

## Contribution and review

Use `OPEN_RESEARCH.md` for research-method/positioning changes and `RESEARCH_TEMPLATE.md` for new research records. State artifact identities, transformations actually executed, checks actually run, evidence actually observed, and unresolved boundaries.

## Permanent boundary

```text
research record != capability claim
publication != validation
usage != adoption
citation != reproduction
metadata consistency != scientific correctness
external indexing != repository self-definition
```
