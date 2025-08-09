def get_weekday(number):
    """
    Returns weekday based on number with input validation
    """
    weekdays = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday"
    }

    if number < 1:
        return "Number must be at least 1"
    elif number > 7:
        return "There are only 7 days in a week"
    else:
        return weekdays[number]


def main():
    try:
        day_number = int(input("Enter a number (1-7) to get the weekday: "))
        print(get_weekday(day_number))
    except ValueError:
        print("Please enter a valid integer.")


if __name__ == "__main__":
    main()