def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age % 2 == 0:
        return f"Age {age} is even"
    else:
        return f"Age {age} is odd"


try:
    age = int(input("Enter your age: "))
    print(check_age(age))
except ValueError as e:
    print("Error:", e)
