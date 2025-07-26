import math

def area_rectangle(a,b):
    """the program calculates the area of a rectangle"""
    area = a*b
    return area

def area_triangle(a,b,c):
    """the program calculates the area of a triangle"""
    p = (a+b+c)/2  #half perimeter
    area = (p*(p-a)*(p-b)*(p-c))**0.5
    return round(area,2)

def area_circle(r):
    """the program calculates the area of a circle"""
    PI = math.pi
    area = PI*r**2
    return round(area,2)


figure = input("Which shape do you want to calculate the area of (rectangle, triangle, or circle)?    ")

match (figure.lower().strip()):
    case "rectangle":
        a = int(input("Enter the length of side a: "))
        b = int(input("Enter the length of side b: "))
        print(f"Area of a rectangle = {area_rectangle(a,b)}")
    case "triangle":
        a = int(input("Enter the length of side a: "))
        b = int(input("Enter the length of side b: "))
        c = int(input("Enter the length of side c: "))
        print(f"Area of a triangle = {area_triangle(a,b,c)}")
    case "circle":
        r = int(input("Enter the radius of the circle "))
        print(f"Area of a circle = {area_circle(r)}")
    case _:
        print("Invalid input")
