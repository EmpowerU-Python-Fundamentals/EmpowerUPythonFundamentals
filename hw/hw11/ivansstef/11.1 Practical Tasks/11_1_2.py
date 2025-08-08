def get_day(number):
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
        raise ValueError("Number must be between 1 and 7")
    return days[number]

try:
    num = int(input("Enter number of day (1-7): "))
    print(get_day(num))
except ValueError as e:
    print("Error:", e)
