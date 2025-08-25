def validate_password(password):

    # Check password length
    if not 6 <= len(password) <= 16:
        return False

    has_lowercase = False
    has_uppercase = False
    has_digit = False
    has_special = False

    for char in password:
        if 'a' <= char <= 'z':
            has_lowercase = True
        elif 'A' <= char <= 'Z':
            has_uppercase = True
        elif '0' <= char <= '9':
            has_digit = True
        elif char in ['$', '#', '@']:
            has_special = True

    # Return True only if all conditions are met
    return has_lowercase and has_uppercase and has_digit and has_special

if __name__ == "__main__":
    while True:
        user_password = input("Enter a password to validate: ")
        if validate_password(user_password):
            print("Password is valid.")
        else:
            print("Password is not valid. Please ensure it meets all the criteria:")
            print("- At least 1 lowercase letter")
            print("- At least 1 uppercase letter")
            print("- At least 1 number")
            print("- At least 1 special character ($, #, or @)")
            print("- Length is between 6 and 16 characters")