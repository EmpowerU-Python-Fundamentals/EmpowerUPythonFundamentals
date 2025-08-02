from math import pow, pi

def rectangle_area(a: float, b: float) -> float:
    return round((a * b),1)

def triangle_area(a: float, h: float) -> float:
    area = 0.5 * h * a
    return round(area,1)

def circle_area (radius: float) -> float:
    return round((pi * pow(radius,2)),1)
