# Цей файл містить функції для обчислення площі.
# У реальному проекті це був би окремий модуль.

import math

def area_rectangle(length, width):
    """
    Обчислює площу прямокутника.
    
    Аргументи:
        length (float): Довжина прямокутника.
        width (float): Ширина прямокутника.
        
    Повертає:
        float: Площа прямокутника.
    """
    return length * width

def area_triangle(base, height):
    """
    Обчислює площу трикутника.
    
    Аргументи:
        base (float): Основа трикутника.
        height (float): Висота трикутника.
        
    Повертає:
        float: Площа трикутника.
    """
    return 0.5 * base * height

def area_circle(radius):
    """
    Обчислює площу кола.
    
    Аргументи:
        radius (float): Радіус кола.
        
    Повертає:
        float: Площа кола.
    """
    return math.pi * (radius ** 2)

# __all__ визначає, які імена будуть імпортовані при 'from area import *'
__all__ = ["area_rectangle", "area_triangle", "area_circle"]