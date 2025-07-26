'''This module contains function to calculate areas of rectangle, triangle and circle'''
__all__ = ['ar_circle', 'ar_rectng', 'ar_triangle']

import math

def ar_circle(radius):
    '''This func accept radius and return the area of circle'''
    return math.pi * pow(radius, 2)

def ar_rectng(higth, width):
    '''This func accept higth and width then return the area of rectangle'''
    return higth * width

def ar_triangle(higth, side):
    '''This func accept higth and side then return the area of triangle'''
    return 0.5 * higth * side
