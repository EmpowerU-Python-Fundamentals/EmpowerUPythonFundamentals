import math

def rectangle_area(length, width):
    """
    Обчислює площу прямокутника.

    Аргументи:
    length (float): довжина прямокутника
    width (float): ширина прямокутника

    Повертає:
    float: площа прямокутника
    """
    return length * width


def triangle_area(base, height):
    """
    Обчислює площу трикутника.

    Аргументи:
    base (float): основа трикутника
    height (float): висота трикутника

    Повертає:
    float: площа трикутника
    """
    return 0.5 * base * height


def circle_area(radius):
    """
    Обчислює площу кола.

    Аргументи:
    radius (float): радіус кола

    Повертає:
    float: площа кола
    """
    return math.pi * radius ** 2


def main():
    print("Оберіть фігуру для обчислення площі:")
    print("1. Прямокутник")
    print("2. Трикутник")
    print("3. Коло")

    choice = input("Ваш вибір (1/2/3): ")

    if choice == "1":
        length = float(input("Введіть довжину: "))
        width = float(input("Введіть ширину: "))
        area = rectangle_area(length, width)
        print(f"Площа прямокутника: {area}")
    elif choice == "2":
        base = float(input("Введіть основу: "))
        height = float(input("Введіть висоту: "))
        area = triangle_area(base, height)
        print(f"Площа трикутника: {area}")
    elif choice == "3":
        radius = float(input("Введіть радіус: "))
        area = circle_area(radius)
        print(f"Площа кола: {area}")
    else:
        print("Невірний вибір. Спробуйте ще раз.")

# Запуск головної функції
main()
