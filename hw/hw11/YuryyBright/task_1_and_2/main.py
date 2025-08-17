from core import ProcessorManager

def main():
    manager = ProcessorManager()

    # Age input loop
    age_valid = False
    while not age_valid:
        try:
            age = input("Enter your age: ")
            age_result, age_valid = manager.process_age(age)
            print(f"Your age is {age_result}")
            # if not age_valid:
            #     print(f"Error: {age_result}. Please try again.")
        except KeyboardInterrupt:
            print("\nProgram terminated by user.")
            return
        except Exception as e:
            print(f"An unexpected error occurred: {e}. Please try again.")

    # Day input loop
    day_valid = False
    while not day_valid:
        try:
            day_num = input("Enter a number (1-7) for the day of the week: ")
            day_result, day_valid = manager.process_day(day_num)
            print(f"The day is {day_result}")
            # if not day_valid:
            #     print(f"Error: {day_result}. Please try again.")
        except KeyboardInterrupt:
            print("\nProgram terminated by user.")
            return
        except Exception as e:
            print(f"An unexpected error occurred: {e}. Please try again.")

if __name__ == "__main__":
    main()