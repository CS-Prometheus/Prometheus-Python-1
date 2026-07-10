# Exercise 02 — File I/O and JSON (Homework)

*Week 4, Day 1*

Write your answers as Python code by filling in the functions in `exercise.py`. Test each one by running the tests.

## 1. Journal Logger

Write a function called `log_entry` that takes `path` and `text`.

Append `text` as a new line to the file at `path`. Before appending, check whether the file exists yet with `os.path.exists()` (the append mode `"a"` will create the file automatically either way). Return `True` if this call created the file (it did not exist before), `False` if the file already existed.

Write a function called `read_numbered_entries` that takes `path`.

Open the file at `path` in read mode, use `readlines()` to get every entry, and return a list of strings with a number in front of each one, like `"1: <entry text>"`.

## 2. Word Frequency Counter

Write a function called `word_frequency` that takes `path` and `text`.

Write `text` to the file at `path` using `write()`. Open the file again and iterate over it line by line. For each line, split it into words (`str.split()`) and build a dictionary that counts how many times each word appears (lowercase the words first so `"The"` and `"the"` count together). Return the dictionary.

Write a function called `save_word_counts` that takes `path` and `counts`.

Save `counts` to the file at `path` using `json.dump()` with `indent=2`, then read it back with `json.load()` and return the loaded dictionary.

## 3. Directory Report

Write a function called `directory_report` that takes `folder` and `filenames` (a list).

For each filename, use `os.path.exists()` and `os.path.isfile()` to determine whether it exists as a file in `folder`. Build a report as a list of strings, one per file, like `"greeting.txt: FOUND"` or `"missing_file.txt: NOT FOUND"`. Use `os.path.join()` to construct each path.

Write a function called `save_report` that takes `path` and `report` (a list of strings).

Write the report to the file at `path` using `write()` or `writelines()`, one line per entry.

## 4. Student Grades JSON Store

Write a function called `save_grades_and_honor_roll` that takes `grades_path`, `honor_path`, and `students` (a list of dicts with `'name'` and `'grade'`).

Use `json.dump()` with `indent=2` to save the full list to `grades_path`. Then use `json.load()` to read the file back into a new variable. Filter the loaded list to only students with a grade of 90 or above, and save that filtered list to `honor_path`, also using `json.dump()` with `indent=2`. Return a list of the names of the students who made the honor roll.

## 5. Config File Manager

Write a function called `load_config` that takes `path`.

If the folder for `path` does not exist, create it with `os.makedirs()`. If the file does not exist, write a default config dictionary (`{"volume": 50, "difficulty": "easy"}`) to it with `json.dump()`. Then always finish by reading the file with `json.load()` and returning the dictionary.

Write a function called `save_config` that takes `path` and `config`.

Write `config` back to the file at `path` using `json.dump()` with `indent=2`.
