def get_day_of_week(day_number):
    """
    Повертає назву дня тижня за його номером.
    """
    days = {
        1: "Понеділок",
        2: "Вівторок",
        3: "Середа",
        4: "Четвер",
        5: "П'ятниця",
        6: "Субота",
        7: "Неділя"
    }

    if day_number in days:
        print(f"День тижня, що відповідає числу {day_number}, — це {days[day_number]}.")
    else:
        print("Введене число не відповідає жодному дню тижня (має бути від 1 до 7).")

# Основний блок коду
try:
    user_input = input("Будь ласка, введіть число від 1 до 7: ")
    day_number = int(user_input)
    get_day_of_week(day_number)
except ValueError:
    print("Помилка: Ви ввели нечислове значення. Будь ласка, введіть ціле число.")