import re

password = input("Enter password: ")

def check_password(password):
    if re.search(r'[a-z]', password) and re.search(r'[A-Z]', password) and re.search(r'[$#@]', password) and re.search(r'\d', password) \
            and 6 <= len(password) <= 16:
        print("Пароль валідний!")
    else:
        print("Пароль не валідний!")

check_password(password)