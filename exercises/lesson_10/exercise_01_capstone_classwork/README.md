# Exercise 01 — Capstone Project (Classwork)

*Week 6, Day 1*

Write your answers as Python code by filling in the functions in `exercise.py`. Test each one by running the tests.

## 1. Add and List Mini Program

Write a function called `build_task_list` that takes `names` and `priorities` (two parallel lists). For each pair, build a task dict `{"name": n, "priority": p}`, then return a list of formatted strings `"<priority> priority: <name>"` for each task, in order.

```
build_task_list(["Buy groceries"], ["High"])  # returns: ["High priority: Buy groceries"]
```

## 2. JSON Save and Load

Write a function called `save_and_load_snacks` that takes `path` and `snacks` (a list of dicts like `{"name": "Pretzels", "calories": 110}`). Write `snacks` to the file at `path` using `json.dump()` with `indent=2`. Then read the file back in using `json.load()` and return a list containing just the `"name"` field of each loaded record, in order.

## 3. Predict and Debug

The original `get_price` function was supposed to look up a price in a dictionary and return `None` if the item is not found, but it had a bug: it caught `IndexError` instead of `KeyError`, so a missing item crashed the program.

Write a function called `get_price` that takes `prices` (a dict) and `item`. Return `prices[item]` if `item` is a key in `prices`. If `item` is missing, return `None` instead of crashing.

```
get_price({"apple": 1.50}, "apple")  # returns: 1.50
get_price({"apple": 1.50}, "bread")  # returns: None
```
