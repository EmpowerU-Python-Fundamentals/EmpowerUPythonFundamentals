def get_day(number):
    weekdays = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday"
    }
    return weekdays.get(number)


def main():
    user_input = input("Please enter a number between 1 and 7 to get the corresponding weekday: ")
    try:
        value = float(user_input)
        if not value.is_integer():
            print("Only whole numbers are allowed.")
            return
        day_number = int(value)
        day_name = get_day(day_number)
        if day_name:
            print(f"Number {day_number} corresponds to {day_name}.")
        else:
            print("Number out of range! Enter a value from 1 to 7.")
    except ValueError:
        print("Invalid entry! Please type a numeric value.")


if __name__ == "__main__":
    main()
