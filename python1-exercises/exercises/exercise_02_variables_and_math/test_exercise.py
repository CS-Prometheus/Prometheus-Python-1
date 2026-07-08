from exercise import rectangle_area, is_even


def test_rectangle_area_basic():
    assert rectangle_area(3, 4) == 12


def test_rectangle_area_zero():
    assert rectangle_area(0, 5) == 0


def test_is_even_true():
    assert is_even(6) is True


def test_is_even_false():
    assert is_even(7) is False
