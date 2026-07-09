def safe_divide(a, b):
    """
    Return a divided by b. Wrap the division in a try/except block
    that catches ZeroDivisionError and returns the string
    "Cannot divide by zero" instead of crashing.

    Example:
    safe_divide(10, 2) -> returns: 5.0
    safe_divide(10, 0) -> returns: "Cannot divide by zero"
    """
    # TODO: replace the line below with your solution
    pass


def to_int(text):
    """
    Try to convert text to an integer using int() and return it. If
    a ValueError occurs (because text is not a valid number), catch
    it and return None instead.

    Example:
    to_int("42") -> returns: 42
    to_int("banana") -> returns: None
    """
    # TODO: replace the line below with your solution
    pass


def get_favorite(data, key):
    """
    data is a dictionary. In a try block, look up data[key]. If it
    raises a KeyError, append "Key not found: <key>" to a log list.
    If the lookup succeeds, use an else block to append "Found it!"
    and the value (as a string) to the log. Regardless of what
    happens, use a finally block to append "Lookup attempt
    complete." to the log. Return the log list.

    Example:
    get_favorite({"color": "blue"}, "color")
    -> returns: ["Found it!", "blue", "Lookup attempt complete."]
    """
    # TODO: replace the line below with your solution
    pass
