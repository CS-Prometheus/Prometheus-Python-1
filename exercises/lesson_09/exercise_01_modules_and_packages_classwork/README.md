# Exercise 01 — Modules and Packages (Classwork)

*Week 5, Day 1*

Write your answers as Python code by filling in the functions in `exercise.py`. Test each one by running the tests.

## 1. Use the `math` Module

Write a function called `circle_area` that takes `radius`. Import the `math` module and return `math.pi` multiplied by `radius` squared.

```
circle_area(4)  # returns: 50.26548245743669
```

Write a function called `sqrt_of` that takes `value` and returns `math.sqrt(value)`.

```
sqrt_of(144)  # returns: 12.0
```

## 2. Reproducible Random Numbers

Write a function called `dice_rolls` that takes `seed` and `n`. Call `random.seed(seed)` so results are repeatable. Then use `random.randint(1, 6)` to simulate rolling a six sided die `n` times, returning the results as a list. Because you seeded with the same number, calling this again with the same `seed` and `n` should return the exact same list.

```
dice_rolls(7, 5)  # returns: [3, 2, 4, 6, 1]
```

## 3. Format a Date

Write a function called `format_date` that takes `dt` (a `datetime.datetime` object). Use `strftime()` to return it formatted as `"Month Day, Year"` (for example `"July 08, 2026"`) using the format string `"%B %d, %Y"`.

```
format_date(datetime.datetime(2026, 7, 8))  # returns: "July 08, 2026"
```
