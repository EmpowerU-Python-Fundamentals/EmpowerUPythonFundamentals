"""08.3 Practical tasks. Calculate area module """

import math

def rectangle_area(x):
    """Function calculates area of a reactangle"""
    return round(x[0] * x[1], 2)

def triangle_area(x):
    """Function calculates area of a triangle"""
    return round(x[0] * x[1] / 2, 2)

def circle_area(x):
    """Function calculates area of a circle"""
    return round(math.pi * math.pow(x[0], 2), 2)
