def parity_age_check(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")
    elif age % 2 == 0:
        print(f"The age {age} is even.")
    else:
        print(f"The age {age} is odd.")

def main():
    try:
        user_input = int(input("Enter your age: "))
        parity_age_check(user_input)
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()