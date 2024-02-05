from db import get_db, add_counter, increment_counter
from analyse import calculate_count
from counter import Counter
from datetime import datetime, timedelta

class TestCounter:

    def setup_method(self):
        self.db = get_db("test.db")
        add_counter(self.db, "test_counter", "daily")

        current_date = datetime.strptime("2023-01-06", "%Y-%m-%d")
        for _ in range(4 * 7):  # 4 weeks with 7 days each
            increment_counter(self.db, "test_counter", current_date.strftime("%Y-%m-%d"))
            current_date += timedelta(days=1)

    def test_counter(self):
        counter = Counter("test_counter_1", "test_description_1")
        counter.store(self.db)

        counter.increment()
        counter.add_event(self.db)
        counter.reset()
        counter.increment()

    def test_db_counter(self):
        data = get_counter_data(self.db, "test_counter")
        assert len(data) == 4   #Expected 4 records in the database for 'test_db_counter'

        count = calculate_count(self.db, "test_counter")
        assert count == 4 #"Expected count to be 4 for 'test_db_counter'."

    def test_multiple_habits(self):
        counter1 = Counter("habit1", "daily")
        counter2 = Counter("habit2", "weekly")

        counter1.store(self.db)
        counter2.store(self.db)

        counter1.increment()
        counter1.add_event(self.db)

        counter2.increment()
        counter2.add_event(self.db)

        count1 = calculate_count(self.db, "habit1")
        count2 = calculate_count(self.db, "habit2")

        assert count1 == 1
        assert count2 == 1

    def teardown_method(self):
        import os
        os.remove("test.db")
