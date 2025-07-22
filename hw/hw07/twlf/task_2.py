import re

def area_rectangle(l, w):
    """Return the area of a rectangle."""
    return l * w

def area_circle(r):
    """Return the area of a circle."""
    return (r ** 2) * 3.14159

def area_triangle(b,h):
    """Return the area of a triangle (using the simplest formula)."""
    return b * h / 2


def main_area(l=None, w=None, r=None, b=None,h=None):
    """Calculate area of rectangle, circle, or triangle based on given parameters.
    Parameters:
    length, width -- for rectangle;
    radius -- for circle;
    base, height -- for triangle;
    Returns:
    Area as a float or None if parameters are insufficient."""

    if r is not None:
        return area_circle(r)
    elif b is not None and h is not None:
        return area_triangle(b, h)
    elif l is not None and w is not None:
        return area_rectangle(l,w)

def validate_user_input(user_input):
    """Check if the input is a valid figure name"""
    pattern = r'^(circle|triangle|rectangle)$'
    return re.fullmatch(pattern, user_input.strip().lower()) is not None

print('Hello. This program calculates the area of a rectangle, triangle, or circle.')

figure = input('Please write which area you need: ').lower()

if not validate_user_input(figure):
    print('Invalid figure. Please enter one of: circle, triangle, rectangle.')
else:

    if figure == 'circle':
        try:
            r = float(input('Enter the radius of your circle: '))
            print(f'Area:', round(main_area(r=r),2))
        except ValueError:
            print('Invalid input! Please enter valid number.')
    elif figure == 'triangle':
        try:
            b = float(input('Enter the base of your triangle: '))
            h = float(input('Enter the height of your triangle: '))
            print(f'Area:', round(main_area(b=b, h=h),2))
        except ValueError:
            print('Invalid input! Please enter valid numbers.')
    elif figure == 'rectangle':
        try:
            l = float(input('Enter the length of your rectangle: '))
            w = float(input('Enter the width of your rectangle: '))
            print(f'Area:', round(main_area(l=l, w=w),2))
        except ValueError:
            print('Invalid input! Please enter valid numbers.')
