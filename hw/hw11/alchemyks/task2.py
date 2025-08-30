from calendar import day_name

class WeekdayError(Exception):
    def __init__(self, message="Invalid weekday"):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return self.message


def check_weekday(day):
    if day < 1 or day > 7:
        raise WeekdayError("Invalid weekday. Please enter a number between 1 and 7.")
    return f"Day {day} is {day_name[day - 1]}."


def main():
    try:
        day = int(input("Enter a weekday (1-7): "))
        result = check_weekday(day)
        print(result)
    except ValueError as e:
        print("Error: Please enter a valid integer number for the weekday.")
    except WeekdayError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()