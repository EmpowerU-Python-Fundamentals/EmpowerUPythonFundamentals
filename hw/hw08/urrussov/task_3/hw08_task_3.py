import re
import area_functions



def checked_figure():
    """
    Prompts the user to enter the name of a geometric figure ('rectangle', 'triangle', or 'circle').
    Continues to prompt until a valid figure name is entered (case-insensitive).
    Returns:
        str: The name of the valid figure entered by the user.
    """


    while True:
        figure = input('Enter rectangle, triangle or circle: ').lower()
        pattern = r"rectangle|triangle|circle"
        match = re.search(pattern, figure)
        if match:
            return figure
        else: 
            print('Your enter wrong figure. Try again!')
            continue


area_figure = checked_figure()

match area_figure:
    case 'rectangle':
        l = float(input("Enter a length of rectangle in cm: "))
        w = float(input("Enter a width of rectangle in cm: "))
        result = area_functions.area_of_rectangle(l,w)
        print(f"The area of rectangle is {result} cm^2")
    case 'triangle':
        b = float(input("Enter a base of triangle in cm: "))
        h = float(input("Enter a height of triangle in cm: "))
        result = area_functions.area_of_triangle(b,h)
        print(f"The area of triangle is {result} cm^2")
    case 'circle':
        r = float(input("Enter a radius of circle in cm: "))
        result = round(area_functions.area_of_circle(r), 2)
        print(f"The area of circle is {result} cm^2")

