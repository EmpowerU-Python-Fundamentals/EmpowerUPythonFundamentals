import math
def area_rectangle(width, length): 
    if type(width) is int and type(length) is int:
        return width * length
    else:
        return None

def area_triangle_side_height(side, height):
    if type(side) is int and type(height) is int:
        return 1 / 2 * side * height
    else:
        return None

def area_circle(radius):   
    if type(radius) is int:
        return math.pi * math.pow(radius,2)
    else:
        return None