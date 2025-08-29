class NegativeAgeError(Exception):
    def __init__(self, age):
        super().__init__(f"Неприпустимий вік: {age}. Вік не може бути від’ємним.")

def check_age(age_str):
    age = int(age_str)
    if age < 0:
        raise NegativeAgeError(age)
    if age % 2 == 0:
        return f"Вік {age} — парний."
    else:
        return f"Вік {age} — непарний."

try:
    user_input = input("Введи свій вік: ")
    result = check_age(user_input)
    print(result)
except ValueError:
    print("Помилка: введено нечислове значення.")
except NegativeAgeError as e:
    print(e)