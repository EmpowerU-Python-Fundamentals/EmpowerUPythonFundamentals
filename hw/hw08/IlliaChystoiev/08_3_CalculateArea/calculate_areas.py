from math import pi, pow

def rectangle_area(length, width):
    """Площа прямокутника S = length * width"""
    return length * width

def triangle_area(base, height):
    """Площа трикутника S = 0.5 * base * height"""
    return 0.5 * base * height

def circle_area(radius):
    """Площа кола S = π * r²"""
    return pi * pow(radius, 2)

