# Frontier Research Part C3 — Build Attestation and Release-State Provenance

## Identity

- Stage: `C / 2024-Q3`
- Coverage: `SEARCH_BOUNDED`
- Status: `COMPLETE`

## Research question

What can signed build provenance and release-process metadata establish about artifact origin without inheriting semantic or scientific authority

## Objects and sources

- O4 Matplotlib 3.9.1, release date 2024-07-04, announcement 2024-07-06
- O5 Matplotlib 3.9.2, 2024-08-12
- O6 RO-Crate 1.2 release-planning issue, opened 2024-09-09
- S6 Matplotlib 3.9.1 announcement: https://discourse.matplotlib.org/t/matplotlib-announce-ann-matplotlib-3-9-1/24539
- S7 Matplotlib 3.9.2 release statistics: https://matplotlib.org/3.9.2/users/github_stats.html
- S8 RO-Crate 1.2 release issue: https://github.com/ResearchObject/ro-crate/issues/353

Matplotlib and RO-Crate are independent project families

## Observations

Matplotlib 3.9.1 explicitly added GitHub artifact attestations for source distribution and wheel artifacts while also shipping many behavior bugfixes

This cleanly separates two evidence classes

- an attestation can bind a distributed artifact to an expected build/source process
- the release's behavior still depends on code and may require later bugfixes

Matplotlib 3.9.2 followed on 2024-08-12, reinforcing that a signed/attested 3.9.1 artifact remains an authentic 3.9.1 artifact even when later behavior is corrected

The RO-Crate 1.2 release issue opened on 2024-09-09 records a release procedure/milestone task

It is evidence that a release process was active

It is not evidence that RO-Crate 1.2 was already a released Recommendation in Q3 2024; the eventual 1.2 publication occurred later

## Analysis

The Stage can now distinguish:

```text
artifact bytes/hash
build attestation
release state
semantic behavior
scientific validity
```

These evidence planes can be linked, but none substitutes for the others

A signed attestation can improve origin/process verification while leaving scientific correctness completely open

A release issue can prove planning/workflow state while leaving released normative state false or unknown

## Strong counterexample

If an attested Matplotlib 3.9.1 wheel contains a behavior later fixed in 3.9.2, the attestation still serves its provenance purpose

Therefore:

```text
provenance verified
!= behavior defect absent
```

## Repository relation

The mechanism supports keeping artifact identity, process provenance, lineage and scientific validity as separate fields

No current repository change is inferred

## Conclusion

`SUPPORTED_OBSERVATION`

Q3 strengthens provenance from “which bytes” toward “which build process and release state”, while preserving:

```text
attestation != semantic equivalence
attestation != scientific validity
release workflow != released specification
```
