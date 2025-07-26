# Task2.
# Write a program that calculates the area of a rectangle, triangle and circle
# (write three functions to calculate the area. 
#   And call them in the main program depending on the user's choice).

from math import pi
from math import sin
from math import sqrt

def rect_area_calc():
    """Calculates the area of a rectangle by it's height and width."""
    height = float(input("Enter the height of the rectangle: "))
    widht = float(input("Enter the width of the rectangle: "))
    return height * widht

def triangle_area_calc():
    """Calculates the area of a triangle by it's characteristics
    (three variants in dialogue mode)."""
    print("What do you know about the triangle:")
    print("1 - height and base")
    print("2 - two sides and the angle between them")
    print("3 - lengths of all three sides")
    choice = input("Enter your choice: ")

    match choice:
        case "1":
            height = float(input("Enter the height of the triangle: "))
            base = float(input("Enter the base of the triangle: "))
            return 0.5 * height * base
        case "2":
            side1 = float(input("Enter the 1st side length: "))
            side2 = float(input("Enter the 2nd side length: "))
            angle = float(input("Enter the angle (in degrees) between the sides: "))
            return 0.5 * side1 * side2 * sin(angle / 180 * pi)
        case "3":
            side1 = float(input("Enter the 1st side length: "))
            side2 = float(input("Enter the 2nd side length: "))
            side3 = float(input("Enter the 3rd side length: "))
            half_perimeter = 0.5 * (side1 + side2 + side3)
            return sqrt(half_perimeter 
                        * (half_perimeter - side1)
                        * (half_perimeter - side2)
                        * (half_perimeter - side3)
                        )
        case _:
            print("Invalid input. Read carefully next time.")


def circle_area_calc():
    """Calculates the area of a circle by it's radius."""
    radius = float(input("Enter the radius of the circle: "))
    return pi * radius**2


# main
options = {
    "1": "rectangle",
    "2": "triangle",
    "3": "circle"
    }

calculators = {
    "1": rect_area_calc,
    "2": triangle_area_calc,
    "3": circle_area_calc
    }

print("")
print("Available figure types to calculate the area:")
for item in options:
    print(f"{item} - {options[item]}")

choice = input("Enter your choice: ")
keys = options.keys()
if choice not in keys:
    print(f"Invalid choice. Next time enter one of the following: {", ".join(keys)}")
    print()
    exit()

area = calculators[choice]()
if area is not None:
    print(f"The area of the {options[choice]} is: {area}")
print()