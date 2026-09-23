# D3 — Release Process Without Released Specification

## Question
How should a long-running release process be represented when the target specification is not actually published inside the Stage window?

## Objects and sources
- O5: RO-Crate 1.2 release issue opened 2024-09-09 and active as a release procedure/milestone.
- O6: RO-Crate 1.2.0 Recommendation, published later on 2025-06-04.
- S5: https://github.com/ResearchObject/ro-crate/issues/353
- S6: https://github.com/ResearchObject/ro-crate/releases

## Observations
The release issue established that work toward 1.2 existed before Q4. Current release history identifies the eventual 1.2 Recommendation publication as 2025-06-04.

That later publication date provides a hard temporal bound: Q4 2024 may contain release planning, issue closure work, drafts or milestone progress, but it cannot be recorded as the released 1.2 Recommendation.

## Analysis
This is negative-space evidence with a precise lifecycle meaning:

```text
release procedure active
+ milestone work
+ future publication
!= publication during Q4
```

Later evidence changes current knowledge of the lifecycle without rewriting what was true during the Stage window.

## Counterevidence / limits
- This Stage does not reconstruct every issue/commit in the 1.2 milestone.
- Later release metadata is used to bound timing, not to import 2025 normative content into Q4.

## Conclusion
`SUPPORTED_TEMPORAL_BOUNDARY`

```text
planned release
!= released specification
later recommendation
!= earlier recommendation state
```
