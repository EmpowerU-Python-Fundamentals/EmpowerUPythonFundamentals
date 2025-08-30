def check_age(age):
    """
    Function that checks if the age is even or odd.
    Raises an exception if the age is negative.
    """
    if age < 0:
        raise ValueError("Age cannot be negative!")
    
    if age % 2 == 0:
        return "Even"
    else:
        return "Odd"

def main():
    try:
        user_input = input("Enter your age: ")
        age = int(user_input)
        message = check_age(age)
        print(check_age(age))
    
    except ValueError as ve:
        print(f"Error: {ve}")

if __name__ == "__main__":
    main()