# Frontier Research Part B3 — Security, Citation and Forward-Correction Provenance

## Identity

- **Stage:** `B / 2024-Q2`
- **Coverage:** `SEARCH_BOUNDED`
- **Status:** `COMPLETE`

## Research question

What do Q2 security, bibliography, caption and template fixes imply about provenance that cannot be recovered from a final artifact hash alone?

## Evidence

Typst 0.11.1 fixed a vulnerability where an image at a known path outside the project directory could be embedded into a PDF

The same release fixed multiple bibliography/citation behaviors including et-al handling, title suppression, initials and footnote citations

Pandoc 3.2.1 improved caption association and explicitly avoids silently dropping captions that cannot be associated with an element

It also added OpenXML template customization beyond `--reference-doc`

## Analysis

These fixes expose at least four provenance dimensions:

1. **input authority boundary** — whether referenced content is permitted to enter the artifact
2. **citation transformation** — how source identity is represented
3. **structural association** — whether captions/labels remain bound to the intended object
4. **template execution context** — which structural template shaped the output

A SHA-256 of the resulting PDF/DOCX identifies bytes after the fact but cannot by itself prove that all embedded inputs were authorized, that citations were transformed correctly, or that captions retained their intended association

## Counterevidence

A security fix does not mean prior artifacts were exploited

A citation bug does not mean every document produced incorrect citations

A caption fix does not establish semantic correctness of every caption

## Repository relation

`DIRECTLY_RELEVANT` to provenance vocabulary, but `NO_CURRENT_REPOSITORY_DRIFT`

## Conclusion

`SUPPORTED_OBSERVATION`

Q2 reinforces:

```text
artifact identity
!= input authorization
!= citation correctness
!= structural association correctness
```

Forward patches create new evidence states and should not silently rewrite the meaning of earlier generated artifacts
