# D2 — Converter Configuration and Sandbox State

## Question
When do converter configuration and security semantics become part of derivative provenance?

## Objects and sources
- O3: Pandoc 3.5, released 2024-10-04.
- O4: Pandoc 3.6, released 2024-12-07.
- S4: https://pandoc.org/releases.html

## Observations
Pandoc 3.5 added environment-variable interpolation for `to` and `from` in defaults files, making external environment values capable of changing reader/writer selection when defaults files are used.

Pandoc 3.6 corrected the interaction between `--sandbox` and `--embed-resources`: the release notes state that sandbox previously did not affect embedded resources as the manual implied, allowing local paths to be embedded despite sandbox use.

## Analysis
The same source document and nominal command family can traverse materially different paths because of converter revision, defaults, environment values and security behavior.

```text
source bytes
+ defaults file
+ environment variables
+ converter revision
+ security flags
= bounded transformation context
```

The Q4 security correction is especially important: declared intent and documented option presence are weaker than revision-matched executed behavior.

## Counterevidence / limits
- No vulnerable Pandoc version was executed.
- No local file exfiltration reproduction was performed.
- A fixed release does not imply every earlier derivative was affected.

## Conclusion
`SUPPORTED_OBSERVATION`

```text
sandbox flag present
!= sandbox behavior verified for this revision/path

converter configuration
!= source-content identity
```
