def main():
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

    try:
        day = int(input("Enter a number (1-5) for the weekday: "))
        if day < 1 or day > 5:
            raise ValueError("Number must be between 1 and 5")
        print(f"The day is: {weekdays[day - 1]}")
    except ValueError as e:
        print(f"Invalid input: {e}")

if __name__ == "__main__":
    main()