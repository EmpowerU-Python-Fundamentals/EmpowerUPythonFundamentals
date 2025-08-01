from random import *


def get_checking_input():
    """
    Prompts the user to enter a number and validates the input.

    Continuously asks the user for input until a valid integer is entered.
    If the input is not a valid integer, displays an error message and prompts again.

    """
    while True:
        try:
            x = int(input("Enter number: "))
            return x
        except ValueError:
            print("You didn't write a number")


def game_main():
    """
    Runs a number guessing game where the player has up to 10 attempts to guess a randomly generated number between 1 and 100.
    The function generates a random number and prompts the user to guess it. After each guess, it provides feedback indicating whether the guess was too high or too low. If the player guesses the number correctly within 10 attempts, the function returns "You win!". Otherwise, it returns "You loose!".
    Returns:
        str: "You win!" if the player guesses the number correctly within 10 attempts, otherwise "You loose!".
    """


    ran_num = randint(1,100)
    for i in range(1,11):
        guess_num = get_checking_input()
        if guess_num == ran_num:
            return f"You win in {i} attempts!"
        elif guess_num > ran_num:
            print(f'Attempt {i}: Too high!')
        else:
            print(f'Attempt {i}: Too low!')
    return f"You lose! The number was {ran_num}"


if __name__ == "__main__":    
    Result_Game = game_main()
    print(Result_Game)