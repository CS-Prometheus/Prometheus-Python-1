import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
sys.modules.pop("exercise", None)

from exercise import (
    field_trip_eligibility,
    truthy_falsy_report,
    if_else_and_ternary,
    graded_with_boost,
    ticket_price,
)


def test_field_trip_eligibility_meets_all_conditions(capsys):
    field_trip_eligibility(True, 0, 8, False)
    captured = capsys.readouterr()
    assert captured.out == "Eligible for the trip!\nEligible for the trip!\n"


def test_field_trip_eligibility_override_only(capsys):
    field_trip_eligibility(False, 0, 8, True)
    captured = capsys.readouterr()
    assert captured.out == "Not eligible yet.\nEligible for the trip!\n"


def test_field_trip_eligibility_neither(capsys):
    field_trip_eligibility(False, 10, 2, False)
    captured = capsys.readouterr()
    assert captured.out == "Not eligible yet.\nNot eligible yet.\n"


def _expected_truthy_falsy(values):
    lines = []
    for v in values:
        label = "Truthy" if v else "Falsy"
        lines.append(f"{v!r} -> {label}")
    return "\n".join(lines) + "\n"


def test_truthy_falsy_report(capsys):
    values = ["", "hi", 0, 5, []]
    truthy_falsy_report(values)
    captured = capsys.readouterr()
    assert captured.out == _expected_truthy_falsy(values)


def test_truthy_falsy_report_other_values(capsys):
    values = [0, "text", [], 42, ""]
    truthy_falsy_report(values)
    captured = capsys.readouterr()
    assert captured.out == _expected_truthy_falsy(values)


def test_if_else_and_ternary(capsys):
    if_else_and_ternary(17, 12, 30, 16)
    captured = capsys.readouterr()
    assert captured.out == "True True True\n"


def test_if_else_and_ternary_other_values(capsys):
    if_else_and_ternary(4, 50, 9, 20)
    captured = capsys.readouterr()
    assert captured.out == "True True True\n"


def test_graded_with_boost_boosted(capsys):
    graded_with_boost(87, True)
    captured = capsys.readouterr()
    assert captured.out == "Base grade: B\nBoosted: True\n"


def test_graded_with_boost_no_extra_credit(capsys):
    graded_with_boost(88, False)
    captured = capsys.readouterr()
    assert captured.out == "Base grade: B\nBoosted: False\n"


def test_graded_with_boost_wrong_band(capsys):
    graded_with_boost(95, True)
    captured = capsys.readouterr()
    assert captured.out == "Base grade: A\nBoosted: False\n"


def test_ticket_price_student_tuesday_gold(capsys):
    ticket_price(16, True, "Tuesday", "gold")
    captured = capsys.readouterr()
    assert captured.out == "Final price: $7.20\nMembership: VIP\n"


def test_ticket_price_senior_monday_silver(capsys):
    ticket_price(70, False, "Monday", "silver")
    captured = capsys.readouterr()
    assert captured.out == "Final price: $6.00\nMembership: Standard\n"
