import re

def validate_password(password):
    if len(password) < 6 or len(password) > 16:
        return False
    
    if not re.search(r'[a-z]', password):
        return False
    
    if not re.search(r'[A-Z]', password):
        return False
    
    if not re.search(r'[0-9]', password):
        return False
    
    if not re.search(r'[$#@]', password):
        return False
    
    return True


user_password = input("Введіть пароль: ")

# Проверка и вывод результата
if validate_password(user_password):
    print("Пароль прийнято.")
else:
    print("Пароль не відповідаю умові!")
