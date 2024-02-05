import json
from datetime import date

def get_db(name="main.db"):
    """
       Retrieve the database from a JSON file or create a new one if not found.
       Args:
           name (str): The name of the database file.
       Returns:
           dict: The database as a dictionary.
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
    Save the given database dictionary to a JSON file.
    Args:
            db (dict): The database dictionary to be saved.
            name (str): The name of the database file.
    """
    with open(name, 'w') as file:
        json.dump(db, file)

def add_counter(db, name, period, creation_date):
    """
    Add a counter to the database.
    Args:
         db (dict): The database dictionary.
         name (str): The name of the counter.
         period (str): The period of the counter (e.g., "daily", "weekly").
         creation_date (str): The creation date of the counter.

        Note:
            The counter is added with an initial creation date.
    """

    counter = {"name": name, "period": period, "creation_date": creation_date}
    db["counter"].append(counter)
    save_db(db)

def increment_counter(db, name, event_date=None):
    """
    Increment a counter and record the event in the database.
    Args:
        db (dict): The database dictionary.
        name (str): The name of the counter.
        event_date (str, optional): The date of the event. Defaults to today.

    Note:
       If no event date is provided, the current date is used.
    """

    if not event_date:
        event_date = str(date.today())
    event = {"date": event_date, "counterName": name}
    db["tracker"].append(event)
    save_db(db)

def get_habits_by_period(db, period):
    """
    Retrieve a list of counters with the specified period from the database.
    Args:
            db (dict): The database dictionary.
            period (str): The period of the counters to retrieve.

    Returns:
         list: A list of counters with the specified period.
    """

    return [habit for habit in db["counter"] if habit["period"].lower() == period.lower()]

def get_counter_date(db, name):
    """
    Retrieve a list of events for a specific counter from the database.

    Args:
        db (dict): The database dictionary.
        name (str): The name of the counter.

    Returns:
          list: A list of events for the specified counter.
    """
    return [event for event in db["tracker"] if event["counterName"] == name]
