from counter import Counter
from db import get_db, add_counter, increment_counter, get_counter_date
from analyse import calculate_count
from datetime import date, datetime
import os


class TestCounter:

    def setup_method(self):
        self.db = get_db("test.db")
        add_counter(self.db, "test_counter", "daily")
        increment_counter(self.db, "test_counter", "2024-01-06")
        increment_counter(self.db, "test_counter", "2024-02-07")

        increment_counter(self.db, "test_counter", "2024-01-09")
        increment_counter(self.db, "test_counter", "2024-02-10")

    def test_counter(self):
        counter = Counter("test_counter_1", "daily")
        counter.store(self.db)

        counter.increment(self.db)
        counter.add_event(self.db)
        counter.reset()
        counter.increment(self.db)

        # Add assertions here if needed

    def test_db_counter(self):
        data = get_counter_date(self.db, "test_counter")
        assert len(data) == 4

        count = calculate_count(self.db, "test_counter")
        assert count == 4

    def test_multiple_habits(self):
        counter1 = Counter("habit1", "daily")
        counter2 = Counter("habit2", "weekly")

        counter1.store(self.db)
        counter2.store(self.db)

        counter1.increment(self.db)
        counter1.add_event(self.db)

        counter2.increment(self.db)
        counter2.add_event(self.db)

        count1 = calculate_count(self.db, "habit1")
        count2 = calculate_count(self.db, "habit2")

        assert count1 == 1
        assert count2 == 1

    def teardown_method(self):
        os.remove("test.db")
