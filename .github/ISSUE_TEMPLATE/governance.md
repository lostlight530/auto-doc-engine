---
name: Contract or documentation reconciliation
about: Report drift between current implementation, machine contracts, maintenance control, and current documentation
title: "[Governance] "
labels: ""
assignees: ""
---

## Drifted claim or surface
Identify the exact implementation behavior, machine-readable contract, maintenance rule, or current document that is inconsistent.

## Current repository basis
- Current `main` revision:
- Owning surface/task:
- Logical period/evidence window, when applicable:
- Relevant live PR/branch ownership:

Cite current repository paths. Distinguish implementation/contract truth from dated maintenance or historical evidence.

## Proposed reconciliation
Describe the minimum semantically complete correction and every current surface that must remain synchronized.

If another live owner already covers the same surface/period, record `COORDINATE` instead of proposing a parallel repair. If inspection confirms no defect, record `NO_CHANGE_REQUIRED` rather than manufacturing an edit.

## Execution evidence
State what was actually executed, what was only inspected, and what remains `NOT_EXECUTED` or `EXECUTION_NOT_OBSERVED`.

## Historical preservation
State which dated maintenance/snapshot artifacts remain immutable point-in-time evidence and whether a forward correction/reconciliation is required.

## Public/private boundary
Do not attach private Jules prompts, hidden reasoning, repository memory, credentials, or unrelated operator context. Preserve only repository-visible evidence and the public effect of governance rules.

## Review and rollback
Define non-goals, expected Draft-PR delivery boundary if a repair is accepted, and the smallest rollback.
