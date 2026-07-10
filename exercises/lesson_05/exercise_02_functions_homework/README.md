# Exercise 02 — Functions (Homework)

*Week 1, Day 5*

Write your answers as Python code by filling in the functions in `exercise.py`. Test each one by running the tests; the last one is the most involved.

## 1. Build a Profile

Write a function called `build_profile` that takes required positional parameters `name` and `age`, and a keyword parameter `city` with a default of `"Unknown"`. It should return a dictionary with keys `'name'`, `'age'`, and `'city'`.

```
build_profile("Ana", 12)
# returns: {'name': 'Ana', 'age': 12, 'city': 'Unknown'}

build_profile("Ben", 13, city="Austin")
# returns: {'name': 'Ben', 'age': 13, 'city': 'Austin'}

build_profile(age=14, city="Denver", name="Cleo")
# returns: {'name': 'Cleo', 'age': 14, 'city': 'Denver'}
```

## 2. Flexible Order Total

Write a function called `order_total` that accepts any number of item prices via `*args`, a keyword parameter `tax_rate` defaulting to `0.08`, and any number of extra named fees via `**kwargs`. It should sum the prices, add tax (sum of prices times `tax_rate`), add the sum of all `kwargs` values, and return the total rounded to 2 decimal places.

```
order_total(12.00, 8.50, 4.25, delivery=2.50, tip=3.00)
# returns: 32.23
```

## 3. Global Score Tracker

A module-level variable `high_score` starts at 0. Write a function called `check_score` that takes `score` and `bonus` (defaulting to 0). It computes a local `final_score = score + bonus`, and, using the `global` keyword, updates `high_score` whenever `final_score` is higher than the current `high_score`. The function returns `final_score`.

```
check_score(50)
# returns: 50, high_score becomes 50

check_score(40, bonus=15)
# returns: 55, high_score becomes 55

check_score(60, bonus=5)
# returns: 65, high_score becomes 65
```

## 4. Top Scorers Report

Write a function called `top_scorers_report` that takes `students`, a list of dictionaries each with `'name'` and `'score'`.

Use `filter()` with a lambda to keep only students scoring 70 or above. Use `sorted()` with a `key=` lambda to sort those students from highest to lowest score. Use `map()` with a lambda to turn the sorted list into strings formatted as `'NAME: SCORE'`. Return the final list.

```
top_scorers_report([
    {"name": "Ivy", "score": 65},
    {"name": "Zane", "score": 91},
    {"name": "Cleo", "score": 78},
    {"name": "Rex", "score": 55},
    {"name": "Sam", "score": 84},
])
# returns: ['Zane: 91', 'Sam: 84', 'Cleo: 78']
```

## 5. Grade Calculator Toolkit

Build a small toolkit of functions.

First, write `average(*scores)` that accepts any number of scores via `*args` and returns their mean rounded to 1 decimal place (include a docstring).

Second, write `letter_grade(score, scale=None)` where, if `scale` is not passed, it defaults inside the function to `{90: 'A', 80: 'B', 70: 'C', 60: 'D'}`; return the letter for the highest threshold the score meets or exceeds, or `'F'` if none apply.

Third, write `class_grade_report(student_scores)` that takes a dictionary mapping each student's name to a list of their scores. For each student, call `average()` on their scores and `letter_grade()` on the result. Use `sorted()` with a lambda key to rank students from highest average to lowest, and return a list of strings formatted as `'NAME: AVERAGE (LETTER)'`.

```
class_grade_report({
    "Ava": [92, 88, 95],
    "Ben": [70, 65, 74],
    "Cleo": [81, 79, 85],
})
# returns: ['Ava: 91.7 (A)', 'Cleo: 81.7 (B)', 'Ben: 69.7 (D)']
```
