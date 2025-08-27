# 07.1.2 Practical Tasks
# Write a program that calculates the area of ​​a rectangle, triangle and circle 
# Write three functions to calculate the area. 
# Call them in the main program deending on the user`s choice.

import math

def rectangle_area(length: float, width: float) -> float:
    """Обчислює площу прямокутника"""
    return length * width

def triangle_area(base: float, height: float) -> float:
    """Обчислює площу трикутника за основою та висотою"""
    return 0.5 * base * height

def circle_area(radius: float) -> float:
    """Обчислюэ площу кола"""
    return math.pi * radius ** 2

def main():
    print("Оберыть фыгуру для обчислення площі:")
    print("1 - Трикутник")
    print("2 - Прямокутник")
    print("3 - Коло")

    choice = input("Ваш вибір 1, 2 або 3): ")

    match choice:
        case "1":
            base = float(input("Введіть основу: "))
            height = float(input("Введіть висоту: "))
            print("Площа трикутника:", triangle_area(base, height))
        
        case "2":
            a = float(input("Введіть довжину: "))
            b = float(input("Введіть  шиину: "))
            print("Площа прямокутника:", rectangle_area(a, b))

        case "3":
            radius = float(input("Введіть радіус: "))
            print("Площа кола:", circle_area(radius))

        case _:
            print("Неправильний вибір")


if __name__ == "__main__":
    main()