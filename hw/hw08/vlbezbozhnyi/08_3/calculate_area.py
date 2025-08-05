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
    return math.pi * math.pow(radius, 2), 2


__all__ = [
    "calculate_area_rectangle",
    "calculate_area_triangle",
    "calculate_area_circle",
]
