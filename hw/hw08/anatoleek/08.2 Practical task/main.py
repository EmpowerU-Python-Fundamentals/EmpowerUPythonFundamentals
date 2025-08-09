import re

def ok_pwd(password):
    """
    Check if the password is valid.
   
    """
    # lenght check
    if not (6 <= len(password) <= 16):
        return False
    # at least one uppercase
    if not re.search(r"[A-Z]", password):
        return False
    # at least one lowercase
    if not re.search(r"[a-z]", password):
        return False
    # at least one digit
    if not re.search(r"\d", password):
        return False
    # at least one special character
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False
    return True

pwd = input("Enter your password: ")

if ok_pwd(pwd):
    print("Password is valid.")
else:
    print("Password is invalid. Please try again.")
    