import random

START = 1
FINISH = 100
ATTEMPTS = 10

def main(): 
    number = random.randint(START, FINISH)

    print(f"Вітаю! Я загадав число від {START} до {FINISH}. Спробуй вгадати його за {ATTEMPTS} спроб.")
    
    for _ in range(ATTEMPTS):
        guess = input("Введи своє припущення: ").strip()
        try:
            g_int = int(guess)
        except (ValueError, TypeError):
            print(f"'{guess}' не вдалося конвертувати у число. Будь ласка, спробуй ще раз.")
            continue
        if g_int == number:
            print(f"Ти відгадав! Це число {number}!")
            another_trial()
        elif g_int < number:
            print("Занадто маленьке!")
        else:
            print("Занадто велике!")
            
    print(f"Сумно, ти не відгадав... Це число {number}.")
    another_trial()
    
    
def another_trial():
    trial = input("Спробуєш ще раз? Т/н ").strip().lower()
    if trial == "т":
        main()
    elif trial == "н":
        exit("До зустрічі у новій грі!")
    else:
        print("Не вдалося розпізнати ввід.") 
        another_trial()   


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        exit("\nДо зустрічі у новій грі!")
        