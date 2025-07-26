from math import pi, pow

def rectangle_area(a: float, b: float):
    """
    Calculate the area of a rectangle
    """
    return a * b

def triangle_area(h: float, a: float):
    """
    Calculate the area of a triangle
    """
    return 0.5 * h * a

def circle_area(r: float):
    """
    Calculate the area of a circle
    """
    return pi * pow(r, 2)