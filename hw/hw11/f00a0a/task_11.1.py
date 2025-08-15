def check_age(age):
    """Check if a user age is even or odd."""
    if age < 0:
        raise ValueError("negative")  
    if age % 2 == 0:
        return "Your age is even."
    else:
        return "Your age is odd."

def main():
    print("Hello, let's find out if your age is even or odd.")
    while True:
        try:
            user_input = input("Enter your age: ")
            if not user_input.isdigit() and not (user_input.startswith('-') and user_input[1:].isdigit()):
                raise ValueError("not_a_number") 
            user_input = int(user_input)
            result = check_age(user_input)
            print(result)
            break

        except ValueError as e:
            if str(e) == "not_a_number":
                print("Error: You must enter a number, not text.")
            elif str(e) == "negative":
                print("Error: You can't enter a negative number.")
            else:
                print("Error:", e)

if __name__ == "__main__":
    main()