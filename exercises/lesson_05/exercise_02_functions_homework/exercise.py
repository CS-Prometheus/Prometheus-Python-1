def build_profile(name, age, city="Unknown"):
    """
    Take required positional parameters name and age, and a keyword
    parameter city with a default of "Unknown". Return a dictionary
    with keys 'name', 'age', and 'city'.

    Example:
    build_profile("Ana", 12) -> returns: {'name': 'Ana', 'age': 12, 'city': 'Unknown'}
    build_profile("Ben", 13, city="Austin") -> returns: {'name': 'Ben', 'age': 13, 'city': 'Austin'}
    """
    # TODO: replace the line below with your solution
    pass


def order_total(*args, tax_rate=0.08, **kwargs):
    """
    Accept any number of item prices via *args, a keyword parameter
    tax_rate defaulting to 0.08, and any number of extra named fees
    via **kwargs. Sum the prices, add tax (sum of prices times
    tax_rate), add the sum of all kwargs values, and return the total
    rounded to 2 decimal places.

    Example:
    order_total(12.00, 8.50, 4.25, delivery=2.50, tip=3.00) -> returns: 32.23
    """
    # TODO: replace the line below with your solution
    pass


high_score = 0


def check_score(score, bonus=0):
    """
    Compute a local final_score = score + bonus, and, using the
    global keyword, update the module-level high_score whenever
    final_score is higher than the current high_score. Return
    final_score.

    Example (called in sequence, starting from high_score = 0):
    check_score(50) -> returns: 50, high_score becomes 50
    check_score(40, bonus=15) -> returns: 55, high_score becomes 55
    check_score(60, bonus=5) -> returns: 65, high_score becomes 65
    """
    # TODO: replace the line below with your solution
    pass


def top_scorers_report(students):
    """
    students is a list of dictionaries, each with 'name' and 'score'.
    Use filter() with a lambda to keep only students scoring 70 or
    above. Use sorted() with a key= lambda to sort those students from
    highest to lowest score. Use map() with a lambda to turn the
    sorted list into strings formatted as 'NAME: SCORE'. Return the
    final list.

    Example:
    top_scorers_report([
        {"name": "Ivy", "score": 65},
        {"name": "Zane", "score": 91},
        {"name": "Cleo", "score": 78},
        {"name": "Rex", "score": 55},
        {"name": "Sam", "score": 84},
    ]) -> returns: ['Zane: 91', 'Sam: 84', 'Cleo: 78']
    """
    # TODO: replace the line below with your solution
    pass


def average(*scores):
    """
    Accept any number of scores via *args and return their mean
    rounded to 1 decimal place.
    """
    # TODO: replace the line below with your solution
    pass


def letter_grade(score, scale=None):
    """
    If scale is not passed, it defaults inside the function to
    {90: 'A', 80: 'B', 70: 'C', 60: 'D'}. Return the letter for the
    highest threshold the score meets or exceeds, or 'F' if none
    apply.
    """
    # TODO: replace the line below with your solution
    pass


def class_grade_report(student_scores):
    """
    student_scores is a dictionary mapping each student's name to a
    list of their scores. For each student, call average() on their
    scores and letter_grade() on the result. Use sorted() with a
    lambda key to rank students from highest average to lowest, and
    return a list of strings formatted as 'NAME: AVERAGE (LETTER)'.

    Example:
    class_grade_report({
        "Ava": [92, 88, 95],
        "Ben": [70, 65, 74],
        "Cleo": [81, 79, 85],
    }) -> returns: ['Ava: 91.7 (A)', 'Cleo: 81.7 (B)', 'Ben: 69.7 (D)']
    """
    # TODO: replace the line below with your solution
    pass
