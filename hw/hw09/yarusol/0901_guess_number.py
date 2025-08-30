# Task 1.
# Write a game script that randomly generates a number
#   from a range of 1 to 100 
#   and asks the user to guess that number in 10 tries.
# The program reads the numbers entered by the user 
#   and prompts the user whether the guessed number 
#   is greater or less than the number entered by the user.
# The game must continue until the user has used 10 attempts
#   and guessed the number.
# If the user guessed the number, the program prints a congratulatory message,
#   and if 10 attempts have been exhausted
#   and the user did not have time to guess the number,
#   then the corresponding message is displayed.
# (to perform the task, you need to import the random module,
# and from it the randint() function)


from random import randint
from time import sleep

MIN_NUMBER = 1
MAX_NUMBER = 100
MAX_TRIES = 10

def get_guess(hint: str) -> int:
    guess = None
    while not guess:
        print()
        try:
            guess = int(input(hint))
            if guess < MIN_NUMBER or guess > MAX_NUMBER:
                raise ValueError
        except ValueError:
            print("Oh... you entered somesing strange...")
            print(F"I'm still expecting an integer number from {MIN_NUMBER} to {MIN_NUMBER} (including both)")
            print("Type your guess once more. And more carefully.")
            sleep(1.5)
    return guess

def start_game():
    secret = randint(MIN_NUMBER, MAX_NUMBER)
    print(f"I have thought of a number from {MIN_NUMBER} to {MAX_NUMBER} (including both).")
    print("Could you guess it in 10 tries?")

    try_number = 1
    while try_number <= MAX_TRIES:
        guess = get_guess(f"The try #{try_number} : ")
        
        if guess > secret:
            print("It's too much!")
        elif guess < secret:
            print("Hah! Too little! My number is bigger!")
        else:
            print("So.... You HAVE GUESSED it!!!!")
            print("Congratulations!!!")
            print()
            return
        
        try_number += 1
        if try_number <= MAX_TRIES:
            print("Try to guess once more. I beleive in you!")
        else:
            print("You exhausted all 10 tries... Pretty pity for me...")
            print("Actually - not! :D")


if __name__ == "__main__":
    print()
    print()
    print()
    start_game()
    print()
