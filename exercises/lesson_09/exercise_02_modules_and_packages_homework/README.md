# Exercise 02 — Modules and Packages (Homework)

*Week 5, Day 2*

Write your answers as Python code by filling in the functions in `exercise.py`. Test each one by running the tests.

## 1. Dice Game Simulator

Write a function called `dice_game_sums` that takes `seed` and `n`. Call `random.seed(seed)` for repeatable results. Simulate rolling two six sided dice `n` times, storing the sum of each roll (2 to 12) in a list. Use `collections.Counter` on the list of sums to tally how often each total occurred. Return a tuple of `(sums, counter)`.

## 2. Countdown Scheduler

Write a function called `days_until` that takes `event_name`, `base_datetime`, and `days_from_now`. Add a `datetime.timedelta(days=days_from_now)` to `base_datetime` to compute the event date, and return a message like `"<event_name> is on <formatted date> (<days_from_now> days away)"` using `strftime("%A, %B %d, %Y")` to format the date.

```
days_until("Coding Quiz", datetime.datetime(2026, 7, 8), 5)
# returns: "Coding Quiz is on Monday, July 13, 2026 (5 days away)"
```

## 3. Build and Import Your Own Module

Write functions called `area_rectangle(w, h)` and `perimeter_rectangle(w, h)`.

Write a function called `parse_args_or_exit` that takes `args` (a list simulating `sys.argv[1:]`). If `args` has fewer than 2 items, print a usage message and call `sys.exit(1)`. Otherwise convert the first two items to floats and return them as a tuple `(width, height)`.

```
parse_args_or_exit(["3", "4"])  # returns: (3.0, 4.0)
parse_args_or_exit(["3"])       # raises SystemExit(1)
```

## 4. Word Tally with `defaultdict`

Write a function called `word_tally` that takes `sentences` (a list of strings). Use `collections.defaultdict(int)` to build a dictionary that counts how many times each word appears across all sentences combined (split each sentence into words first). Return the dictionary.

Write a function called `highlight_word` that takes `counts` (a dictionary like the one returned by `word_tally`) and `seed`. Call `random.seed(seed)` then use `random.choice()` on the list of unique words (the dictionary keys) and return the chosen word.

## 5. Command Line Contact Report

Write a function called `contact_report` that takes `contacts` (a list of dicts with `"name"` and `"city"` keys), `command`, and an optional `now`. If `command` is `"count"`, use `collections.Counter` to count how many contacts are in each city and return the Counter. If `command` is `"recent"`, return a list containing every contact's name (in order) followed by one final string `f"Report generated at {now}"` (use `now` if given, otherwise `datetime.datetime.now()`). For any other command, print a usage message listing the valid commands and call `sys.exit(1)`.
