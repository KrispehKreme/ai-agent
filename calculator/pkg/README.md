# README.md

## Overview
This directory contains the implementation of a simple calculator package named `calculator`. The package provides a `Calculator` class that can evaluate basic arithmetic expressions consisting of the operators `+`, `-`, `*`, and `/`.

## Files

- **`calculator.py`**
  - Implements the `Calculator` class with methods to evaluate infix expressions.
  - Defines operator functions and their precedence.

- **`render.py`**
  - Contains utility functions for formatting JSON output of calculator results.
  - `format_json_output` formats the expression and result into a pretty-printed JSON string.

- **`morelorem.txt`**
  - A placeholder text file, likely used for testing or documentation purposes.

## Usage
To use the calculator, import the `Calculator` class from `calculator.py` and call its `evaluate` method with a space-separated expression string.

```python
from calculator import Calculator

calc = Calculator()
result = calc.evaluate("3 + 5 * 2")
print(result)  # Output: 13.0
```

## Contributing
Contributions are welcome. Please ensure any additions follow the existing coding style and include appropriate tests.

## License
This project is licensed under the MIT License.
