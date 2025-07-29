from math import pi
from math import pow

def calculate_rectangle_area(a: float, b: float) -> float:
    """Calculates the area of a rectangle by it's height and width."""
    return a * b

def calculate_triangle_area(h: float, a: float) -> float:
    """Calculates the area of a triangle by it's height and base"""
    return 0.5 * h * a

def calculate_circle_area(r: float) -> float:
    """Calculates the area of a circle by it's radius."""
    return pi * r * pow(r, 2)