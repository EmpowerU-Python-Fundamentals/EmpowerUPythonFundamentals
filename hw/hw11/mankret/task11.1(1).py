# Write the program thats prompts the user to enter their age, and then display a message starting whether the age is
# even or odd. The program must provide the ability to enter a negative number, and in this case generate an
# exception. The master code should call a function that processes the infromation entered.


def check_age_parity(age_input):
    try:
        age = int(age_input)

        if age < 0:
            raise ValueError("Age cannot be a negative number.")

        if age % 2 == 0:
            return f"Your age, {age}, is an even number."
        else:
            return f"Your age, {age}, is an odd number."

    except ValueError as e:
        return f"Error: {e}"
    except Exception as e:
        return f"An unexpected error occurred: {e}"


user_age = input("Please enter your age: ")

result_message = check_age_parity(user_age)
print(result_message)

