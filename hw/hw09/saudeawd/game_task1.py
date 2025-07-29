import random

attempt = 0
number = random.randint(1, 100)

while attempt < 10:
    user_number = int(input("Enter your guess: "))
    if user_number < number:
        print('Higher')
    elif user_number > number:
        print('Lower')
    else:
        print('Congratulations! You guessed the number!')
        quit()
    attempt += 1
print(f"I`m sorry, you didn`t guess the number.. Your number is {number}")