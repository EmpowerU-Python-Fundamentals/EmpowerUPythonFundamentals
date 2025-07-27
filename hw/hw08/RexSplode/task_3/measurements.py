from math import pi, pow
import re as regex

def is_not_number(*inputs: float) -> bool:
    number_pattern = regex.compile(r'^-?(?:\d+\.\d+|\d+)$')
    for input in inputs: 
        if not number_pattern.match(input):
            return True
    return False

def calc_triangle_area(base: float, height: float) -> float:
    if is_not_number(base, height):
        print("One of the params wasn't a number")
        return 0.0
    return round(0.5 * float(base) * float(height), 2)

def calc_square_area(side1: float, side2: float) -> float:
    if is_not_number(side1, side2):
        print("One of the params wasn't a number")
        return 0.0
    return round(float(side1) * float(side2), 2)

def calc_circle_area(radius: float) -> float:
    if is_not_number(radius):
        print("The parameter you entered is not a number")
        return 0.0
    return round(pow(float(radius), 2) * pi)




