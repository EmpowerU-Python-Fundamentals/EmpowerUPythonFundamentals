from math import pow, pi

def rectangle_area(a, b):
    '''This function calculates area of rectangle'''
    return round((a * b),1)

def triangle_area(a, h):
    '''This function calculates area of triangle by formula S = 0,5*h*a'''
    
    area = 0.5 * h * a
    return round(area,1)

def circle_area (radius):
    '''This function calculates area of circle'''
    return round((pi * pow(radius,2)),1)
