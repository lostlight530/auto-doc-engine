.PHONY: clean test test-contract test-all test-incremental test-cross-ref test-health test-sarif

clean:
	rm -rf __pycache__ .pytest_cache output/ incremental/
	@echo "Cleaned caches and generated artifacts"

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
