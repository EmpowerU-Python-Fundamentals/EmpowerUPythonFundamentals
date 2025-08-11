def your_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age % 2 == 0:
        return "Your age is even"
    else:
        return "Your age is odd"

def main():
    try:
        age = int (input("Enter your age: "))
        message = your_age(age)
    except ValueError as error:
        print(f"Error: {error}")
    except Exception as error:
        print(f"Unexpected error {error}")
    else:
        print(message)

if __name__ == "__main__":
    main()