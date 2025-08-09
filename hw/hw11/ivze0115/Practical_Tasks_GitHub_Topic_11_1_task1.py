def check_age(age):
    if age < 0:
        raise ValueError("Age should be positive.")
    if age % 2 == 0:
        return "Your age is even."
    else:
        return "Your age is odd."

if __name__=='__main__':
    try:
        user_input = input("Enter your age: ")
        age = int(user_input)
        result = check_age(age)
        print(result)
    except ValueError as e:
        print(f"Error: {e}")
