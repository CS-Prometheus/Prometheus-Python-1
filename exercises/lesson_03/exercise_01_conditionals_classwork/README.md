# Exercise 01 — Conditionals (Classwork)

*Week 1, Day 3*

Write your answers as Python code by filling in the functions in
`exercise.py`. Test each one by running the tests.

## 1. Grade Classifier

Write a function called `classify_grade` that takes `score` and prints a
single letter using an if/elif/else chain: `"A"` for 90+, `"B"` for 80 to
89, `"C"` for 70 to 79, and `"F"` otherwise.

```python
classify_grade(82)
# prints: B
```

## 2. Range Check with Chained Comparisons

Write a function called `range_checks` that takes `temperature` and
`age`.

1. Using a single chained comparison (`60 <= temperature <= 80`), print
   `"Comfortable"` if it's true, otherwise print `"Not comfortable"`.
2. Using a second chained comparison, print whether `age` is a valid
   teenager age (13 to 19 inclusive): `print(13 <= age <= 19)`.

```python
range_checks(72, 15)
# prints:
# Comfortable
# True
```

## 3. Membership Checks

Write a function called `membership_checks` that takes `fruits` (a list)
and `word` (a string). Using `in` and `not in`, print whether `"banana"`
is in `fruits`, whether `"grape"` is not in `fruits`, and whether the
letter `"y"` is in `word`.

```python
membership_checks(["apple", "banana", "mango"], "python")
# prints:
# True
# True
# True
```

---

Edit `exercise.py` and fill in each function where you see `# TODO`. Then
run the tests to check your work.
