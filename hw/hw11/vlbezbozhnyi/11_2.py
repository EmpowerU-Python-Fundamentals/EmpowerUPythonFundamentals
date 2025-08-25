WEEKDAYS = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
]


def number_to_dayweek():
    """Convert a number to the corresponding day of the week."""
    number = input("Enter a number: ").strip()
    try:
        day_index = int(number) - 1
        if 0 <= day_index < len(WEEKDAYS):
            return f"{number} is {WEEKDAYS[day_index]}"
        return ValueError("Number must be between 1 and 7")
    except (ValueError, TypeError):
        return ValueError("Input must be a valid number")


print(number_to_dayweek())
