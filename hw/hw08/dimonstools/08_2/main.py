import re

def is_valid_password(password):
    if re.search(r"^.{6,16}$", password):
        return True
    if re.search(r"[a-z]", password):
        return True
    if re.search(r"[A-Z]", password):
        return True
    if re.search(r"[0-9]", password):
        return True
    if re.search(r"[$#@]", password):
        return True
    return False

# Main program
password = input("Enter your password: ")

if is_valid_password(password):
    print("Password is valid.")
else:
    print("Password is invalid.")