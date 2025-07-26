'''homework by Astronaut-08'''

def area_circle(radius: float):
    '''The func acces a radius of circle and return the area'''
    if isinstance(radius, str):
        return 'Wrong type of radius'
    return 3.14 * radius**2

def area_rectangle(length: float, width: float):
    '''The func acces a length and width of rectangle and return the area'''
    if isinstance(length, str) or isinstance(width, str):
        return 'Wrong type of length or width'
    return length * width

def area_triangle(side1: float, side2: float, side3: float):
    '''The func acces a length three sides of triangle and return the area'''
    if str in (type(side1), type(side2), type(side3)):
        return 'Wrong type of length'
    s = (side1 + side2 + side3) / 2 #It's semiperimetr
    return (s * (s - side1) * (s - side2) * (s - side3)) * 0.5

print('Area of circle: ', area_circle(5))
print('Area of rectangle: ', area_rectangle(5, 2))
print('Area of triangle: ', area_triangle(5, 4, 3))
