# 1. Write a program that prompts the user to enter their age,
#   and then displays a message stating whether the age is even or odd.
# The program must provide the ability  to enter a negative number,
#   and in this case generate an exception.
# The master code should call a function 
#   that processes the information entered

def process_age(text):
    age = int(text)
    if age < 0:
        raise ValueError
    return "odd" if age % 2 else "even"

if __name__ == "__main__":
    text = input("Enter your age: ")
    try:
        result = process_age(text)
    except ValueError:
        print(f"You've entered invalid value for age: '{text}'")
    else:
        print(f"Your age is {result}.")
    finally:
        print()