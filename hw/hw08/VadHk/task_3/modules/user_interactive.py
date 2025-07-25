from utils.figures_area import *


def main():
    request = input("Enter the figure type (circle, rectangle, triangle): ").strip().lower()   
    
    match request:
        case "circle":
            radius = float(input("Enter the radius of the circle: "))
            area = calculate_circle_area(radius)
            print(f"The area of the circle is: {area:.2f}")
        case "rectangle":
            height = float(input("Enter the height of the rectangle: "))
            base = float(input("Enter the base of the rectangle: "))
            area = calculate_rectangle_area(height, base)
            print(f"The area of the rectangle is: {area:.2f}")
        case "triangle":
            height = float(input("Enter the height of the triangle: "))
            base = float(input("Enter the base of the triangle: "))
            area = calculate_triangle_area(height, base)
            print(f"The area of the triangle is: {area:.2f}")
        case _:
            print("Invalid figure type. Please enter 'circle', 'rectangle', or 'triangle'.")
            return