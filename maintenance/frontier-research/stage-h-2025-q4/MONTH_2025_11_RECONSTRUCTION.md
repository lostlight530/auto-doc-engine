# November 2025 Reconstruction — Stage H

## Selected event
SLSA v1.2 was released on 2025-11-24 with the Source Track.

## Narrative
November shifts the upstream boundary: artifact provenance is no longer only a build/release question. Source authoring, review, and source-management state become separately modelable evidence.

## Boundary
Source-management provenance is not source truth, review quality, or proof that an implementation satisfies SLSA.

## Decision
`APPEND_RELATION — SOURCE_IDENTITY_AND_CONTROL_SEPARATED`
