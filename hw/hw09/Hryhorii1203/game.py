import random


def guess_number():
    secret_number = random.randint(1, 100)
    attempts = 10

    print("Вгадай чісло від 1 до 100 за 10 спроб!")

    for attempt in range(1, attempts + 1):
        try:
            guess = int(input(f"Спроба {attempt}. Введіть число: "))
        except ValueError:
            print("Помилка! Введіть ціле число.")
            continue

        if guess == secret_number:
            print(f"Вітаю! Ви вгадали число {secret_number} за {attempt} спроб!")
            return
        elif guess < secret_number:
            print("Загаданне число більше.")
        else:
            print("Загаданне число меньше.")

    print(f"УПС! Ви вичерпали всі свої спроби. Число було: {secret_number}.")


if __name__ == "__main__":
    guess_number()