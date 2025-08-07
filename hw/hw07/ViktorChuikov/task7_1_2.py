def area_of_rectangle(a, b):
    return a * b

def area_of_triangle(a, b):
    return 0.5 * a * b

def area_of_circle(r):
    return 3.14 * r ** 2

def calc():
   
    choice = int(input('Enter: \n1 - for rectangle\n2 - for triangle\n3 - for circle \narea calculation: '))

    if choice == 1:
        a = float(input('Enter width: '))
        b = float(input('Enter height: '))
        print('Area of rectangle:', area_of_rectangle(a, b))

    elif choice == 2:
        a = float(input('Enter width: '))
        b = float(input('Enter height: '))
        print('Area of triangle:', area_of_triangle(a, b))

    elif choice == 3:
        r = float(input('Enter radius: '))
        print('Area of circle:', area_of_circle(r))

    else:
        print('Invalid choice')

calc()