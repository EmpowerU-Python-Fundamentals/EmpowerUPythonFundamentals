import math

def rectangle_area(a, b):
    """Обчислює площу прямокутника"""
    return a * b

def triangle_area(base, height):
    """Обчислює площу трикутника"""
    return 0.5 * base * height

def circle_area(radius):
    """Обчислює площу кола"""
    return math.pi * math.pow(radius, 2)