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
    if number in days:
        return days[number]
    else:
        raise ValueError("Invalid number! Enter a number from 1 to 7.")

try:
    user_input = input("Enter a number (1-7): ")
    number = int(user_input)  # обработка ошибок преобразования
    print(get_day_of_week(number))
except ValueError as e:
    print("Error:", e)
