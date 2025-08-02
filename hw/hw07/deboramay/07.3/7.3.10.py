def bool_to_word(boolean):
    """
    The method takes a boolean value and return a "Yes" string for true, 
    or a "No" string for false.
    """
    return "Yes" if boolean else "No"

#Test:
print(bool_to_word(True))
print(bool_to_word(False))