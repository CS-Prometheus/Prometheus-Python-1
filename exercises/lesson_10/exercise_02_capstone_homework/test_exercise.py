import json

from exercise import (
    add_contact,
    search_contact,
    list_contacts,
    save_contacts,
    load_contacts,
    add_score,
    leaderboard,
    check_out,
    return_book,
    list_available,
    parse_menu_choice,
    add_expense,
    summary_report,
    parse_amount,
)


def test_add_contact():
    contacts = []
    result = add_contact(contacts, "Jane Doe", "555-1234", "jane@email.com")
    assert result == [
        {"name": "Jane Doe", "phone": "555-1234", "email": "jane@email.com"}
    ]


def test_search_contact_found():
    contacts = [
        {"name": "Jane Doe", "phone": "555-1234", "email": "jane@email.com"},
        {"name": "Bob", "phone": "555-9999", "email": "bob@email.com"},
    ]
    assert search_contact(contacts, "Bob") == {
        "name": "Bob",
        "phone": "555-9999",
        "email": "bob@email.com",
    }


def test_search_contact_not_found():
    contacts = [{"name": "Jane Doe", "phone": "555-1234", "email": "jane@email.com"}]
    assert search_contact(contacts, "Nobody") is None


def test_list_contacts():
    contacts = [{"name": "Jane Doe", "phone": "555-1234", "email": "jane@email.com"}]
    assert list_contacts(contacts) == ["Jane Doe | 555-1234 | jane@email.com"]


def test_save_and_load_contacts(tmp_path):
    path = tmp_path / "contacts.json"
    contacts = [{"name": "Jane Doe", "phone": "555-1234", "email": "jane@email.com"}]
    save_contacts(str(path), contacts)
    with open(path) as f:
        saved = json.load(f)
    assert saved == contacts
    assert load_contacts(str(path)) == contacts


def test_load_contacts_missing(tmp_path):
    path = tmp_path / "missing.json"
    assert load_contacts(str(path)) == []


def test_add_score():
    scores = []
    result = add_score(scores, "Alex", 9800)
    assert result == [{"name": "Alex", "score": 9800}]


def test_leaderboard():
    scores = [
        {"name": "Alex", "score": 9800},
        {"name": "Sam", "score": 9950},
        {"name": "Lee", "score": 100},
    ]
    assert leaderboard(scores) == [
        "#1 Sam: 9950",
        "#2 Alex: 9800",
        "#3 Lee: 100",
    ]


def _make_books():
    return [
        {"title": "Dune", "author": "Herbert", "checked_out": False},
        {"title": "Emma", "author": "Austen", "checked_out": True},
    ]


def test_check_out_success():
    books = _make_books()
    assert check_out(books, "Dune") == "Checked out Dune."
    assert books[0]["checked_out"] is True


def test_check_out_already_out():
    books = _make_books()
    assert check_out(books, "Emma") == "Emma is already checked out."


def test_check_out_not_found():
    books = _make_books()
    assert check_out(books, "Nowhere") == "Nowhere not found."


def test_return_book_success():
    books = _make_books()
    assert return_book(books, "Emma") == "Returned Emma."
    assert books[1]["checked_out"] is False


def test_return_book_not_checked_out():
    books = _make_books()
    assert return_book(books, "Dune") == "Dune was not checked out."


def test_list_available():
    books = _make_books()
    assert list_available(books) == ["Dune by Herbert"]


def test_parse_menu_choice_ok():
    assert parse_menu_choice("3") == 3


def test_parse_menu_choice_invalid():
    assert parse_menu_choice("abc") is None


def test_add_expense():
    expenses = []
    result = add_expense(expenses, 12.50, "Food", "2026-07-08")
    assert result == [{"amount": 12.50, "category": "Food", "date": "2026-07-08"}]


def test_summary_report():
    expenses = [
        {"amount": 12.50, "category": "Food", "date": "2026-07-08"},
        {"amount": 40.00, "category": "Transport", "date": "2026-07-08"},
        {"amount": 7.50, "category": "Food", "date": "2026-07-09"},
    ]
    assert summary_report(expenses) == [
        ("Transport", 40.00),
        ("Food", 20.00),
    ]


def test_parse_amount_ok():
    assert parse_amount("12.50") == 12.50


def test_parse_amount_invalid():
    assert parse_amount("abc") is None
