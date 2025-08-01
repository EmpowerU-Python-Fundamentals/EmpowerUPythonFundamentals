from math import sqrt, pi

# Task2. Write a program that calculates the area of a rectangle, triangle and circle
# (write three functions to calculate the area. And call them in the main program depending on the user's choice)
def get_rectangle_area(a, b):
    return a*b
		
def get_triangle_area(a, b, c):
    p=(a+b+c)/2
    return round(sqrt(p*(p-a)*(p-b)*(p-c)), 2)

def get_circle_area(r):
    return round((pi*r**2),2)

def main():
    print("Choose a shape to calculate the area:")
    print("1. Rectangle")
    print("2. Triangle")
    print("3. Circle")

    choice = input("Enter your choice (1/2/3): ")

    match choice:
        case "1":
            print("You selected rectangle")
            width = int(input("Enter the width of the rectangle: "))
            length = int(input("Enter the length of the rectangle: "))
            print("Area of a rectangle =", get_rectangle_area(width, length))
        case "2":
            print("You selected triangle")
            a = int(input("Enter the length of the first side of the triangle: "))
            b = int(input("Enter the length of the second side of the triangle: "))
            c = int(input("Enter the length of the third side of the triangle: "))
            print("Area of a triangle =", get_triangle_area(a, b, c))
        case "3":
            print("You selected circle")
            r = int(input("Enter the radius of the circle: "))
            print("Area of a circle =", get_circle_area(r))
        case _:
            print("Unknown shape selected.")

main()