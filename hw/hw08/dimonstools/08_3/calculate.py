__all__ = ['area_rectangle', 'area_triangle', 'area_circle']

from math import pi, pow

def area_rectangle(a, b):
    return a * b

def area_triangle(a, h):
    return 0.5 * h * a

def area_circle(r):
    return pi * pow(r, 2)