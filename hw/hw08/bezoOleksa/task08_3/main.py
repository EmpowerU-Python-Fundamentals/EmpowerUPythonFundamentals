from funcs import areaRectangle, areaTriangle, areaCircle

figure = input('Which figure\'s area do you want to calculate (rect/tri/circ)? ')
figure = figure.lower()

if figure == 'rect' or figure == 'rectangle':
    a = float(input('Enter the length of the first side: '))
    b = float(input('Enter the length of the second side: '))
    print('Area of your rectangle is', round(areaRectangle(a, b), 2))
elif figure == 'tri' or figure == 'triangle':
    a = float(input('Enter the length of the side: '))
    h = float(input('Enter the height of the side: '))
    print('Area of your triangle is', round(areaTriangle(a, h), 2))
elif figure == 'circ' or figure == 'circle':
    r = float(input('Enter the radius of your circle: '))
    print('Area of your circle is', round(areaCircle(r), 2))
else:
    print('Incorrect figure; please choose only among rectangle, triangle, and circle')

