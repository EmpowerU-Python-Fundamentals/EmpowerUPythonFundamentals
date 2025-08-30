class AgeError(Exception):
    def __init__(self, message="Age cannot be negative"):
        self.message = message

    def __str__(self):
        return self.message


def check_age(age):
    if age < 0:
        raise AgeError("Age cannot be negative")
    if age % 2 == 0:
        return f"Age {age} is even"
    else:
        return f"Age {age} is odd"
    

def main():
    try:
        age = int(input("Enter your age: "))
        result = check_age(age)
        print(result)
    except ValueError as e:
        print("Error: Please enter a valid integer number for age.")
    except AgeError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main() 