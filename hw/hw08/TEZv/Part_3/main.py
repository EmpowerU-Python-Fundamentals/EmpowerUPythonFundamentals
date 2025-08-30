# Цей файл є основною програмою, яка використовує функції з area.py.

from area import *

def main_program():
    """
    Головна функція, яка взаємодіє з користувачем і обчислює площу фігур.
    """
    print("This program calculates the area of different shapes. And you can test its usage!")
    print("Choose a shape to calculate its area:")
    print("1. Rectangle")
    print("2. Triangle")
    print("3. Circle")

    try:
        choice = int(input("Your choice (1, 2, or 3): "))

        match choice:
            case 1:
                length = float(input("Enter length: "))
                width = float(input("Enter width: "))
                area = area_rectangle(length, width)
                print(f"Rectangle area is: {round(area, 2)}")
            case 2:
                base = float(input("Enter basis: "))
                height = float(input("Enter height: "))
                area = area_triangle(base, height)
                print(f"Triangle area is: {round(area, 2)}")
            case 3:
                radius = float(input("Enter radius: "))
                area = area_circle(radius)
                print(f"Circle area is: {round(area, 2)}")
            case _:
                print("Wrong choice. Please enter 1, 2, or 3.")

    except ValueError:
        print("Wrong input. Please enter a valid number.")

if __name__ == "__main__":
    main_program()