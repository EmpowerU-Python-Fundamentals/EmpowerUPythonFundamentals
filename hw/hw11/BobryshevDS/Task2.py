class InvalidDayError(Exception):
    def __init__(self, value):
        super().__init__(f"Немає дня тижня для числа: {value}")

def get_day_of_week(value):
    days = {
        1: "Понеділок",
        2: "Вівторок",
        3: "Середа",
        4: "Четвер",
        5: "П’ятниця",
        6: "Субота",
        7: "Неділя"
    }
    number = int(value)
    if number not in days:
        raise InvalidDayError(number)
    return days[number]

try:
    user_input = input("Введи число від 1 до 7, щоб дізнатися день тижня: ")
    day = get_day_of_week(user_input)
    print(f"Це — {day}.")
except ValueError:
    print("Помилка: введено нечислове значення.")
except InvalidDayError as e:
    print(e)
