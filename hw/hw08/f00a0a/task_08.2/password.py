import re

def validate_password(password):
    """validate_password"""
    errors = []

    if len(password) < 6:
        errors.append("Password is too short (less than 6 characters)")
    elif len(password) > 16:
        errors.append("Password is too long (more than 16 characters)")

    if not re.search("[a-z]", password):
        errors.append("No lowercase letter (a-z)")

    if not re.search("[A-Z]", password):
        errors.append("No capital letter (A-Z)")

    if not re.search("[0-9]", password):
        errors.append("No number (0-9)")

    if not re.search("[$#@]", password):
        errors.append("No special character ($, # or @)")

    return errors  


while True:
    user_password = input("Enter password: ")

    issues = validate_password(user_password)

    if not issues:
        print("The password is valid!")
        break 
    else:
        print("The password is not valid. Reasons:")
        for err in issues:
            print(" -", err)
        print("Try again.\n")