# Contributing

Thanks for your interest in contributing to `labo-audio-testkit`.

## Development setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .[dev]
```

## Local checks

```bash
ruff format .
ruff check .
mypy src tests
pytest
```

## Pull requests

1. Create a focused branch.
2. Add or update tests for behavior changes.
3. Keep CI green.
4. Open a PR with context, approach, and validation notes.
