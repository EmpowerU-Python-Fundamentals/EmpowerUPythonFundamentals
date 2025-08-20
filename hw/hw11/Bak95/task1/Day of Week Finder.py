def get_day_of_week(number):

    days = {
        1: "Понеділок",
        2: "Вівторок",
        3: "Середа",
        4: "Четвер",
        5: "П'ятниця",
        6: "Субота",
        7: "Неділя"
    }

    if number in days:
        return f"Число {number} відповідає дню: {days[number]}"
    else:
        return f"Число {number} не відповідає жодному дню тижня (введіть число від 1 до 7)"


def main():

    print("Програма для визначення дня тижня")
    print("1 - Понеділок, 2 - Вівторок, ..., 7 - Неділя")
    print("-" * 50)

    while True:
        try:
            # Отримання числа від користувача
            user_input = input("Введіть число (або 'exit' для виходу): ")

            if user_input.lower() == 'exit':
                print("До побачення!")
                break

            # Перетворення в ціле число
            number = int(user_input)

            # Виклик функції для визначення дня
            result = get_day_of_week(number)
            print(result)
            print()

        except ValueError:
            print("Помилка: Введіть коректне число або 'exit' для виходу!")
            print()
        except Exception as e:
            print(f"Несподівана помилка: {e}")
            print()


if __name__ == "__main__":
    main()