class NegativeAgeError(Exception):
    pass

def page(age):
    if age < 0:
        raise NegativeAgeError("Age cannot be negative!")
    if age % 2 == 0:
        return f"Age {age} is even."
    else:
        return f"Age {age} is odd."

try:
    age = int(input("Enter your age: "))
    print(page(age))
except ValueError:
    print("Invalid input! Please enter a number.")
except NegativeAgeError as e:
    print(e)