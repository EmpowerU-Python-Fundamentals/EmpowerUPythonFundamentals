import random

numbers = random.randint(1, 100)

print("Let's play the game. Guess, what number i generated ")

count = 0

while count <= 10:
    input_from_user = input("Enter your number: ")
    if input_from_user.isdigit():
        if count == 10:
            print(f'The attempts are over. You lose. My number: {numbers}')
            break
        elif int(input_from_user) == numbers:
            print(f"Congrats, you win, its number {numbers}")
            break
        elif int(input_from_user) < numbers:
            count += 1
            print(f'Your number lesser, try again. You have {10 - count} attempts')

        elif int(input_from_user) > numbers:
            count += 1
            print(f'Your number bigger, try again. You have {10 - count} attempts')

    else:
        print(f"Invalid input. {input_from_user} must be digit. Try again")
