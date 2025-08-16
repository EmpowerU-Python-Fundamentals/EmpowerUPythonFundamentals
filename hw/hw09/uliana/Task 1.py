import random

number = random.randint(1, 100)
print(number)
tries = 10

while tries > 0:
    print(f"You have {tries} tries left")
    guess_number = int(input("Guess the number "))
    if guess_number == number:
        break
    elif guess_number > number:
        print("Your number is too high!")
    else:
        print("You number is too small!")
    tries -= 1

if guess_number == number:
    print("Congratulations! You've guessed the number!")
else:
    print("Unfortunately, you have no tries left.")