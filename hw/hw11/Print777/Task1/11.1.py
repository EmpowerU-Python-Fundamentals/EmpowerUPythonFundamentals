# Task 1 (age verification, even/odd, processing negative numbers)

def process_age(age: int) -> str:
    if age < 0:
        raise ValueError("Age cannot be negative!")
    if age % 2 == 0:
        return f"Your age ({age}) is even."
    else:
        return f"Your age ({age}) is odd."

def main():
    try:
        age = int(input("Enter your age: "))
        result = process_age(age)
        print(result)
    except ValueError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
