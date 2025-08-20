def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    else:
        if age % 2 == 0:
            print(f'Your age {age} is even')
        else:
            print(f'Your age {age} is odd')


def main():
    while True:
        try:
            age = int(input("Enter your age: "))
            check_age(age)
            break
        except TypeError:
            print("Please enter a valid integer for age.")
        except ValueError as e:
            print(f"Invalid input: {e}")

if __name__ == "__main__":
    main()