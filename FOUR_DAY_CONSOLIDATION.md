# Four-Day Consolidation — auto-doc-engine

**Window:** 2026-08-24 → 2026-08-27  
**Repository role:** research-artifact / document-evidence plane

## Consolidated outcome

The repository moved from document automation with diagnostics toward explicit research-artifact infrastructure:

```text
structured source
  -> typed document structure
  -> structural-change evidence
  -> document/reference diagnostics
  -> declared process context
  -> rendered derivatives
  -> optional artifact-record
  -> optional RO-Crate 1.3 packaging
```

## What became concrete

- typed Markdown AST rather than regex mutation;
- SHA-256 structural/artifact identity;
- explicit add/modify/delete/unchanged structural evidence;
- document graph and bounded frontmatter diagnostics;
- SARIF 2.1.0 + Approved Errata 01 interchange;
- explicit optional Pandoc boundaries;
- conservative RO-Crate 1.3 output;
- declared AI/tool/human-review process metadata;
- lightweight artifact-record handoff;
- R0–R3 vocabulary with R3 reserved for an actual separate rerun.

## Stable identifier cleanup

Project-owned identifiers were normalized to stable semantic names:

```text
auto-doc-engine/doctor
auto-doc-engine/sarif
auto-doc-engine/artifact-record
auto-doc-engine/process-disclosure
auto-doc-engine/frontmatter-validation
auto-doc-engine/ro-crate
autoDocFinding
```

Decorative `@1/@2` and `/v1` suffixes were removed. This intentionally does not remove real external standards/runtime versions such as RO-Crate 1.3, SARIF 2.1.0 + Approved Errata 01 or CFF 1.2.0.

## Artifact record versus RO-Crate

```text
auto-doc-engine/artifact-record
  = bounded project handoff for one source/derivative set

RO-Crate 1.3
  = external Research Object packaging
```

If both are emitted, the artifact record may be packaged as an ordinary file. The repository does not invent RO-Crate vocabulary for the custom record or claim unsupported Run Crate conformance.

## Cross-repository handoff

```text
auto-doc-engine/artifact-record
        ↓ optional reference
epistemic-pipeline/claim-verification
epistemic-pipeline/evidence-envelope
        ↓ optional reference
sci-render-kit/figure-claim-audit
sci-render-kit/figure-evidence
```

The handoff uses files/references, not hidden imports.

## Non-hallucination rule

Unknown provider/model/version/source/review state remains unknown or `not_declared`. Evidence records should never be made to look more complete by inventing metadata.

## Research-engineering boundary

External autonomous-science, provenance, claim-observability and Research Object work motivates stronger artifact identity and re-openable context. Those sources do not certify this repository or establish scientific correctness.

## Hard boundaries

```text
provenance != truth
hash identity != semantic equivalence
structural diff != conflict resolution
source reference != source credibility
process disclosure != authorship adjudication
human review != peer review
artifact record != external standard
RO-Crate packaging != reproduction
```

## Maintenance boundary

GitHub Actions, CI, CodeQL, dependency bots, branch-protection assumptions and merge gates were not added as research architecture. Local checks remain optional maintenance aids and test execution is not used as completion evidence for this consolidation.
