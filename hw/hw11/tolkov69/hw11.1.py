def check_age(age):
    """Check if age is even or odd with validation"""
    if age < 0:
        raise ValueError("Age cannot be negative!")
    return "even" if age % 2 == 0 else "odd"

def main():
    try:
        age = int(input("Please enter your age: "))
        result = check_age(age)
        print(f"Your age is {result}.")
    except ValueError as e:
        print(f"Error: {e}")
    except:
        print("Error: Invalid input")

if __name__ == "__main__":
    main()
