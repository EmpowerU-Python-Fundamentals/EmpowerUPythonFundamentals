import re

def password_validation(password):
    if len(password) < 6 or len(password) > 16:
        return False
    if not re.search(r"[a-z]", password):
        return False
    if not re.search(r"[A-Z]", password):
        return False
    if not re.search(r"[$,#,@]", password):
        return False
    if not re.search(r"[0-9]", password):
        return False
    return True

user_password = input('Enter your password:  ')

if password_validation(user_password):
    print(f"Valid - {user_password}")  
else:
    while not password_validation(user_password):
        print(f"Not valid - {user_password}")
        user_password = input('Enter your password:  ')
    print(f"Valid - {user_password}")
