def check_age(age):
    if age < 0:
        raise ValueError("Your age cannot be negative.")
    if age % 2 == 0:
        return("Your age is an even .")
    else:
        return("Your age is odd.")

while True:
    try:
        user_age_str = input("Please input your number: ")
        user_age = int(user_age_str)
        print(check_age(user_age))
        break
    except ValueError as e:
        print(f"Error: {e}")
    except TypeError:
        print("Error: Input data is not a number.")