def process_age():
    age = int(input("Enter your age: "))

    if age < 0:
        raise ValueError("Age cannot be negative!")

    if age % 2 == 0:
        print(f"Your age {age} is even.")
    else:
        print(f"Your age {age} is odd.")

try:
    process_age()
except ValueError as e:
    print("Error:", e)
