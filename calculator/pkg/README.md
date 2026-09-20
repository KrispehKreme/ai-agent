# Calculator Package

This package provides a simple arithmetic calculator implementation with expression evaluation and JSON output formatting utilities.

## Files

- `calculator.py` - Main calculator implementation
- `render.py` - JSON output formatting utilities
- `morelorem.txt` - Placeholder text file

## Calculator Module (`calculator.py`)

The `Calculator` class provides infix expression evaluation with support for basic arithmetic operations:

### Supported Operations

| Operator | Description |
|----------|-------------|
| `+` | Addition |
| `-` | Subtraction |
| `*` | Multiplication |
| `/` | Division |

### Usage

```python
from calculator import Calculator

calc = Calculator()
result = calc.evaluate("3 + 4 * 2")  # Returns 11.0
```

### Features

- **Operator Precedence**: Correctly handles operator precedence (`*` and `/` before `+` and `-`)
- **Infix Evaluation**: Evaluates space-separated infix expressions
- **Error Handling**: Raises `ValueError` for invalid tokens or malformed expressions

### Methods

- `evaluate(expression: str) -> float | None`: Evaluates an arithmetic expression
- `_evaluate_infix(tokens: list[str]) -> float`: Internal method for token-based evaluation
- `_apply_operator(operators: list[str], values: list[float]) -> None`: Internal method for applying operators

## Render Module (`render.py`)

The `render` module provides utilities for formatting calculator output as JSON.

### Usage

```python
from render import format_json_output

json_output = format_json_output("3 + 4", 7)
# Returns: '{"expression": "3 + 4", "result": 7}'
```

### Features

- Converts float results to integers when they are whole numbers
- Returns properly indented JSON output

## Example

```python
from calculator import Calculator
from render import format_json_output

calc = Calculator()
result = calc.evaluate("10 / 2")
json_output = format_json_output("10 / 2", result)
print(json_output)
# Output: {"expression": "10 / 2", "result": 5}
```
