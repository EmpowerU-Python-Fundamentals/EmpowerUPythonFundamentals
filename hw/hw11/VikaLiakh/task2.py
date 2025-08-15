days_of_week = {
    1: "Monday", 2: "Tuesday", 3: "Wednesday",
    4: "Thursday", 5: "Friday", 6: "Saturday", 7: "Sunday"
}

try:
    day = int(input("Enter number of day: "))
    day_name = days_of_week.get(day)
    if day_name is None:
        raise KeyError(f"There is no day with number {day}")
    print(f"Day with number {day} is {day_name}")
except KeyError as e:
    print(e)
except ValueError:
    print("Invalid input")

    