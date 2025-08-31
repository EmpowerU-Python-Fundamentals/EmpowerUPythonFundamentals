"""This modules contains functions for calculating area of rectangle, triagnle, and circle."""
__all__ = ["calculate_area_circle", "calculate_area_rectangle", "calculate_area_triangle"]

import math

def calculate_area_circle(r):
    """This function calculates the area of circle."""
    return math.pi * math.pow(r, 2)

def calculate_area_rectangle(higth, width):
    """This function calculates the area of rectangle."""
    return higth * width

def calculate_area_triangle(higth, side):
    """This function calculates the area of triangle."""
    return 0.5 * higth * side