DAYS = {
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday",
    7: "Sunday"
}

def get_day_name(day):
    try:
        day_number = int(day)
        if 1 <= day_number <= 7:
            print(f"The day of the week is: {DAYS.get(day_number)}")
        else:
            print(f"Number {day_number} does not correspond to a day of the week (must be between 1 and 7).")
    except ValueError:
        print("Error: You must enter a numeric value between 1 and 7.")

day = input("Enter a number (1–7) to get the day of the week: ")
get_day_name(day)
