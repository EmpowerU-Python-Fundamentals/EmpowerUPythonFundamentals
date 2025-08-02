import random
from random import randint

def number_guessing_game():
    # Generate a random number between 1 and 100
    secret_number = randint(1, 100)
    attempts = 10
    
    print("Welcome to the Number Guessing Game!")
    print(f"I'm thinking of a number between 1 and 100. You have {attempts} attempts to guess it.")
    
    for attempt in range(1, attempts + 1):
        print(f"\nAttempt {attempt} of {attempts}")
        
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number between 1 and 100.")
            continue
            
        if guess < 1 or guess > 100:
            print("Your guess must be between 1 and 100!")
            continue
            
        if guess == secret_number:
            print(f"\nCongratulations! You guessed the number {secret_number} in {attempt} attempts!")
            return
        elif guess < secret_number:
            print("The secret number is higher than your guess.")
        else:
            print("The secret number is lower than your guess.")
    
    print(f"\nGame over! You've used all {attempts} attempts.")
    print(f"The secret number was {secret_number}.")

number_guessing_game()
