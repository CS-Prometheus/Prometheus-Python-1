from exercise import greet


def test_greet_ava():
    assert greet("Ava") == "Hello, Ava!"


def test_greet_sam():
    assert greet("Sam") == "Hello, Sam!"


def test_greet_empty_string():
    assert greet("") == "Hello, !"
