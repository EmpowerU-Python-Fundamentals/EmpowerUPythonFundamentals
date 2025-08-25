def check_age(age):
    """
    Перевіряє вік на парність/непарність і викидає виняток для від'ємних чисел.
    """
    if age < 0:
        raise ValueError("Вік не може бути від'ємним.")
    
    if age % 2 == 0:
        print(f"Ваш вік ({age}) — парне число.")
    else:
        print(f"Ваш вік ({age}) — непарне число.")

try:
    user_age_str = input("Будь ласка, введіть ваш вік: ")
    user_age = int(user_age_str)
    check_age(user_age)

except ValueError as e:
    print(f"Помилка: {e}")