from areas_func import main_area
from validator import validate_user_input

print('Hello. This program calculates the area of a rectangle, triangle, or circle.')
while True:
    print("(If you want a quit, enter 'q')\n")
    figure = input('Please write which area you need: ').lower()
    if figure.lower() == 'q':
        print('See you later!')
        break
    else:
        if not validate_user_input(figure):
            print('Invalid figure. Please enter one of: circle, triangle, rectangle.\n')
        else:
            if figure == 'circle':
                try:
                    r = float(input('Enter the radius of your circle: '))
                    print(f'Area:', round(main_area(r=r),2))
                except ValueError:
                    print('Invalid input! Please enter valid number.\n')
            elif figure == 'triangle':
                try:
                    b = float(input('Enter the base of your triangle: '))
                    h = float(input('Enter the height of your triangle: '))
                    print(f'Area:', round(main_area(b=b, h=h),2))
                except ValueError:
                    print('Invalid input! Please enter valid numbers.\n')
            elif figure == 'rectangle':
                try:
                    l = float(input('Enter the length of your rectangle: '))
                    w = float(input('Enter the width of your rectangle: '))
                    print(f'Area:', round(main_area(l=l, w=w),2))
                except ValueError:
                    print('Invalid input! Please enter valid numbers.')
