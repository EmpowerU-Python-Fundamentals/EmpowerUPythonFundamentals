import math


def calculate_area_rectangle(width: int | float = 0, height: int | float = 0):
    """
    Calculate the area of a rectangle.
    """
    return width * height


def calculate_area_triangle(base: int | float = 0, height: int | float = 0):
    """
    Calculate the area of a triangle.
    """
    return 0.5 * base * height


def calculate_area_circle(radius: int | float = 0):
    """
    Calculate the area of a circle.
    """
    return math.pi * radius**2


def prompt_and_calculate_area():
    """
    Prompt the user for a shape and calculate its area.
    Type of shape ('rectangle', 'triangle', 'circle')
    """
    shape = input("Type of shape ('rectangle', 'triangle', 'circle'): ").lower()
    if shape == "rectangle":
        width = float(input("Enter width: "))
        height = float(input("Enter height: "))
        return calculate_area_rectagle(width, height)
    if shape == "triangle":
        base = float(input("Enter base: "))
        height = float(input("Enter height: "))
        return calculate_area_triangle(base, height)
    if shape == "circle":
        radius = float(input("Enter radius: "))
        return calculate_area_circle(radius)
    raise ValueError("Unknown shape type")
