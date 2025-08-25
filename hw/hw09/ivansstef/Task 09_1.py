import random

secret_number = random.randint(1, 100)

print("I have picked a number between 1 and 100. You have 10 tries to guess it!")

for attempt in range(1, 11):
    guess = int(input(f"Attempt {attempt}: Enter your guess: "))

    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print(f"Congratulations! You guessed the number {secret_number} in {attempt} tries!")
        break
else:
    print(f"Sorry, you've used all your tries. The number was {secret_number}.")
