def get_day_of_week(number):
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
        num = int(input("Enter a number (1-7): "))
        day = get_day_of_week(num)
        print(f"The day is {day}.")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
