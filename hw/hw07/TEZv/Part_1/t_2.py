# --- Task 2: Calculate the area of different shapes ---
# This program contains three functions to calculate the area of a rectangle, triangle, and circle,
# and a main program that lets the user choose which one to run.

import math

def rectangle_area(length, width):
    """
    Обчислює площу прямокутника, використовуючи його довжину та ширину.

    Аргументи:
        length (float): Довжина прямокутника.
        width (float): Ширина прямокутника.

    Повертає:
        float: Площа прямокутника.
    """
    return length * width

def triangle_area(base, height):
    """
    Обчислює площу трикутника за його основою та висотою.

    Аргументи:
        base (float): Довжина основи трикутника.
        height (float): Висота трикутника.

    Повертає:
        float: Площа трикутника.
    """
    return (base * height) / 2

def circle_area(radius):
    """
    Обчислює площу кола за його радіусом.

    Аргументи:
        radius (float): Радіус кола.

    Повертає:
        float: Площа кола.
    """
    # Використання math.pi забезпечує вищу точність, ніж 3.14.
    return round(math.pi * radius ** 2, 2)

# Основна частина програми для взаємодії з користувачем
def main_area_calculator():
    """
    Пропонує користувачеві обрати фігуру та обчислює її площу.
    """
    try:
        print('This program calculates the area of different shapes. And you can test its usage!')
        choice = int(input('Enter 1, 2 or 3 to calculate the area of a rectangle, triangle, or circle: '))
        
        # Використання `match...case` для обробки вибору - це ефективний підхід.
        match choice:
            case 1:
                length = float(input('Enter length: '))
                width = float(input('Enter width: '))
                print(f"Rectangle area: {rectangle_area(length, width)}")
            case 2:
                base = float(input('Enter base: '))
                height = float(input('Enter height: '))
                print(f"Triangle area: {triangle_area(base, height)}")
            case 3:
                radius = float(input('Enter radius: '))
                print(f"Circle area: {circle_area(radius)}")
            case _:
                print("Invalid choice. Please enter 1, 2, or 3.")
    except ValueError:
        print("Invalid input. Please enter a number.")

# Запуск програми
if __name__ == "__main__":
    main_area_calculator()