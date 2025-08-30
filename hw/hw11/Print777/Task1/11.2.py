# Task 2 (number - day of the week, with validation)

def get_day_of_week(number: int) -> str:
    days = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday"
    }
    
    if number not in days:
        raise ValueError("Number must be between 1 and 7!")

    return days[number]

def main():
    try:
        number = int(input("Enter a number (1-7): "))
        day = get_day_of_week(number)
        print(f"{number} corresponds to {day}.")
    except ValueError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
