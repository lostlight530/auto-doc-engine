# F2 — Pandoc 3.7 Structural Transformation Fidelity

## Evidence
Pandoc 3.7 was released 2025-05-14, followed by 3.7.0.1 on 2025-05-17 and 3.7.0.2 on 2025-05-28. The sequence includes structured JSON template variables, row/colspan handling, figure/caption representation changes, tagged-PDF fixes, LaTeX alt-text output, figure-attribute preservation and grid-table regression fixes.

Source: https://pandoc.org/releases.html

## Analysis
The Q2 converter story is not just format breadth. It shows that structural fidelity, accessibility metadata and regressions are revision-sensitive.

```text
source structure
+ converter revision/config
-> derivative structure

feature added
!= every derivative preserved correctly
later fix
!= every earlier artifact invalid
```

## Runtime boundary
No local 3.6→3.7 conversion matrix, tagged-PDF inspection, accessibility validation or semantic-equivalence test was run.

## Outcome
`SUPPORTED_OBSERVATION`
