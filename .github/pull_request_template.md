## Outcome and exact scope
What changed, why, and what remains intentionally unchanged?

## Repository basis
- Base revision / current `main` observed:
- Owning implementation / maintenance surface:
- Logical period or evidence window, when applicable:
- Producer / maintainer:
- Run identity, when available:
- Machine contracts / current documents affected:

## Live ownership
- [ ] Open PRs / live branches were checked for overlapping ownership before writing
- [ ] Overlap is coordinated rather than duplicated
- [ ] This PR is not activity-only churn for a `NO_CHANGE_REQUIRED` inspection

## Evidence boundary
- [ ] Current implementation behavior is distinguished from documentation or metadata description
- [ ] Structural validation is not presented as scientific validation
- [ ] Current state is distinguished from dated maintenance/history
- [ ] Unknown, missing, or unverified semantics remain explicit

## Synchronization
List every `MANIFEST.yaml`, contract, status document, maintenance configuration, operator guide, metadata surface, or example that must remain consistent with the owning change.

## Verification actually performed
List commands/checks actually run and the revision/result observed.

## Verification not performed
List relevant checks not run as `NOT_EXECUTED`; use `EXECUTION_NOT_OBSERVED` when execution itself was not observed. Contract/source inspection is not a PASS.

## Aggregate diff and delivery
- [ ] Final `main...branch` diff was reviewed
- [ ] Current `main` / overlap state was refreshed before delivery
- [ ] Delivery is a bounded Draft PR for maintainer review
- [ ] No auto-merge, force-push, or direct maintenance write to `main` is requested

## Historical preservation
- [ ] Dated maintenance records and historical snapshots remain point-in-time evidence
- [ ] Corrections move forward through reconciliation rather than silently rewriting historical execution

## Security and privacy
State relevant parser, converter, external-tool, data, or disclosure impact. Do not publish credentials, private Jules prompts, hidden reasoning, repository memory, or unrelated operator context. Follow `SECURITY.md` for sensitive details.

## Rollback
Describe the smallest safe rollback.

## Final review
- [ ] Change is focused and reviewable
- [ ] No unrelated architecture or cadence redesign is bundled into this PR
- [ ] Draft PR status is not being presented as validation or merge success
