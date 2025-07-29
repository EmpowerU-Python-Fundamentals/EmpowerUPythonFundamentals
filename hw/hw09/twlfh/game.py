import random

min_number = 1
max_number = 100
max_attempts = 10

sacred_number = random.randint(min_number, max_number)

message = 'Hello, I guessed an integer number from 1 to 100. You have 10 attempts to guess it.'

print(message)
def num_s():
    for attempt in range(1,11):
        try:
            number = int(input('Please, enter your number: '))
        except ValueError:
            print('Please, enter an integer number!')
            continue
        if number < sacred_number:
            print('Your number is less than what I guessed.')
            print(f'\tAttempts left: {max_attempts-attempt}.')
        elif number > sacred_number:
            print('Your number is greater than what I guessed.')
            print(f'\tAttempts left: {max_attempts - attempt}.')
        else:
            print('Congratulations! You won.')
            print(f'\tYou guessed it in {attempt} attempt(s).')
            break
    else:
        print(f'Game over. The number I remembered is {sacred_number}')

num_s()



