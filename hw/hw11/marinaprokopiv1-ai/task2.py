def get_day_of_week(num):
    days = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday"
    }
    if num not in days:
        raise ValueError("Invalid day number")
    return days[num]

try:
    number = int(input("Enter a number (1-7): "))
    print(get_day_of_week(number))
except ValueError as e:
    print(f"Error: {e}")
