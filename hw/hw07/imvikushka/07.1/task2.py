# Task 2. Write a program that calculates the area of a rectangle, triangle and circle.
import math

def areaOfRectangle(a, b):
    return f"The area of a rectangle {round(a * b)} cm²."
    
def areaOfTriangle(a, h):
    # The area of a triangle is calculated using its side and height: 
    # the area is equal to half the product of the side and the height drawn to that side.
    return f"The area of a rectangle {round(1/2 * a * h)} cm²."

def areaOfCircle(r):
    return f"The area of a circle {round(math.pi * r**2)} cm²."

userChoise = input("Write the number of the shape whose area you want to calculate:\n1. Rectangle\n2. Triangle\n3. Circle\n")

if userChoise == "1":
    a = int(input("Enter the length of the rectangle: "))
    b = int(input("Enter the width of the rectangle: "))

    print(areaOfRectangle(a, b))
elif userChoise == "2":
    a = int(input("Enter the length of the side: "))
    h = int(input("Enter the length of the height drawn to this side: "))

    print(areaOfTriangle(a, h))
elif userChoise == "3":
    r = int(input("Enter the area of the circle: "))

    print(areaOfCircle(r))
else:
    print("The number you entered is incorrect. Please try again.")