# area_calculations.py

from math import pi, pow

def area_rectangle(length, width):
    """
    Calculates the area of a rectangle.
    S = length * width
    """
    return length * width

def area_triangle(base, height):
    """
    Calculates the area of a triangle.
    S = 0.5 * base * height
    """
    return 0.5 * base * height

def area_circle(radius):
    """
    Calculates the area of a circle.
    S = pi * r**2
    """
    return pi * pow(radius, 2)