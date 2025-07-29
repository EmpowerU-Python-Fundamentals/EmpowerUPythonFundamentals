import math

def areaRectangle(a, b):
    return a * b

def areaTriangle(a, b, c):  # Heron's formula
    p = (a + b + c) / 2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))

def areaCircle(r):
    return math.pi * r**2

figure = input('Which figure\'s area do you want to calculate (rect/tri/circ)? ')
figure = figure.lower()

if figure == 'rect' or figure == 'rectangle':
    a = float(input('Enter the length of the first side: '))
    b = float(input('Enter the length of the second side: '))
    print('Area of your rectangle is', round(areaRectangle(a, b), 2))
elif figure == 'tri' or figure == 'triangle':
    a = float(input('Enter the length of the first side: '))
    b = float(input('Enter the length of the second side: '))
    c = float(input('Enter the length of the third side: '))
    print('Area of your triangle is', round(areaTriangle(a, b, c)))
elif figure == 'circ' or figure == 'circle':
    r = float(input('Enter the radius of your circle: '))
    print('Area of your circle is', round(areaCircle(r)))
else:
    print('Incorrect figure; please choose only among rectangle, triangle, and circle')
