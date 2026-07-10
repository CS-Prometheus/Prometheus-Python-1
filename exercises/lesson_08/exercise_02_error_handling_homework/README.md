# Exercise 02 — Error Handling (Homework)

*Week 4, Day 2*

Write your answers as Python code by filling in the functions in `exercise.py`. Test each one by running the tests.

## 1. Safe Calculator

Write a function called `calculate` that takes `a`, `b`, and `op` (one of `"+"`, `"-"`, `"*"`, `"/"`).

Use `if`/`elif` to perform the matching operation. Wrap the whole thing in error handling that catches: `ZeroDivisionError` (when `op` is `"/"` and `b` is 0) returning `"Error: division by zero"`; `TypeError` (when `a` or `b` is not a number) returning `"Error: inputs must be numbers"`; and a case where `op` is not one of the four symbols, which should raise `ValueError(f"Unknown operator: {op}")` yourself using `raise`, caught by an `except ValueError` that returns `"Error: unknown operator"`.

```
calculate(6, 3, "/")   # returns: 2.0
calculate(6, 0, "/")   # returns: "Error: division by zero"
calculate(6, "x", "+") # returns: "Error: inputs must be numbers"
calculate(6, 3, "^")   # returns: "Error: unknown operator"
```

## 2. Custom Exception: InsufficientFundsError

Define a custom exception class `InsufficientFundsError` that subclasses `Exception`.

Write a function called `withdraw` that takes `balance` and `amount`. It raises `InsufficientFundsError(f"Cannot withdraw {amount}, balance is only {balance}")` if `amount > balance`; otherwise it returns `balance` minus `amount`.

## 3. Safe File Reader

Write a function called `read_safely` that takes `path`.

Try to open the file at `path` inside a `try` block and read its contents. Catch `FileNotFoundError` and use `f"Missing file: {path}"` as the result instead of crashing. Use a `finally` block that always appends `f"Finished attempt for {path}"` to a log list, regardless of success or failure. Return a tuple of `(result, log)`.

## 4. Data Validator

You are given a list of "user records" (dictionaries), some malformed, e.g.: `records = [{"name": "Sam", "age": 14}, {"name": "Lee"}, {"name": "Ana", "age": "twelve"}, {"age": 10}]`.

Write a function called `validate` that takes `record`. It looks up `record["name"]` and `record["age"]` (letting a `KeyError` happen naturally if a key is missing); checks that `age` is an `int` using `isinstance()`, and if not, raises `TypeError("age must be an int")`; and returns a success message like `"Sam: OK"` if both checks pass.

Write a function called `build_report` that takes `records` (a list). Loop over `records`, call `validate()` on each inside a `try`/`except` that catches both `KeyError` and `TypeError`, and build a report list: successes look like `"Sam: OK"`, failures look like `"Missing key: 'age'"` or `"Ana: age must be an int"`. Return the report.

## 5. Robust Grade Processor

Define a custom exception class `OutOfRangeError(Exception)` for grades outside the 0 to 100 range.

Write a function called `process` that takes `raw_grades` (a list of strings). It loops over the list and, for each entry, tries to: convert it to `float()`; if the conversion fails, catch `ValueError` and record `("invalid", entry, "not a number")`; if the conversion succeeds but the value is outside 0-100, manually raise `OutOfRangeError(f"{entry} is out of range")` and catch it, recording `("invalid", entry, "out of range")`; otherwise record `("valid", entry, float value)`. Return the list of results.

Write a function called `summarize` that takes `raw_grades`. Call `process(raw_grades)`. Collect all valid float values and compute their average inside a `try`/`except ZeroDivisionError` (using `None` as the average if there are none). Return a tuple of `(valid_count, invalid_count, average)`.
