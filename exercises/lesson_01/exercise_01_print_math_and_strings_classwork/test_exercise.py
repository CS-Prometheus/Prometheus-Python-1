from exercise import (
    intro_line,
    loading_message,
    quote_block,
    show_order_of_operations,
)


def test_intro_line(capsys):
    intro_line("Ava", "Smith", "reading")
    captured = capsys.readouterr()
    assert captured.out == "Ava | Smith | reading\n"


def test_intro_line_different_values(capsys):
    intro_line("Sam", "Lee", "chess")
    captured = capsys.readouterr()
    assert captured.out == "Sam | Lee | chess\n"


def test_loading_message(capsys):
    loading_message()
    captured = capsys.readouterr()
    assert captured.out == "Loading...done!\n"


def test_quote_block(capsys):
    quote_block()
    captured = capsys.readouterr()
    expected = (
        "My favorite quote is:\n"
        "\t\"Practice makes perfect.\"\n"
        "Saved to: C:\\Python\\notes.txt\n"
    )
    assert captured.out == expected


def test_show_order_of_operations(capsys):
    show_order_of_operations()
    captured = capsys.readouterr()
    expected = (
        "2 + 3 * 4 = 14\n"
        "(2 + 3) * 4 = 20\n"
        "17 // 5 = 3\n"
        "17 % 5 = 2\n"
        "2 ** 3 ** 2 = 512\n"
    )
    assert captured.out == expected
