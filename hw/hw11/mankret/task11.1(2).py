# Write a program that analyze the entered number and, depending on the number, gives a day of the week that corresponds
# to this number (1 is Monday, 2 is Tuesday, etc.). Take into account cases of entering numbers from 8 and more, as well
# as cases of entering non-numerical data.


def get_day_of_week(number_input):
    days_of_week = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday"
    }

    try:
        day_number = int(number_input)

        if day_number in days_of_week:
            return f"The day corresponding to {day_number} is {days_of_week[day_number]}."
        else:
            return f"Error: The number {day_number} is out of the valid range (1-7)."

    except ValueError:
        return "Error: Please enter a valid numerical value."
    except Exception as e:
        return f"An unexpected error occurred: {e}"


user_number = input("Please enter a number from 1 to 7: ")

result_message = get_day_of_week(user_number)
print(result_message)
