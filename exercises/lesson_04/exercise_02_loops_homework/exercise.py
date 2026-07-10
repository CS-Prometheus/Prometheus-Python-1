def vowel_counter(sentence):
    """
    Loop through sentence character by character with a for loop. Use
    continue to skip spaces. Use an accumulator to count how many of
    the remaining characters are vowels (a, e, i, o, u; treat upper
    and lower case the same), and a second accumulator to count the
    total number of letters seen. Print both counts, then print the
    vowel percentage of total letters, rounded to 1 decimal place.

    Example:
    vowel_counter("Loops are powerful and fun") -> prints:
    Vowels: 9
    Total letters: 22
    Vowel percentage: 40.9%
    """
    # TODO: replace the line below with your solution
    pass


def login_attempt_validator(correct_pin, attempts):
    """
    Using a while loop, go through attempts one at a time (track your
    position with a counter you increment manually). Skip (using
    continue) any attempt that is not exactly 4 characters long, and
    do not count skipped attempts. Stop checking (using break) as soon
    as you find an attempt that matches correct_pin, and print
    "Access granted after N attempt(s)" where N is the number of
    attempts actually checked (not skipped). If the loop finishes with
    no match, print "Access denied".

    Example:
    login_attempt_validator("4821", ["12", "9034", "48213", "4821", "1111"])
    -> prints: Access granted after 2 attempt(s)
    """
    # TODO: replace the line below with your solution
    pass


def team_roster_report(names, numbers):
    """
    names and jersey numbers are given in matching order. Use zip()
    together with enumerate() to loop through both lists at once while
    tracking a row number starting at 1. Print each line as
    "ROW. NAME wears #NUMBER", then after the loop print the total
    number of players using len().

    Example:
    team_roster_report(["Ava", "Noah", "Mia", "Liam"], [7, 23, 15, 4])
    -> prints:
    1. Ava wears #7
    2. Noah wears #23
    3. Mia wears #15
    4. Liam wears #4
    Total players: 4
    """
    # TODO: replace the line below with your solution
    pass


def prime_finder(low, high):
    """
    Loop through the numbers low to high (inclusive) with a for loop.
    For each number, use a nested for loop that checks every possible
    divisor from 2 up to (but not including) the number itself; if a
    divisor divides it evenly, break out of the inner loop. Attach a
    for...else clause to the inner loop so its else block (which
    appends the number to a primes list) only runs when the inner loop
    completed without a break. Print the final primes list.

    Example:
    prime_finder(2, 30) -> prints:
    Primes from 2 to 30: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    """
    # TODO: replace the line below with your solution
    pass


def class_quiz_tracker(scores):
    """
    scores is a dictionary where each key is a student's name and each
    value is a list of that student's quiz scores. Loop over the
    dictionary with .items(), and for each student use a nested for
    loop with enumerate() (starting at 1) over their scores. Print the
    student's name, then print each quiz result indented as
    "  Quiz N: SCORE". While looping, add each score to a running
    total. If any score is below 60, print
    "  Attendance/quiz flag: early stop" immediately after that quiz
    line and break out of the inner loop for that student (skip
    printing their total/average). Otherwise, after all of a student's
    quizzes are printed, print their total and their average (rounded
    to 1 decimal place).

    Example:
    class_quiz_tracker({"Ava": [88, 92, 79], "Noah": [55, 90, 60]}) -> prints:
    Ava
      Quiz 1: 88
      Quiz 2: 92
      Quiz 3: 79
      Total: 259
      Average: 86.3
    Noah
      Quiz 1: 55
      Attendance/quiz flag: early stop
    """
    # TODO: replace the line below with your solution
    pass
