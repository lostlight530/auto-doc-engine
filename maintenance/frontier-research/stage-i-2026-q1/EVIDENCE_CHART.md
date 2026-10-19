# Frontier Research Stage I / 2026-Q1 — structured evidence chart
- Extracted 2026-10-19; no invented flow counts, effect size or universal quality score.
| Versioned object | Direct publisher observation | Research interpretation | Competing interpretation / limitation |
|---|---|---|---|
| I-O1 / 0.9.28 | uv reports CPython/OpenSSL update, Windows Pyodide support, warnings on multiple default package indexes. | The same dependency declaration can depend on runtime build and source-index policy; both belong in artifact provenance. | No installed environment, security posture or resulting document was tested. |
| I-O2 / 3.9 | Pandoc reports a WASM/browser build whose sandbox cannot fetch arbitrary HTTP resources, execute system commands or produce PDFs. | An identical converter family can have a different execution/resource envelope on the web versus native systems. | No local browser/native output comparison occurred. |
| I-O3 / 0.11.0 | uv reports system-certificate verifier changes and a rename/deprecation of native-TLS configuration, cautioning trust outcomes may differ. | A lockfile cannot alone establish whether artifact acquisition succeeded under a particular TLS trust policy. | Impact depends on configuration/platform; no certificate audit was run. |
Finding class: upstream version statement supported by one publisher-family source; downstream execution, independence and current repository drift remain `NOT_ASSESSED`.
