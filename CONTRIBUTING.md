# Contributing to auto-doc-engine

## Getting Started

1. Clone the repository.
2. Create an isolated environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # or .venv\Scripts\activate on Windows
   pip install jinja2 mistune pyyaml
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

## Pull Request Checklist

- [ ] All tests pass (`make test`)
- [ ] README contract test passes (`make test-contract`)
- [ ] No new dependencies without justification
- [ ] New modules are marked with `[EXPERIMENTAL]` if not integrated into main chain
- [ ] Documentation updated if behavior changes

## License

By contributing, you agree that your contributions are licensed under the MIT License.
