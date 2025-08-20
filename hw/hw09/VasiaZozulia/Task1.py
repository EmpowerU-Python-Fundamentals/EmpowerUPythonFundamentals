import random

# Define the range within which the number will be guessed
MIN_NUMBER = 1
MAX_NUMBER = 100

# Set the maximum number of attempts the user has to guess the number
ATTEMPTS = 10

# Hints for the user's guesses
SMALL = 'Your number is too small'
BIG = 'Your number is too hight'
WIN = 'Congratulations, you won the game!'
LOSS = 'Unfortunately, you lost the game. All your attempts were unsuccessful.'
INPUT_GUESS_MESSAGE = 'Enter your assumption: '
RANGE_ERROR = 'The range within which the number will be guessed is incorrect. The first value should be smaller than the second value.'
INPUT_NUMBER_ERROR = 'Please enter the whole number!'

# Checking if the guess range is within the correct bounds.
try:
    # Randomly select a number between the specified range
    random_number = random.randint(MIN_NUMBER, MAX_NUMBER)

    print ("Welcome to the game 'Guess the Number.'")
    print (f"I’ve picked a number between {MIN_NUMBER} and {MAX_NUMBER}. You have {ATTEMPTS} tries to guess it. Let's play!")

    # Start the game
    while ATTEMPTS > 0:
        try:
            guess = int(input(INPUT_GUESS_MESSAGE))
        except ValueError:
            print (INPUT_NUMBER_ERROR)
            continue

        # Checking if the user's number is within the correct bounds.
        if guess < MIN_NUMBER or guess > MAX_NUMBER:
            print (f"The number should be between {MIN_NUMBER} and {MAX_NUMBER}")
            continue

        # Checking if the user's input number equal random number
        if guess == random_number:
            print (f"{WIN}. The number was {random_number}.")
            break
        elif guess < random_number:
            print (f"{SMALL}.")
        else:
            print (f"{BIG}.")

        # User attempts decrease each time they try to guess the number.
        ATTEMPTS -= 1
        print (f"{ATTEMPTS} tries left! Try again!")
    else:
        print (f"{LOSS} The number was {random_number}.")

except ValueError:
    print (RANGE_ERROR)