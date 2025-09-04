def process_age(age):
    """
    Аналізує вік і повертає, чи є він парним, чи непарним.
    Генерує виняток, якщо вік від'ємний.
    """

    if age < 0 or age > 130:
        raise ValueError("Вік повинен бути між 0 та 120 роками.")
    elif age % 2 == 0:
        return f"Ваш вік ({age}) — парне число."
    else:
        return f"Ваш вік ({age}) — непарне число."

while True:
    try:
        user_age = int(input("Будь ласка, введіть свій вік: "))
        result = process_age(user_age)
        print(result)
        break 
    except ValueError as e:
        print(f"Помилка: {e}")
