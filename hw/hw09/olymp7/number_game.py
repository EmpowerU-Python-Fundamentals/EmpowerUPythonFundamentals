import random


secret_num = random.randint(1, 100)
attempts = 10
num_attempt = 0

print("Вітаю Вас в грі. Я загадав число від 1 до 100, яке вам потрібно відгадати за 7 спроб.")

while num_attempt < attempts:
    try:
        guess_num = int(input("Введіть ваше припущення: "))
        num_attempt += 1

        if secret_num > guess_num:
            print("Занадто маленьке!!!")

        elif secret_num < guess_num:
            print("Занадто велике!!!")

        else:
            print(f"Вітаю ви вгадали число {secret_num} за {num_attempt} спроб.")
            break

    except ValueError:
        print("Будь ласка, введіть ціле число!")

if num_attempt == attempts and secret_num != guess_num:
    print(f"Гра закінчена!!! Ви не змогли вгадати число {secret_num} за {attempts} спроб.")