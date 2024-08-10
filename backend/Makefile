.ONESHELL:
ENV_PREFIX=$(shell python -c "if __import__('pathlib').Path('.venv/bin/pip').exists(): print('.venv/bin/')")
USING_POETRY=$(shell grep "tool.poetry" settings.toml && echo "yes")

.PHONY: help
help:	## Show this help message
	@echo "Usage: make [target]"
	@echo ""
	@echo "Targets:"
	@echo "  install         Install dependencies"
	@echo "  run             Run the backend"
	@echo "  test            Run tests"
	@echo "  lint            Run linter"
	@echo "  format          Run formatter"
	@echo "  clean           Clean up"
	@echo "  help            Show this help message"
	@fgrep "##" Makefile | fgrep -v fgrep

.PHONY: show
show:	## Show the current environment
	@echo "Current environment:"
	@if [ "$(USING_POETRY)" = "yes" ]; then poetry env info && exit; fi
	@echo "Running using $(ENV_PREFIX)"
	@$(ENV_PREFIX)python -V
	@$(ENV_PREFIX)python -m site"

.PHONY: lint
lint:	## Run linter
	@if [ "$(USING_POETRY)" = "yes" ]; then poetry run flake8; exit; fi
	@$(ENV_PREFIX)isort src/
	@$(ENV_PREFIX)black -l 79 src/ --extend-exclude src/grpc_gen/
	@$(ENV_PREFIX)black -l 79 tests/