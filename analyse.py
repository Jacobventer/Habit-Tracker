from db import get_counter_date

def calculate_count(db, counter):
    """
    Calculate the count of the counter without breaking the streak.

    :param db: An initialized sqlite database connection
    :param counter: Name of the counter present in the DB
    :return: Length of the counter increment events without breaking the streak
    """
    events = get_counter_date(db, counter)
    streak_count = 0

    for i, event in enumerate(events):
        if i == 0 or (i > 0 and events[i]["date"] == events[i - 1]["date"]):
            streak_count += 1

    return streak_count
