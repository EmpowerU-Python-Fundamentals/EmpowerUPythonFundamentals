import math

print("Виберіть фігуру для обчислення площі:")
print("1. Прямокутник")
print("2. Трикутник")
print("3. Коло")

choice = input("Введіть ваш вибір (1/2/3): ")

if choice == '1':
    length = float(input("Введіть довжину: "))
    width = float(input("Введіть ширину: "))
    area = length * width
    print(f"Площа прямокутника: {area}")
elif choice == '2':
    base = float(input("Введіть основу: "))
    height = float(input("Введіть висоту: "))
    area = 0.5 * base * height
    print(f"Площа трикутника: {area}")
elif choice == '3':
    radius = float(input("Введіть радіус: "))
    area = math.pi * radius**2
    print(f"Площа кола: {area}")
else:
    print("Невірний вибір. Будь ласка, спробуйте ще раз.")