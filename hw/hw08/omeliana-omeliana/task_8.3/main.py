from area import circle_area, triangle_area, rectangle_area
from math import pi, pow

def main():
    shape = input("Please choose a shape:\n\ncircle - 1, triangle - 2, rectangle - 3\n ")

    if shape == '1':
        radius = float(input("Enter radius: "))
        area = circle_area(radius)
        print(f"Area of circle: {area}")

    elif shape == '2':
        base = float(input("Enter base: "))
        height = float(input("Enter height: "))
        area = triangle_area(base, height)
        print(f"Area of triangle: {area}")

    elif shape == '3':
        length = float(input("Enter length: "))
        width = float(input("Enter width: "))
        area = rectangle_area(length, width)
        print(f"Area of rectangle: {area}")2

    else:
        print("Invalid option.")

if __name__ == "__main__":
    main()