# Instructor Guide (not shown to students)

## 1. Push this repo to GitHub

```bash
git init
git add .
git commit -m "Initial exercise template"
git branch -M main
git remote add origin https://github.com/CS-Prometheus/Prometheus-Python-1.git
git push -u origin main
```

## 2. Mark it as a Template Repository
    
On the repo's GitHub page: **Settings -> General -> Template repository**
(check the box).

## 3. Distributing to students (GitHub Classroom is retired)

GitHub Classroom stopped accepting new signups in May 2026 and shuts down
fully in August 2026, so this repo uses the **"Use this template"**
workflow instead — the same one used across Prometheus-Python-1/2/4/6:

1. Add each student to the `CS-Prometheus` org (or an appropriate team)
   with at least "Write" access.
2. Students go to this repo's page and click **Use this template ->
   Create a new repository**, creating their own **private** repo under
   `CS-Prometheus` (e.g. `CS-Prometheus/python1-jsmith`).
3. Each student clones their own repo and works locally — see the
   student-facing `README.md` for the rest of the setup.
4. The `.github/workflows/classroom.yml` workflow (already included) runs
   `pytest` on every push in each student's repo and shows a green/red
   check — the same autograding signal GitHub Classroom used to provide.

## 4. Tracking progress

Since every student repo lives under the `CS-Prometheus` org, you can see
all of them (and their Actions pass/fail status) from the org's repository
list. There's no separate roster page like GitHub Classroom had, but the
org view serves the same purpose at no cost on GitHub's Free tier.

## 5. Adding real exercises from the PowerPoint

For each exercise, copy an existing exercise folder as a template and
rename it, e.g. `exercises/lesson_11/exercise_01_new_topic_classwork/`:

```
exercises/lesson_NN/exercise_NN_short_description/
    README.md          <- instructions for students
    exercise.py         <- starter code with TODOs, functions/classes with pass
    test_exercise.py     <- test cases (pytest asserts)
```

Naming convention: `exercise_NN_short_description` inside `lesson_NN` —
the `run_tests.py` script formats this automatically into a readable
label (e.g. "Lesson 04 / Exercise 01 - Loops Classwork").

Because every exercise ships its own `exercise.py` and `test_exercise.py`,
give each `test_exercise.py` this three-line header so the many identically
named files don't collide when pytest imports them together:

```python
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
sys.modules.pop("exercise", None)
```

together with the repo-root `pytest.ini` (included in this repo):

```
[pytest]
addopts = --import-mode=importlib
```

The `importlib` import mode plus that header is what lets the VS Code
Testing panel discover every `test_exercise.py` across all lessons in one
session without an "import file mismatch" error. `run_tests.py` runs each
exercise in its own process, so it works either way; the header matters for
whole-suite runs.

## 6. Source material

This repo's exercises are adapted from the "Python 1" foundational slide
deck (Days 1-10, covering print/math/strings, variables and data types,
conditionals, loops, functions, data structures, file I/O and JSON, error
handling, modules and packages, and a capstone project).
