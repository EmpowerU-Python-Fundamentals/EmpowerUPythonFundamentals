import re

def password_check(password):
    '''check the validity of a password'''

    if (6 <= len(password) <= 16 and
        re.search(r"[a-z]", password) and
        re.search(r"[A-Z]", password) and
        re.search(r"[0-9]", password) and
        re.search(r"[$#@]", password)):
        return True
    return False

password = input("Введіть пароль: ")
password_check(password)