# 01 — Source and Explanation

This class answers three durable questions:

1. **What does auto-doc-engine actually implement?**
2. **Where is that behavior explained?**
3. **Which observations are engineering evidence rather than scientific validation?**

## Implementation map

| Surface | Repository role | Boundary |
|---|---|---|
| `core/` | document parsing, transformation, artifact/diagnostic logic, and executable library behavior | source code defines implemented predicates; prose cannot add capability |
| `templates/` | repository-owned document templates and rendering inputs | a template describes structure, not successful generation or scientific quality |
| `sync/` | declared synchronization targets and related behavior | configured target != successful external synchronization |
| `tests/` | executable regression/contract evidence for tested behavior | passing tests apply only to the tested revision/environment/cases |
| `Makefile` | supported engineering command entry points | command presence != command execution |

`core/maintenance_cadence.py` remains executable source in this class because classification follows implementation role, even though that module supports maintenance documents elsewhere.

## Architecture and explanatory documents

- root [`README.md`](../../README.md) — public repository entry point and capability overview.
- root [`README_zh.md`](../../README_zh.md) — Chinese public entry point; should remain semantically aligned with the English surface where both describe the same capability.
- [`ARCHITECTURE.md`](./ARCHITECTURE.md) — detailed current architecture, component boundaries, data/control flow, optional-tool boundaries, and cross-repository handoff context.
- [`ARCHITECTURE_zh.md`](./ARCHITECTURE_zh.md) — Chinese architecture explanation; translation alignment does not mean either document outranks implementation.

## How to establish current behavior

For a concrete capability claim, read in this order:

```text
owning implementation
→ machine-readable contract/configuration for that subject
→ revision-matched test or observed execution when claimed
→ active specialized contract
→ Architecture / README explanation
```

A historical maintenance record, an archived publication, or a successful documentation build cannot silently strengthen what the implementation supports.

## Engineering evidence boundary

Keep these identities separate:

```text
source code present
!= code executed

test defined
!= test executed

artifact generated
!= artifact scientifically valid

SHA-256 identity
!= semantic equivalence

optional external tool documented
!= tool available in a particular environment
```

When execution matters, retain the revision, environment, exact command/input, result, and untested boundary.

## Related long-lived contracts

The documents under [`../02-examples-and-contracts/`](../02-examples-and-contracts/) explain how implemented behavior is represented, constrained, transferred, and interpreted. They do not replace source ownership.

The current document taxonomy is routed from [`../README.md`](../README.md). Current maintenance routing is separate under class 03 and should not be treated as the primary description of auto-doc-engine itself.
