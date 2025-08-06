from math import pi, pow

def rectanlegle_area(length, width):
    '''Rectangle area'''
    return length * width

def triangle_area(base, height):
    '''Triangle area'''
    return (base * height) / 2

def circle_area(radius):
    '''Circle area'''
    return round(pow(pi * radius, 2), 2)