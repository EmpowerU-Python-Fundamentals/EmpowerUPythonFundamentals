def check_age(age: int):
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age % 2 == 0:
        return "You are even-aged."
    else:
        return "You are odd-aged."

try:
    age = int(input("Enter your age: "))
    result = check_age(age)
    print(result)
except ValueError as e:
    print("Invalid input:", e)

