import json
import os


def add_contact(contacts, name, phone, email):
    """
    Append a new dict {"name": name, "phone": phone, "email": email}
    to the contacts list and return the list.
    """
    # TODO: replace the line below with your solution
    pass


def search_contact(contacts, name):
    """
    Loop through contacts and return the first contact dict whose
    "name" matches name exactly. Return None if no match is found.
    """
    # TODO: replace the line below with your solution
    pass


def list_contacts(contacts):
    """
    Return a list of formatted strings, one per contact, in the form
    "<name> | <phone> | <email>", in the same order as contacts.
    """
    # TODO: replace the line below with your solution
    pass


def save_contacts(path, contacts):
    """
    Write contacts to the file at path as JSON using json.dump() with
    indent=2.
    """
    # TODO: replace the line below with your solution
    pass


def load_contacts(path):
    """
    If a file exists at path (check with os.path.exists), load and
    return its contents using json.load(). Otherwise return an empty
    list.
    """
    # TODO: replace the line below with your solution
    pass


def add_score(scores, name, score):
    """
    Append a new dict {"name": name, "score": score} to the scores
    list and return the list.
    """
    # TODO: replace the line below with your solution
    pass


def leaderboard(scores):
    """
    Use sorted() with a lambda key to rank scores from highest to
    lowest (sorted(scores, key=lambda s: s["score"], reverse=True)).
    Return a list of formatted strings "#<rank> <name>: <score>",
    starting at rank 1 (use enumerate(ranked, start=1)).
    """
    # TODO: replace the line below with your solution
    pass


def check_out(books, title):
    """
    books is a list of dicts with "title", "author", and
    "checked_out" keys. Find the book with a matching title. If it
    exists and is not already checked out, set checked_out to True
    and return f"Checked out {title}.". If it exists but is already
    checked out, return f"{title} is already checked out.". If no
    book with that title exists, return f"{title} not found.".
    """
    # TODO: replace the line below with your solution
    pass


def return_book(books, title):
    """
    Find the book with a matching title. If it exists and is checked
    out, set checked_out back to False and return
    f"Returned {title}.". If it exists but was not checked out,
    return f"{title} was not checked out.". If no book with that
    title exists, return f"{title} not found.".
    """
    # TODO: replace the line below with your solution
    pass


def list_available(books):
    """
    Return a list of formatted strings "<title> by <author>" for
    every book where checked_out is False, in order.
    """
    # TODO: replace the line below with your solution
    pass


def parse_menu_choice(text):
    """
    Try to convert text to an int using int() and return it. If a
    ValueError occurs, catch it and return None instead of crashing
    (simulating a friendly "Please enter a number" message).
    """
    # TODO: replace the line below with your solution
    pass


def add_expense(expenses, amount, category, date):
    """
    Append a new dict {"amount": amount, "category": category,
    "date": date} to the expenses list and return the list.
    """
    # TODO: replace the line below with your solution
    pass


def summary_report(expenses):
    """
    Build a dictionary accumulating total spending per category (use
    totals[category] = totals.get(category, 0) + amount in a loop
    over expenses). Then return sorted(totals.items(),
    key=lambda pair: pair[1], reverse=True) so the biggest spending
    category comes first.
    """
    # TODO: replace the line below with your solution
    pass


def parse_amount(text):
    """
    Try to convert text to a float using float() and return it. If a
    ValueError occurs, catch it and return None instead of crashing.
    """
    # TODO: replace the line below with your solution
    pass
