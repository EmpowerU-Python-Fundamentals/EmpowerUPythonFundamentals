import re

def valid_password(password):

    if len(password) < 6 or len(password) > 16:
        print("Invalid input. Password length must be between 6 and 16 characters.")
        return False
    if not re.search(r"[a-z]", password):
        print("Invalid input. Password must contain at least one letter from the range [a-z]")
        return False
    if not re.search(r"[A-Z]", password):
        print("Invalid input. Password must contain at least one letter from the range [A-Z]")
        return False
    if not re.search(r"[$,#,@]", password):
        print("Invalid input. Password must contain at least one of the characters [$,#,@]")
        return False
    return True


user_password = input('Enter you password:  ')

while not valid_password(user_password):
    user_password = input('Please, enter correct password:  ')

print("Successfully!")
