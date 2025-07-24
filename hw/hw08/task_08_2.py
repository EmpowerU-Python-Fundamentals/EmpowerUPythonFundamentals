import re

password=input("Password: ")

def pswrd():
    if not (6 <= len(password) <= 16):
        return "Пароль не надійний: довжига повинна бути від  6 до 16 символів"
    elif not re.search(r"[a-z]", password):
        return "Пароль не надійний: повинна бути хоча б одна літера маленька латинецею"
    elif not re.search(r"[A-Z]", password):
        return "Пароль не надійний: повинна бути хоча б одна велика літера латинецею"
    elif not re.search(r"\d", password):
        return "Пароль не надійний: повиненна бути хоча б одна цифра"
    elif not re.search(r"[@#(%$]", password):
        return "Пароль не надійний: повинен бути хоча б один спецсимвол"
    else:
        return "Пароль надійний"

print(pswrd())


