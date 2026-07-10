# Exercise 01 — File I/O and JSON (Classwork)

*Week 4, Day 1*

Write your answers as Python code by filling in the functions in `exercise.py`. Test each one by running the tests.

## 1. Write and Read a File

Write a function called `write_and_read_greeting` that takes `path` and `text`.

Open the file at `path` in write mode and write `text` to it (use a `with` statement). Then open the file again in read mode and return its contents.

```
write_and_read_greeting("greeting.txt", "Hello, Python learner!")
# returns: "Hello, Python learner!"
```

## 2. Count the Lines

Write a function called `count_lines` that takes `path` and `notes` (a list of strings).

Write `notes` to the file at `path`, one per line, using `writelines()` (remember each item needs a newline character). Then reopen the file, use `readlines()` to load the lines into a list, and return how many lines were read.

```
count_lines("notes.txt", ["Bring pencil", "Review loops", "Ask about JSON", "Submit homework"])
# returns: 4
```

## 3. Save and Load JSON

Write a function called `save_and_load_book` that takes `path`, `title`, `author`, and `pages`.

Create a dictionary describing a book with keys `'title'`, `'author'`, and `'pages'`. Use `json.dump()` to save it to the file at `path` with `indent=2`. Then use `json.load()` to read it back and return a sentence built from the loaded data.

```
save_and_load_book("book.json", "Charlotte's Web", "E.B. White", 184)
# returns: "Charlotte's Web by E.B. White has 184 pages."
```
