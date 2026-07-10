# Exercise 01 — Data Structures (Classwork)

*Week 2, Day 1*

Write your answers as Python code by filling in the functions in `exercise.py`. Test each one by running the tests.

## 1. List Cleanup

Write a function called `list_cleanup` that takes `numbers` (a list).

Append 50 to the end, insert 5 at index 0, and remove 99 from the list. Return the final list.

```
list_cleanup([12, 99, 30, 7])
# returns: [5, 12, 30, 7, 50]
```

## 2. Coordinates Unpacking

Write a function called `coordinates_unpacking` that takes `point` (a 3-tuple).

Unpack it into three variables `x`, `y`, and `z` in a single line, then return a sentence reporting all three values.

```
coordinates_unpacking((4, -2, 9))
# returns: "x=4, y=-2, z=9"
```

## 3. Contact Card

Write a function called `contact_card` that takes `name`, `phone`, `updated_phone`, and `email`.

Create a dictionary `contact` with keys `'name'` and `'phone'`. Add a new key `'email'`. Update the `'phone'` value. Use `.get()` to safely look up a key `'address'` that doesn't exist, defaulting to `'Not on file'`. Return a tuple of `(address_lookup, contact)`.

```
contact_card("Priya", "555-0101", "555-0199", "priya@example.com")
# returns: ("Not on file", {"name": "Priya", "phone": "555-0199", "email": "priya@example.com"})
```
