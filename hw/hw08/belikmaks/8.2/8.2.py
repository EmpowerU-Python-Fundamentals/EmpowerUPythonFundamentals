def validate_password(password):
    if len(password) < 6 or len(password) > 16:
        return False

    has_lower = False
    has_upper = False
    has_digit = False
    has_special = False
    special_chars = "$#@"

    for char in password:
        if char.islower():
            has_lower = True
        elif char.isupper():
            has_upper = True
        elif char.isdigit():
            has_digit = True
        elif char in special_chars:
            has_special = True

    return has_lower and has_upper and has_digit and has_special


password = input("Enter password: ")

if validate_password(password):
    print("Valid password")
else:
    print("Invalid password")