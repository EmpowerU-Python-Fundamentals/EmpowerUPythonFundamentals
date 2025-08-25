import random

def play_game():
    """
    The 'Guess the Number' game.
    
    The user tries to guess a randomly generated number
    from 1 to 100 in 10 attempts.
    """
    secret_number = random.randint(1, 100)
    max_attempts = 10
    
    print("Let's play 'Guess the Number' game ~~")
    print("I'm thinking of a number between 1 and 100. Try to guess it!")
    print(f"You have {max_attempts} attempts.")

    for attempt in range(1, max_attempts + 1):
        try:
            user_guess = int(input(f"\nAttempt #{attempt}. Enter your number: "))
        except ValueError:
            print("Please enter a valid number.")
            continue  # Repeat the current attempt without decrementing the counter

        if user_guess == secret_number:
            print(f"\n🎉 Congratulations! You guessed the number {secret_number} in {attempt} attempts!")
            break
        elif user_guess < secret_number:
            print("The secret number is higher. Try again.")
        else: # user_guess > secret_number
            print("The secret number is lower. Try again.")
    else:
        # This 'else' block runs if the loop completes without a 'break'
        print(f"\n🙁 Sorry, you've run out of attempts. The secret number was: {secret_number}.")

if __name__ == "__main__":
    play_game()
