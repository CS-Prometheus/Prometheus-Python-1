from exercise import (
    sum_even_numbers,
    countdown_with_break,
    numbered_shopping_list,
)


def test_sum_even_numbers_2_to_20(capsys):
    sum_even_numbers(2, 20)
    captured = capsys.readouterr()
    assert captured.out == "Sum of even numbers 2 to 20: 110\n"


def test_sum_even_numbers_other_values(capsys):
    sum_even_numbers(4, 10)
    captured = capsys.readouterr()
    assert captured.out == "Sum of even numbers 4 to 10: 28\n"


def test_countdown_with_break(capsys):
    countdown_with_break(5, 3)
    captured = capsys.readouterr()
    assert captured.out == "1\n2\n3\nLoop stopped early!\n"


def test_countdown_with_break_other_values(capsys):
    countdown_with_break(4, 2)
    captured = capsys.readouterr()
    assert captured.out == "1\n2\nLoop stopped early!\n"


def test_numbered_shopping_list(capsys):
    numbered_shopping_list(["Milk", "Eggs", "Bread", "Apples"])
    captured = capsys.readouterr()
    assert captured.out == "1) Milk\n2) Eggs\n3) Bread\n4) Apples\n"


def test_numbered_shopping_list_other_values(capsys):
    numbered_shopping_list(["Pen", "Paper"])
    captured = capsys.readouterr()
    assert captured.out == "1) Pen\n2) Paper\n"
