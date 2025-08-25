from random import randint

def greet_user():
    print("Вітаю! Я загадав число від 1 до 100. Спробуйте вгадати його за 7 спроб.")

def get_guess(attempt):
    while True:
        try:
            guess = int(input(f"\nСпроба {attempt}: Введіть ваше припущення: "))
            if 1 <= guess <= 100:
                return guess
            else:
                print("Введіть число в діапазоні від 1 до 100.")
        except ValueError:
            print("Будь ласка, введіть ціле число.")

def give_feedback(guess, secret_number):
    if guess < secret_number:
        print("Занадто маленьке!")
    elif guess > secret_number:
        print("Занадто велике!")
    else:
        print(f"Ви вгадали! Це число {secret_number}!")

def play_game():
    secret_number = randint(1, 100)
    max_attempts = 7
    greet_user()

    for attempt in range(1, max_attempts + 1):
        guess = get_guess(attempt)
        if guess == secret_number:
            give_feedback(guess, secret_number)
            return
        else:
            give_feedback(guess, secret_number)

    print(f"\n Ви не вгадали. Загадане число було: {secret_number}")
    
play_game()