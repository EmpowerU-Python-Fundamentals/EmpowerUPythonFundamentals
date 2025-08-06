from math import pi, pow

def areaOfRectangle(a: float, b: float):
    return f"The area of a rectangle {round(a * b)} cm²."

def areaOfTriangle(a: float, h: float):
    return f"The area of a rectangle {round(1/2 * a * h)} cm²."

def areaOfCircle(r: float):
    return f"The area of a circle {round(pi * pow(r, 2), 2)} cm²."