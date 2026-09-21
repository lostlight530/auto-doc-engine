# Frontier Research Part A3 — Release, Proposal, and Lineage Boundaries

## 0. Part identity

- **Repository:** `lostlight530/auto-doc-engine`
- **Stage:** `A / 2024-Q1`
- **Part ID:** `A3`
- **Research design:** `COMPARATIVE_TECHNICAL_STUDY + TARGETED_EVIDENCE_SYNTHESIS`
- **Window:** `2024-01-01 through 2024-03-31`
- **Reconstructed:** `2026-09-21`
- **Coverage:** `SEARCH_BOUNDED`
- **Status:** `COMPLETE`

## 1. Research question

> How should released specifications, patch/release lines, and forward proposals be represented without conflating proposal, supersession, or semantic equivalence?

## 2. Scope

Compare three state types observed in this Stage: a released versioned schema (DataCite 4.5), a maintained release line (Quarto 1.4 Q1 tags), and a future-change RFC (DataCite 2024-03-26).

## 3. Selection

Only explicit status-bearing primary sources are used.

## 4. Discovery method

Direct navigation from the DataCite 4.5 release material to the 2024-03-26 RFC, plus Quarto Q1 tag history already collected in A2.

## 5. Objects

- O1 = DataCite 4.5 released schema.
- O2 = Quarto 1.4 Q1 release line.
- O3 = DataCite 2024-03-26 metadata schema RFC event.

## 6. Sources

- S1-S3 as registered for DataCite 4.5.
- **S9:** DataCite, “Requesting Your Feedback on DataCite Metadata Schema Changes,” 2024-03-26: https://datacite.org/blog/metadata-schema-rfc-march_2024/
- S6-S8 Quarto Q1 tag commits.

## 7. Evidence extraction

| Finding | Object | Evidence | Status |
|---|---|---|---|
| F7 | O1 | S1,S2 | RELEASED |
| F8 | O3 | S9 | PROPOSED / NOT A COMPLETE SCHEMA VERSION |
| F9 | O2 | S6-S8 | VERSIONED RELEASE LINE |

## 8. Observations

### O1 — Proposal state was explicit

DataCite's 2024-03-26 RFC states that the proposed changes were not yet a complete schema version and could be distributed across future versions depending on complexity and compatibility.

### O2 — Same organization does not collapse release and proposal into one authority state

The January 4.5 release and March RFC share a producer but differ in normative status. Treating the RFC as if it modified 4.5 in place would rewrite history.

### O3 — Patch/tag progression establishes chronology, not semantic equivalence

Quarto's Q1 tags demonstrate version progression. Without a semantic diff and execution evidence, hash/tag succession alone cannot establish that outputs are identical, fully compatible, or equivalent.

## 9. Counterevidence

No selected source supports treating proposed DataCite changes as already normative in March 2024. No selected evidence supports treating all Quarto 1.4 tags as semantically identical.

## 10. Negative space

- Full semantic diffs between Quarto Q1 tags: `NOT_EXECUTED`
- Adoption of proposed DataCite RFC items in Q1: impossible by definition for unreleased proposals unless separately implemented; not asserted here.

## 11. Appraisal

Status language is explicit and high-authority. Cross-project comparison is interpretive, not a standards claim.

## 12. Analysis

This Stage exposes three different lineage edges:

```text
released_version -> later_released_version
release_line_revision -> later_revision
released_version -> proposal_for_future_change
```

These edges are not interchangeable. A documentation engine that records only “newer than” loses authority state. The minimal safe model needs version/revision identity plus status and effective date. It also needs forward correction rather than rewriting an earlier artifact to make it look as though later proposals were already part of the earlier release.

## 13. Interpretation

The strongest generalizable insight is governance-oriented: **temporal lineage needs typed state transitions**. “Supersedes” may be appropriate for some released versions, but an RFC normally has a different relation such as proposes/amends-candidate-for. The specific relation must be caller-declared or source-supported, not inferred from chronology alone.

## 14. Relation to repository

`DIRECTLY_RELEVANT` to typed lineage and historical preservation. It reinforces existing boundaries rather than exposing a defect.

## 15. Current-repository implication

- Implementation defect: **NO**
- Contract drift: **NO**
- Runtime change justified: **NO**

## 16. Deviations

`NONE`.

## 17. Contribution/provenance

No automated semantic-diff tooling was run.

## 18. Part conclusion

`SUPPORTED_OBSERVATION / NO_CURRENT_REPOSITORY_DRIFT`

Q1 2024 evidence strongly supports distinguishing released state, release-line revision, and proposal state. **Later proposal != earlier release; newer hash/tag != semantic equivalence; chronology != authority relation.**

## 19. Unresolved questions

- Which relation vocabulary best captures proposal and candidate-supersession states across heterogeneous scholarly systems?

## 20. Inputs to synthesis

Carry forward typed transition-state requirement and forward-only correction logic.
