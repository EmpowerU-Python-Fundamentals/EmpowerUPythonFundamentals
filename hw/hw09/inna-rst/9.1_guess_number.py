import random

def greetings_play(range_numbers, max_attempts):
    print("=" * 50)
    print("Welcome to the game 'Guess the number'!")
    print("=" * 50)
    print(f"\nI thought of a number from {range_numbers[0]} to {range_numbers[1]}.")
    print(f"You have {max_attempts} attempts to guess it.")
    print("After each attempt I will tell you whether your number is higher or lower.\n")

MAX_ATTEMPTS = 10
attempts_used = 0
MIN_NUMBER = 1
MAX_NUMBER = 100

guessed = False
guessed_number = random.randint(MIN_NUMBER, MAX_NUMBER)


greetings_play((MIN_NUMBER, MAX_NUMBER), MAX_ATTEMPTS)

while not guessed and attempts_used < MAX_ATTEMPTS:
    attempts_used += 1
    remaining = MAX_ATTEMPTS - attempts_used

    print(f"--- Attempt #{attempts_used} (attempts remaining: {remaining}) ---")
    try:
        user_number = int(input("Enter a number between 1 and 100: "))

        if user_number <= MIN_NUMBER  or user_number > MAX_NUMBER:
            print("Please enter a number between 1 and 100!")
            attempts_used -= 1
            continue
    except ValueError:
        print("Error! Enter an integer!")
        attempts_used -= 1
        continue

    if user_number == guessed_number:
        print("You guessed it!")
        guessed = True
    elif attempts_used < MAX_ATTEMPTS:
        if user_number < guessed_number:
            print("Too low!")
        else:
            print("Too high!")
    elif attempts_used == MAX_ATTEMPTS:
        print("You ran out of attempts!")


