#!/usr/bin/env python3
"""
Friendly test runner for the Python 1 exercises.

Usage:
    python run_tests.py                                          # run every exercise
    python run_tests.py exercise_01_print_math_and_strings_classwork  # run just one exercise
"""

import re
import subprocess
import sys
from pathlib import Path

EXERCISES_DIR = Path(__file__).parent / "exercises"

# Matches pytest's short summary line, e.g.:
#   "3 passed in 0.02s"
#   "2 passed, 1 failed in 0.03s"
#   "1 failed, 2 errors in 0.01s"
SUMMARY_RE = re.compile(
    r"(?:(?P<passed>\d+) passed)?"
    r"(?:, )?(?:(?P<failed>\d+) failed)?"
    r"(?:, )?(?:(?P<errors>\d+) error)?"
)


def pretty_name(folder_name: str) -> str:
    """exercise_01_print_math_and_strings_classwork -> Exercise 01 - Print Math And Strings Classwork"""
    parts = folder_name.split("_")
    if parts and parts[0] == "exercise":
        parts = parts[1:]
    if parts and parts[0].isdigit():
        number, words = parts[0], parts[1:]
        title = " ".join(w.capitalize() for w in words)
        return f"Exercise {number} - {title}"
    return folder_name.replace("_", " ").title()


def run_one(exercise_dir: Path):
    result = subprocess.run(
        [sys.executable, "-m", "pytest", str(exercise_dir), "-q", "--tb=short"],
        capture_output=True,
        text=True,
    )
    output = result.stdout + result.stderr

    passed = failed = errors = 0
    for line in output.splitlines():
        match = SUMMARY_RE.search(line)
        if match and any(match.groups()):
            passed = int(match.group("passed") or 0)
            failed = int(match.group("failed") or 0)
            errors = int(match.group("errors") or 0)

    total = passed + failed + errors
    ok = result.returncode == 0
    return ok, passed, total, output


def main():
    if not EXERCISES_DIR.exists():
        print(f"Couldn't find an 'exercises' folder at {EXERCISES_DIR}")
        sys.exit(1)

    requested = sys.argv[1] if len(sys.argv) > 1 else None

    exercise_dirs = sorted(
        d for d in EXERCISES_DIR.iterdir()
        if d.is_dir() and (d / "test_exercise.py").exists()
    )

    if requested:
        exercise_dirs = [d for d in exercise_dirs if d.name == requested]
        if not exercise_dirs:
            print(f"No exercise folder named '{requested}' found.")
            sys.exit(1)

    if not exercise_dirs:
        print("No exercises with tests found yet.")
        sys.exit(0)

    print()
    any_failed = False
    failing_output = {}

    for ex_dir in exercise_dirs:
        label = pretty_name(ex_dir.name)
        ok, passed, total, output = run_one(ex_dir)
        dots = "." * max(3, 50 - len(label))
        status = "PASS" if ok else "FAIL"
        print(f"{label} {dots} {status} ({passed}/{total})")
        if not ok:
            any_failed = True
            failing_output[label] = output

    print()

    if failing_output:
        print("-" * 60)
        print("Details for failing exercises:")
        print("-" * 60)
        for label, output in failing_output.items():
            print(f"\n>>> {label}\n")
            print(output)

    sys.exit(1 if any_failed else 0)


if __name__ == "__main__":
    main()
