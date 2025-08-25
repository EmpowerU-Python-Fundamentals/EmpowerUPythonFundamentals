class InputAgeError(Exception):
    def __init__(self, msg):
        self.msg = msg


def get_valid_age():
    """
    Prompt user for age and validate input until a valid integer is received.
    """
    while True:
        age_input = input("Please enter your age: ")
        try:
            age = int(age_input)
            if age < 0:
                raise InputAgeError("Age cannot be negative.")
            return age
        except ValueError:
            print("Invalid input. Please enter a numeric value for age.")
        except InputAgeError as e:
            print(e.msg)


def check_even_odd_age(age):
    """Check if the age is even or odd."""
    return "Your age is even." if age % 2 == 0 else "Your age is odd."


def main_age_check():
    """The main function is to initiate the age verification process."""
    age = get_valid_age()
    result = check_even_odd_age(age)
    print(result)


if __name__ == "__main__":
    main_age_check()
