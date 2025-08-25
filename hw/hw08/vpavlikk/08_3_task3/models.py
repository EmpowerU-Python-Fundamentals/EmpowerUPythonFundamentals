import math


def calculate_triangle(width, height):
    if width is None or height is None:
        return "Missing width or height for triangle"
    return print(f"The triangle area is {0.5 * width * height}")


def calculate_rectangle(width, height):
    if width is None or height is None:
        return "Missing width or height for rectangle"
    return print(f"The rectangle area is {width * height}")


def calculate_circle(radius):
    if radius is None:
        return "Missing radius for circle"
    return print(f"The circle radius is {math.pi * math.pow(radius, 2)}")
