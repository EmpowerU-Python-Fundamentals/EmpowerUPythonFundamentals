"""This modules contains functions for calculating area of rectangle, triagnle, and circle."""
__all__ = ["calculate_area_circle", "calculate_area_rectangle", "calculate_area_triangle"]

import math

def calculate_area_circle(r):
    """This function calculates the area of circle."""
    return math.pi * math.pow(r, 2)

def calculate_area_rectangle(height, width):
    """This function calculates the area of rectangle."""
    return height * width

def calculate_area_triangle(height, side):
    """This function calculates the area of triangle."""
    return (height * side) / 2