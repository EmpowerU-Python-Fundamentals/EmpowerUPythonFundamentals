def check_age(age):
    if age > 0:
        return print("age is even") if age % 2 == 0 else print("age is odd")
    elif age < 0:
        raise ValueError("nagative age")


try:
    user_age = int(input("Write your age: "))
    check_age(user_age)
except ValueError as e:
    print(f"Error: {e}")
