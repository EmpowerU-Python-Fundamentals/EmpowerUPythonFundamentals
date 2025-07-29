import re

def validity_of_password(password):
    if len(password) < 6 and len(password) > 16:
        return False
    
    has_lower = len(re.findall(r'[a-z]', password)) > 0
    has_upper = len(re.findall(r'[A-Z]', password)) > 0
    has_digit = len(re.findall(r'[0-9]', password)) > 0
    has_special = len(re.findall(r'[$#@]', password)) > 0

    return has_lower and has_upper and has_digit and has_special


password = input("Enter a password: ")
if validity_of_password(password):
    print(f"'{password}' is a valid password!")
else:
    print(f"Your password is too easy")


    