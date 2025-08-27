import random

def game():
    num=random.randint(1, 100) # Random number
    ATTEMPTS = 10 # Number of attempts

    print("Welcome to the game! You have 10 attempts to guess the number between 1 and 100."
          " Good luck!" )
    
    for i in range(1, ATTEMPTS+1):
        guess = int(input(f"Attempt {i}: Enter your guess: "))
        
        if guess == num:
            print(f"Congratulations! You guessed the number {num}!"
                  f"You win! you correctly guessed the number in {i} attempts.")
            break
        elif guess < num:
            print("Your guess is too low. Try again.") 
        else:
            print("Your guess is too high. Try again.")
    else:
        print(f"GAME OVER. "
              f"The correct number was {num}. Better luck next time!")
        
ok = True
while ok:
    game()
    ok = input("Do you want to play again? (yes/no): ").strip().lower() == 'yes'
    if not ok:
        print("Thank you for playing! Goodbye!")
        break