from math import pi, pow

def rectangle_area(a, b):
    """Calculate the area of a rectangle: S = a * b"""
    return a * b

def triangle_area(h, a):
    """Calculate the area of a triangle: S = 0.5 * h * a"""
    return 0.5 * h * a

def circle_area(r):
    """Calculate the area of a circle: S = pi * r^2"""
    return pi * pow(r, 2)