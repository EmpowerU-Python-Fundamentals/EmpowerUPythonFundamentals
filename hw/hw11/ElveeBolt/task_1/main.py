class NegativeAgeError(Exception):
    pass

def process_age_input(age_input):
    try:
        age = int(age_input)
        if age < 0:
            raise NegativeAgeError(f"Your age is negative: {age}")
        if age % 2 == 0:
            print(f"Your age {age} is even")
        else:
            print(f"Your age {age} is odd.")
    except ValueError:
        print("Please enter a valid integer for age.")


user_input = input("Enter your age: ")
process_age_input(user_input)