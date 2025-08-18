import random

def number_guessing_game():

    # Генеруємо випадкове число від 1 до 100
    target_number = random.randint(1, 100)
    attempts = 10
    attempts_used = 0

    print("🎮 Ласкаво просимо до гри 'Вгадай число'!")
    print("Я загадав число від 1 до 100. У вас є 10 спроб, щоб його відгадати.")
    print("-" * 50)

    while attempts_used < attempts:
        remaining_attempts = attempts - attempts_used
        print(f"Спроба {attempts_used + 1} з {attempts} (залишилось: {remaining_attempts})")

        try:
            # Отримуємо введення від користувача
            user_guess = int(input("Введіть ваше число: "))
            attempts_used += 1

            # Перевіряємо діапазон
            if user_guess < 1 or user_guess > 100:
                print("Будь ласка, введіть число від 1 до 100!")
                continue

            # Порівнюємо з загаданим числом
            if user_guess == target_number:
                print(f"Вітаємо! Ви відгадали число {target_number}!")
                print(f"Ви використали {attempts_used} спроб з {attempts}.")
                return
            elif user_guess < target_number:
                print("Загадане число більше за ваше.")
            else:
                print("Загадане число менше за ваше.")

        except ValueError:
            print("Будь ласка, введіть коректне число!")
            continue

        print("-" * 30)

    # Якщо спроби закінчились
    print(f"Спроби закінчились! Загадане число було: {target_number}")
    print("Спробуйте ще раз!")


def main():
    """Головна функція програми"""
    while True:
        number_guessing_game()

        # Питаємо чи хоче користувач грати знову
        play_again = input("\nХочете зіграти ще раз? (y/n): ").lower().strip()
        if play_again not in ['y', 'yes', 'так', 'т']:
            print("Дякую за гру!")
            break
        print("\n" + "=" * 50 + "\n")


if __name__ == "__main__":
    main()