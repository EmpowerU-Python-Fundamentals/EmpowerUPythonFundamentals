def check_age(age):

    if age < 0:
        raise ValueError("Вік не може бути від'ємним числом!")

    if age % 2 == 0:
        return f"Вік {age} - парне число"
    else:
        return f"Вік {age} - непарне число"


def main():

    print("Програма для перевірки віку на парність/непарність")
    print("-" * 50)

    while True:
        try:
            # Отримання віку від користувача
            age_input = input("Введіть ваш вік (або 'exit' для виходу): ")

            if age_input.lower() == 'exit':
                print("До побачення!")
                break

            # Перетворення в ціле число
            age = int(age_input)

            # Виклик функції для обробки віку
            result = check_age(age)
            print(result)
            print()

        except ValueError as e:
            if "invalid literal" in str(e):
                print("Помилка: Введіть коректне число!")
            else:
                print(f"Помилка: {e}")
            print()
        except Exception as e:
            print(f"Несподівана помилка: {e}")
            print()


if __name__ == "__main__":
    main()