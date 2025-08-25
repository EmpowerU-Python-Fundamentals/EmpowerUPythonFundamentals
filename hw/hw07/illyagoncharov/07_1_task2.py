def rectangle_area(a,b):
    """The function calculates the area of a rectangle"""
    return round(a*b,2)

def triangle_area(height, base):
    """The function calculates the area of a triangle"""
    return round(0.5*height*base,2)

def circle_area(radius):
    """The function calculates the area of a circle"""
    pi = 3.14
    return round(pi*pow(radius,2),2)

figure = input("Which shape do you need to calculate the area of? \n"
               " Choose: \n"
               " 1 - if it is a rectangle, \n"
               " 2 - if it is a triangle, \n"
               " 3 - if it is a circle \n")
if figure =='1':
    a = float(input("Specify the length of one side:"))
    b = float(input("Specify the length of second side:"))
    print(f"Area rectangle = {rectangle_area(a,b)}")
elif figure =='2':
    height = float(input("Specify the length of height of triangle:"))
    base = float(input("Specify the length of base of triangle:"))
    print(f"Area triangle = {triangle_area(height,base)}")
elif figure =='3':
    radius = float(input("Specify the radius of circle:"))
    print(f"Area circle = {circle_area(radius)}")
else:
    print("Incorrect data")