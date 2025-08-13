from math import pow, pi
from areas_of_figures import *

def main():
    print("Choose a shape to calculate the area:")
    print("1. Rectangle")
    print("2. Triangle")
    print("3. Circle")

    choice = input("Enter your choice (1/2/3): ")

    match choice:
        case "1":
            print("You selected rectangle")
            width = int(input("Enter the width of the rectangle: "))
            length = int(input("Enter the length of the rectangle: "))
            print("Area of a rectangle =", get_area_of_rectangle(width, length))
        case "2":
            print("You selected triangle")
            height = int(input("Enter the height of the triangle: "))
            base = int(input("Enter the base of the triangle: "))
            print("Area of a triangle =", get_area_of_triangle(height, base))
        case "3":
            print("You selected circle")
            r = int(input("Enter the radius of the circle: "))
            print("Area of a circle =", get_area_of_circle(pi, r))
        case _:
            print("Unknown shape selected.")

main()