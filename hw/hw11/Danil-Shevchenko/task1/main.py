def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative!")
    if age % 2 == 0:
        return "The age is even."
    else:
        return "The age is odd."

try:
    user_input = input("Enter your age: ")
    age = int(user_input)  # обработка ошибок преобразования
    print(check_age(age))
except ValueError as e:
    print("Error:", e)
