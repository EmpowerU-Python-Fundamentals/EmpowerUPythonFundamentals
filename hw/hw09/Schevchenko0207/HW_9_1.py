import random


def guess_the_number():
    """
    Plays a number guessing game where the user has 10 attempts to guess
    a randomly generated number between 1 and 100.
    """
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10

    print("Ласкаво просимо до гри 'Вгадай число'!")
    print(
        f"Я загадав число від 1 до 100. У вас є {max_attempts} спроб, щоб його вгадати."
    )

    while attempts < max_attempts:
        try:
            user_guess = int(
                input(f"Спроба {attempts + 1}/{max_attempts}. Введіть ваше число: ")
            )

            # Validate the input number
            if not (1 <= user_guess <= 100):
                print("Будь ласка, введіть число від 1 до 100.")
                continue  # Ask for input again without counting as an attempt

            attempts += 1  # Increment attempt count only for valid guesses

            if user_guess == secret_number:
                print(
                    f"🎉 Вітаємо! Ви вгадали число {secret_number} за {attempts} спроб!"
                )
                break  # Exit the loop if the number is guessed
            elif user_guess < secret_number:
                print("Занадто мало! Спробуйте більше число.")
            else:
                print("Занадто багато! Спробуйте менше число.")

        except ValueError:
            print("Невірний ввід. Будь ласка, введіть ціле число.")
            # Do not increment attempts for invalid input type, let them try again

    else:
        # This block executes if the while loop finishes without a 'break' (i.e., attempts exhausted)
        print(
            f"\nКінець гри! У вас закінчилися спроби. Загадане число було: {secret_number}."
        )


# Start the game
if __name__ == "__main__":
    guess_the_number()
