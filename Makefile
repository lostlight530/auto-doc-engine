.PHONY: clean test test-contract test-incremental test-all

clean:
	rm -rf __pycache__ .pytest_cache output/ incremental/
	@echo "Cleaned caches and generated artifacts"

test: test-contract test-all test-incremental

test-contract:
	python -m unittest tests.test_readme_contract -v

test-all:
	python tests/test_all.py

test-incremental:
	python tests/test_incremental.py
