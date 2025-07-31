import random

def main():
    """
    Main function to run a number guessing game.

    The program randomly selects a number between 1 and 100.
    The player has 10 attempts to guess the number.
    After each guess, the program provides feedback whether the guessed number
    is too big, too low, or correct.
    If the player guesses the number correctly, a congratulatory message is shown.
    If the player fails to guess in 10 attempts, player loses and the correct number is revealed.
    """
    
    number_to_guess = random.randint(1, 100)
    total_attempts= 10
    attempt_number=1
    while attempt_number<=total_attempts:
        guess = int(input("Input the number: \n"))        
        if guess==number_to_guess:
            print("Congratulations! You win!")
            break
        elif guess>number_to_guess:
            print("Your number is too big")
        else:
            print("Your number is too small")
        attempts_left= total_attempts-attempt_number
        if (attempts_left>0):
            print(f"{attempts_left} attempts left \n")
        attempt_number+=1
    else:
        print (f"You lost! The correct number was {number_to_guess}. Good luck next time.")            


if __name__ =="__main__":
    main()