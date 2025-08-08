# Task 1
def check_age():
    try:
        age = int(input("Enter your age: "))
        if age < 0:
            raise ValueError("Age cannot be negative.")
        if age % 2 == 0:
            print(f"Your age ({age}) is even.")
        else:
            print(f"Your age ({age}) is odd.")
    except ValueError as e:
        print("Error:", e)


# Task 2
def day_of_week():
    days = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday"
    }
    try:
        num = int(input("Enter a number (1-7): "))
        if num in days:
            print(f"Day {num} is {days[num]}.")
        else:
            print("Invalid number. Please enter a number between 1 and 7.")
    except ValueError:
        print("Invalid input. Please enter a number.")


# Master code
if __name__ == "__main__":
    print("--- Task 1 ---")
    check_age()

    print("\n--- Task 2 ---")
    day_of_week()
