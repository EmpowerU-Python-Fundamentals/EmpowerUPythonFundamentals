def get_day_of_week_by_number(number):
    weekdays = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday"
    }

    if number in weekdays:
        return f"The day of the week is: {weekdays[number]}"
    else:
        raise ValueError("Number must be between 1 and 7.")

if __name__=='__main__':
    try:
        user_input = input("Enter a number (1-7) to get the corresponding day of the week: ")
        number = int(user_input)
        result = get_day_of_week_by_number(number)
        print(result)
    except ValueError as e:
        print(f"Error: {e}")
