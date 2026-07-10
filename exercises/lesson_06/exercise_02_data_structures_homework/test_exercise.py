from exercise import (
    leaderboard_top3,
    club_set_operations,
    inventory_value_report,
    pass_fail_checks,
    team_formation_analyzer,
)


def test_leaderboard_top3():
    scores = [
        {"player": "Kai", "points": 340},
        {"player": "Lena", "points": 512},
        {"player": "Omar", "points": 275},
        {"player": "Tia", "points": 460},
        {"player": "Zoe", "points": 398},
    ]
    assert leaderboard_top3(scores) == [
        "1. Lena - 512 pts",
        "2. Tia - 460 pts",
        "3. Zoe - 398 pts",
    ]


def test_leaderboard_top3_other_values():
    scores = [
        {"player": "A", "points": 10},
        {"player": "B", "points": 30},
        {"player": "C", "points": 20},
    ]
    assert leaderboard_top3(scores) == ["1. B - 30 pts", "2. C - 20 pts", "3. A - 10 pts"]


def test_club_set_operations():
    chess = {"Ana", "Ben", "Cleo", "Drew"}
    robotics = {"Cleo", "Drew", "Eli", "Faye"}
    assert club_set_operations(chess, robotics) == {
        "union": {"Ana", "Ben", "Cleo", "Drew", "Eli", "Faye"},
        "intersection": {"Cleo", "Drew"},
        "chess_only": {"Ana", "Ben"},
        "symmetric_difference": {"Ana", "Ben", "Eli", "Faye"},
    }


def test_club_set_operations_other_values():
    chess = {"X", "Y"}
    robotics = {"Y", "Z"}
    assert club_set_operations(chess, robotics) == {
        "union": {"X", "Y", "Z"},
        "intersection": {"Y"},
        "chess_only": {"X"},
        "symmetric_difference": {"X", "Z"},
    }


def test_inventory_value_report():
    inventory = {
        "Notebook": (2.50, 40),
        "Pencil": (0.75, 120),
        "Backpack": (18.00, 6),
    }
    totals, grand_total = inventory_value_report(inventory)
    assert totals == {"Notebook": 100.0, "Pencil": 90.0, "Backpack": 108.0}
    assert grand_total == 298.0


def test_inventory_value_report_other_values():
    inventory = {"Pen": (1.00, 10), "Eraser": (0.50, 4)}
    totals, grand_total = inventory_value_report(inventory)
    assert totals == {"Pen": 10.0, "Eraser": 2.0}
    assert grand_total == 12.0


def test_pass_fail_checks():
    students = [
        {"name": "Jo", "scores": [70, 65, 80]},
        {"name": "Ray", "scores": [95, 92, 98]},
        {"name": "Ana", "scores": [55, 60, 58]},
    ]
    assert pass_fail_checks(students) == (False, True, [71.7, 95.0, 57.7])


def test_pass_fail_checks_other_values():
    students = [
        {"name": "A", "scores": [80, 80, 80]},
        {"name": "B", "scores": [70, 75, 65]},
    ]
    assert pass_fail_checks(students) == (True, False, [80.0, 70.0])


def test_team_formation_analyzer():
    volunteers = [
        ("Ana", "Designer", 3),
        ("Ben", "Developer", 6),
        ("Cleo", "Developer", 2),
        ("Drew", "Designer", 1),
        ("Eli", "Tester", 4),
    ]
    assert team_formation_analyzer(volunteers) == (
        True,
        False,
        {"Designer": ["Ana", "Drew"], "Developer": ["Ben", "Cleo"], "Tester": ["Eli"]},
    )


def test_team_formation_analyzer_other_values():
    volunteers = [
        ("A", "X", 6),
        ("B", "X", 7),
        ("C", "Y", 1),
    ]
    assert team_formation_analyzer(volunteers) == (
        True,
        False,
        {"X": ["A", "B"], "Y": ["C"]},
    )
