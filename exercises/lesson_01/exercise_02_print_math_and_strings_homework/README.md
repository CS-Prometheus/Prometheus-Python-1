# Exercise 02 — Print, Math and Strings (Homework)

*Week 1, Day 1*

Write your answers as Python code by filling in the functions in
`exercise.py`. Test each one by running the tests; the last one is the
most involved.

## 1. Formatted Name Banner

Write a function called `name_banner` that takes `name` and prints a banner
around it using string repetition and concatenation:

1. a border line made of `"*"` repeated `(len(name) + 8)` times
2. a line that is `"* " + name + " *"`
3. the border again

Then, with **one** `print()` call, print `"Welcome"`, `"to"`, `"Python"` as
three separate arguments with `sep="\n"` so they appear stacked as three
lines.

**Example** (`name = "Sam"`):

```
**********
* Sam *
**********
Welcome
to
Python
```

## 2. Mini Calculator

Write a function called `mini_calculator` that takes four numbers `a`, `b`,
`c`, `d` and prints, with a label for each: the sum, difference, product,
true division result (`a / b`), floor division (`a // b`), remainder
(`a % b`), and `a` squared (`a ** 2`).

Then print `c + d` on its own line. Finally, print the results of
`a + b * 2` and `(a + b) * 2` side by side (each labeled) to show how
parentheses change precedence.

**Example** (`a=17, b=5, c=3.5, d=2`):

```
Sum: 22
Difference: 12
Product: 85
True division: 3.4
Floor division: 3
Remainder: 2
a squared: 289
5.5
a + b * 2 = 27
(a + b) * 2 = 44
```

## 3. Receipt Line Builder

Write a function called `receipt_lines` that takes `items`, a list of
`(name, price)` tuples (price already a string, e.g. `("Notebook",
"$2.50")`). For each item, print a receipt line that is **exactly 24
characters wide**: the name, then `"."` characters (`24 - len(name) -
len(price)` of them) to pad it out, then the price. After all items,
print a divider line of `"="` repeated 24 times.

**Example:**

```
Notebook................$2.50
Pencil...................$0.50
Backpack.................$18.00
========================
```

## 4. Escaped Story with Comments

Write a function called `escaped_story` that prints a short "story" (at
least 5 lines of output) using **one** `print()` call that relies on `\n`
to separate lines, `\t` to indent one line of dialogue, and `\"` around
the dialogue itself. Include **at least two `#` comments** in your code
(inside the function) explaining what different parts of the print
statement do — the tests check that your comments exist, not just your
output.

After the story, print `"THE END"` using `end="\n\n"`, then print
`"~ fin ~"` on the next line by itself. The story content is up to you.

## 5. Grocery Receipt Calculator

This one combines everything from this lesson. Write a function called
`grocery_receipt` that takes `items`, a list of `(name, price, qty)`
tuples, e.g. `[("Apples", 0.50, 6), ("Bread", 2.50, 2)]`.

For each item, compute its line total (`price * quantity`). Compute
`subtotal` as the sum of all line totals, `tax` as `subtotal * 0.08`, and
`total` as `subtotal + tax`.

Print a receipt:

1. a divider line of `"="` repeated 28 times
2. one line per item: `print(name, "x" + str(qty), " $" + str(line_total))`
3. the divider again
4. `"Subtotal: $" + str(subtotal)`
5. `"Tax: $" + str(round(tax, 2))`
6. `"Total: $" + str(round(total, 2))`

**Example** (`items = [("Apples", 0.50, 6), ("Bread", 2.50, 2), ("Milk", 3.50, 1)]`):

```
============================
Apples x6  $3.0
Bread x2  $5.0
Milk x1  $3.5
============================
Subtotal: $11.5
Tax: $0.92
Total: $12.42
```

---

Edit `exercise.py` and fill in each function where you see `# TODO`. Then
run the tests to check your work.
