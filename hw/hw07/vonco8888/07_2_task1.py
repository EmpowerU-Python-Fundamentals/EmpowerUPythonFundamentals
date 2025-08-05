def greet(name):
    """
    Повертає привітання для користувача.
    Якщо ім'я — 'Johnny', повертає особливе привітання.

    Аргументи:
    name (str): ім'я користувача

    Повертає:
    str: рядок привітання
    """
    if name == "Johnny":
        return "Hello, my love!"
    else:
        return f"Hello, {name}!"
