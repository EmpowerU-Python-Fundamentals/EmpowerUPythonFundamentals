import random

secret = random.randint(1, 100)
MAX_TRIES = 10
print('I picked a number from 1 to 100. You have 10 attempts.')

for i in range(1, MAX_TRIES + 1):
    while True:
        s = input(f'Attempt {i}: enter an integer: ')
        try:
            guess = int(s)
        except ValueError:
            print('That is not an integer. Try again.')
            continue
        if not 1 <= guess <= 100:
            print('The number must be between 1 and 100. I will not count this as an attempt.')
            continue
        break

    if guess == secret:
        print(f'Correct! The number was {secret}. Attempts used: {i}.')
        break
    elif guess < secret:
        print('My number is higher.')
    else:
        print('My number is lower.')
else:
    print(f'No attempts left. The number was {secret}.')