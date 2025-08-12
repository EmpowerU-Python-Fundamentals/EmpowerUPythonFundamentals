# This program prompts the user for a number (1-7) and prints the corresponding day of the week.
# It includes robust error handling for non-integer input and numbers outside the valid range.

def get_day_of_week():
    """
    A function that prompts the user for a number, validates the input, and
    prints the day of the week corresponding to the number.
    """
    days_of_week = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday"
    }

    while True:
        try:
            # Prompt the user for input and try to convert it to an integer.
            user_input = input("Please enter a number (1-7) to get the day of the week: ")
            number = int(user_input)

            # Check if the number is outside the valid range (1 to 7).
            if number < 1 or number > 7:
                raise ValueError("Number is out of range. Please enter a number between 1 and 7.")

            # If the input is a valid integer in the range, get the corresponding day.
            day = days_of_week[number]

        except ValueError as ve:
            # This block handles two cases:
            # 1. Non-integer input (e.g., "hello")
            # 2. Number is outside the valid range (e.g., 0, 8)
            print(f"Error: {ve}")
            print("Please enter a valid integer between 1 and 7.")
            
        except Exception as e:
            # A generic catch-all for any other unexpected errors.
            print(f"An unexpected error occurred: {e}")
        
        else:
            # The 'else' block is executed only if the 'try' block completes without errors.
            print(f"The day corresponding to the number {number} is {day}.")
            # We can now successfully break the loop.
            break
        
        finally:
            # The 'finally' block is always executed, whether an exception occurred or not.
            print("--- End of attempt ---")

# The master code calls the function to start the program.
if __name__ == "__main__":
    get_day_of_week()