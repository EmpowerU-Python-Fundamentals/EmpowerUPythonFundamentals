import re

def valid_password(password):
    if len(password) < 6 or len(password) > 16:
        return False
    if not re.search(r"[a-z]", password):
        return False
    if not re.search(r"[A-Z]", password):
        return False
    if not re.search(r"[$#@]", password):
        return False
    return True

password = input("Please enter your password")

if valid_password(password):
    print("Valid password")
else:
    print("Invalid password")

    