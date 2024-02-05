from db import add_counter, increment_counter, get_counter_date
from datetime import date as dt_date, datetime

class Counter:
    def __init__(self, name: str, period: str):
        """
        Initialize a new habit counter.
        :param name: Name of the habit.
        :param period: Period of the habit (e.g., "daily" or "weekly").
        """
        self.name = name
        self.period = period
        self.count = 0
        self.create_date = str(dt_date.today())  # Storing the date when the habit is created
        self.daily_habit_streak = 0  # Add a daily streak attribute
        self.weekly_habit_streak = 0  # Add a weekly streak attribute

    def check_consistency(self, db):
        """
        Check the consistency of habit streaks based on the period (daily or weekly).
        :param db: The database to retrieve habit events.
        """
        events = get_counter_date(db, self.name)

        if self.period.lower() == "daily":
            current_date = datetime.today().date()
            last_checked_date = datetime.strptime(events[-1]["date"], "%Y-%m-%d").date() if events else None

            # Check if the habit has been checked off today
            if last_checked_date != current_date:
                self.reset_daily_streak()

        elif self.period.lower() == "weekly":
            current_date = datetime.today().date()
            last_checked_date = datetime.strptime(events[-1]["date"], "%Y-%m-%d").date() if events else None

            # Check if the habit has been checked off this week
            if last_checked_date and (current_date - last_checked_date).days > 7:
                self.reset_weekly_streak()

    def increment(self, db):
        """
        Increment the habit counter and update streaks.
        :param db: The database to check consistency and update the habit.
        """
        self.count += 1
        self.check_consistency(db)
        self.daily_habit_streak += 1  # Increment the daily streak
        self.weekly_habit_streak += 1  # Increment the weekly streak

    def reset_daily_streak(self): #Reset daily to 0
        self.daily_habit_streak = 0

    def reset_weekly_streak(self): #Reset weekly to 0
        self.weekly_habit_streak = 0

    def __str__(self):
        return f"{self.name}: {self.count}"

    def store(self, db): #Store data in database
        add_counter(db, self.name, self.period, self.create_date)

    def add_event(self, db, date: str = None):
        """
        Add a habit-checking event to the database and update streaks.
        :param db: The database to add the event and update the habit.
        :param date: The date of the event (defaults to today).
        """

        if not date:
            date = str(dt_date.today())
        else:
            # Convert date string to datetime object for comparison
            event_date = datetime.strptime(date, "%Y-%m-%d")
            current_date = datetime.today()

            # Check if the event is for the current day/week
            if self.period.lower() == "daily" and event_date.date() != current_date.date():
                return
            elif self.period.lower() == "weekly" and (current_date - event_date).days > 7:
                return

            # Check for consistency before incrementing streaks
            self.check_consistency(db)

        # Increment streaks only if the checks pass
        self.increment(db)
