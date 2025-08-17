import  random

number = random.randint(1, 100)
tries = 10

print("Guess the random number from 1 to 100. You have 10 attempts.")

for i in range(tries):
    attempt = int(input(f'Try #{i + 1} - Enter your guess: '))
    if attempt > number:
        print("You entered the higher number")
    if attempt < number:
        print("You entered the lower number")
    if attempt == number:
        print(f"Congratulations! You entered the correct number: {number}")
        break
else:
    print("You lose :(")