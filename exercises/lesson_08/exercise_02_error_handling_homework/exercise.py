def calculate(a, b, op):
    """
    op is one of "+", "-", "*", "/". Use if/elif to perform the
    matching operation. Wrap the whole thing in error handling that
    catches: ZeroDivisionError (when op is "/" and b is 0) returning
    "Error: division by zero"; TypeError (when a or b is not a
    number) returning "Error: inputs must be numbers"; and a case
    where op is not one of the four symbols, which should raise
    ValueError(f"Unknown operator: {op}") yourself using raise,
    caught by an except ValueError that returns
    "Error: unknown operator".

    Example:
    calculate(6, 3, "/") -> returns: 2.0
    calculate(6, 0, "/") -> returns: "Error: division by zero"
    """
    # TODO: replace the line below with your solution
    pass


class InsufficientFundsError(Exception):
    """Raised when a withdrawal amount exceeds the available balance."""
    pass


def withdraw(balance, amount):
    """
    Raise InsufficientFundsError(f"Cannot withdraw {amount}, balance
    is only {balance}") if amount > balance; otherwise return
    balance minus amount.
    """
    # TODO: replace the line below with your solution
    pass


def read_safely(path):
    """
    Try to open the file at path inside a try block and read its
    contents. Catch FileNotFoundError and use
    f"Missing file: {path}" as the result instead of crashing. Use a
    finally block that always appends f"Finished attempt for {path}"
    to a log list, regardless of success or failure. Return a tuple
    of (result, log).
    """
    # TODO: replace the line below with your solution
    pass


def validate(record):
    """
    record is a dict. Look up record["name"] and record["age"]
    (letting a KeyError happen naturally if a key is missing); check
    that age is an int using isinstance(), and if not, raise
    TypeError("age must be an int"); return a success message like
    "Sam: OK" if both checks pass.
    """
    # TODO: replace the line below with your solution
    pass


def build_report(records):
    """
    records is a list of dicts. Loop over records, call validate()
    on each inside a try/except that catches both KeyError and
    TypeError, and build a report list: successes look like
    "Sam: OK", failures look like "Missing key: 'age'" or
    "Ana: age must be an int". Return the report.
    """
    # TODO: replace the line below with your solution
    pass


class OutOfRangeError(Exception):
    """Raised when a grade is outside the 0-100 range."""
    pass


def process(raw_grades):
    """
    raw_grades is a list of strings. Loop over the list and, for
    each entry, try to: convert it to float(); if the conversion
    fails, catch ValueError and record
    ("invalid", entry, "not a number"); if the conversion succeeds
    but the value is outside 0-100, manually raise
    OutOfRangeError(f"{entry} is out of range") and catch it,
    recording ("invalid", entry, "out of range"); otherwise record
    ("valid", entry, float value). Return the list of results.
    """
    # TODO: replace the line below with your solution
    pass


def summarize(raw_grades):
    """
    Call process(raw_grades). Collect all valid float values and
    compute their average inside a try/except ZeroDivisionError
    (using None as the average if there are none). Return a tuple of
    (valid_count, invalid_count, average).
    """
    # TODO: replace the line below with your solution
    pass
