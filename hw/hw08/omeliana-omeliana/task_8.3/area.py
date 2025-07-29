from math import pi, pow

def circle_area(radius):
    """Calculate the area of a circle"""
    return round(pi * pow(radius, 2), 2)

def triangle_area(base, height):
    """Calculate the area of a triangle"""
    return round(0.5 * base * height, 2)

def rectangle_area(length, width):
    """Calculate the area of a rectangle"""
    return round(length * width, 2)