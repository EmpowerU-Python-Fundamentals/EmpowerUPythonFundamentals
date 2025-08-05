from calculate_area import *


def prompt_and_calculate_area():
    """
    Prompt the user for a shape and calculate its area.
    Type of shape ('rectangle', 'triangle', 'circle')
    """
    shape = input("Type of shape ('rectangle', 'triangle', 'circle'): ").lower()
    if shape == "rectangle":
        width = float(input("Enter width: "))
        height = float(input("Enter height: "))
        return calculate_area_rectangle(width, height)
    if shape == "triangle":
        base = float(input("Enter base: "))
        height = float(input("Enter height: "))
        return calculate_area_triangle(base, height)
    if shape == "circle":
        radius = float(input("Enter radius: "))
        return calculate_area_circle(radius)
    raise ValueError("Unknown shape type")


print(prompt_and_calculate_area())
