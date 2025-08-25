def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative!")
    if age % 2 == 0:
        return "Your age is even."
    else:
        return "Your age is odd."

def main():
    try:
        age_input = int(input("Enter your age: "))
        message = check_age(age_input)
        print(message)
    except ValueError as e:
        if str(e) == "Cannot be negative!":
            print(f"Error: {e}")
        else:
            print("Please enter a valid integer number for age.")

if __name__ == "__main__":
    main()