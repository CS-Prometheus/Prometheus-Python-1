import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
sys.modules.pop("exercise", None)

import json

from exercise import (
    build_task_list,
    save_and_load_snacks,
    get_price,
)


def test_build_task_list():
    result = build_task_list(
        ["Buy groceries", "Clean house", "Walk dog"],
        ["High", "Low", "Medium"],
    )
    assert result == [
        "High priority: Buy groceries",
        "Low priority: Clean house",
        "Medium priority: Walk dog",
    ]


def test_build_task_list_empty():
    assert build_task_list([], []) == []


def test_save_and_load_snacks(tmp_path):
    path = tmp_path / "snacks.json"
    snacks = [
        {"name": "Pretzels", "calories": 110},
        {"name": "Apple", "calories": 95},
        {"name": "Granola Bar", "calories": 140},
    ]
    result = save_and_load_snacks(str(path), snacks)
    assert result == ["Pretzels", "Apple", "Granola Bar"]
    with open(path) as f:
        saved = json.load(f)
    assert saved == snacks


def test_get_price_found():
    prices = {"apple": 1.50, "banana": 0.75, "milk": 3.25}
    assert get_price(prices, "apple") == 1.50


def test_get_price_missing():
    prices = {"apple": 1.50, "banana": 0.75, "milk": 3.25}
    assert get_price(prices, "bread") is None
