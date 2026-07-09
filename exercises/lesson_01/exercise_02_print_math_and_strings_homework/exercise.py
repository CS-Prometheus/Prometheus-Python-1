def name_banner(name):
    """
    Print a banner around `name`:
        1. a border line made of "*" repeated (len(name) + 8) times
        2. a line that is "* " + name + " *"
        3. the border again

    Then, with ONE print() call, print "Welcome", "to", "Python" as three
    separate arguments with sep="\n" so they appear stacked as three lines.
    """
    # TODO: replace the line below with your solution
    pass


def mini_calculator(a, b, c, d):
    """
    Print, with a label for each: the sum, difference, product, true
    division result (a / b), floor division (a // b), remainder (a % b),
    and a squared (a ** 2). Then print c + d. Then print the results of
    a + b * 2 and (a + b) * 2, each labeled, to show precedence.
    """
    # TODO: replace the line below with your solution
    pass


def receipt_lines(items):
    """
    items is a list of (name, price_str) tuples, e.g.
        [("Notebook", "$2.50"), ("Pencil", "$0.50")]

    For each item, print a receipt line exactly 24 characters wide: the
    item name, followed by "." characters (based on 24 - len(name) -
    len(price)) to pad out the line, followed by the price. Then print a
    final divider line of "=" repeated 24 times.
    """
    # TODO: replace the line below with your solution
    pass


def escaped_story():
    """
    Using ONE print() call, write a short story (at least 5 lines of
    output) that uses \n to separate lines, \t to indent one line of
    dialogue, and \" around the dialogue itself. Include at least two
    # comments inside this function explaining what different parts of
    the print statement do.

    After the story, print "THE END" using end="\n\n" (leaving a blank
    line after it), then print "~ fin ~" on the next line by itself.
    """
    # TODO: replace the line below with your solution.
    # Remember: at least two "#" comments of your own, a print() call
    # using \n / \t / \", then the "THE END" / "~ fin ~" lines.
    pass


def grocery_receipt(items):
    """
    items is a list of (name, price, qty) tuples, e.g.
        [("Apples", 0.50, 6), ("Bread", 2.50, 2), ("Milk", 3.50, 1)]

    For each item, compute its line total (price * quantity). Compute
    subtotal as the sum of the line totals, tax as subtotal * 0.08, and
    total as subtotal + tax.

    Print a receipt: a divider line of "=" repeated 28 times, one line
    per item showing name, quantity, and line total, then the divider
    again, then lines for Subtotal, Tax, and Total (tax/total rounded to
    2 decimals).
    """
    # TODO: replace the line below with your solution
    pass
