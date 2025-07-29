"""calculates areas"""
import math

def rectangle_area(length: int, width: int) -> int:
    """calculates the area of rectangle
    Args:
        length (int): length
        width (int): width
    Returns:
        int: final area
    """
    return length * width

def triangle_area(base: int, height: int) -> int:
    """calculates the area of trianle
    Args:
        base (int): base
        height (int): height

    Returns:
        int: final area
    """
    return 1/2 * base * height

def circle_area(radius: int, pi=3.14) -> int:
    """calculates the area of circle
    Args:
        radius (int): radius
        pi (float, optional): num pi. Defaults to 3.14.

    Returns:
        int: _final area
    """
    return math.pi * (math.pow(radius, 2))
