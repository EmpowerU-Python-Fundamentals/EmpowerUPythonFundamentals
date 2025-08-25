from random import randint
"""Script that randomly generates a number from a range of 1 to 100 and asks the user to guess that number in 10 attempts."""

def main():
    print('Hello! Welcome to the game \n"Guess the number!"\nGood luck!.')
    max_attempt = 10
    min = 1
    max = 100
    print(f"You have {max_attempt} attempts to guess a number from {min} to {max}.")

    secret_number = randint(min, max)
    attempt = 1
    while attempt <= max_attempt:
        print(f"\nAttempt {attempt} of {max_attempt}")
        try:
            guess = int(input("Your guess: "))
            if min <= guess <= max:
                if guess == secret_number:
                    print(f"Congratulations! You guessed it right. The number was {secret_number}")
                    break
                if guess < secret_number:
                    print("Too low!")
                    attempt +=1
                else:
                    print("Too high!")
                    attempt+=1
            else:
                print(f"Number must be between {min} and {max}.")
        except:
            print("Invalid input. Please enter a whole number.")

    else:
        print(f"\nYou used all attempts. The number was {secret_number}.")

if __name__ == "__main__":
    main()