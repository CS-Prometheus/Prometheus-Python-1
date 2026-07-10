def write_and_read_greeting(path, text):
    """
    Open the file at path in write mode and write text to it (use a
    with statement). Then open the file again in read mode and
    return its contents.

    Example:
    write_and_read_greeting("greeting.txt", "Hello, Python learner!")
    -> returns: "Hello, Python learner!"
    """
    # TODO: replace the line below with your solution
    pass


def count_lines(path, notes):
    """
    Write notes (a list of strings) to the file at path, one per
    line, using writelines() (each item needs a newline character).
    Then reopen the file, use readlines() to load the lines into a
    list, and return how many lines were read.

    Example:
    count_lines("notes.txt", ["Bring pencil", "Review loops", "Ask about JSON", "Submit homework"])
    -> returns: 4
    """
    # TODO: replace the line below with your solution
    pass


def save_and_load_book(path, title, author, pages):
    """
    Create a dictionary describing a book with keys 'title', 'author',
    and 'pages' from the given arguments. Use json.dump() to save it
    to the file at path with indent=2. Then use json.load() to read
    it back and return a sentence built from the loaded data.

    Example:
    save_and_load_book("book.json", "Charlotte's Web", "E.B. White", 184)
    -> returns: "Charlotte's Web by E.B. White has 184 pages."
    """
    # TODO: replace the line below with your solution
    pass
