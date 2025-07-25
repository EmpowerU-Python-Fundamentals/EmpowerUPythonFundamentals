def is_password_valid(password):
    """
    Checks the validity of a password according to the specified criteria:

    - At least 1 lowercase letter [a-z]
    - At least 1 uppercase letter [A-Z]
    - At least 1 digit [0-9]
    - At least 1 special character from [$#@]
    - Minimum length 6 characters
    - Maximum length 16 characters
    """
    
    def check_char(password, start_range, end_range):
        """
        Сheck for at least one character of password in the range
        """
  
        has_char = False
        for char in password:
            if start_range <= char <= end_range:
                has_char = True
                break
        return has_char


    # Check password length
    if not (6 <= len(password) <= 16):
        print("Password must be between 6 and 16 characters long.")
        return False

    # Check for at least one lowercase letter
    if not check_char(password, 'a', 'z'):
        print("Password must contain at least one lowercase letter (a-z).")
        return False

    # Check for at least one uppercase letter
    if not check_char(password, 'A', 'Z'):
        print("Password must contain at least one uppercase letter (A-Z).")
        return False

    # Check for at least one digit
    if not check_char(password, '0', '9'):
        print("Password must contain at least one digit (0-9).")
        return False

    # Check for at least one special character from [$#@]
    has_special = False
    special_chars = "$#@"
    for char in password:
        if char in special_chars:
            has_special = True
            break
    if not has_special:
        print("Password must contain at least one special character ($, #, or @).")
        return False

    # If all checks pass
    return True

# Main part of the program
while True:
    user_password = input("Enter your password: ")
    if is_password_valid(user_password):
        print("Password is valid!")
        break
    else:
        print("Please try again.")
