import re

user_password = input("Enter your password: ")

def password_checker(password):
    if len(user_password) < 6 or len(user_password) > 16:
        return "The password must contain between 6 and 16 characters."
    elif not re.search("[a-z]", user_password):
        return "The password must contain at least one small letter"
    elif not re.search("[A-Z]", user_password):
        return "The password must contain at least one big letter"
    elif not re.search("\d", user_password):
        return "The password must contain at least one digit"
    elif not re.search("[$#@]", user_password):
        return "The password must contain at least one symbol"
    else:
        return "The password is checked successfully!"

print(password_checker(user_password))