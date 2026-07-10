import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
sys.modules.pop("exercise", None)

import datetime
import collections

import pytest

from exercise import (
    dice_game_sums,
    days_until,
    area_rectangle,
    perimeter_rectangle,
    parse_args_or_exit,
    word_tally,
    highlight_word,
    contact_report,
)


def test_dice_game_sums():
    sums, counter = dice_game_sums(3, 20)
    assert len(sums) == 20
    assert counter == collections.Counter(sums)
    assert counter.most_common(1) == [(7, 7)]


def test_days_until():
    base = datetime.datetime(2026, 7, 8)
    result = days_until("Coding Quiz", base, 5)
    assert result == "Coding Quiz is on Monday, July 13, 2026 (5 days away)"


def test_days_until_other():
    base = datetime.datetime(2026, 7, 8)
    result = days_until("Winter Break", base, 40)
    assert result == "Winter Break is on Monday, August 17, 2026 (40 days away)"


def test_area_perimeter():
    assert area_rectangle(3, 4) == 12
    assert perimeter_rectangle(3, 4) == 14


def test_parse_args_or_exit_ok():
    assert parse_args_or_exit(["3", "4"]) == (3.0, 4.0)


def test_parse_args_or_exit_missing():
    with pytest.raises(SystemExit) as exc_info:
        parse_args_or_exit(["3"])
    assert exc_info.value.code == 1


def test_word_tally():
    sentences = [
        "the sun is bright",
        "the moon is bright too",
        "stars shine at night",
    ]
    counts = word_tally(sentences)
    assert counts == {
        "the": 2,
        "sun": 1,
        "is": 2,
        "bright": 2,
        "moon": 1,
        "too": 1,
        "stars": 1,
        "shine": 1,
        "at": 1,
        "night": 1,
    }


def test_highlight_word():
    counts = {"the": 2, "sun": 1, "is": 2, "bright": 2}
    assert highlight_word(counts, 42) == "the"


def test_contact_report_count():
    contacts = [
        {"name": "Ana", "city": "Austin"},
        {"name": "Ben", "city": "Boston"},
        {"name": "Cleo", "city": "Austin"},
    ]
    result = contact_report(contacts, "count")
    assert result == collections.Counter({"Austin": 2, "Boston": 1})


def test_contact_report_recent():
    contacts = [
        {"name": "Ana", "city": "Austin"},
        {"name": "Ben", "city": "Boston"},
    ]
    now = datetime.datetime(2026, 7, 8, 10, 0, 0)
    result = contact_report(contacts, "recent", now=now)
    assert result == ["Ana", "Ben", f"Report generated at {now}"]


def test_contact_report_bad_command():
    with pytest.raises(SystemExit) as exc_info:
        contact_report([], "bogus")
    assert exc_info.value.code == 1
