def get_day(num):
    days = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday"
    }
    if num in days:
        return days[num]
    else:
        return "Invalid number! Please enter 1-7."

try:
    number = int(input("Enter a number (1-7): "))
    print(get_day(number))
except ValueError:
    print("Invalid input! Please enter a number.")