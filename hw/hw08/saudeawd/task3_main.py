"""main"""
import task3_functions
user_area = input('Which figure you want to calculate (rectangle, triangle, circle)?\n')
match user_area:
    case 'rectangle':
        length_rectangle = int(input('Enter the lenth of rectangle: '))
        width_rectangle = int(input('Enter the width of rectangle: '))
        print(task3_functions.rectangle_area(length_rectangle, width_rectangle))
    case 'triangle':
        base_triangle = int(input('Enter the base of triangle: '))
        height_triangle = int(input('Enter the height of triangle: '))
        print(task3_functions.triangle_area(base_triangle, height_triangle))
    case 'circle':
        radius_circle = int(input('Enter the radius of circle: '))
        print(task3_functions.circle_area(radius_circle))
