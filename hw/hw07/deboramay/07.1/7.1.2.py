import math

def area_rectangle(length, width):
    """
    Calculates the area of a rectangle
    """
    return length * width

def area_triangle(base, height):
    """
    Calculates the area of a triangle
    """
    return 0.5 * base * height

def area_circle(radius):
    """
    Calculates the area of a circle
    """
    return math.pi * radius ** 2


print("Choose a shape to calculate the area:")
print("1. Rectangle")
print("2. Triangle")
print("3. Circle")

choice = input("Enter your choice (1/2/3): ")

if choice == "1":
    l = float(input("Enter the length: "))
    w = float(input("Enter the width: "))
    print("Area of rectangle:", area_rectangle(l, w))

elif choice == "2":
    b = float(input("Enter the base: "))
    h = float(input("Enter the height: "))
    print("Area of triangle:", area_triangle(b, h))

elif choice == "3":
    r = float(input("Enter the radius: "))
    print("Area of circle:", area_circle(r))

else:
    print("Invalid choice.")
