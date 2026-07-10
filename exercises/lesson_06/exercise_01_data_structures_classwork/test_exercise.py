from exercise import (
    list_cleanup,
    coordinates_unpacking,
    contact_card,
)


def test_list_cleanup():
    assert list_cleanup([12, 99, 30, 7]) == [5, 12, 30, 7, 50]


def test_list_cleanup_other_values():
    assert list_cleanup([99, 1, 2]) == [5, 1, 2, 50]


def test_coordinates_unpacking():
    assert coordinates_unpacking((4, -2, 9)) == "x=4, y=-2, z=9"


def test_coordinates_unpacking_other_values():
    assert coordinates_unpacking((0, 0, 1)) == "x=0, y=0, z=1"


def test_contact_card():
    assert contact_card("Priya", "555-0101", "555-0199", "priya@example.com") == (
        "Not on file",
        {"name": "Priya", "phone": "555-0199", "email": "priya@example.com"},
    )


def test_contact_card_other_values():
    assert contact_card("Sam", "111", "222", "sam@x.com") == (
        "Not on file",
        {"name": "Sam", "phone": "222", "email": "sam@x.com"},
    )
