import random

secret_number = random.randint(1, 100)
attempts = 10

print("Я загадав число від 1 до 100. У тебе є 10 спроб, щоб його вгадати!")

for i in range(1, attempts + 1):
    guess = int(input(f"Спроба {i}: Введи своє число: "))

    if guess == secret_number:
        print(f"Вітаю! Ти вгадав число з {i}-ї спроби!")
        break
    elif guess < secret_number:
        print("Моє число більше.")
    else:
        print("Моє число менше.")

else:
    print(f"Гру завершено. Я загадав число {secret_number}.")