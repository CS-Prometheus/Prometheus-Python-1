from exercise import (
    classify_grade,
    range_checks,
    membership_checks,
)


def test_classify_grade_b(capsys):
    classify_grade(82)
    captured = capsys.readouterr()
    assert captured.out == "B\n"


def test_classify_grade_all_bands(capsys):
    for score, expected in [(95, "A"), (82, "B"), (75, "C"), (50, "F")]:
        classify_grade(score)
        captured = capsys.readouterr()
        assert captured.out == f"{expected}\n"


def test_range_checks_comfortable_teen(capsys):
    range_checks(72, 15)
    captured = capsys.readouterr()
    assert captured.out == "Comfortable\nTrue\n"


def test_range_checks_uncomfortable_not_teen(capsys):
    range_checks(50, 25)
    captured = capsys.readouterr()
    assert captured.out == "Not comfortable\nFalse\n"


def test_membership_checks(capsys):
    membership_checks(["apple", "banana", "mango"], "python")
    captured = capsys.readouterr()
    assert captured.out == "True\nTrue\nTrue\n"


def test_membership_checks_other_values(capsys):
    membership_checks(["kiwi", "grape"], "sky")
    captured = capsys.readouterr()
    # "banana" in fruits -> False, "grape" not in fruits -> False, "y" in "sky" -> True
    assert captured.out == "False\nFalse\nTrue\n"
