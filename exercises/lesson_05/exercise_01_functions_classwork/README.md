# Exercise 01 — Functions (Classwork)

*Week 1, Day 5*

Write your answers as Python code by filling in the functions in `exercise.py`. Test each one by running the tests.

## 1. Rectangle Area

Write a function called `rectangle_area` that takes two parameters, `width` and `height`, and returns their product. Give the function a docstring describing what it does.

```
rectangle_area(6, 3)
# returns: 18
```

## 2. Friendly Greeting

Write a function called `greet` that takes a `name` parameter and a `greeting` parameter that defaults to `"Hello"`. It should return a string formatted as `"GREETING, NAME!"`.

```
greet("Sam")
# returns: "Hello, Sam!"

greet("Sam", "Good morning")
# returns: "Good morning, Sam!"
```

## 3. Square with Lambda

Write a function called `square_numbers` that takes `numbers` (a list).

Use a lambda to create a function that returns a number's square. Then use `map()` with your lambda to apply it to `numbers`, convert the result to a list, and return it.

```
square_numbers([2, 5, 8, 1])
# returns: [4, 25, 64, 1]
```
