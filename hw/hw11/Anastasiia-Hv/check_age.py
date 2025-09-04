def check_age(age: int) -> str:
    """
    Function that checks if the age is even or odd.
    Raises an exception if the age is negative.
    """
    if age < 0:
        raise ValueError("Age cannot be negative!")
    
    if age % 2 == 0:
        return f"Your age {age} is even."
    else:
        return f"Your age {age} is odd."


def main():
    try:
        age = int(input("Enter your age: "))
        result = check_age(age)
        print(result)
    except ValueError as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
