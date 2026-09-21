# Source and Research-Object Register — Stage B / 2024-Q2

## Identity

- **Repository:** `lostlight530/auto-doc-engine`
- **Stage:** `B / 2024-Q2`
- **Coverage:** `SEARCH_BOUNDED`
- **Registered:** `2026-09-22`

## Object register

| ID | Object | Type | Q2 date/state | Notes |
|---|---|---|---|---|
| O1 | JupyterLab 4.2 release line | computational workspace/notebook environment | beta 2024-04-02; stable 2024-05-06; patches through 2024-06-26 | workspace/export, partial rendering, accessibility/UI state |
| O2 | Jupyter Notebook 7.2 | notebook application release | 2024-05-16 | based on JupyterLab 4.2 generation |
| O3 | Pandoc 3.1.13 | converter release | 2024-04-07 | Typst 0.11 structure support |
| O4 | Pandoc 3.2/3.2.1 | converter release line | 2024-05-11; 2024-06-24 | file-scope, captions, templates, format semantics |
| O5 | Typst 0.11.1 | document compiler patch release | 2024-05-17 | security, citation, layout fixes |

## Source register

| ID | Source | Family | Date | Authority | Limit |
|---|---|---|---|---|---|
| S1 | https://jupyterlab.readthedocs.io/en/4.2.x/getting_started/changelog.html | Jupyter | versioned changelog | 4.2 feature semantics | current hosted docs |
| S2 | https://pypi.org/project/jupyterlab/4.2.0b0/ | Jupyter/PyPI | 2024-04-02 | public prerelease chronology | package metadata |
| S3 | https://pypi.org/project/jupyterlab/4.2.0/ | Jupyter/PyPI | 2024-05-06 | stable release chronology | package metadata |
| S4 | https://pypi.org/project/notebook/7.2.0/ | Jupyter/PyPI | 2024-05-16 | release chronology | package metadata |
| S5 | https://www.pandoc.org/releases.html | Pandoc | mutable release history | exact release notes/dates | producer source |
| S6 | https://typst.app/docs/changelog/0.11.1/ | Typst | 2024-05-17 | release semantics | producer source |
| S7 | https://pypi.org/project/jupyterlab/4.2.1/ | Jupyter/PyPI | 2024-05-23 | patch chronology | package metadata |
| S8 | https://pypi.org/project/jupyterlab/4.2.2/ | Jupyter/PyPI | 2024-06-10 | patch chronology | package metadata |
| S9 | https://pypi.org/project/jupyterlab/4.2.3/ | Jupyter/PyPI | 2024-06-26 | patch chronology | package metadata |

## Source-family map

- SF1 Jupyter: S1-S4,S7-S9
- SF2 Pandoc: S5
- SF3 Typst: S6

Multiple pages/releases inside one family are not independent corroboration

## Identity rules

```text
prerelease != stable release
workspace state != execution environment
converter version != target semantic equivalence
patch != retroactive earlier state
package metadata != scientific validation
```

## Limitations

No local notebook execution, workspace round-trip, Pandoc conversion matrix, Typst compilation, adoption study, or independent reproduction
