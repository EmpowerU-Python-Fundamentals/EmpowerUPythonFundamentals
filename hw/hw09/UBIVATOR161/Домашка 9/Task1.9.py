import random
s = random.randint(1, 100)
m = 10
print("Вгадай число від 1 до 100. У тебе є 10 спроб!")
for i in range(1, max_tries + 1):
    try:
        guess = int(input(f"Спроба {i}: Введи число: "))
    except ValueError:
        print("Будь ласка, введи коректне число.")
        continue

    if g < s:
        print("Загадане число більше.")
    elif g > s:
        print("Загадане число менше.")
    else:
        print(f"Вітаю! Ти вгадав число {s} з {i} спроби.")
        break
else:
    print(f"На жаль, ти не вгадав. Загадане число було {s}.")