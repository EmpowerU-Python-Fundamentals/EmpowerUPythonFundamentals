from random import randint

random_number = randint(1, 100)

MAX_TRIES = 10
attempts = 0
guessed = False

print(f"Guess the number between 1 and 100! You have {MAX_TRIES} tries.")

while attempts < MAX_TRIES:
    try:
        guess = int(input(f"Attempt {attempts + 1}: Enter your guess: "))
    except ValueError:
        print("Please enter a valid integer.")
        continue

    attempts += 1

    if guess < random_number:
        print("Too low")
    elif guess > random_number:
        print("Too high")
    else:
        print(f"Congratulations! You guessed the number in {attempts} tries.")
        guessed = True
        break

if not guessed:
    print(f"You've used all {MAX_TRIES} attempts. The number was {random_number}.")
