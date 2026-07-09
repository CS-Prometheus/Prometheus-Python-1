from exercise import (
    show_variable_types,
    augmented_assignment_demo,
    fstring_intro,
)


def test_show_variable_types(capsys):
    show_variable_types(7, 3.14, "hello", True)
    captured = capsys.readouterr()
    expected = (
        "7\n"
        "<class 'int'>\n"
        "3.14\n"
        "<class 'float'>\n"
        "hello\n"
        "<class 'str'>\n"
        "True\n"
        "<class 'bool'>\n"
    )
    assert captured.out == expected


def test_show_variable_types_other_values(capsys):
    show_variable_types(42, 2.5, "world", False)
    captured = capsys.readouterr()
    expected = (
        "42\n"
        "<class 'int'>\n"
        "2.5\n"
        "<class 'float'>\n"
        "world\n"
        "<class 'str'>\n"
        "False\n"
        "<class 'bool'>\n"
    )
    assert captured.out == expected


def _expected_augmented_assignment(score):
    after_plus5 = score + 5
    after_minus3 = after_plus5 - 3
    after_mult2 = after_minus3 * 2
    after_floordiv4 = after_mult2 // 4
    return (
        f"After +5: {after_plus5}\n"
        f"After -3: {after_minus3}\n"
        f"After *2: {after_mult2}\n"
        f"After //4: {after_floordiv4}\n"
    )


def test_augmented_assignment_demo(capsys):
    augmented_assignment_demo(10)
    captured = capsys.readouterr()
    assert captured.out == _expected_augmented_assignment(10)


def test_augmented_assignment_demo_other_value(capsys):
    augmented_assignment_demo(20)
    captured = capsys.readouterr()
    assert captured.out == _expected_augmented_assignment(20)


def _expected_fstring_intro(name, age, price):
    return f"My name is {name} and I am {age} years old.\n${price:.2f}\n"


def test_fstring_intro(capsys):
    fstring_intro("Riley", 12, 19.999)
    captured = capsys.readouterr()
    assert captured.out == _expected_fstring_intro("Riley", 12, 19.999)


def test_fstring_intro_other_values(capsys):
    fstring_intro("Sam", 30, 100.1)
    captured = capsys.readouterr()
    assert captured.out == _expected_fstring_intro("Sam", 30, 100.1)
