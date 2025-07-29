from measurements import *

def ask_params_and_calc_triangle():
    base = input('Enter the length of the triangle base\n')
    height = input('Enter the height of the triangle\n')
    print(f'The area of your triangle is: {calc_triangle_area(base, height)}')

def ask_params_and_calc_circle():
    radius = input('Enter the radius of your circle\n')
    print(f'The area of your circle is: {calc_circle_area(radius)}')

def ask_params_and_calc_rectangle():
    side1 = input("Enter the first side length\n")
    side2 = input("Enter the second side length\n")
    print(f'The area of your rectangle is: {calc_square_area(side1, side2)}')
    

figure_name = input("Program calculates figure area. Enter a figure name." \
" Options: rectangle, circle, triangle.\n").lower()
match figure_name:
    case 'circle':
        ask_params_and_calc_circle()
    case 'rectangle':
        ask_params_and_calc_rectangle()
    case 'triangle':
        ask_params_and_calc_triangle()
    case _:
        print(f'unsupported figure type: {figure_name}')
