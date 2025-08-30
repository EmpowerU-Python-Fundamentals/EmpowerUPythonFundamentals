import random

def main():
    number_to_guess = random.randint(1, 100)
    attempts = 10

    print("I have chosen a number between 1 and 100.")
    print(f"You have {attempts} tries to guess it!")

    for attempt in range(1, attempts + 1):
        while True:
            try:
                guess = int(input(f"Attempt {attempt}: Enter your guess: "))
                if 1 <= guess <= 100:
                    break
                else:
                    print("Please enter a number between 1 and 100.")
            except ValueError:
                print("Invalid input! Please enter an integer.")

        if guess == number_to_guess:
            print(f"Congratulations! You guessed the number {number_to_guess} in {attempt} tries.")
            break
        elif guess < number_to_guess:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

        remaining = attempts - attempt
        if remaining > 0:
            print(f"You have {remaining} attempts left.\n")

    else:
        print(f"Sorry, you didn't guess the number. The correct number was {number_to_guess}.")

if __name__ == "__main__":
    main()
