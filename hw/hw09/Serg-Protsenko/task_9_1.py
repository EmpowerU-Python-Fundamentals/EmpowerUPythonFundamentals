import random

# Генеруємо випадкове число від 1 до 100
secret_number = random.randint(1, 100)
attempts = 10

print("Я загадав число від 1 до 100. У тебе є 10 спроб, щоб вгадати його!")

for i in range(1, attempts + 1):
    try:
        guess = int(input(f"Спроба {i}: Введи своє число: "))
    except ValueError:
        print("Будь ласка, введи коректне число!")
        continue

    if guess < secret_number:
        print("Загадане число більше.")
    elif guess > secret_number:
        print("Загадане число менше.")
    else:
        print(f"Вітаю! Ти вгадав число за {i} спроб!")
        break
else:
    print(f"На жаль, ти не вгадав. Загадане число було {secret_number}.")
