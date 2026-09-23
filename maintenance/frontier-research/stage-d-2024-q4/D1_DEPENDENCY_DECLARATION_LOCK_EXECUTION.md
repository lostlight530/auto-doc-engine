# D1 — Dependency Declaration, Lock State, and Execution

## Question
What changed in Q4 2024 about the identity of dependency intent, and what still cannot be inferred from that identity?

## Objects and sources
- O1: PEP 735, Dependency Groups in `pyproject.toml`, resolution 2024-10-10.
- O2: PEP 751, lockfile-format proposal; Q4 evidence is proposal/discussion state, with final resolution only in 2025.
- S1: https://peps.python.org/pep-0735/
- S2: https://packaging.python.org/en/latest/specifications/dependency-groups/
- S3: https://peps.python.org/pep-0751/

## Observations
PEP 735 standardized named dependency groups for project/tooling needs while explicitly stating that dependency groups are not locked dependency data. They may serve as input to lockfile generation, but they cannot store several properties expected of lock records, including hashes.

PEP 751 was discussed during Q4 as a proposal for a lockfile format but was not resolved until 2025. Therefore its current Final state cannot be projected backward into 2024-Q4.

## Analysis
Q4 makes a useful provenance chain explicit:

```text
dependency group / declared requirements
-> resolver input
-> lock representation
-> environment synchronization
-> command execution
-> artifact
```

Each arrow requires separate evidence. A standard declaration improves interchange of intent without proving the resolved environment or executed artifact.

## Counterevidence / limits
- No PEP 735 tool interoperability test was executed here.
- No PEP 751 implementation existed as a Q4 accepted standard by inference from its later Final page.
- No lock/environment reproduction was executed.

## Conclusion
`SUPPORTED_OBSERVATION`

```text
standardized dependency intent
!= locked resolution
!= installed environment
!= executed research workflow
```
