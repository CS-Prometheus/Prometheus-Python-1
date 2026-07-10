# Exercise 02 — Variables and Data Types (Homework)

*Week 1, Day 2*

Write your answers as Python code by filling in the functions in
`exercise.py`. Test each one by running the tests; the last one is the
most involved.

In real life you'd use `input()` to collect these values from the user.
Since the tests need to run without a person typing anything, each
function below takes the "typed" values in as parameters instead of
calling `input()` — but the conversions and logic are exactly what you'd
do with real input.

## 1. Input and Type Conversion

Write a function called `convert_and_report` that takes `birth_year_text`
(a string, e.g. `"2000"`), `height_text` (a string, e.g. `"5.5"`), and
`score` (an int).

1. Convert `birth_year_text` to an int with `int()` and compute
   `age = 2026 - birth_year`.
2. Convert `height_text` to a float with `float()`.
3. Print `age` and its `type()` on one line (`print(age, type(age))`),
   then `height` and its `type()` on the next line the same way.
4. Finally, build a sentence by concatenating `score` into a string with
   `str()` and print it: `"Your score was " + str(score)`.

**Example** (`birth_year_text="2000", height_text="5.5", score=95`):

```
26 <class 'int'>
5.5 <class 'float'>
Your score was 95
```

## 2. Formatted Report Card

Write a function called `report_card` that takes three numeric scores:
`math`, `science`, `english`. Using f-strings and format specs, print one
line per subject where: the subject name is right-aligned to a fixed
width with `:>10`, the score is shown with exactly 2 decimal places using
`:.2f`, and a rank number (1 for math, 2 for science, 3 for english) is
padded with zeros to 3 digits using `:05d`. Then print the average of the
three scores, centered in a line 20 characters wide with 2 decimal places,
using `:^20.2f`.

**Example** (`math=88.5, science=91.25, english=76.0`):

```
      Math: 88.50 rank 00001
   Science: 91.25 rank 00002
   English: 76.00 rank 00003
        85.25
```

(the average line is centered — the exact spacing comes from the `:^20.2f`
format spec).

## 3. Slicing a Username

Write a function called `slice_demo` that takes `full_name` (a string
like `"Jordan Alexander Lee"` where the first and last names are each 6
and 3 characters long, respectively). Using indexing and slicing only (no
string methods), print: the first character, the last character (with a
negative index), the first name using `full_name[0:6]`, the last name
using `full_name[-3:]`, and finally a username built from the first 3
letters of the first name concatenated with the last 3 letters of the
last name.

**Example** (`full_name="Jordan Alexander Lee"`):

```
J
e
Jordan
Lee
JorLee
```

## 4. Cleaning Messy Data

Write a function called `clean_names` that takes `raw`, a messy string
like `" Alice,Bob, Charlie ,Dana "`. Use `strip()` to remove outer
whitespace, `split(",")` to turn it into a list of names, then a loop
(or comprehension) with `strip()` on each name to remove extra spaces
around individual names. Use `join()` to combine the cleaned list back
into a single string separated by `" | "` and print it. Then print the
result of `find("Charlie")` on that joined string, and the result of
`replace("Bob", "Bobby")` on it.

**Example** (`raw=" Alice,Bob, Charlie ,Dana "`):

```
Alice | Bob | Charlie | Dana
14
Alice | Bobby | Charlie | Dana
```

## 5. User Profile Card Generator

This one combines everything from this lesson. Write a function called
`profile_card` that takes `full_name`, `age_text`, and `color` (all
strings, standing in for what `input()` would have returned).

1. Strip extra whitespace from `full_name`.
2. Convert `age_text` to an int with `int()`.
3. Use slicing to get the first name only — everything before the first
   space (you can use `find(" ")` to locate it).
4. Uppercase `color` with `upper()`.
5. Print a profile card: a border of `"="` repeated 24 times, a centered
   title line reading `"PROFILE CARD"` using `:^24`, the border again,
   then lines for Name, First name, Age (right-aligned in a field 10 wide
   with `:>10`), and Favorite Color (uppercased).

**Example** (`full_name="Priya Nair", age_text="13", color="teal"`):

```
========================
      PROFILE CARD
========================
Name: Priya Nair
First name: Priya
Age:         13
Favorite Color: TEAL
```

---

Edit `exercise.py` and fill in each function where you see `# TODO`. Then
run the tests to check your work.
