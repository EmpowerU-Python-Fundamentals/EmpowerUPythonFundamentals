import re

def password_validity(password):
    if 6 <= len(password) <= 16 and re.search(r"[a-z]", password) and re.search(r"[A-Z]", password) and\
            re.search(r"[0-9]", password) and re.search(r"[$#@]", password):
        print("Password is valid!")
    else:
        print("Your password is incorrect")

password_validity(input("Your password: "))