# Exercise 01 — Print, Math and Strings (Classwork)

*Week 1, Day 1*

Write your answers as Python code by filling in the functions in
`exercise.py`. Test each one by running the tests.

## 1. Custom Separators and Endings

Write a function called `intro_line` that takes `first_name`, `last_name`,
and `hobby` and prints them as three separate arguments to a **single**
`print()` call, using `sep=" | "` so a vertical bar appears between each
one.

```python
intro_line("Ava", "Smith", "reading")
# prints: Ava | Smith | reading
```

Then write a function called `loading_message` that makes **two** `print()`
calls: the first prints `"Loading"` using `end=""` (no newline), and the
second prints `"...done!"` right after it, so both appear together on one
line.

```python
loading_message()
# prints: Loading...done!
```

## 2. Escape Sequences

Write a function called `quote_block` that uses a **single** `print()`
statement (and the escape sequences `\n`, `\t`, and `\"`) to output exactly
these three lines:

```
My favorite quote is:
	"Practice makes perfect."
Saved to: C:\Python\notes.txt
```

## 3. Order of Operations

Write a function called `show_order_of_operations` that predicts and prints
the result of each expression below, one per line, labeled like this:

```python
print("2 + 3 * 4 =", 2 + 3 * 4)
```

Print, in this order:

```
2 + 3 * 4
(2 + 3) * 4
17 // 5
17 % 5
2 ** 3 ** 2
```

---

Edit `exercise.py` and fill in each function where you see `# TODO`. Then
run the tests to check your work.
