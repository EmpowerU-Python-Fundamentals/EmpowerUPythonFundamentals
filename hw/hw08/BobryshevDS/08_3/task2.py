#Напишіть програму, яка обчислює площу прямокутника, трикутника та кола (напишіть три функції для обчислення площі. 
#І викликайте їх у головній програмі залежно від вибору користувача).
import math

def rectangle_area(length, width):
    return length * width

def triangle_area(base, height):
    return 0.5 * base * height

def circle_area(radius):
    return math.pi * (radius ** 2)

def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Помилка: потрібно ввести число!")

def calculate_area(choice):
    if choice == '1':
        length = get_float("Введіть довжину прямокутника: ")
        width = get_float("Введіть ширину прямокутника: ")
        return rectangle_area(length, width)

    elif choice == '2':
        base = get_float("Введіть основу трикутника: ")
        height = get_float("Введіть висоту трикутника: ")
        return triangle_area(base, height)

    elif choice == '3':
        radius = get_float("Введіть радіус кола: ")
        return circle_area(radius)

    else:
        print("Некоректний вибір! Потрібно ввести 1, 2 або 3.")
        return None

def main():
    print("Оберіть фігуру для обчислення площі:")
    print("1. Прямокутник")
    print("2. Трикутник")
    print("3. Коло")

    choice = input("Введіть номер вибору (1/2/3): ")
    area = calculate_area(choice)

    if area is not None:
        print(f"Площа: {area}")

if __name__ == "__main__":
    main()