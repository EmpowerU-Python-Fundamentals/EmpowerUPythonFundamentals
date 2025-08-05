import random
target = random.randint(1,100)
attempts = 10
print(f"Вітаю! Я загадав число від 1 до 100. Спробуй вгадати його за {attempts} спроб")
for i in range(attempts+1):
    print(i)
    if i == attempts:
        print(f"Спроби закінчились. Загадане число - {target}")
        # break
    number = int(input("Введіть ваше припущення:"))
    if number==target:
        print(f"Ви вгадали! Це число {target}")
        break
    elif number>target:
        print("Занадто велике!")
    elif number<target:
        print("Занадто маленьке!")