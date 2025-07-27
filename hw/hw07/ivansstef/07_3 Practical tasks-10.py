# Code written by Ivan Savytsky
# Code reviewed for PEP 8 compliance by ChatGPT

def bool_to_word(value):
    """Return 'Yes' if True, 'No' if False."""
    if not isinstance(value, bool):
        return "Please enter a boolean value."

    return "Yes" if value else "No"

def main():
    print(bool_to_word(True))     # Yes
    print(bool_to_word(False))    # No
    print(bool_to_word("yes"))    # Error

if __name__ == "__main__":
    main()
