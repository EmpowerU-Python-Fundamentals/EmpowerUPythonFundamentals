import random

def guess_number_game():
    # Генеруємо випадкове число від 1 до 100
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10
    
    print("Ласкаво просимо до гри 'Вгадай число'!")
    print(f"Я загадав число від 1 до 100. У вас є {max_attempts} спроб, щоб його вгадати!")
    print("Готові? Почнемо! \n")
    
    while attempts < max_attempts:
        try:
            # Отримуємо введення від користувача
            user_guess = int(input(f"Спроба {attempts + 1}/{max_attempts}. Введіть ваше число: "))
            attempts += 1
            
            # Перевіряємо введене число
            if user_guess == secret_number:
                print(f"Вітаю! Ви вгадали число {secret_number} за {attempts} спроб!")
                if attempts <= 3:
                    print("Неймовірно! Ви справжній майстер!")
                elif attempts <= 6:
                    print("Чудова робота!")
                else:
                    print("Добре зіграно!")
                return
            elif user_guess < secret_number:
                remaining = max_attempts - attempts
                if remaining > 0:
                    print(f"Загадане число БІЛЬШЕ за {user_guess}. Залишилось спроб: {remaining}")
                else:
                    print(f"Загадане число БІЛЬШЕ за {user_guess}.")
            else:
                remaining = max_attempts - attempts
                if remaining > 0:
                    print(f"Загадане число МЕНШЕ за {user_guess}. Залишилось спроб: {remaining}")
                else:
                    print(f"Загадане число МЕНШЕ за {user_guess}.")
                    
        except ValueError:
            print("Будь ласка, введіть правильне число!")
            continue
    
    # Якщо всі спроби вичерпані
    print(f"\nНа жаль, ви не вгадали число за {max_attempts} спроб.")
    print(f"Загаданим числом було: {secret_number}")
    print("Спробуйте ще раз! Удачі!")

def main():
    while True:
        guess_number_game()
        play_again = input("\nХочете зіграти ще раз? (так/ні): ").lower().strip()
        if play_again not in ['так', 'yes', 'y', 'да']:
            print("Дякуємо за гру! До побачення! 👋")
            break
        print("\n" + "="*50 + "\n")

if __name__ == "__main__":
    main()