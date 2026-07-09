# Instructor Guide (not shown to students)

## 1. Push this repo to GitHub

```bash
git init
git add .
git commit -m "Initial exercise template"
git branch -M main
git remote add origin https://github.com/<your-org-or-username>/python1-exercises.git
git push -u origin main
```

## 2. Mark it as a Template Repository

On the repo's GitHub page: **Settings -> General -> Template repository**
(check the box).

## 3. Create a GitHub Classroom assignment

1. Go to https://classroom.github.com and create/select your classroom.
2. **New Assignment** -> "Individual assignment".
3. Under "Add a template repository," pick this repo.
4. Under "Add autograding tests" you can optionally set up autograding
   through Classroom's UI, OR just rely on the `.github/workflows/classroom.yml`
   workflow already included — it runs `pytest` on every push and shows up
   as a green/red check on each student's repo and in the Classroom roster.
5. Get the invite link and share it with students. Each student who clicks
   it gets their own private repo cloned from this template.

## 4. Tracking progress

- The Classroom "Assignments" page shows each student's repo, last commit
  time, and (if you set up autograding) a pass/fail score per exercise.
- You can also bulk-clone every student repo at once using the
  [GitHub Classroom CLI](https://github.com/github/gh-classroom) if you
  want to inspect code locally:

  ```bash
  gh classroom clone student-repos
  ```

## 5. Adding real exercises from the PowerPoint

For each exercise, copy an existing exercise folder as a template and
rename it, e.g. `exercise_03_loops/`:

```
exercises/exercise_03_loops/
    README.md          <- instructions for students
    exercise.py         <- starter code with TODOs, functions return None/pass
    test_exercise.py     <- test cases (pytest asserts)
```

Naming convention: `exercise_NN_short_description` — the `run_tests.py`
script formats this automatically into a readable label (e.g.
"Exercise 03 - Loops").
