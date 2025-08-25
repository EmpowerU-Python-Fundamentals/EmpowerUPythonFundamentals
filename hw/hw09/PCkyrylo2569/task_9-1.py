import random

print("Hi guess the number between 0 and 100! You have 10 attempts.")

user = input("Enter your name: ")
number = random.randint(1, 100)
attempts = 0
max_attempts = 10

while attempts < max_attempts:
    guess = int(input(f"Attempt {attempts + 1}: Enter your guess: "))
    attempts += 1
    
    if guess < number:
        print("Too low! The number is greater.")
    elif guess > number:
        print("Too high! The number is smaller.")
    else:
        print(f"Congratulations {user}, you guessed the number {number} in {attempts} attempts.")
        break
else:
    print(f"😔 Sorry {user}, you lose. The number was {number}.")