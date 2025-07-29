import math

def rectangle_area(length, width):
    """Повертає площу прямокутника."""
    return length * width

def triangle_area(base, height):
    """Повертає площу трикутника."""
    return 0.5 * base * height

def circle_area(radius):
    """Повертає площу круга."""
    return math.pi * radius ** 2

# Основна програма
def main():
    print("Оберіть фігуру:\n1 - Прямокутник\n2 - Трикутник\n3 - Коло")
    choice = input("Ваш вибір: ")

    if choice == "1":
        l = float(input("Введіть довжину: "))
        w = float(input("Введіть ширину: "))
        print("Площа прямокутника:", rectangle_area(l, w))
    elif choice == "2":
        b = float(input("Введіть основу: "))
        h = float(input("Введіть висоту: "))
        print("Площа трикутника:", triangle_area(b, h))
    elif choice == "3":
        r = float(input("Введіть радіус: "))
        print("Площа круга:", circle_area(r))
    else:
        print("Невірний вибір!")

main()
