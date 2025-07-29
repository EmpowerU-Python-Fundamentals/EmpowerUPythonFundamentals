import re as regex


def is_valid_password(password: str) -> bool:
    """
    Check if the password is valid according to the specified rules:
    - Minimum 6 characters long
    - Maximum 16 characters long
    - Contains at least one character from [$#@]
    - Contains at least one letter between [A-Z] and one letter between [a-z]
    - Contains at least one number between [0-9]

    :param password: The password to validate.
    :return: True if the password is valid, False otherwise.
    """
    if len(password) < 6 or len(password) > 16:
        return False

    if not regex.search(r'[A-Z]', password) or not regex.search(r'[a-z]', password):
        return False

    if not regex.search(r'[$#@]', password):
        return False

    if not regex.search(r'[0-9]', password):
        return False

    return True