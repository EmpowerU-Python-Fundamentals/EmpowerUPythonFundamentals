'''Це гра в вгадування числа за 10 спроб'''
import  random

the_number = random.randint(1, 100)
USER_TRY = 10

print('Вітаю! Я загадав число від 1 до 100. Спробуйте вгадати його за 7 спроб.')
while True:
    # Перевіряємо чи залишились спроби
    if USER_TRY == 0:
        print(f'Всі спроби вичерпано. Це було число {the_number}.')
        break

    attempt = input('Введіть ваше припущення: ')
    # Перевіряємо чи користувач ввів ціле число і в межах
    try:
        attempt = int(attempt)
        if attempt < 1 or attempt > 100:
            print('Введіть число в межах від 1 до 100 будь ласка!')
            continue
    except ValueError:
        print('Введіть будь ласка ціле число!')
        continue
    # перевіряємо чи число збігається
    if attempt > the_number:
        print('Занадто велике!')
        USER_TRY -= 1
    elif attempt < the_number:
        print('Занадто маленьке!')
        USER_TRY -= 1
    else:
        print(f'Ви вгадали! Це число {the_number}.')
        break
