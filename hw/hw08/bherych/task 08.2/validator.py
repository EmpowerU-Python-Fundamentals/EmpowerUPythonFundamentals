import re

def validate_password(password):
    """Validates password inputet by user for containing necessary characters."""
    if re.search('[a-z]', password) == False:
        return False
    elif re.search('[A-Z]', password) == False:
        return False
    elif re.search('[0-9]', password) == False:
        return False
    elif re.search('[$#@]', password) == False:
        return False
    elif len(password) < 6 or 16 < len(password):
        return False

    return True

def main():
    user_input = input("Please, enter your password: ")
    if validate_password(user_input):
        print("Your password is valid.")
    else:
        print("Please, try another password.")

main()