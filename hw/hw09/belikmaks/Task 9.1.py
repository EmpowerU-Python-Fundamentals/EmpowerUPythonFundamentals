import random

number = random.randint(1, 100)

attempts = 10

print("Guess the number between 1 and 100. You have 10 tries.")

for i in range(attempts):
    try:
        guess = int(input(f"Attempt {i+1}: Enter your guess: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    else:
        print(f"Congratulations! You guessed the number in {i+1} tries.")
        break
else:
    print(f"Sorry! You've used all {attempts} attempts. The number was {number}.")
