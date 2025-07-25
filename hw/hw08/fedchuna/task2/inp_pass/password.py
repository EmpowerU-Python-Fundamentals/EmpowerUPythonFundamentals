__all__ = ['input_pass']
def input_pass():
    """Returns the password input from the user."""
    import getpass
    a = getpass.getpass(prompt='Enter your password: ')
    return a