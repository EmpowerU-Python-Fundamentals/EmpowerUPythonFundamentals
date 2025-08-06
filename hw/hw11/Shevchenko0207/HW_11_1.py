# This program prompts the user for their age and determines if it is even or odd.
# It includes error handling for non-integer input and specifically for negative ages.

def check_age_even_odd():
    """
    A function that prompts the user for their age, validates the input, and
    prints whether the age is even or odd. It raises an exception for negative ages.
    """
    while True:
        try:
            # Prompt the user for input and try to convert it to an integer.
            user_input = input("Please enter your age: ")
            age = int(user_input)

            # Check if the age is a negative number and raise a specific exception.
            if age < 0:
                raise ValueError("Age cannot be a negative number.")

            # If the input is a valid non-negative integer, check if it's even or odd.
            if age % 2 == 0:
                print(f"Your age, {age}, is an even number.")
            else:
                print(f"Your age, {age}, is an odd number.")

        except ValueError as ve:
            # This block handles two cases:
            # 1. Non-integer input (e.g., "twenty")
            # 2. Negative age input, which we explicitly raised above.
            print(f"Error: {ve}")
            print("Please enter a valid, non-negative integer for your age.")
            
        except Exception as e:
            # A generic catch-all for any other unexpected errors.
            print(f"An unexpected error occurred: {e}")
        
        else:
            # The 'else' block is executed only if the 'try' block completes without errors.
            # This is where we can successfully break the loop.
            break
        
        finally:
            # The 'finally' block is always executed.
            print("--- End of attempt ---")

# The master code calls the function to start the program.
if __name__ == "__main__":
    check_age_even_odd()