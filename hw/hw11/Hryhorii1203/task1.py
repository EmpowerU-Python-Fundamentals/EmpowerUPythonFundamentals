def check_age(age):
    """
    Checks if age is even or odd and handles negative numbers
    """
    if age < 0:
        raise ValueError("Age cannot be negative!")
    return "even" if age % 2 == 0 else "odd"

def main():
    try:
        age = int(input("Please enter your age: "))
        result = check_age(age)
        print(f"Your age is {result}.")
    except ValueError as e:
        if "invalid literal" in str(e):
            print("Please enter a valid integer.")
        else:
            print(e)

if __name__ == "__main__":
    main()