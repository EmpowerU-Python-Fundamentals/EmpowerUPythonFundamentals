import re


def is_valid(password):
    """This function checks validity of a password"""

    if len(password) < 6 or len(password) > 16:     # Перевірка довжини
        return False

    patterns = [        # Регулярні вирази для перевірки умов:
        r"[a-z]",       # хоча б одна маленька літера
        r"[A-Z]",       # хоча б одна велика літера
        r"[0-9]",       # хоча б одна цифра
        r"[$#@]"        # хоча б один спецсимвол
    ]

    return all(re.search(p, password) for p in patterns)


password = input("Enter your password: ")
if is_valid(password):
    print("Valid password.")
else:
    print("!! Invalid password !!")
