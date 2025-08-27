import random

random_number = random.randint(1, 100)
tries_count = 0 
while True:
    user_input = input("Guess a number between 1 and 100 (or type 'exit' to quit): ")
    if user_input.lower() == 'exit':
        print("Thanks for playing!")
        break
    try:
        guess = int(user_input)
        if guess < 1 or guess > 100:
            print("Please guess a number within the range of 1 to 100.")
            continue
        if guess < random_number:
            print("Too low! Try again.")
        elif guess > random_number:
            print("Too high! Try again.")
        else:
            print("Congratulations! You've guessed the correct number.")
            break
        tries_count += 1
        if tries_count >= 10:
            print(f"Sorry, you've used all your tries. The correct number was {random_number}.")
            break
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 100 or 'exit' to quit.")