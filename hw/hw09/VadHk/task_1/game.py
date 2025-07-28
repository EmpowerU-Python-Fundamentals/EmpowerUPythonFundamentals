from random import randint

def game():
    print("Welcome to the game! You must guess the secret number from 1 to 100. You have 10 tries.")
    max_tries = 10
    tries_counter = 0
    secret_number = randint(1, 100)
    while tries_counter < max_tries:
        guess = int(input("Enter your guess: "))
        tries_counter += 1
        if guess < secret_number:
            print(f"Too low! Try again. You have {max_tries - tries_counter} tries left.")
        elif guess > secret_number:
            print(f"Too high! Try again. You have {max_tries - tries_counter} tries left.")
        else:
            print(f"Congratulations! You've guessed the number {secret_number} in {tries_counter} tries.")
            return
