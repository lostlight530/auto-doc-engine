.PHONY: help clean test test-contract test-all test-incremental test-cross-ref test-health test-sarif

help:
	@echo "auto-doc-engine manual maintenance commands"
	@echo "  make test            optional local repository checks"
	@echo "  make clean           remove generated local artifacts"
	@echo "  python core/doctor.py <docs_dir>"
	@echo "  python core/sarif.py <docs_dir> -o output/doctor.sarif"
	@echo "  python core/ro_crate.py <root> <payload...> --name NAME --description TEXT"
	@echo "These commands are local tools, not GitHub merge gates."

clean:
	rm -rf __pycache__ .pytest_cache output/ incremental/
	@echo "Cleaned caches and generated artifacts"

# Existing checks remain available manually. Nothing in this Makefile implies
# GitHub Actions, branch protection, or a required merge policy.
test: test-contract test-all test-incremental test-cross-ref test-health test-sarif

test-contract:
	python -m unittest tests.test_readme_contract -v

test-all:
	python tests/test_all.py

test-incremental:
	python tests/test_incremental.py

test-cross-ref:
	python -m unittest tests.test_cross_ref -v

test-health:
	python -m unittest tests.test_diagnostics -v
	python -m unittest tests.test_frontmatter -v
	python -m unittest tests.test_doctor -v
	python -m unittest tests.test_readability -v
	python -m unittest tests.test_doc_examples -v

test-sarif:
	python -m unittest tests.test_sarif -v
