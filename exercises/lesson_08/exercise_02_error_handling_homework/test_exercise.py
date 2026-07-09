import pytest

from exercise import (
    calculate,
    InsufficientFundsError,
    withdraw,
    read_safely,
    validate,
    build_report,
    OutOfRangeError,
    process,
    summarize,
)


def test_calculate_division():
    assert calculate(6, 3, "/") == 2.0


def test_calculate_division_by_zero():
    assert calculate(6, 0, "/") == "Error: division by zero"


def test_calculate_type_error():
    assert calculate(6, "x", "+") == "Error: inputs must be numbers"


def test_calculate_unknown_operator():
    assert calculate(6, 3, "^") == "Error: unknown operator"


def test_withdraw_success():
    assert withdraw(100, 40) == 60


def test_withdraw_insufficient_funds():
    with pytest.raises(InsufficientFundsError):
        withdraw(100, 150)


def test_read_safely_existing(tmp_path):
    path = tmp_path / "book.txt"
    path.write_text("hello")
    result, log = read_safely(str(path))
    assert result == "hello"
    assert log == [f"Finished attempt for {path}"]


def test_read_safely_missing(tmp_path):
    path = tmp_path / "missing.txt"
    result, log = read_safely(str(path))
    assert result == f"Missing file: {path}"
    assert log == [f"Finished attempt for {path}"]


def test_validate_and_build_report():
    records = [
        {"name": "Sam", "age": 14},
        {"name": "Lee"},
        {"name": "Ana", "age": "twelve"},
        {"age": 10},
    ]
    report = build_report(records)
    assert report[0] == "Sam: OK"
    assert "Missing key" in report[1]
    assert report[2] == "Ana: age must be an int"
    assert "Missing key" in report[3]


def test_validate_ok():
    assert validate({"name": "Sam", "age": 14}) == "Sam: OK"


def test_summarize():
    raw_grades = ["88", "92.5", "not_a_grade", "150", "-5", "76"]
    assert summarize(raw_grades) == (3, 3, 85.5)


def test_summarize_all_invalid():
    assert summarize(["abc", "200"]) == (0, 2, None)
