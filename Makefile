lint:
	. .venv/bin/activate && \
	pylint script.module.simple-requests/libs/simple_requests.py

PHONY: lint

test:
	. .venv/bin/activate && \
	python3 tests/tests.py

PHONY: test
