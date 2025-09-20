# Refactored Python Function - Executive Document

## Overview
This repository contains the refactored version of a Python function originally written with poor variable naming and unclear structure.  
The goal was to **improve readability, maintainability, and clarity** by applying **software engineering principles**.

---

## Original Code
```python
def calc(a, b, c):
    r = a * b
    if c == 1
        r = r * 0.9
        return r
```
## Problems:

Variable names (a, b, c, r) are not descriptive.

The function name calc is vague.

Indentation and structure reduce readability.

No documentation about parameters or expected behavior.

## Improvements Made

Function name:

Changed from calc → calculate_total for clarity.

## Variable names:

a → price (unit price of the product).

b → quantity (number of units).

c → apply_discount (boolean, easy to understand).

r → total (result of the calculation).

## Code documentation:

Added a docstring explaining parameters and return value.

## Type hints:

Included Python type annotations (float, int, bool) to improve maintainability.

## Readability:

Clear indentation, spacing, and inline comment for the discount.
## Conclusion

This refactoring exercise demonstrates how meaningful names, documentation, and type annotations improve code quality.
Such practices make the system easier to understand, maintain, and extend in the future.
