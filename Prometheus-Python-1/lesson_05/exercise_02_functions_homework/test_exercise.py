import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
sys.modules.pop("exercise", None)

import exercise
from exercise import (
    build_profile,
    order_total,
    top_scorers_report,
    average,
    letter_grade,
    class_grade_report,
)


def test_build_profile_positional_only():
    assert build_profile("Ana", 12) == {"name": "Ana", "age": 12, "city": "Unknown"}


def test_build_profile_city_keyword():
    assert build_profile("Ben", 13, city="Austin") == {
        "name": "Ben",
        "age": 13,
        "city": "Austin",
    }


def test_build_profile_all_keywords_reordered():
    assert build_profile(age=14, city="Denver", name="Cleo") == {
        "name": "Cleo",
        "age": 14,
        "city": "Denver",
    }


def test_order_total():
    assert order_total(12.00, 8.50, 4.25, delivery=2.50, tip=3.00) == 32.23


def test_order_total_other_values():
    assert order_total(10.00, 5.00, tax_rate=0.05, delivery=1.00) == 16.75


def test_check_score_sequence():
    r1 = exercise.check_score(50)
    r2 = exercise.check_score(40, bonus=15)
    r3 = exercise.check_score(60, bonus=5)
    assert r1 == 50
    assert r2 == 55
    assert r3 == 65
    assert exercise.high_score == 65


def test_top_scorers_report():
    students = [
        {"name": "Ivy", "score": 65},
        {"name": "Zane", "score": 91},
        {"name": "Cleo", "score": 78},
        {"name": "Rex", "score": 55},
        {"name": "Sam", "score": 84},
    ]
    assert top_scorers_report(students) == ["Zane: 91", "Sam: 84", "Cleo: 78"]


def test_top_scorers_report_other_values():
    students = [
        {"name": "A", "score": 70},
        {"name": "B", "score": 95},
        {"name": "C", "score": 50},
    ]
    assert top_scorers_report(students) == ["B: 95", "A: 70"]


def test_average():
    assert average(92, 88, 95) == 91.7


def test_average_has_docstring():
    assert average.__doc__ is not None
    assert len(average.__doc__.strip()) > 0


def test_letter_grade_default_scale():
    assert letter_grade(91.7) == "A"
    assert letter_grade(69.7) == "D"


def test_letter_grade_below_all_thresholds():
    assert letter_grade(40) == "F"


def test_letter_grade_custom_scale():
    assert letter_grade(55, {50: "P", 0: "F"}) == "P"


def test_class_grade_report():
    student_scores = {
        "Ava": [92, 88, 95],
        "Ben": [70, 65, 74],
        "Cleo": [81, 79, 85],
    }
    assert class_grade_report(student_scores) == [
        "Ava: 91.7 (A)",
        "Cleo: 81.7 (B)",
        "Ben: 69.7 (D)",
    ]


def test_class_grade_report_other_values():
    student_scores = {
        "Xan": [60, 62, 58],
        "Yuki": [99, 100, 97],
    }
    assert class_grade_report(student_scores) == [
        "Yuki: 98.7 (A)",
        "Xan: 60.0 (D)",
    ]
