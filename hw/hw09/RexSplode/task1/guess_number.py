import random

target = random.randint(1, 10)
attempts = 10
user_won = False

print("Guess a number from 1 to 10\n")

while not user_won and attempts != 0:
    guess = input(f"You have {attempts} attempts remaining.\n")
    attempts -= 1
    
    if guess.isdigit():
        guess = int(guess)
        user_won = guess == target
        
if user_won:
    print("Congratulations! You won!")
else:
    print("You ran out of attempts. Better luck next time!")