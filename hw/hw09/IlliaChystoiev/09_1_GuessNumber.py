import random

def guess_the_number():
    # Комп'ютер загадує число
    secret_number = random.randint(1, 100)
    attempts = 10

    print("\nГра 'Вгадай число'!\n")
    print("Я загадав число від 1 до 100. У тебе 10 спроб.")

    for attempt in range(1, attempts + 1):
        try:
            guess = int(input(f"\nСпроба {attempt}/{attempts}. Введи число: "))
        except ValueError:
            print("Будь ласка, введи ціле число.")
            continue

        if guess == secret_number:
            print(f"Вітаю! Ти вгадав число {secret_number} за {attempt} спроб.")
            break
        elif guess < secret_number:
            print("Загадане число більше.")
        else:
            print("Загадане число менше.")

        if attempt == attempts:
            print(f"\nНа жаль, ти не встиг. Загадане число було {secret_number}.")

