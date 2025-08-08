def check_age(age):
    """
    Checks the person's age: even or odd.

    Args:
        age - user's age.
        Age cannot be negative.
    """
    if age < 0:
        raise ValueError("Age cannot be negative!")
    if age % 2:
        return "Even"
    else:
        return "Odd"
    
def main():
    try:
        age = int(input("Enter your age: "))
        print(check_age(age))
    except ValueErrror as e:
        print(f"Error : {e}")

if __name__ == "__main__":
    main()
