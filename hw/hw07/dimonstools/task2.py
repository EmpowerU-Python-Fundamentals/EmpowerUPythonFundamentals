import math

def area_rectangle(length, width):
    """
    Calculate the area of a rectangle.

    length: Length of the rectangle.
    width: Width of the rectangle.

    Return: Area of the rectangle.
    """
    return length * width

def area_triangle(base, height):
    """
    Calculate the area of a triangle.

    base: Base of the triangle.
    height: Height of the triangle.

    Return: Area of the triangle.
    """
    return 0.5 * base * height

def area_circle(radius):
    """
    Calculate the area of a circle.

    radius: Radius of the circle.

    Return: Area of the circle.
    """
    return math.pi * radius ** 2

def main():
    print("Choose a shape to calculate the area:")
    print("1. Rectangle")
    print("2. Triangle")
    print("3. Circle")
    
    choice = input("Enter 1, 2, or 3: ")

    if choice == "1":
        length = float(input("Enter the length: "))
        width = float(input("Enter the width: "))
        print("Area of rectangle:", area_rectangle(length, width))
    elif choice == "2":
        base = float(input("Enter the base: "))
        height = float(input("Enter the height: "))
        print("Area of triangle:", area_triangle(base, height))
    elif choice == "3":
        radius = float(input("Enter the radius: "))
        print("Area of circle:", area_circle(radius))
    else:
        print("Invalid choice!")

# Run the program
main()