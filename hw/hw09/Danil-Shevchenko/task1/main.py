import random

random_number=random.randint(1,100)
counter=0
print('Вітаю! Я загадав число від 1 до 100. Спробуйте вгадати його за 10 спроб. ')
while True:
    guess_number = int(input('Введіть ваше припущення: '))
    counter = counter + 1
    if random_number == guess_number:
        print(f'Ви вгадали. Це число {random_number} ')
        break
    elif random_number > guess_number:
        print(f'Занадто маленьке!')
    else:
        print(f'Занадто велике!')
    if random_number != guess_number and counter > 10: 
        print(f'Ви приграли. Це число {random_number} ')
        break