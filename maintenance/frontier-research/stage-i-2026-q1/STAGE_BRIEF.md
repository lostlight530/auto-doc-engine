# Frontier Research Stage I / 2026-Q1 — research brief
- Repository: `lostlight530/auto-doc-engine`; source window 2026-01-01–2026-03-31; `RETROSPECTIVE`.
- Protocol recorded 2026-10-19 **after targeted source discovery**, not preregistered during the historical months.
- Specification: `2026-09-19-first-batch`; design `HISTORICAL_FRONTIER_RECONSTRUCTION + TARGETED_EVIDENCE_SYNTHESIS`; coverage `SOURCE_BOUNDED`; status `COMPLETE`.
## Rationale and research question
**Theme:** Portable execution and trust policy. **Question:** How does portable execution and trust policy change the evidence needed to assess artifact evidence, dependency/installer provenance, converter configuration and semantic output identity without inferring local implementation?
## Eligibility and source method
On 2026-10-19, inspect the selected publishers' GitHub `GET /repos/{owner}/{repo}/releases?per_page=100&page=1` and exact `/releases/tags/{tag}` records. Select dated release/version objects inside the quarter relevant to the repository lens; one release is one object, even with many reported features. Exclude outside-window dates and undated speculation. Mark prereleases precisely, not as GA. The sample is neither exhaustive external research nor independent reproduction.
## Research Parts / unit of analysis
- I-O1 — What runtime and index-selection evidence belongs with the declared dependency?; publisher [astral-sh/uv 0.9.28](https://github.com/astral-sh/uv/releases/tag/0.9.28) dated 2026-01-29
- I-O2 — When does converter substrate become part of derivative identity?; publisher [jgm/pandoc 3.9](https://github.com/jgm/pandoc/releases/tag/3.9) dated 2026-02-04
- I-O3 — Can dependency acquisition identity be separated from package-lock intent?; publisher [astral-sh/uv 0.11.0](https://github.com/astral-sh/uv/releases/tag/0.11.0) dated 2026-03-23
## Charting and review plan
Version/date, object/source identity, publisher-stated behavior, analytic interpretation, alternative reading, source-family independence and missing local verification. A producer review can close a source-bounded documentary Stage if its limitations are explicit; independent scholarly review is not claimed.
Hard boundary: `lineage != truth; lock != environment; checksum != semantic equivalence; release != local conformance`.
