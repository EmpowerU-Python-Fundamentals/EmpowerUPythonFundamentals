def process_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative!")
    if age % 2 == 0:
        print(f"Age {age} is even")
    else:
        print(f"Age {age} is odd")

try:
    user_input = int(input("Enter your age: "))
    process_age(user_input)
except ValueError as e:
    print("Error:", e)
