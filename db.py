import json
from datetime import date

def get_db(name="main.db"):
    """
    Get the database.
    :param name: Name of the database file.
    :return: The database.
    """
    try:
        with open(name, 'r') as file:
            db = json.load(file)
    except FileNotFoundError:
        db = {"counter": [], "tracker": []}
        save_db(db, name)

    return db

def save_db(db, name="main.json"):
    """
    Save the database.
    :param db: The database to be saved.
    :param name: Name of the database file.
    """
    with open(name, 'w') as file:
        json.dump(db, file)

def add_counter(db, name, period, creation_date):
    counter = {"name": name, "period": period, "creation_date": creation_date}
    db["counter"].append(counter)
    save_db(db)

def increment_counter(db, name, event_date=None):
    if not event_date:
        event_date = str(date.today())
    event = {"date": event_date, "counterName": name}
    db["tracker"].append(event)
    save_db(db)

def get_habits_by_period(db, period):
    return [habit for habit in db["counter"] if habit["period"].lower() == period.lower()]

def get_counter_date(db, name):
    return [event for event in db["tracker"] if event["counterName"] == name]
