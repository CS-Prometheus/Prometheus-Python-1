# Exercise 01 — Loops (Classwork)

*Week 1, Day 4*

Write your answers as Python code by filling in the functions in `exercise.py`. Test each one by running the tests.

## 1. Sum of Even Numbers

Write a function called `sum_even_numbers` that takes `start` and `end`.

Use a `for` loop with `range()` to add up every even number from `start` to `end` (inclusive). Print the total using an accumulator variable.

```
sum_even_numbers(2, 20)
# prints:
# Sum of even numbers 2 to 20: 110
```

## 2. Countdown with a Break

Write a function called `countdown_with_break` that takes `limit` and `stop_at`.

Starting a counter at 1, use a `while` loop that keeps looping while the counter is less than or equal to `limit`. Inside the loop, print the counter value. The moment the counter equals `stop_at`, print `"Loop stopped early!"` and use `break` to exit the loop immediately (before printing any later numbers).

```
countdown_with_break(5, 3)
# prints:
# 1
# 2
# 3
# Loop stopped early!
```

## 3. Numbered Shopping List

Write a function called `numbered_shopping_list` that takes `items` (a list).

Use `enumerate()` to print each item with its position number starting at 1, in the format `"N) item"`.

```
numbered_shopping_list(["Milk", "Eggs", "Bread", "Apples"])
# prints:
# 1) Milk
# 2) Eggs
# 3) Bread
# 4) Apples
```
