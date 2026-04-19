# Contributing

## Setup
```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
pre-commit install
```

## Checks
```bash
ruff check .
ruff format .
mypy .
pytest
```

## PR Guidelines
- Keep changes small and focused
- Add tests for new behavior
- Update README if behavior changes
