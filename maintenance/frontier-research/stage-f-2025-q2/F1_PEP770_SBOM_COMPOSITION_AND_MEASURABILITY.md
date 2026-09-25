# F1 — PEP 770 SBOM Composition and Package Measurability

## Evidence
PEP 770 resolved Final on 2025-04-11. It reserves `.dist-info/sboms` for SBOM documents in Python distributions/installed projects. The PEP treats SBOM documents as opaque, permits multiple documents, and recommends established formats such as CycloneDX or SPDX plus creation/tool/component identity fields.

Source: https://peps.python.org/pep-0770/

## Analysis
Stage E's lock artifact described selected dependencies. PEP 770 adds a different evidence surface: packaged composition/provenance about bundled software.

```text
lock selection
!= bundled composition description
SBOM document present
!= SBOM content correct
!= installed/runtime behavior proven
```

SBOM identity, generating tool and creation time can improve reconstruction while still requiring downstream validation.

## Outcome
`SUPPORTED_OBSERVATION / NO_CURRENT_REPOSITORY_DRIFT`
