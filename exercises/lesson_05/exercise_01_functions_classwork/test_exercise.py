from exercise import (
    rectangle_area,
    greet,
    square_numbers,
)


def test_rectangle_area():
    assert rectangle_area(6, 3) == 18


def test_rectangle_area_other_values():
    assert rectangle_area(4, 5) == 20


def test_rectangle_area_has_docstring():
    assert rectangle_area.__doc__ is not None
    assert len(rectangle_area.__doc__.strip()) > 0


def test_greet_default():
    assert greet("Sam") == "Hello, Sam!"


def test_greet_custom_greeting():
    assert greet("Sam", "Good morning") == "Good morning, Sam!"


def test_greet_other_values():
    assert greet("Alex") == "Hello, Alex!"
    assert greet("Alex", "Hey") == "Hey, Alex!"


def test_square_numbers():
    assert square_numbers([2, 5, 8, 1]) == [4, 25, 64, 1]


def test_square_numbers_other_values():
    assert square_numbers([3, 4]) == [9, 16]
