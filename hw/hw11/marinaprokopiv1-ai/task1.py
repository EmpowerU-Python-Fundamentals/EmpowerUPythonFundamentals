class NegativeAgeError(Exception):
    pass

def check_age(age):
    if age < 0:
        raise NegativeAgeError("Age cannot be negative")
    if age % 2 == 0:
        return "Even age"
    else:
        return "Odd age"

try:
    user_age = int(input("Enter your age: "))
    print(check_age(user_age))
except NegativeAgeError as e:
    print(f"Error: {e}")
except ValueError:
    print("Error: Please enter a valid integer for age.")
