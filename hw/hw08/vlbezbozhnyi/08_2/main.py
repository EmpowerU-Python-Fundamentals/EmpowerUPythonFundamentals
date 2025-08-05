import re

user_password = input("Enter your password: ")


def is_valid_password(user_pass):
    """
    Check if the password is valid based on specific criteria.
    """
    pattern = re.compile(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[$#@])[a-zA-Z0-9$#@]{6,16}$")
    if pattern.match(user_pass):
        print("Password is valid.")
        return True
    else:
        print(
            (
                "Password must contain at least one lowercase letter, one uppercase letter, "
                "one number, and one special character. And 6-16 symbols long."
            )
        )
        return False


is_valid_password(user_password)
