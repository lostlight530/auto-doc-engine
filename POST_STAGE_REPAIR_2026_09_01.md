# Post-Stage Repair — auto-doc-engine — 2026-09-01

**Status:** current repair note for the closed August research-infrastructure stage  
**Stage remains closed:** 2026-08-24 → 2026-08-31

This repair does not create a new research stage and does not rewrite the August stage-close record.

## Repairs

### Maintenance-report portability

`core/maintenance_cadence.py` no longer emits repository-local history/configuration paths as machine-specific absolute paths.

Repo-local configuration is identified by a repository-relative path plus SHA-256 of the exact configuration bytes.

### Repository-scope enforcement

Configured canonical paths, scan paths, governance paths, and history patterns are constrained to the repository root. Absolute paths, `..` traversal, and resolved paths outside the root fail closed as maintenance findings.

This makes the scanner's implementation match its stated repository-maintenance scope.

### Report-write semantics

The earlier statement that the scanner performs no repository-file writes was too broad because the CLI supports explicit `--output`.

The accurate contract is now:

```text
inspected source/config/history mutated = false
caller-requested report write = explicitly recorded
```

### Artifact-lineage self-reference

A local lineage target that resolves to the source artifact-record sidecar itself now fails explicitly rather than creating a meaningless self-loop.

## External calibration checked through 2026-09-01

Current scientific-agent work continues to reinforce two relevant engineering lessons:

- terminal success is not sufficient evidence that intermediate structures were sound;
- autonomous scientific actions increasingly require explicit interface/state/safety boundaries rather than implicit side effects.

The repository borrows only the inspectability and boundary-discipline principle. It does not claim equivalence, certification, or scientific validity from external work.

## Boundaries

```text
portable report != reproduced result
scope containment != scientific validity
config hash != config correctness
self-loop rejection != complete provenance validation
maintenance clean != correctness proof
provenance != truth
```

No GitHub Actions, CI, CodeQL, dependency bots, branch protection, or merge gates are introduced by this repair. No test execution is used as completion evidence.
