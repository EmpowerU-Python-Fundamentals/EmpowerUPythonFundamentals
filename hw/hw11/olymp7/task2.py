def get_day_of_week(day_number_input):
    try:
        day_number = int(day_number_input)
        if 1 <= day_number <= 7:
            days = {
                1: "Понеділок",
                2: "Вівторок",
                3: "Середа",
                4: "Четвер",
                5: "П'ятниця",
                6: "Субота",
                7: "Неділя"
            }
            return f"Число {day_number} відповідає дню: {days[day_number]}"
        else:
            return "Ви ввели число, яке не відповідає жодному дню тижня (має бути від 1 до 7)."
    except ValueError:
        return "Помилка: Ви ввели нечислові дані. Будь ласка, введіть число."

def main():
    user_input = input("Будь ласка, введіть число від 1 до 7: ")
    result = get_day_of_week(user_input)
    print(result)

if __name__ == "__main__":
    main()