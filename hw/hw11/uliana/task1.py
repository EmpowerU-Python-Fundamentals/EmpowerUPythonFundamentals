class NegativeNumberError(Exception):
    pass


def checking_number(age):
    try:
        if age < 0:
            raise NegativeNumberError("Your age must be positive")
        elif age % 2 == 0:
            print("Your age is even")
        elif age % 2 == 1:
            print("Your age is odd")
    except NegativeNumberError as e:
        print(f'Error: {e}')


age = int(input("Enter your age: "))
checking_number(age)
