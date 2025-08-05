import re

def validate_password(pass_func):
    def wrapper(pass_wrd):
        if not re.match(r"^(?=.*\d)(?=.*[A-Za-z])(?=.*[$#@]).{3,16}$", pass_wrd):
            raise ValueError("Invalid password")
        return pass_func(pass_wrd)
    return wrapper