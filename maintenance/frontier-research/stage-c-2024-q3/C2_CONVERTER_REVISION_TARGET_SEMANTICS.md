# Frontier Research Part C2 — Converter Revision and Target Semantics

## Identity

- Stage: `C / 2024-Q3`
- Coverage: `SEARCH_BOUNDED`
- Status: `COMPLETE`

## Research question

How can converter revision and target-specific behavior change a derived research artifact without changing its source content

## Objects and sources

- O2 Pandoc 3.3 release, dated 2024-07-28 in Pandoc release history and announced 2024-07-29
- O3 Pandoc 3.4 release, announced 2024-09-10
- S4 Pandoc releases: https://pandoc.org/releases.html
- S5 Pandoc 3.4 announcement: https://github.com/jgm/pandoc/discussions/10167

One Pandoc source family

## Q3 evidence

Pandoc 3.3 fixed a serious Docx nested-list regression introduced in 3.2.1 and added `--link-images` for ODT

This is direct evidence that an earlier conversion revision can generate structurally different output and that a later release can forward-correct it

Pandoc 3.4 added target-facing controls such as table/figure caption position across HTML, LaTeX/Beamer, Docx, ODT/OpenDocument and Typst, added ANSI output, and changed the default HTML-to-PDF engine to WeasyPrint

These are not merely version labels: they alter target behavior and, in the PDF case, the default execution path

## Analysis

A source document plus a generic label such as “converted with Pandoc” is under-specified for exact artifact provenance

A stronger identity can require:

```text
source artifact identity
+ converter version
+ target format
+ relevant target options
+ selected/default engine
+ execution environment
```

The Q3 chronology also reinforces:

```text
3.2.1 output
!= corrected 3.3 output

same source
+ changed default engine
can yield changed derived artifact
```

## Counterevidence and negative space

No conversion matrix was executed locally

The Stage does not claim that every document is affected by the cited changes

A bugfix does not prove all earlier outputs were wrong

A caption-position option does not prove semantic equivalence among formats

## Repository relation

This is direct external convergence with typed derivative identity and target-specific validation

It does not justify automatic runtime change

## Conclusion

`SUPPORTED_OBSERVATION / PARALLEL_CONVERGENCE`

Converter revision is part of derived-artifact provenance whenever revision/default/target semantics can change output

```text
same source
!= same derivative across converter state
```
