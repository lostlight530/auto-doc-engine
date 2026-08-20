# Contributing to auto-doc-engine

## Getting Started

1. Clone the repository.
2. Create an isolated environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # or .venv\Scripts\activate on Windows
   pip install jinja2 "mistune>=3.2.1" pyyaml
   ```
3. Run tests to verify baseline:
   ```bash
   make test
   ```

## Development Principles

- **AST-first**: Never manipulate document text with RegEx. Use `ASTEngine` methods to traverse and mutate `ASTNode` objects.
- **No `shell=True`**: All subprocess calls in `core/sync.py` must use argument lists.
- **Incremental by design**: Changes should preserve the `DiffTracker`'s structural path uniqueness.
- **Honest status**: New features must be accurately labeled as Implemented / Optional / Experimental / Not Integrated in README and MANIFEST.
- **Bilingual docs**: `README.md`/`README_zh.md` and `ARCHITECTURE.md`/`ARCHITECTURE_zh.md` are updated in pairs.
- **Executable docs**: ` ```python ` blocks in the README and ARCHITECTURE files are executed by `tests/test_doc_examples.py`; keep them runnable or mark them `# doc-example: skip`.
- **Dependency policy**: Runtime dependencies are limited to `jinja2`, `mistune` (>= 3.2.1 recommended), and `pyyaml`; format conversion uses external commands (pandoc, xelatex). New dependencies require justification and must be recorded in README and MANIFEST.

See [AGENTS.md](AGENTS.md) for the full module map, test suite layout, and hard rules.

## Pull Request Checklist

- [ ] All tests pass (`make test`)
- [ ] README contract test passes (`make test-contract`)
- [ ] No new dependencies without justification
- [ ] New modules are marked with `[EXPERIMENTAL]` if not integrated into main chain
- [ ] Documentation updated if behavior changes

## License

By contributing, you agree that your contributions are licensed under the MIT License.
