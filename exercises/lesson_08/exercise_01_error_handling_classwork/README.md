# Exercise 01 — Error Handling (Classwork)

*Week 4, Day 2*

Write your answers as Python code by filling in the functions in `exercise.py`. Test each one by running the tests.

## 1. Catch a ZeroDivisionError

Write a function called `safe_divide` that takes `a` and `b`.

Return `a` divided by `b`. Wrap the division in a `try`/`except` block that catches `ZeroDivisionError` and returns the string `"Cannot divide by zero"` instead of crashing.

```
safe_divide(10, 2)   # returns: 5.0
safe_divide(10, 0)   # returns: "Cannot divide by zero"
```

## 2. Validate a Number Input

Write a function called `to_int` that takes `text`.

Try to convert `text` to an integer using `int()` and return it. If a `ValueError` occurs (because `text` is not a valid number), catch it and return `None` instead.

```
to_int("42")      # returns: 42
to_int("banana")  # returns: None
```

## 3. Try / Except / Else / Finally

Write a function called `get_favorite` that takes `data` (a dictionary) and `key`.

In a `try` block, look up `data[key]`. If it raises a `KeyError`, append `"Key not found: <key>"` to a log list. If the lookup succeeds, use an `else` block to append `"Found it!"` and the value (as a string) to the log. Regardless of what happens, use a `finally` block to append `"Lookup attempt complete."` to the log. Return the log list.

```
get_favorite({"color": "blue"}, "color")
# returns: ["Found it!", "blue", "Lookup attempt complete."]
```
