def day_of_week(day):
    """Check a number of the day of the week"""
    days = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday"
        }
    if day < 1 or day > 7:
        raise ValueError("day_not_in_range")
    if day in days:
        day_name = days.get(day)
        return f"Your day is {day_name}"
    
def main():
    print("Hello, enter a number of the day of the week (1-7)")
    while True:
        try:
            user_input = input("Enter a number of a day (1-7)")
            if not user_input.isdigit() and not (user_input.startswith('-') and user_input[1:].isdigit()):
                raise ValueError("not_a_number")
            user_input = int(user_input)
            result = day_of_week(user_input)
            print(result)
            break 

        except ValueError as e:
            if str(e) == "not_a_number":
                print("Error: You must enter a number (1-7), not text.")
            elif str(e) == "day_not_in_range":
                print("Error: You're enter negative number. Please check that you enter a number between (1-7)")
            else:
                print("Error:", e)

if __name__ == "__main__":
    main()