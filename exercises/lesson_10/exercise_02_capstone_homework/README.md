# Exercise 02 — Capstone Project (Homework)

*Week 6, Day 2*

These functions are pulled out of the five menu-driven programs from the homework (Contact Book, Contact Book + JSON Persistence, High Score Tracker, Library Checkout System, and the Personal Expense Tracker final project) so they can be tested directly, the same way the slides describe them. Write your answers as Python code by filling in the functions in `exercise.py`. Test each one by running the tests.

## 1. Contact Book (In Memory)

Write `add_contact(contacts, name, phone, email)`: append a new dict `{"name": name, "phone": phone, "email": email}` to `contacts` and return it.

Write `search_contact(contacts, name)`: loop through `contacts` and return the first contact dict whose `"name"` matches `name` exactly. Return `None` if no match is found.

Write `list_contacts(contacts)`: return a list of formatted strings, one per contact, in the form `"<name> | <phone> | <email>"`.

## 2. Contact Book + JSON Persistence

Write `save_contacts(path, contacts)`: write `contacts` to the file at `path` as JSON using `json.dump()` with `indent=2`.

Write `load_contacts(path)`: if a file exists at `path` (check with `os.path.exists`), load and return its contents using `json.load()`. Otherwise return an empty list.

## 3. High Score Tracker

Write `add_score(scores, name, score)`: append a new dict `{"name": name, "score": score}` to `scores` and return it.

Write `leaderboard(scores)`: use `sorted()` with a lambda key to rank scores from highest to lowest (`sorted(scores, key=lambda s: s["score"], reverse=True)`). Return a list of formatted strings `"#<rank> <name>: <score>"`, starting at rank 1 (use `enumerate(ranked, start=1)`).

## 4. Library Checkout System

Write `check_out(books, title)`: `books` is a list of dicts with `"title"`, `"author"`, and `"checked_out"` keys. Find the book with a matching title. If it exists and is not already checked out, set `checked_out` to `True` and return `f"Checked out {title}."`. If it exists but is already checked out, return `f"{title} is already checked out."`. If no book with that title exists, return `f"{title} not found."`.

Write `return_book(books, title)`: same lookup, but flips `checked_out` back to `False` if it was `True` and returns `f"Returned {title}."`; returns `f"{title} was not checked out."` if it wasn't checked out; returns `f"{title} not found."` if missing.

Write `list_available(books)`: return a list of formatted strings `"<title> by <author>"` for every book where `checked_out` is `False`.

Write `parse_menu_choice(text)`: try to convert `text` to an `int` using `int()` and return it. If a `ValueError` occurs, catch it and return `None` instead of crashing.

## 5. Final Project: Personal Expense Tracker

Write `add_expense(expenses, amount, category, date)`: append a new dict `{"amount": amount, "category": category, "date": date}` to `expenses` and return it.

Write `summary_report(expenses)`: build a dictionary accumulating total spending per category (`totals[category] = totals.get(category, 0) + amount` in a loop over `expenses`). Return `sorted(totals.items(), key=lambda pair: pair[1], reverse=True)` so the biggest spending category comes first.

Write `parse_amount(text)`: try to convert `text` to a `float` using `float()` and return it. If a `ValueError` occurs, catch it and return `None` instead of crashing.
