# Exercise 02 — Data Structures (Homework)

*Week 2, Day 1*

Write your answers as Python code by filling in the functions in `exercise.py`. Test each one by running the tests; the last one is the most involved.

## 1. Leaderboard Slice & Sort

Write a function called `leaderboard_top3` that takes `scores`, a list of dictionaries each with `'player'` and `'points'`.

Use `sorted()` with a `key=` lambda to build a new list ranked from highest points to lowest (do not modify the original). Slice that ranked list to grab the top 3. Loop through the slice with `enumerate()` and return a list of strings for each entry's rank (starting at 1), player name, and points as `'RANK. NAME - POINTS pts'`.

```
leaderboard_top3([
    {"player": "Kai", "points": 340},
    {"player": "Lena", "points": 512},
    {"player": "Omar", "points": 275},
    {"player": "Tia", "points": 460},
    {"player": "Zoe", "points": 398},
])
# returns: ['1. Lena - 512 pts', '2. Tia - 460 pts', '3. Zoe - 398 pts']
```

## 2. Club Roster Set Operations

Write a function called `club_set_operations` that takes `chess` and `robotics` (two sets of student names).

Return a dictionary with keys `'union'`, `'intersection'`, `'chess_only'`, and `'symmetric_difference'`, mapping to the corresponding set operation result.

```
club_set_operations({"Ana", "Ben", "Cleo", "Drew"}, {"Cleo", "Drew", "Eli", "Faye"})
# returns: {
#     "union": {"Ana", "Ben", "Cleo", "Drew", "Eli", "Faye"},
#     "intersection": {"Cleo", "Drew"},
#     "chess_only": {"Ana", "Ben"},
#     "symmetric_difference": {"Ana", "Ben", "Eli", "Faye"},
# }
```

## 3. Inventory Value Report

Write a function called `inventory_value_report` that takes `inventory`, a dictionary mapping item names to a `(price, quantity)` tuple.

Use a dictionary comprehension with `.items()` and tuple unpacking to build `totals`, mapping each item to its total value (`price * quantity`). Return a tuple of `(totals, grand_total)` where `grand_total` is the sum of all values in `totals`.

```
inventory_value_report({
    "Notebook": (2.50, 40),
    "Pencil": (0.75, 120),
    "Backpack": (18.00, 6),
})
# returns: ({"Notebook": 100.0, "Pencil": 90.0, "Backpack": 108.0}, 298.0)
```

## 4. Pass/Fail Checks

Write a function called `pass_fail_checks` that takes `students`, a list of dictionaries each with `'name'` and `'scores'` (a list of numbers).

Use a list comprehension to build `averages`, each student's average score rounded to 1 decimal place. Use `all()` to check whether every average is 60 or above, and `any()` to check whether any average is 90 or above. Return a tuple of `(all_passing, any_honors, averages)`.

```
pass_fail_checks([
    {"name": "Jo", "scores": [70, 65, 80]},
    {"name": "Ray", "scores": [95, 92, 98]},
    {"name": "Ana", "scores": [55, 60, 58]},
])
# returns: (False, True, [71.7, 95.0, 57.7])
```

## 5. Team Formation Analyzer

Write a function called `team_formation_analyzer` that takes `volunteers`, a list of `(name, role, years_experience)` tuples.

Using a set comprehension over the tuples, collect the unique roles. Using a dictionary comprehension (with tuple unpacking in the loop), build `by_role` mapping each role to a list of the names who hold it. Use `any()` to check whether at least one volunteer has 5+ years of experience, and `all()` to check whether every role in `by_role` has at least 2 volunteers. Return a tuple of `(has_senior, all_roles_staffed, by_role)`.

```
team_formation_analyzer([
    ("Ana", "Designer", 3),
    ("Ben", "Developer", 6),
    ("Cleo", "Developer", 2),
    ("Drew", "Designer", 1),
    ("Eli", "Tester", 4),
])
# returns: (True, False, {"Designer": ["Ana", "Drew"], "Developer": ["Ben", "Cleo"], "Tester": ["Eli"]})
```
