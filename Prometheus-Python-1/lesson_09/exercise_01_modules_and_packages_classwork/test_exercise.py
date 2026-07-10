import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
sys.modules.pop("exercise", None)

import datetime

from exercise import (
    circle_area,
    sqrt_of,
    dice_rolls,
    format_date,
)


def test_circle_area():
    assert round(circle_area(4), 2) == 50.27


def test_sqrt_of():
    assert sqrt_of(144) == 12.0


def test_dice_rolls():
    assert dice_rolls(7, 5) == [3, 2, 4, 6, 1]


def test_dice_rolls_repeatable():
    assert dice_rolls(7, 5) == dice_rolls(7, 5)


def test_format_date():
    dt = datetime.datetime(2026, 7, 8)
    assert format_date(dt) == "July 08, 2026"


def test_format_date_other():
    dt = datetime.datetime(2025, 1, 1)
    assert format_date(dt) == "January 01, 2025"
