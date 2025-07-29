# Code written by Ivan Savytsky
# Code reviewed for PEP 8 compliance by ChatGPT


def number_to_string(num):
    """Convert number to string."""
    try:
        return str(int(num))
    except ValueError:
        return "Invalid input. Enter a number."


def main():
    print(number_to_string(123))     # "123"
    print(number_to_string("999"))   # "999"
    print(number_to_string("abc"))   # Error


if __name__ == "__main__":
    main()
