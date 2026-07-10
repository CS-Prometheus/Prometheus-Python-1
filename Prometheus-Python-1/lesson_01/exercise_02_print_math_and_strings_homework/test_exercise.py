import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
sys.modules.pop("exercise", None)

import inspect

from exercise import (
    name_banner,
    mini_calculator,
    receipt_lines,
    escaped_story,
    grocery_receipt,
)


def test_name_banner_sam(capsys):
    name_banner("Sam")
    captured = capsys.readouterr()
    border = "*" * (len("Sam") + 8)
    expected = f"{border}\n* Sam *\n{border}\nWelcome\nto\nPython\n"
    assert captured.out == expected


def test_name_banner_longer_name(capsys):
    name_banner("Prometheus")
    captured = capsys.readouterr()
    border = "*" * (len("Prometheus") + 8)
    expected = f"{border}\n* Prometheus *\n{border}\nWelcome\nto\nPython\n"
    assert captured.out == expected


def _expected_calculator_output(a, b, c, d):
    return (
        f"Sum: {a + b}\n"
        f"Difference: {a - b}\n"
        f"Product: {a * b}\n"
        f"True division: {a / b}\n"
        f"Floor division: {a // b}\n"
        f"Remainder: {a % b}\n"
        f"a squared: {a ** 2}\n"
        f"{c + d}\n"
        f"a + b * 2 = {a + b * 2}\n"
        f"(a + b) * 2 = {(a + b) * 2}\n"
    )


def test_mini_calculator_lesson_values(capsys):
    mini_calculator(17, 5, 3.5, 2)
    captured = capsys.readouterr()
    assert captured.out == _expected_calculator_output(17, 5, 3.5, 2)


def test_mini_calculator_other_values(capsys):
    mini_calculator(20, 6, 1.5, 4)
    captured = capsys.readouterr()
    assert captured.out == _expected_calculator_output(20, 6, 1.5, 4)


def _expected_receipt_lines(items):
    lines = []
    for name, price in items:
        dots = "." * (24 - len(name) - len(price))
        lines.append(name + dots + price)
    lines.append("=" * 24)
    return "\n".join(lines) + "\n"


def test_receipt_lines_lesson_items(capsys):
    items = [("Notebook", "$2.50"), ("Pencil", "$0.50"), ("Backpack", "$18.00")]
    receipt_lines(items)
    captured = capsys.readouterr()
    assert captured.out == _expected_receipt_lines(items)


def test_receipt_lines_other_items(capsys):
    items = [("Eraser", "$1.00"), ("Ruler", "$3.25")]
    receipt_lines(items)
    captured = capsys.readouterr()
    assert captured.out == _expected_receipt_lines(items)


def test_escaped_story_ends_correctly(capsys):
    escaped_story()
    captured = capsys.readouterr()
    assert captured.out.endswith("THE END\n\n~ fin ~\n")


def test_escaped_story_has_enough_lines(capsys):
    escaped_story()
    captured = capsys.readouterr()
    story_part = captured.out.split("THE END")[0]
    lines = [line for line in story_part.split("\n") if line != ""]
    assert len(lines) >= 5


def test_escaped_story_has_indented_quoted_dialogue(capsys):
    escaped_story()
    captured = capsys.readouterr()
    story_part = captured.out.split("THE END")[0]
    assert "\t" in story_part
    assert '"' in story_part


def test_escaped_story_has_comments():
    source = inspect.getsource(escaped_story)
    comment_lines = [
        line for line in source.split("\n") if line.strip().startswith("#")
    ]
    assert len(comment_lines) >= 2


def _expected_grocery_receipt(items):
    divider = "=" * 28
    lines = [divider]
    line_totals = []
    for name, price, qty in items:
        line_total = price * qty
        line_totals.append(line_total)
        lines.append(f"{name} x{qty}  ${line_total}")
    lines.append(divider)
    subtotal = sum(line_totals)
    tax = subtotal * 0.08
    total = subtotal + tax
    lines.append(f"Subtotal: ${subtotal}")
    lines.append(f"Tax: ${round(tax, 2)}")
    lines.append(f"Total: ${round(total, 2)}")
    return "\n".join(lines) + "\n"


def test_grocery_receipt_lesson_example(capsys):
    items = [("Apples", 0.50, 6), ("Bread", 2.50, 2), ("Milk", 3.50, 1)]
    grocery_receipt(items)
    captured = capsys.readouterr()
    assert captured.out == _expected_grocery_receipt(items)


def test_grocery_receipt_other_items(capsys):
    items = [("Eggs", 3.00, 2), ("Cheese", 4.25, 1)]
    grocery_receipt(items)
    captured = capsys.readouterr()
    assert captured.out == _expected_grocery_receipt(items)
