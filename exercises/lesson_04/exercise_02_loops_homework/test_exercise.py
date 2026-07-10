import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
sys.modules.pop("exercise", None)

from exercise import (
    vowel_counter,
    login_attempt_validator,
    team_roster_report,
    prime_finder,
    class_quiz_tracker,
)


def test_vowel_counter(capsys):
    vowel_counter("Loops are powerful and fun")
    captured = capsys.readouterr()
    assert captured.out == "Vowels: 9\nTotal letters: 22\nVowel percentage: 40.9%\n"


def test_vowel_counter_other_values(capsys):
    vowel_counter("Hello World")
    captured = capsys.readouterr()
    assert captured.out == "Vowels: 3\nTotal letters: 10\nVowel percentage: 30.0%\n"


def test_login_attempt_validator_granted(capsys):
    login_attempt_validator("4821", ["12", "9034", "48213", "4821", "1111"])
    captured = capsys.readouterr()
    assert captured.out == "Access granted after 2 attempt(s)\n"


def test_login_attempt_validator_denied(capsys):
    login_attempt_validator("9999", ["12", "9034", "48213", "4821", "1111"])
    captured = capsys.readouterr()
    assert captured.out == "Access denied\n"


def test_team_roster_report(capsys):
    team_roster_report(["Ava", "Noah", "Mia", "Liam"], [7, 23, 15, 4])
    captured = capsys.readouterr()
    assert captured.out == (
        "1. Ava wears #7\n"
        "2. Noah wears #23\n"
        "3. Mia wears #15\n"
        "4. Liam wears #4\n"
        "Total players: 4\n"
    )


def test_team_roster_report_other_values(capsys):
    team_roster_report(["Zoe", "Sam"], [1, 2])
    captured = capsys.readouterr()
    assert captured.out == "1. Zoe wears #1\n2. Sam wears #2\nTotal players: 2\n"


def test_prime_finder(capsys):
    prime_finder(2, 30)
    captured = capsys.readouterr()
    assert captured.out == "Primes from 2 to 30: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]\n"


def test_prime_finder_other_values(capsys):
    prime_finder(10, 20)
    captured = capsys.readouterr()
    assert captured.out == "Primes from 10 to 20: [11, 13, 17, 19]\n"


def test_class_quiz_tracker(capsys):
    class_quiz_tracker({"Ava": [88, 92, 79], "Noah": [55, 90, 60], "Mia": [70, 75, 82]})
    captured = capsys.readouterr()
    assert captured.out == (
        "Ava\n"
        "  Quiz 1: 88\n"
        "  Quiz 2: 92\n"
        "  Quiz 3: 79\n"
        "  Total: 259\n"
        "  Average: 86.3\n"
        "Noah\n"
        "  Quiz 1: 55\n"
        "  Attendance/quiz flag: early stop\n"
        "Mia\n"
        "  Quiz 1: 70\n"
        "  Quiz 2: 75\n"
        "  Quiz 3: 82\n"
        "  Total: 227\n"
        "  Average: 75.7\n"
    )


def test_class_quiz_tracker_other_values(capsys):
    class_quiz_tracker({"Ben": [50, 90], "Cleo": [70, 80, 90]})
    captured = capsys.readouterr()
    assert captured.out == (
        "Ben\n"
        "  Quiz 1: 50\n"
        "  Attendance/quiz flag: early stop\n"
        "Cleo\n"
        "  Quiz 1: 70\n"
        "  Quiz 2: 80\n"
        "  Quiz 3: 90\n"
        "  Total: 240\n"
        "  Average: 80.0\n"
    )
