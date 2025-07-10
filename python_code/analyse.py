from db import get_counter_date

def calculate_count(db, counter):
    # Retrieve events for the given counter from the database
    events = get_counter_date(db, counter)

    # Initial streak count
    streak_count = 0

    # Loop through events to calculate streak count
    for i, event in enumerate(events):
        # Check if it's the first event or if the date is the same as the previous event
        if i == 0 or (i > 0 and events[i]["date"] == events[i - 1]["date"]):
            streak_count += 1

    # Return the calculated streak count
    return streak_count

