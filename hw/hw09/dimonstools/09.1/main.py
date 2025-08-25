import  random

number = random.randint(1, 100)
tries = 10

print("Random number is generated. Try to guess it in 10 tries!")

for i in range(tries):
    attempt = int(input(f'Try #{i + 1} - Enter your number from 1 to 100: '))
    if attempt > number:
        print("You entered the greater number")
    if attempt < number:
        print("You entered the less number")
    if attempt == number:
        print(f"Congratulations! You entered the correct number: {number}")
        break
else:
    print("You lose :(")