import re

def check_password(password: str) -> bool:
    """
    Password validation rules:
    - at least one lowercase letter [a-z]
    - at least one uppercase letter [A-Z]
    - at least one digit [0-9]
    - at least one special character from [$#@]
    - length between 6 and 16 characters
    """
    if len(password) < 6 or len(password) > 16:
        return False
    if not re.search("[a-z]", password):
        return False
    if not re.search("[A-Z]", password):
        return False
    if not re.search("[0-9]", password):
        return False
    if not re.search("[$#@]", password):
        return False
    return True

if __name__ == "__main__":
    pwd = input("Enter a password to check: ")
    if check_password(pwd):
        print("Password is valid")
    else:
        print("Password is invalid")

