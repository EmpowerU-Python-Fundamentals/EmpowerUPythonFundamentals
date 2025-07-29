"""09.1 Practical tasks. Guess the number game"""

import random

randint = random.randint(1,100)
i = 0
game_won = False
MAX_TRIES = 10

print("Вітаю! Я загадав число від 1 до 100. Спробуйте вгадати його за " + str(MAX_TRIES) + " спроб.")
#print(str(randint))
while i < MAX_TRIES:
    guess = int(input("Введіть ваше припущення: "))
    if guess < randint:
        print("Занадто маленьке!")
    elif guess > randint:
        print("Занадто велике!")
    else:
        game_won = True
    i += 1

if game_won:
    print("Ви вгадали! Це число " + str(randint) + ".")
else:
    print("Ви програли! Це було число " + str(randint) + ".")
