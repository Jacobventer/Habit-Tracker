import questionary
from db import get_db, get_habits_by_period
from counter import Counter
from analyse import calculate_count
from datetime import date

def cli():
    db = get_db()
    print("Welcome to Habit Tracker. Lets begin? Press one of the arrows to initiate the optons:")

    habits = [] # List to strore 5 habtis

    stop = False
    while not stop:
        choice = questionary.select("Select one of the following options:", choices = ["Create", "Check off", "Analyse", "Exit"]).ask()
        print(choice)

        if choice == "Create":
            create_choices = ["Running", "Gym", "Floss", "Read", "Journal", "Back"]
            habit_name = questionary.select("Choose one of the following Habits:", choices=create_choices).ask()

            if habit_name == "Back":
                continue  # Go back to the main menu
            print(f"{habit_name} has been added")
            # User choose between daily and weekly period
            period_choices = ["Daily", "Weekly", "Back"]
            period = questionary.select("What is the period of your Habit?",choices=period_choices).ask()
            print(f"You have added {habit_name} as a {period} habit")

            if period != "Back":
                counter = Counter(habit_name, period)
                counter.store(db)
                habits.append(counter)

        elif choice == "Check off":
            while True:
                habit_names = [habit.name for habit in habits]
                habit_names.append("Back")  # option to go back to the main menu
                name = questionary.select("Which Habit do you want to check off?", choices=habit_names).ask()

                if name == "Back":
                    break  # Break out of the loop to go back to the main menu

                habit_to_check_off = next((habit for habit in habits if habit.name == name), None)

                if habit_to_check_off:
                    habit_to_check_off.increment(db)
                    habit_to_check_off.add_event(db)
                    print(f"{habit_to_check_off.name} has been checked off.")
                    break

        elif choice == "Analyse":
            def list_habits_by_period(db, selected_period):
                habits = get_habits_by_period(db, selected_period)
                if not habits:
                    print(f"No habits found with {selected_period} period.")

                else:
                    print(f"List of habits with {selected_period} period:")
                    for habit in habits:
                        name = habit.get('name', 'N/A')
                        create_date = habit.get('create_date', 'N/A')
                        print(f"{name} - Created on: {create_date}")
                    # Additional menu for daily and weekly options

                    if selected_period != "Back":
                        period_menu_choices = ["Daily", "Weekly", "Back"]
                        period_menu_choice = questionary.select("Choose the period:", choices=period_menu_choices).ask()
                        if period_menu_choice == "Daily":
                            list_habits_by_period(db, "daily")
                        elif period_menu_choice == "Weekly":
                            list_habits_by_period(db, "weekly")
                        elif period_menu_choice == "Back":
                            return  # Return to exit the function and go back to the main menu
                        else:
                            pass  # Handle any additional options or logic you need

            while True:
                analyse_choices = ["List all Habits", "List Habits with the same period", "Longest streak of all Habits",
                                   "Longest streak of a specific Habit", "Back"]

                analyse = questionary.select("Choose one of the following Habits:", choices=analyse_choices).ask()
                if analyse == "List all Habits":
                    print("List of all habits:")
                    for habit in habits:
                        print(f"{habit.name} {habit.period.capitalize()} - Created on: {habit.create_date}")


                elif analyse == "List Habits with the same period":
                    selected_period = questionary.select("Choose the period:", choices=["Daily", "Weekly", "Back"]).ask()
                    if selected_period == "Daily":
                        list_habits_by_period(db, "daily")
                    elif selected_period == "Weekly":
                        list_habits_by_period(db, "weekly")
                    elif selected_period == "Back":
                        break  # Break out of the loop to go back to the main menu
                    else:
                        pass  # Handle any additional options or logic you need

                elif analyse == "Longest streak of all Habits":
                    period_choices = ["Daily", "Weekly", "Back"]
                    selected_period = questionary.select("Choose the period:", choices=period_choices).ask()
                    if selected_period == "Back":
                        break  # Break out of the loop to go back to the main menu

                    longest_streak = 0
                    longest_habits = []
                    # Separate habits based on the selected period

                    period_habits = [habit for habit in habits if habit.period.lower() == selected_period.lower()]
                    for habit in period_habits:
                        if habit.daily_habit_streak > longest_streak:
                            longest_streak = habit.daily_habit_streak
                            longest_habits = [habit.name]

                        elif habit.daily_habit_streak == longest_streak:
                            longest_habits.append(habit.name)

                    if longest_streak == 0:
                        print(f"No {selected_period.lower()} habits with streaks found.")

                    elif not longest_habits:
                        print(f"Error: No {selected_period.lower()} habits found.")

                    elif len(longest_habits) == 1:
                        print(f"Your longest streak of all {selected_period.lower()} habits is: '{longest_habits[0]}' and your current streak is: {longest_streak}")
                    else:
                        habits_str = " and ".join(f"'{habit}'" for habit in longest_habits)
                        print(f"{habits_str} are on an equal {selected_period.lower()} streak of {longest_streak} habits.")

                elif analyse == "Longest streak of a specific Habit":
                    habit_to_analyse_choices = ["Running", "Gym", "Floss", "Read", "Journal", "Back"]
                    habit_name_to_check = questionary.select("Which habit's longest streak do you want to see?:",choices=habit_to_analyse_choices).ask()

                    if habit_name_to_check == "Back":
                        break  # Break out of the loop to go back to the main menu

                    habit_to_check = next((habit for habit in habits if habit.name == habit_name_to_check), None)

                    if habit_to_check:
                        streak_count = calculate_count(db, habit_name_to_check)
                        print(f"Longest streak for {habit_name_to_check}: {streak_count}")

                    else:
                        print(f"No habit found with the name {habit_name_to_check}")

                elif analyse == "Back":
                    break  # Break out of the loop to go back to the main menu

        else:
            print("Goodbye!")
            stop = True

if __name__ == "__main__":
    cli()
