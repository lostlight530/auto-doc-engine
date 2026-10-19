# Frontier Research Stage J / 2026-Q2 — research brief
- Repository: `lostlight530/auto-doc-engine`; source window 2026-04-01–2026-06-30; `RETROSPECTIVE`.
- Protocol recorded 2026-10-19 **after targeted source discovery**, not preregistered during the historical months.
- Specification: `2026-09-19-first-batch`; design `HISTORICAL_FRONTIER_RECONSTRUCTION + TARGETED_EVIDENCE_SYNTHESIS`; coverage `SOURCE_BOUNDED`; status `COMPLETE`.
## Rationale and research question
**Theme:** Validation and serialization evidence. **Question:** How does validation and serialization evidence change the evidence needed to assess artifact evidence, dependency/installer provenance, converter configuration and semantic output identity without inferring local implementation?
## Eligibility and source method
On 2026-10-19, inspect the selected publishers' GitHub `GET /repos/{owner}/{repo}/releases?per_page=100&page=1` and exact `/releases/tags/{tag}` records. Select dated release/version objects inside the quarter relevant to the repository lens; one release is one object, even with many reported features. Exclude outside-window dates and undated speculation. Mark prereleases precisely, not as GA. The sample is neither exhaustive external research nor independent reproduction.
## Research Parts / unit of analysis
- J-O1 — Why does a failure-evidence artifact differ from a verification pass?; publisher [astral-sh/uv 0.11.7](https://github.com/astral-sh/uv/releases/tag/0.11.7) dated 2026-04-15
- J-O2 — Which archive/installer states must be kept for reproducibility claims?; publisher [astral-sh/uv 0.11.15](https://github.com/astral-sh/uv/releases/tag/0.11.15) dated 2026-05-18
- J-O3 — When are logical evidence object and interchange schema different identities?; publisher [CycloneDX/specification 1.7.1](https://github.com/CycloneDX/specification/releases/tag/1.7.1) dated 2026-06-02
- J-O4 — When is a defaulted converter option part of the generated document evidence?; publisher [jgm/pandoc 3.10](https://github.com/jgm/pandoc/releases/tag/3.10) dated 2026-06-04
## Charting and review plan
Version/date, object/source identity, publisher-stated behavior, analytic interpretation, alternative reading, source-family independence and missing local verification. A producer review can close a source-bounded documentary Stage if its limitations are explicit; independent scholarly review is not claimed.
Hard boundary: `lineage != truth; lock != environment; checksum != semantic equivalence; release != local conformance`.
