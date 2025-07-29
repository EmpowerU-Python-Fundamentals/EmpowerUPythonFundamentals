import re
import pwinput

def check_password(password):
    # Check password length
    if len(password) < 6 or len(password) > 16:
        return False

    # Check for at least one lowercase letter
    if not re.search(r'[a-z]', password):
        return False

    # Check for at least one uppercase letter
    if not re.search(r'[A-Z]', password):
        return False

    # Check for at least one digit
    if not re.search(r'[0-9]', password):
        return False

    # Check for at least one special character ($, #, @)
    if not re.search(r'[$#@]', password):
        return False

    return True

if __name__=='__main__':
    # Get user password and mask it with asterisks
    password = pwinput.pwinput(prompt="Enter your password: ", mask='*')
    if check_password(password):
        print("Valid password")
    else:
        print("Invalid password")
