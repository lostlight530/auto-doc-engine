# August 2025 Reconstruction — Immutable Publication State

## Monthly event
On 2025-08-26 GitHub announced immutable releases in public preview.

The platform-described state protects published release assets from later addition/modification/deletion, protects the associated tag from movement/deletion, and links release assets with signed attestations. GitHub's attestation guidance separately preserves the boundary that provenance evidence is not a security guarantee.

## Historical interpretation
The August story moves artifact identity from "which release name/tag?" toward "what was published, what bytes belong to it, what provenance statement accompanies them, and may that publication surface later change in place?"

```text
release label
-> protected tag
-> asset identity
-> attestation
-> immutable publication state
```

This strengthens publication traceability without turning immutability into correctness.

## Month boundary
The feature was a public preview and was not enabled or tested in this repository. No attestation was verified locally.
