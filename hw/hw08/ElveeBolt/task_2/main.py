import re

def password_validator(password):
    length = len(password)
    if not 6 <= length <= 16:
        return False

    if not re.search(r"[a-z]", password):
        return False
    if not re.search(r"[A-Z]", password):
        return False
    if not re.search(r"[0-9]", password):
        return False
    if not re.search(r"[$#@]", password):
        return False

    return True

user_password = input("Enter password: ")

if password_validator(user_password):
    print(f"Good password - {user_password}!")
else:
    print(f"Bad password - {user_password}!")