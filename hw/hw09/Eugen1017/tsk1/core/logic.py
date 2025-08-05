import os
import sys
from random import randint
from time import sleep

DIFFICULTY = [
    ["easy", 1],
    ["normal", 2],
    ["hard", 3]
]

ATTEMPTS_NUM = {
    1: 3,
    2: 10,
    3: 30,
}

START_MENU = [
    ["start", "enter s"],
    ["exit", "enter e"],
]

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_random_number(hard_option):
    return randint(1, pow(10, hard_option))

def game_cycle():
    while True:
        clear_console()

        print("Hello, welcome to the 'Guess the Number' game")
        print("\nStart menu:")
        for option in START_MENU:
            print(f"{option[0]} ({option[1]})")

        user_choice = input("Enter: ")

        clear_console()

        match user_choice:
            case "e":
                print("See you later!")
                sys.exit(0)
            case "s":
                pass

        clear_console()

        print("Choose difficulty level:")
        for level in DIFFICULTY:
            print(f"{level[0]} ({level[1]})")

        difficulty = -1

        while difficulty not in [1, 2, 3]:
            try:
                difficulty = int(input("Enter: "))
            except ValueError:
                continue

        guess_number = get_random_number(difficulty)

        attempts = ATTEMPTS_NUM[difficulty]

        clear_console()

        print(f"I have chosen a number, try to guess it, you have {attempts} attempts")

        while attempts > 0:
            sleep(3)
            clear_console()
            try:
                user_number = int(input("Your guess: "))
            except ValueError:
                continue

            if user_number == guess_number:
                print(f"You guessed it! The number is {user_number}\nSee you later!")
                sys.exit(0)

            elif user_number < guess_number:
                print("Too low!")
                attempts -= 1
                continue
            else:
                print("Too high!")
                attempts -= 1
                continue

        print("Sorry, you ran out of attempts!")
        print("Would you like to play again? (y/n)")
        replay_choice = input("Enter: ").lower()
        if replay_choice != 'y':
            print("See you later!")
            sys.exit(0)