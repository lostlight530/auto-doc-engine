# Frontier Research Stage K / 2026-Q3 — research brief
- Repository: `lostlight530/auto-doc-engine`; source window 2026-07-01–2026-09-30; `RETROSPECTIVE`.
- Protocol recorded 2026-10-19 **after targeted source discovery**, not preregistered during the historical months.
- Specification: `2026-09-19-first-batch`; design `HISTORICAL_FRONTIER_RECONSTRUCTION + TARGETED_EVIDENCE_SYNTHESIS`; coverage `SOURCE_BOUNDED`; status `COMPLETE`.
## Rationale and research question
**Theme:** Packaging and conversion-semantic identity. **Question:** How does packaging and conversion-semantic identity change the evidence needed to assess artifact evidence, dependency/installer provenance, converter configuration and semantic output identity without inferring local implementation?
## Eligibility and source method
On 2026-10-19, inspect the selected publishers' GitHub `GET /repos/{owner}/{repo}/releases?per_page=100&page=1` and exact `/releases/tags/{tag}` records. Select dated release/version objects inside the quarter relevant to the repository lens; one release is one object, even with many reported features. Exclude outside-window dates and undated speculation. Mark prereleases precisely, not as GA. The sample is neither exhaustive external research nor independent reproduction.
## Research Parts / unit of analysis
- K-O1 — How does project-layout intent affect research-object identification?; publisher [astral-sh/uv 0.12.0](https://github.com/astral-sh/uv/releases/tag/0.12.0) dated 2026-07-28
- K-O2 — When is a math-rendering default a meaningful transformation change?; publisher [jgm/pandoc 3.11](https://github.com/jgm/pandoc/releases/tag/3.11) dated 2026-08-29
- K-O3 — What exactly is equivalent when a dependency lock is reused?; publisher [astral-sh/uv 0.12.20](https://github.com/astral-sh/uv/releases/tag/0.12.20) dated 2026-09-28
- K-O4 — Can a converter option change the structure of a derivative without source changes?; publisher [jgm/pandoc 3.12](https://github.com/jgm/pandoc/releases/tag/3.12) dated 2026-09-29
## Charting and review plan
Version/date, object/source identity, publisher-stated behavior, analytic interpretation, alternative reading, source-family independence and missing local verification. A producer review can close a source-bounded documentary Stage if its limitations are explicit; independent scholarly review is not claimed.
Hard boundary: `lineage != truth; lock != environment; checksum != semantic equivalence; release != local conformance`.
