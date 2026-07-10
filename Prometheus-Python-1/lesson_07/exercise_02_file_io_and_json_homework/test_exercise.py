import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
sys.modules.pop("exercise", None)

from exercise import (
    log_entry,
    read_numbered_entries,
    word_frequency,
    save_word_counts,
    directory_report,
    save_report,
    save_grades_and_honor_roll,
    load_config,
    save_config,
)


def test_log_entry_creates_file_once(tmp_path):
    path = str(tmp_path / "journal.txt")
    assert log_entry(path, "first") is True
    assert log_entry(path, "second") is False
    assert log_entry(path, "third") is False


def test_read_numbered_entries(tmp_path):
    path = str(tmp_path / "journal.txt")
    log_entry(path, "Learned about with statements")
    log_entry(path, "Practiced append mode")
    log_entry(path, "Reviewed JSON basics")
    assert read_numbered_entries(path) == [
        "1: Learned about with statements",
        "2: Practiced append mode",
        "3: Reviewed JSON basics",
    ]


def test_word_frequency(tmp_path):
    path = str(tmp_path / "paragraph.txt")
    text = "The cat sat on the mat.\nThe cat ran fast.\n"
    counts = word_frequency(path, text)
    assert counts["the"] == 3
    assert counts["cat"] == 2


def test_word_frequency_other_values(tmp_path):
    path = str(tmp_path / "paragraph2.txt")
    text = "Dogs run. Dogs bark.\n"
    counts = word_frequency(path, text)
    assert counts["dogs"] == 2
    assert counts["run"] == 1


def test_save_word_counts(tmp_path):
    path = str(tmp_path / "word_counts.json")
    counts = {"the": 3, "cat": 2}
    assert save_word_counts(path, counts) == {"the": 3, "cat": 2}


def test_directory_report(tmp_path):
    (tmp_path / "greeting.txt").write_text("hi")
    (tmp_path / "book.json").write_text("{}")
    report = directory_report(str(tmp_path), ["greeting.txt", "book.json", "missing_file.txt"])
    assert report == [
        "greeting.txt: FOUND",
        "book.json: FOUND",
        "missing_file.txt: NOT FOUND",
    ]


def test_directory_report_other_values(tmp_path):
    (tmp_path / "a.txt").write_text("x")
    report = directory_report(str(tmp_path), ["a.txt", "b.txt"])
    assert report == ["a.txt: FOUND", "b.txt: NOT FOUND"]


def test_save_report(tmp_path):
    path = tmp_path / "file_report.txt"
    save_report(str(path), ["a.txt: FOUND", "b.txt: NOT FOUND"])
    assert path.read_text().splitlines() == ["a.txt: FOUND", "b.txt: NOT FOUND"]


def test_save_grades_and_honor_roll(tmp_path):
    students = [
        {"name": "Ana", "grade": 95},
        {"name": "Ben", "grade": 82},
        {"name": "Cleo", "grade": 91},
        {"name": "Deshawn", "grade": 76},
        {"name": "Ellie", "grade": 90},
    ]
    names = save_grades_and_honor_roll(
        str(tmp_path / "grades.json"), str(tmp_path / "honor_roll.json"), students
    )
    assert names == ["Ana", "Cleo", "Ellie"]


def test_save_grades_and_honor_roll_other_values(tmp_path):
    students = [{"name": "A", "grade": 100}, {"name": "B", "grade": 50}]
    names = save_grades_and_honor_roll(
        str(tmp_path / "g.json"), str(tmp_path / "h.json"), students
    )
    assert names == ["A"]


def test_load_config_creates_default(tmp_path):
    path = str(tmp_path / "settings" / "config.json")
    assert load_config(path) == {"volume": 50, "difficulty": "easy"}


def test_load_config_and_save_config(tmp_path):
    path = str(tmp_path / "settings" / "config.json")
    config = load_config(path)
    config["volume"] = 80
    config["difficulty"] = "hard"
    save_config(path, config)
    assert load_config(path) == {"volume": 80, "difficulty": "hard"}
