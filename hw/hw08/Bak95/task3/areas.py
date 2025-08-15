import math

def rectangle_area(a, b):
    """Обчислює площу прямокутника S = a * b"""
    return a * b

def triangle_area(h, a):
    """Обчислює площу трикутника S = 0.5 * h * a"""
    return 0.5 * h * a

def circle_area(r):
    """Обчислює площу кола S = pi * r^2"""
    return math.pi * math.pow(r, 2)