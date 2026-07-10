import random
import collections
import datetime


def dice_game_sums(seed, n):
    """
    Call random.seed(seed) for repeatable results. Simulate rolling
    two six sided dice n times, storing the sum of each roll (2 to 12)
    in a list. Use collections.Counter on the list of sums to tally
    how often each total occurred. Return a tuple of (sums, counter).

    Example:
    dice_game_sums(3, 20) -> returns: (sums_list, Counter({...}))
    """
    # TODO: replace the line below with your solution
    pass


def days_until(event_name, base_datetime, days_from_now):
    """
    Add a datetime.timedelta(days=days_from_now) to base_datetime to
    compute the event date. Return a message like
    "<event_name> is on <formatted date> (<days_from_now> days away)"
    using strftime("%A, %B %d, %Y") to format the date.

    Example:
    days_until("Coding Quiz", datetime.datetime(2026, 7, 8), 5)
    -> returns: "Coding Quiz is on Monday, July 13, 2026 (5 days away)"
    """
    # TODO: replace the line below with your solution
    pass


def area_rectangle(w, h):
    """
    Return the area of a rectangle with width w and height h.
    """
    # TODO: replace the line below with your solution
    pass


def perimeter_rectangle(w, h):
    """
    Return the perimeter of a rectangle with width w and height h.
    """
    # TODO: replace the line below with your solution
    pass


def parse_args_or_exit(args):
    """
    args is a list simulating sys.argv[1:] (command line arguments
    after the script name). If args has fewer than 2 items, print a
    usage message and call sys.exit(1). Otherwise convert the first
    two items to floats and return them as a tuple (width, height).

    Example:
    parse_args_or_exit(["3", "4"]) -> returns: (3.0, 4.0)
    parse_args_or_exit(["3"]) -> raises SystemExit(1)
    """
    # TODO: replace the line below with your solution
    pass


def word_tally(sentences):
    """
    sentences is a list of strings. Use collections.defaultdict(int)
    to build a dictionary that counts how many times each word appears
    across all sentences combined (split each sentence into words
    first). Return the dictionary (a plain dict is fine).

    Example:
    word_tally(["the sun is bright"]) -> returns:
    {"the": 1, "sun": 1, "is": 1, "bright": 1}
    """
    # TODO: replace the line below with your solution
    pass


def highlight_word(counts, seed):
    """
    counts is a dictionary of word counts (like the one returned by
    word_tally). Call random.seed(seed) then use random.choice() on
    the list of unique words (the dictionary keys) and return the
    chosen word.
    """
    # TODO: replace the line below with your solution
    pass


def contact_report(contacts, command, now=None):
    """
    contacts is a list of dicts, each with "name" and "city" keys. If
    command is "count", use collections.Counter to count how many
    contacts are in each city and return the Counter. If command is
    "recent", return a list containing every contact's name (in
    order) followed by one final string
    f"Report generated at {now}" (use now if given, otherwise
    datetime.datetime.now()). For any other command, print a usage
    message listing the valid commands and call sys.exit(1).
    """
    # TODO: replace the line below with your solution
    pass
