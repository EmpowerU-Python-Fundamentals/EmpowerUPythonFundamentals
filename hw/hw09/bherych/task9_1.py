import random

def check_number(guess, number):
    if guess > number:
        print("Bigger")
    elif guess < number:
        print("Smaller")
    elif guess == number:
        print("You win")
        return True
    return False

def game():
    print("Try to guess a number between 1 and 100. You have 10 attempts.")
    max_attempts = 10
    attempts = 0
    number = random.randint(1, 100)

    while attempts <= max_attempts:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Invalid input, try to enter the whole number")
            continue
        attempts += 1
        if check_number(guess, number):
            break
    else:
        print("Ooops, you exhausted your maximum amount of attempts. Better luck next time.")

game()