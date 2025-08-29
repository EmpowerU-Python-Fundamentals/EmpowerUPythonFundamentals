import math

def rectangle_area(a, b):
    """
    Обчислює площу прямокутника S = a * b
    """
    return round( a * b , 4)

def triangle_area(a, h):
    """
    Обчислює площу трикутника S = 0.5 * a * h
    """
    return round( 0.5 * a * h , 4) 

def circle_area(r):
    """
    Обчислює площу круга S = pi * r**2
    """
    return round(math.pi * math.pow(r, 2), 4)