def check_age(age_input):
    try:
        age = int(age_input)
        if age < 0:
            raise ValueError("Вік не може бути від'ємним.")
        elif age % 2 == 0:
            return "Вік парний."
        else:
            return "Вік непарний."
    except ValueError as e:
        return f"Помилка: {e}"

def main():
    user_input = input("Будь ласка, введіть ваш вік: ")
    result = check_age(user_input)
    print(result)

if __name__ == "__main__":
    main()