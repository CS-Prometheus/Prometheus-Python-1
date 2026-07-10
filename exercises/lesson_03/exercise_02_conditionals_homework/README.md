# Exercise 02 — Conditionals (Homework)

*Week 1, Day 3*

Write your answers as Python code by filling in the functions in
`exercise.py`. Test each one by running the tests; the last one is the
most involved.

## 1. Field Trip Eligibility Checker

Write a function called `field_trip_eligibility` that takes
`permission_slip`, `balance_due`, `behavior_points`, and
`special_override`.

1. Using `and` to combine three conditions (`permission_slip` is true,
   `balance_due == 0`, `behavior_points >= 5`), print
   `"Eligible for the trip!"` or `"Not eligible yet."`.
2. Then do a second check: combine the same three conditions with
   `special_override` using `and`/`or` together (parenthesize the three
   normal requirements so the override can bypass all of them at once),
   and print the same two possible messages again.

```python
field_trip_eligibility(True, 0, 8, False)
# prints:
# Eligible for the trip!
# Eligible for the trip!
```

## 2. Truthy or Falsy Validator

Write a function called `truthy_falsy_report` that takes `values` (a
list). For each value, use a plain `if value:` (no comparison
operators) to print the value's `repr()` followed by whether Python
considers it `"Truthy"` or `"Falsy"`.

```python
truthy_falsy_report(["", "hi", 0, 5, []])
# prints:
# '' -> Falsy
# 'hi' -> Truthy
# 0 -> Falsy
# 5 -> Truthy
# [] -> Falsy
```

## 3. If/Else to Ternary Rewrite

Write a function called `if_else_and_ternary` that takes `num`, `x`,
`y`, `age`.

1. Using ordinary if/else statements, compute: `label` ("even"/"odd"
   based on `num`), `bigger` (whichever of `x`, `y` is larger), and
   `status` ("adult"/"minor" based on `age`, 18 cutoff).
2. Then recompute the same three results using one-line ternary
   expressions (`value_if_true if condition else value_if_false`),
   stored as `label2`, `bigger2`, `status2`.
3. Print `label == label2, bigger == bigger2, status == status2` (as
   one `print()` call with three arguments) to confirm they match.

```python
if_else_and_ternary(17, 12, 30, 16)
# prints: True True True
```

## 4. Multi Criteria Grading with Short Circuit Logic

Write a function called `graded_with_boost` that takes `score` and
`extra_credit_completed`.

1. Compute `base_grade` using chained comparisons/elif exactly like
   classwork problem 1.
2. Compute whether the student is `boosted`: only true if `base_grade`
   is `"B"` and `score >= 87`, **and** `extra_credit_completed` is
   `True`. Use short-circuit evaluation (`and`) so you don't need extra
   checks when the grade isn't `"B"`.
3. Print `"Base grade: {base_grade}"` and `"Boosted: {boosted}"`.

```python
graded_with_boost(87, True)
# prints:
# Base grade: B
# Boosted: True
```

## 5. Movie Ticket Price Calculator

Write a function called `ticket_price` that takes `age`, `is_student`,
`day`, `membership`. Start with `base_price = 12.00` inside the
function, then apply these rules:

- **Rule A:** if `age < 13 or age >= 65`, price is `base_price * 0.5`
  (child or senior).
- **Rule B (elif):** otherwise if `is_student` is `True`, price is
  `base_price * 0.75`.
- **Rule C (else):** otherwise, full `base_price`.
- **Rule D:** separately (not part of the if/elif/else above), if `day`
  is in `["Tuesday", "Wednesday"]`, apply an additional 20% off with
  `price = price * 0.8`, regardless of which rule above applied.
- **Rule E:** use a ternary to compute `membership_label`: `"VIP"` if
  `membership == "gold" or membership == "platinum"` else `"Standard"`.

Print the final price rounded to 2 decimals as `"Final price: $X.XX"`,
then `"Membership: {membership_label}"`.

**Example** (`age=16, is_student=True, day="Tuesday", membership="gold"`):

```
Final price: $7.20
Membership: VIP
```

---

Edit `exercise.py` and fill in each function where you see `# TODO`. Then
run the tests to check your work.
