# Exercise 01 — Variables and Data Types (Classwork)

*Week 1, Day 2*

Write your answers as Python code by filling in the functions in
`exercise.py`. Test each one by running the tests.

## 1. Variables and `type()`

Write a function called `show_variable_types` that takes four values —
`whole`, `decimal`, `text`, `flag` — and prints each one followed by its
type on the next line, using `print()` and `type()`.

```python
show_variable_types(7, 3.14, "hello", True)
# prints:
# 7
# <class 'int'>
# 3.14
# <class 'float'>
# hello
# <class 'str'>
# True
# <class 'bool'>
```

## 2. Augmented Assignment Practice

Write a function called `augmented_assignment_demo` that takes a starting
`score` and applies these changes one at a time, printing a labeled result
after each step: add 5, subtract 3, multiply by 2, then floor divide by 4.

```python
augmented_assignment_demo(10)
# prints:
# After +5: 15
# After -3: 12
# After *2: 24
# After //4: 6
```

## 3. Your First f-strings

Write a function called `fstring_intro` that takes `name`, `age`, and
`price`. Use an f-string to print a sentence like `"My name is ___ and I
am ___ years old."`, then use an f-string with the `:.2f` format spec to
print `price` as a dollar amount rounded to two decimal places.

```python
fstring_intro("Riley", 12, 19.999)
# prints:
# My name is Riley and I am 12 years old.
# $20.00
```

---

Edit `exercise.py` and fill in each function where you see `# TODO`. Then
run the tests to check your work.
