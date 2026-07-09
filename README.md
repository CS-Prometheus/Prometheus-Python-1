# Python 1 — Hands-On Exercises

Welcome! This repo has the coding exercises from class, each with automated
tests so you know immediately whether your solution works.

## One-time setup

1. **Get your own copy of this repo** using the GitHub Classroom link your
   instructor gave you. That creates a *private repo just for you* — clone
   that URL, not this template.

   ```bash
   git clone <your-classroom-repo-url>
   cd <your-repo-folder>
   ```

2. **Open the folder in VS Code.**

   ```bash
   code .
   ```

3. **Create a virtual environment and install requirements** (do this once):

   ```bash
   python -m venv .venv
   # Windows:
   .venv\Scripts\activate
   # macOS/Linux:
   source .venv/bin/activate

   pip install -r requirements.txt
   ```

4. When VS Code asks to select a Python interpreter, pick the one inside
   `.venv`.

## Doing an exercise

Each exercise lives in its own folder under `exercises/`:

```
exercises/exercise_01_print_math_and_strings_classwork/
    README.md          <- instructions for this exercise
    exercise.py         <- YOU edit this file
    test_exercise.py     <- tests that check your solution (don't edit)
```

Open `exercise.py`, read the instructions in that folder's `README.md`,
and write your code where you see `# TODO`.

## Running the tests

You have two ways to check your work — use whichever you like:

### Option A: The friendly test runner (recommended)

Run this from the terminal in VS Code:

```bash
python run_tests.py
```

It runs every exercise's tests and prints a simple pass/fail summary like:

```
Exercise 01 - Print Math And Strings Classwork ... PASS (5/5)
Exercise 02 - Print Math And Strings Homework .... PASS (12/12)
```

Run just one exercise:

```bash
python run_tests.py exercise_01_print_math_and_strings_classwork
```

### Option B: The VS Code Testing panel (the flask/lab icon)

Click the flask icon in the left sidebar of VS Code. It will discover all
the tests automatically and let you run/see them with green checks or red
x's, right next to the code.

## Submitting / saving your progress

Just commit and push, same as any git repo:

```bash
git add .
git commit -m "Complete exercise 1"
git push
```

Push often! Your instructor can see your progress on GitHub Classroom as
you go — you don't need to wait until everything is finished.
