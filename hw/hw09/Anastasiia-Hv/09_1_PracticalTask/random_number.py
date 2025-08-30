import random

def guess_the_number():
    number_to_guess = random.randint(1, 100)
    attempts = 10
    
    print("Ласкаво просимо до гри «Вгадай число»!")
    print("Я вибрав число від 1 до 100.")
    print("У вас є 10 спроб, щоб вгадати.\n")
    
    for attempt in range(1, attempts + 1):
        try:
            guess = int(input(f"Спроба {attempt}. Введіть своє припущення:"))
        except ValueError:
            print("Будь ласка, введіть дійсний номер!")
            continue
        
        if guess == number_to_guess:
            print(f"🎉Вітаємо! Ви вгадали число {number_to_guess} з {attempt} спроби!")
            break
        elif guess < number_to_guess:
            print("Моє число більше, ніж ти гадаєш.")
        else:
            print("Моє число менше, ніж ти гадаєш.")
    else:
        print(f"😢Вибачте, ви використали всі {attempts} спроб. Число було {number_to_guess}.")

guess_the_number()