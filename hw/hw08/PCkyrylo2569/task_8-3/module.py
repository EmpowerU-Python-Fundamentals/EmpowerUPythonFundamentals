import math

def area_of_rectangle(length: float, width: float) -> float:
    return length * width

def area_of_triangle(base: float, height: float) -> float:
    return 0.5 * base * height

def area_of_circle(radius: float) -> float:
    return math.pi * pow(radius, 2)
