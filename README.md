# Clean Code Examples

A small collection of Python snippets illustrating Clean Code principles through **before/after** comparisons — readability, the DRY principle, and automated testing.

## Contents

| File | Principle | Description |
|---|---|---|
| [`badExample.py`](badExample.py) | Readability | Cryptic naming and no documentation: a function called `calc` that computes a circle's area. |
| [`GoodExample.py`](GoodExample.py) | Readability | Same logic, rewritten with descriptive names (`calculate_circle_area`, `radius`) so the code is self-explanatory. |
| [`withoutDry.py`](withoutDry.py) | DRY | Area-calculation functions that each repeat their own `print` statement. |
| [`withDry.py`](withDry.py) | DRY | The same functions refactored to share a single `mostrar_resultado` helper, removing the duplication. |
| [`test/`](test/) | Testing | A small math library (`funcoes.py`) with a `unittest` test suite and two interactive test runners. |

## The `test/` folder

- **`funcoes.py`** — math functions: `soma`, `subtracao`, `multiplicacao`, `divisao`, `eh_par`, `fatorial`.
- **`test_funcoes.py`** — `unittest` test cases covering normal inputs and edge cases (e.g. division by zero, negative factorial).
- **`main.py`** — interactive CLI menu to run all tests or a chosen subset.
- **`test_runner.py`** — a `TestRunner` class for programmatically loading and executing test suites, with timing and a pass/fail summary.
- **`config_testes.py`** — test environment configuration (verbosity, timeout, report settings).

## Running the tests

```bash
# Run the full suite directly with unittest
python -m unittest test.test_funcoes -v

# Or use the interactive menu
python test/main.py
```

## Purpose

This repository is meant as a learning reference for:

- Writing **readable** code through clear naming and minimal/needed comments.
- Applying the **DRY (Don't Repeat Yourself)** principle to eliminate duplication.
- Structuring **unit tests** for small utility functions, including edge cases and error handling.

## Requirements

- Python 3.x (no external dependencies — the test suite uses the standard library `unittest`).
