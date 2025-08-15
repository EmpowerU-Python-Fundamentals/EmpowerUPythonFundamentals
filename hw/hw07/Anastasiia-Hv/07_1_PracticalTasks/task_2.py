import math

def rectangle_area(length, width):
    return length * width

def triangle_area(base, height):
    return 0.5 * base * height

def circle_area(radius):
    return math.pi * radius ** 2

print("Виберіть фігуру для обчислення площі:")
print("1 - Прямокутник")
print("2 - Трикутник")
print("3 - Коло")

choice_user = input("Введіть ваш вибір: ")

if choice_user == "1":
    length = float(input("Введіть довжину: "))
    width = float(input("Введіть ширину: "))
    print("Площа прямокутника:", rectangle_area(length, width))

elif choice_user == "2":
    base = float(input("Введіть основу: "))
    height = float(input("Введіть висоту: "))
    print("Площа трикутника:", triangle_area(base, height))

elif choice_user == "3":
    radius = float(input("Введіть радіус: "))
    print("Площа кола:", circle_area(radius))

else:
    print("Невірний вибір!")