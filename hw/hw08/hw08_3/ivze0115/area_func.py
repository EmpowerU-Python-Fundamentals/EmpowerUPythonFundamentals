from math import pi, pow

def rectangle_area(length, width):
    """Return area of rectangle."""
    return length * width

def triangle_area(base, height):
    """Return area of triangle."""
    return 0.5 * base * height

def circle_area(radius):
    """Return area of circle."""
    return pi * pow(radius, 2)
