import random

desired_number = random.randint(1, 100)
attempts = 10

print(
    f"Привіт, я загадав число від 1 до 100. Спробуй відгадати його за {attempts} спроб."
)

for attempt in range(1, attempts + 1):
    while True:
        try:
            user_number = int(
                input(f"Спроба {attempt}/{attempts}, введіть своє припущення: ")
            )
            break
        except ValueError:
            print("Будь ласка введіть ціле число.")
    if user_number > desired_number:
        print("Занадто велике!")
    elif user_number < desired_number:
        print("Занадто маленьке!")
    elif user_number == desired_number:
        print(f"Вгадали! Це число {desired_number}.")
        break
else:
    print(f"Наступного разу пощастить, потрібне число - {desired_number}")
