from  math import pi as PI

def calculate_circle_area(radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative.")
    return PI * pow(radius, 2)

def calculate_rectangle_area(height, base):
    if height < 0 or base < 0:
        raise ValueError("Height and base cannot be negative.")
    return height * base

def calculate_triangle_area(height, base):
    if height < 0 or base < 0:
        raise ValueError("Height and base cannot be negative.")
    return (height * base) / 2