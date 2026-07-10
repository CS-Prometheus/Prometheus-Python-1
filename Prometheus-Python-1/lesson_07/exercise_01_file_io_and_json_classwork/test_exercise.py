import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
sys.modules.pop("exercise", None)

from exercise import (
    write_and_read_greeting,
    count_lines,
    save_and_load_book,
)


def test_write_and_read_greeting(tmp_path):
    path = tmp_path / "greeting.txt"
    assert write_and_read_greeting(str(path), "Hello, Python learner!") == "Hello, Python learner!"


def test_write_and_read_greeting_other_values(tmp_path):
    path = tmp_path / "greeting2.txt"
    assert write_and_read_greeting(str(path), "Goodbye!") == "Goodbye!"


def test_count_lines():
    import tempfile, os
    path = os.path.join(tempfile.mkdtemp(), "notes.txt")
    notes = ["Bring pencil", "Review loops", "Ask about JSON", "Submit homework"]
    assert count_lines(path, notes) == 4


def test_count_lines_other_values():
    import tempfile, os
    path = os.path.join(tempfile.mkdtemp(), "notes2.txt")
    assert count_lines(path, ["One", "Two"]) == 2


def test_save_and_load_book():
    import tempfile, os
    path = os.path.join(tempfile.mkdtemp(), "book.json")
    assert save_and_load_book(path, "Charlotte's Web", "E.B. White", 184) == (
        "Charlotte's Web by E.B. White has 184 pages."
    )


def test_save_and_load_book_other_values():
    import tempfile, os
    path = os.path.join(tempfile.mkdtemp(), "book2.json")
    assert save_and_load_book(path, "Hatchet", "Gary Paulsen", 195) == (
        "Hatchet by Gary Paulsen has 195 pages."
    )
