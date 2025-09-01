def get_day_of_week(number: int) -> str:
    """
    Returns the day of the week for a number 1–7.
    Raises ValueError for numbers outside this range.
    """
    days = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday"
    }
    if number not in days:
        raise ValueError("Invalid number! Please enter a number between 1 and 7.")
    return days[number]


def main():
    try:
        user_input = input("Enter a number day (1–7): ")
        number = int(user_input)
        day = get_day_of_week(number)
        print(f"{number} corresponds to {day}.")
    except ValueError as e:
        print("Error:", e)


if __name__ == "__main__":
    main()