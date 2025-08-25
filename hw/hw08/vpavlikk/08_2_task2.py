import re


def validate_password(password):
    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$#@])[A-Za-z\d$#@]{6,16}$"
    if re.fullmatch(pattern, password):
        return "Valid password"
    else:
        return "Invalid password"


user_input = input("Enter password: ")
print(validate_password(user_input))
