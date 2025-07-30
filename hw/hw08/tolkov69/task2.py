import re

def validate_password(password):
    # Check length requirements
    if len(password) < 6 or len(password) > 16:
        return False
    
    # Check for at least one lowercase letter
    if not re.search("[a-z]", password):
        return False
    
    # Check for at least one uppercase letter
    if not re.search("[A-Z]", password):
        return False
    
    # Check for at least one digit
    if not re.search("[0-9]", password):
        return False
    
    # Check for at least one special character ($, #, or @)
    if not re.search("[$#@]", password):
        return False
    
    # If all checks passed
    return True

# Get password input from user
password = input("Enter your password: ")

# Validate the password
if validate_password(password):
    print("Password is valid!")
else:
    print("Password is invalid. Please ensure it meets all requirements:")
    print("- 6-16 characters long")
    print("- At least 1 lowercase letter [a-z]")
    print("- At least 1 uppercase letter [A-Z]")
    print("- At least 1 number [0-9]")
    print("- At least 1 special character [$#@]")
