import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
sys.modules.pop("exercise", None)

from exercise import (
    safe_divide,
    to_int,
    get_favorite,
)


def test_safe_divide():
    assert safe_divide(10, 2) == 5.0


def test_safe_divide_by_zero():
    assert safe_divide(10, 0) == "Cannot divide by zero"


def test_to_int():
    assert to_int("42") == 42


def test_to_int_invalid():
    assert to_int("banana") is None


def test_get_favorite_found():
    assert get_favorite({"color": "blue"}, "color") == [
        "Found it!",
        "blue",
        "Lookup attempt complete.",
    ]


def test_get_favorite_not_found():
    assert get_favorite({"color": "blue"}, "size") == [
        "Key not found: size",
        "Lookup attempt complete.",
    ]
