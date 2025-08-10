from random import randint


def start_game(number):
    user_count = 1
    print("Type number between 1 and 100: ")
    while True:
        user_number = int(input(f"Your attempt is {user_count}: "))
        if number == user_number:
            print(f"You guessed the number on the {user_count} try. You won.")
            break
        if user_number > number:
            print('The number entered is greater than the guessed one')
        else:
            print("The number entered is less than the guessed one")
        user_count += 1
        if user_count > 10:
            print("You lost, number of attempts 10")
            break


if __name__ == "__main__":
    guess_number = randint(1, 100)
    start_game(guess_number)