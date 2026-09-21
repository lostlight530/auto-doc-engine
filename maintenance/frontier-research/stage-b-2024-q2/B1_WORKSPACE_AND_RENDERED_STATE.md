# Frontier Research Part B1 — Workspace and Rendered-State Boundaries

## Identity

- **Stage:** `B / 2024-Q2`
- **Window:** `2024-04-01 through 2024-06-30`
- **Reconstructed:** `2026-09-22`
- **Coverage:** `SEARCH_BOUNDED`
- **Status:** `COMPLETE`

## Research question

How did Q2 computational-notebook environments expose a difference between workspace state, document state, and what is currently rendered or searchable on screen?

## Objects and sources

- O1 JupyterLab 4.2 release line
- O2 Jupyter Notebook 7.2
- S1 JupyterLab 4.2 changelog: https://jupyterlab.readthedocs.io/en/4.2.x/getting_started/changelog.html
- S2 JupyterLab 4.2.0 PyPI release, 2024-05-06: https://pypi.org/project/jupyterlab/4.2.0/
- S3 Notebook 7.2.0 PyPI release, 2024-05-16: https://pypi.org/project/notebook/7.2.0/
- S4 JupyterLab 4.2.0b0 PyPI release, 2024-04-02: https://pypi.org/project/jupyterlab/4.2.0b0/

All Jupyter sources are one project family

## Observations

JupyterLab 4.2 introduced a Workspaces UI capable of switching, cloning, renaming, resetting, deleting, exporting and importing workspaces

It also integrated recently opened/closed file navigation and made full notebook windowing the default

The changelog explicitly warns that full windowing renders only visible cells and that browser search can therefore produce false negatives, recommending JupyterLab search instead

A Dark High Contrast theme was also added with an intended WCAG AAA color-contrast target, but that statement is not a universal accessibility certification

Notebook 7.2 was released in the same period and is based on JupyterLab 4.2

## Analysis

Q2 makes three states visibly non-collapsible:

```text
workspace state
!= notebook/document state
!= currently rendered viewport state
```

Exporting a workspace improves recoverability of interface/session organization, but does not by itself capture kernel environment, package versions, external files, hidden services, or execution history sufficient for reproduction

Likewise, a browser failing to find text in a windowed notebook is not evidence that the underlying notebook lacks that content

## Counterevidence and limits

- no Jupyter runtime was executed in this Stage
- no exported workspace was round-tripped
- no claim that Notebook 7.2 preserves every JupyterLab 4.2 behavior
- UI recoverability is not computational reproducibility

## Repository relation

`PARALLEL_CONVERGENCE`

The useful repository lesson is that presentation/materialization state must remain distinct from underlying artifact state

No current defect is established

## Conclusion

`SUPPORTED_OBSERVATION / CANDIDATE_REPOSITORY_RELEVANCE`

Q2 notebook tooling provides direct evidence that a research artifact may have valid underlying state that is not fully materialized in the active presentation surface

```text
not rendered now
!= absent from artifact
workspace recoverable
!= experiment reproducible
```
