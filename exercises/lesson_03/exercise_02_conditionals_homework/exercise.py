def field_trip_eligibility(permission_slip, balance_due, behavior_points, special_override):
    """
    1. Print "Eligible for the trip!" or "Not eligible yet." based on
       permission_slip and balance_due == 0 and behavior_points >= 5
       (combined with `and`).
    2. Print the same message again, but this time combine those three
       conditions with special_override using and/or (parenthesize the
       three normal requirements so the override can bypass all of
       them at once).
    """
    # TODO: replace the line below with your solution
    pass


def truthy_falsy_report(values):
    """
    For each value in values, use a plain `if value:` to print
    f"{repr(value)} -> Truthy" or f"{repr(value)} -> Falsy".
    """
    # TODO: replace the line below with your solution
    pass


def if_else_and_ternary(num, x, y, age):
    """
    Using ordinary if/else, compute label ("even"/"odd" based on num),
    bigger (larger of x, y), and status ("adult"/"minor" based on age,
   18 cutoff). Then recompute the same three using ternary
    expressions as label2, bigger2, status2. Finally, print
    label == label2, bigger == bigger2, status == status2 as one
    print() call with three arguments.
    """
    # TODO: replace the line below with your solution
    pass


def graded_with_boost(score, extra_credit_completed):
    """
    Compute base_grade using chained comparisons/elif (same bands as
    classify_grade). Compute boosted: True only if base_grade == "B"
    and score >= 87, and extra_credit_completed is True. Print
    "Base grade: {base_grade}" and "Boosted: {boosted}".
    """
    # TODO: replace the line below with your solution
    pass


def ticket_price(age, is_student, day, membership):
    """
    base_price = 12.00.

    Rule A: if age < 13 or age >= 65, price = base_price * 0.5.
    Rule B (elif): otherwise if is_student, price = base_price * 0.75.
    Rule C (else): otherwise, price = base_price.
    Rule D: separately, if day in ["Tuesday", "Wednesday"], apply
      price = price * 0.8, regardless of which rule above applied.
    Rule E: membership_label = "VIP" if membership == "gold" or
      membership == "platinum" else "Standard" (ternary).

    Print "Final price: ${price:.2f}" then
    "Membership: {membership_label}".
    """
    # TODO: replace the line below with your solution
    pass
