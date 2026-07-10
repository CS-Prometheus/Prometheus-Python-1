import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
sys.modules.pop("exercise", None)

from exercise import (
    convert_and_report,
    report_card,
    slice_demo,
    clean_names,
    profile_card,
)


def _expected_convert_and_report(birth_year_text, height_text, score):
    birth_year = int(birth_year_text)
    age = 2026 - birth_year
    height = float(height_text)
    return (
        f"{age} {type(age)}\n"
        f"{height} {type(height)}\n"
        f"Your score was {score}\n"
    )


def test_convert_and_report(capsys):
    convert_and_report("2000", "5.5", 95)
    captured = capsys.readouterr()
    assert captured.out == _expected_convert_and_report("2000", "5.5", 95)


def test_convert_and_report_other_values(capsys):
    convert_and_report("1995", "6.0", 88)
    captured = capsys.readouterr()
    assert captured.out == _expected_convert_and_report("1995", "6.0", 88)


def _expected_report_card(math, science, english):
    lines = [
        f"{'Math':>10}: {math:.2f} rank {1:05d}",
        f"{'Science':>10}: {science:.2f} rank {2:05d}",
        f"{'English':>10}: {english:.2f} rank {3:05d}",
    ]
    avg = (math + science + english) / 3
    lines.append(f"{avg:^20.2f}")
    return "\n".join(lines) + "\n"


def test_report_card(capsys):
    report_card(88.5, 91.25, 76.0)
    captured = capsys.readouterr()
    assert captured.out == _expected_report_card(88.5, 91.25, 76.0)


def test_report_card_other_values(capsys):
    report_card(70.0, 82.5, 95.25)
    captured = capsys.readouterr()
    assert captured.out == _expected_report_card(70.0, 82.5, 95.25)


def _expected_slice_demo(full_name):
    username = full_name[0:3] + full_name[-3:]
    return (
        f"{full_name[0]}\n"
        f"{full_name[-1]}\n"
        f"{full_name[0:6]}\n"
        f"{full_name[-3:]}\n"
        f"{username}\n"
    )


def test_slice_demo(capsys):
    slice_demo("Jordan Alexander Lee")
    captured = capsys.readouterr()
    assert captured.out == _expected_slice_demo("Jordan Alexander Lee")


def test_slice_demo_other_name(capsys):
    slice_demo("Amanda Grace Fox")
    captured = capsys.readouterr()
    assert captured.out == _expected_slice_demo("Amanda Grace Fox")


def _expected_clean_names(raw):
    trimmed = raw.strip()
    parts = trimmed.split(",")
    cleaned = [p.strip() for p in parts]
    joined = " | ".join(cleaned)
    return (
        f"{joined}\n"
        f"{joined.find('Charlie')}\n"
        f"{joined.replace('Bob', 'Bobby')}\n"
    )


def test_clean_names(capsys):
    clean_names(" Alice,Bob, Charlie ,Dana ")
    captured = capsys.readouterr()
    assert captured.out == _expected_clean_names(" Alice,Bob, Charlie ,Dana ")


def test_clean_names_other_raw(capsys):
    raw = "Bob , Charlie,Eve , Frank"
    clean_names(raw)
    captured = capsys.readouterr()
    assert captured.out == _expected_clean_names(raw)


def _expected_profile_card(full_name, age_text, color):
    name = full_name.strip()
    age = int(age_text)
    first_name = name[:name.find(" ")]
    color_upper = color.upper()
    border = "=" * 24
    lines = [
        border,
        f"{'PROFILE CARD':^24}",
        border,
        f"Name: {name}",
        f"First name: {first_name}",
        f"Age: {age:>10}",
        f"Favorite Color: {color_upper}",
    ]
    return "\n".join(lines) + "\n"


def test_profile_card(capsys):
    profile_card("Priya Nair", "13", "teal")
    captured = capsys.readouterr()
    assert captured.out == _expected_profile_card("Priya Nair", "13", "teal")


def test_profile_card_other_values(capsys):
    profile_card("  Jordan Lee  ", "29", "Blue")
    captured = capsys.readouterr()
    assert captured.out == _expected_profile_card("  Jordan Lee  ", "29", "Blue")
