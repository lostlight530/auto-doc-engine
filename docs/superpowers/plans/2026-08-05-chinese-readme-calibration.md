# Auto Doc Engine Chinese README Calibration Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace the Chinese README's unsupported capability claims with an accurate map of the current cloud implementation.

**Architecture:** Treat current `main` and executable tests as authority. Mirror the English capability-state distinction in Chinese while explicitly separating the unmerged local V2 reference pack from cloud features.

**Tech Stack:** Markdown, Python, unittest, optional Jinja2/Mistune/PyYAML/Pandoc.

## Global Constraints

- Modify only `README_zh.md` and a focused repository test in this urgent pass.
- Do not claim local `D:\Agent-farm\work\mit3-analysis` files are cloud implementation.
- Do not change the root English README, runtime code, templates, or examples.
- Implement on `codex/scientific-closure-20260805`.

---

### Task 1: README truth-contract test

**Files:**
- Create: `tests/test_readme_contract.py`

**Interfaces:**
- Produces: a repository-level narrative and link validator

- [ ] **Step 1: Write the failing test**

Require `已实现`, `可选`, `实验性`, and `当前未集成`; require paths `core/renderer.py`, `core/ast_engine.py`, `core/incremental.py`, and `core/sync.py`. Reject `彻底解决`, `精准无损`, `不可篡改`, `一键分发`, and a tracked `incremental/` directory claim.

- [ ] **Step 2: Run the test**

Run: `python -m unittest tests.test_readme_contract -v`  
Expected: FAIL on the current Chinese README.

- [ ] **Step 3: Commit the failing test**

Commit message: `test: define Chinese README evidence boundary`.

### Task 2: Rewrite `README_zh.md`

**Files:**
- Modify: `README_zh.md`

- [ ] **Step 1: Write the calibrated structure**

Include overview, capability matrix, dependency/failure table, verified quick start, current repository map, limitations, documentation links, and MIT license. State that API/SQLite adapters, complete multi-format conversion, experimental modules, and the local V2 pack are not all part of one verified cloud pipeline.

- [ ] **Step 2: Run README and existing tests**

Run: `python -m unittest tests.test_readme_contract -v`  
Run with declared optional dependencies: `python tests/test_all.py && python tests/test_incremental.py`  
Expected: all pass; unavailable environment tools are reported explicitly rather than counted as success.

- [ ] **Step 3: Commit**

Commit message: `docs: calibrate Chinese capability narrative`.

### Task 3: Cloud PR verification

- [ ] **Step 1: Open one PR from the existing scientific-closure branch**
- [ ] **Step 2: Record the exact tests run and distinguish local reference inputs from cloud files**
- [ ] **Step 3: Merge only after checks exist and pass; otherwise leave the PR open with the failing evidence**
