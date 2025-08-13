import re


def password_validation(password):
    if re.match(r'^(?=.*\d)(?=.*[A-Z])(?=.*[a-z])(?=.*[$#@]).{8,16}$', password):
        print("Password is valid!")
    else:
        print("Password is no valid!")





if __name__ == "__main__":
    password = input("Type password to validate: ")
    password_validation(password)