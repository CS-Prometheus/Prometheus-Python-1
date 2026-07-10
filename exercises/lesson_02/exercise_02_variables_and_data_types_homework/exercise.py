def convert_and_report(birth_year_text, height_text, score):
    """
    birth_year_text and height_text are strings standing in for what
    input() would return (e.g. "2000" and "5.5"). score is already an
    int.

    1. Convert birth_year_text to an int with int() and compute
       age = 2026 - birth_year.
    2. Convert height_text to a float with float().
    3. Print age and type(age) on one line: print(age, type(age)).
    4. Print height and type(height) the same way on the next line.
    5. Print "Your score was " + str(score).
    """
    # TODO: replace the line below with your solution
    pass


def report_card(math, science, english):
    """
    Print one line per subject (math=rank 1, science=rank 2,
    english=rank 3) using f-strings: subject name right-aligned to
    width 10 with :>10, score with :.2f, and rank zero-padded to 3
    digits with :05d. Then print the average of the three scores,
    centered in a line 20 characters wide with 2 decimal places, using
    :^20.2f.
    """
    # TODO: replace the line below with your solution
    pass


def slice_demo(full_name):
    """
    full_name is a string like "Jordan Alexander Lee" whose first and
    last names are 6 and 3 characters long. Using indexing/slicing
    only, print: the first character, the last character (negative
    index), full_name[0:6], full_name[-3:], and finally
    full_name[0:3] + full_name[-3:].
    """
    # TODO: replace the line below with your solution
    pass


def clean_names(raw):
    """
    raw is a messy comma-separated string like
    " Alice,Bob, Charlie ,Dana ". Strip outer whitespace, split on ",",
    strip() each individual name, join the cleaned names with " | ",
    and print the joined string. Then print joined.find("Charlie"),
    then print joined.replace("Bob", "Bobby").
    """
    # TODO: replace the line below with your solution
    pass


def profile_card(full_name, age_text, color):
    """
    full_name, age_text, and color are strings standing in for what
    input() would return.

    1. Strip extra whitespace from full_name.
    2. Convert age_text to an int with int().
    3. Get the first name using slicing, up to the first space (you
       can use full_name.find(" ") to locate it).
    4. Uppercase color with upper().
    5. Print, in order: a border of "=" * 24, a centered title line
       "PROFILE CARD" using :^24, the border again, "Name: {full_name}",
       "First name: {first_name}", "Age: {age:>10}", and
       "Favorite Color: {color_upper}".
    """
    # TODO: replace the line below with your solution
    pass
