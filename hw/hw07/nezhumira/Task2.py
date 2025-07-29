import math

def area_rectangle(length: float, width: float) -> float:
    """
    Calculates the area of a rectangle.

    Parameters:
    length (float): The length of the rectangle.
    width (float): The width of the rectangle.

    Returns:
    float: The area of the rectangle.
    """
    return length * width

def area_triangle(base: float, height: float) -> float:
    """
    Calculates the area of a triangle.

    Parameters:
    base (float): The base of the triangle.
    height (float): The height of the triangle.

    Returns:
    float: The area of the triangle.
    """
    return 0.5 * base * height

def area_circle(radius: float) -> float:
    """
    Calculates the area of a circle.

    Parameters:
    radius (float): The radius of the circle.

    Returns:
    float: The area of the circle.
    """
    return math.pi * radius ** 2


while True:
    print("Choose a shape to calculate the area:")
    print("1. Rectangle")
    print("2. Triangle")
    print("3. Circle")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        length = float(input("Enter length: "))
        width = float(input("Enter width: "))
        print(f"Area of Rectangle = {area_rectangle(length, width):.2f}")
        input("Please press Enter.")
    elif choice == "2":
        base = float(input("Enter base: "))
        height = float(input("Enter height: "))
        print(f"Area of Triangle = {area_triangle(base, height):.2f}")
        input("Please press Enter.")
    elif choice == "3":
        radius = float(input("Enter radius: "))
        print(f"Area of Circle = {area_circle(radius):.2f}")
        input("Please press Enter.")
    elif choice == "4":
        break 
    else:
        input("Invalid choice. \nPlease press Enter.") 
