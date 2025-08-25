import random

secret_number = random.randint(1, 100)
print("Guess the number between 1 and 100")
print("You have 10 tries to guess")

for attempt in range(1, 11):
    guess = int(input(f"Attemp {attempt}: Enter your guess"))

    if guess == secret_number:
        print("Congratulations. You won!")
        break
    elif guess < secret_number:
        print("Try a higher number.")
    elif guess > secret_number:
        print("Try a lower number")
else:
    print("Sorry you didn't guess the number. You don't have more attempts.")
