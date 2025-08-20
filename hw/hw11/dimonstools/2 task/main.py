def day_of_week(number):
    days = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday"
    }
    return days.get(number, None)

def main():
    user_input = input("Enter a number (1-7) for the day of the week: ")
    try:
        num_float = float(user_input)
        if not num_float.is_integer():
            print("Invalid input! Please enter an integer number.")
            return
        num = int(num_float)
        day = day_of_week(num)
        if day:
            print(f"The day of the week for number {num} is {day}.")
        else:
            print("Invalid number! Please enter a number from 1 to 7.")
    except ValueError:
        print("Invalid input! Please enter a numeric value.")


if __name__ == "__main__":
    main()