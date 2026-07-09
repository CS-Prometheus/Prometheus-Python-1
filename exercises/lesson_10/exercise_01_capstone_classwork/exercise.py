import json


def build_task_list(names, priorities):
    """
    names and priorities are parallel lists (same length). For each
    pair, build a task dict {"name": n, "priority": p}, then return a
    list of formatted strings "<priority> priority: <name>" for each
    task, in order.

    Example:
    build_task_list(["Buy groceries"], ["High"])
    -> returns: ["High priority: Buy groceries"]
    """
    # TODO: replace the line below with your solution
    pass


def save_and_load_snacks(path, snacks):
    """
    snacks is a list of dicts like
    {"name": "Pretzels", "calories": 110}. Write snacks to the file at
    path using json.dump() with indent=2. Then read the file back in
    using json.load() and return a list containing just the "name"
    field of each loaded record, in order.

    Example:
    save_and_load_snacks(path, [{"name": "Apple", "calories": 95}])
    -> returns: ["Apple"]
    """
    # TODO: replace the line below with your solution
    pass


def get_price(prices, item):
    """
    prices is a dict mapping item names to prices. Return prices[item]
    if item is a key in prices. If item is missing, return None
    instead of crashing. (The original version of this function
    incorrectly caught IndexError instead of KeyError, so a missing
    item crashed the program - fix that bug here.)

    Example:
    get_price({"apple": 1.50}, "apple") -> returns: 1.50
    get_price({"apple": 1.50}, "bread") -> returns: None
    """
    # TODO: replace the line below with your solution
    pass
