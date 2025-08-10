def week_day(num):
    if num > 0 and num < 8:
        weekdays = [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday",
        ]
        return print(f"{weekdays[num-1]}")
    else:
        raise ValueError("invalid number")


try:
    user_num = int(input("Write your number: "))
    week_day(user_num)
except ValueError as e:
    print(f"Error: {e}")
