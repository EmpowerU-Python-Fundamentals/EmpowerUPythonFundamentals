"""Figure area calculation functions"""
from math import pi, pow


def rectangle_area(a: float, b: float) -> float:
    """Area calculation for rectangle"""
    return a * b


def triangle_area(a: float, h: float) -> float:
    """Area calculation for triangle"""
    return 0.5 * a * h


def circle_area(r: float) -> float:
    """Area calculation for circle"""
    return round(pi * pow(r, 2), 2)
