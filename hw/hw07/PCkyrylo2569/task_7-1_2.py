def rectangle_area(length, width):
    """
    Calculate the area of a rectangle.
    """
    return length * width

def triangle_area(base, height):
    """
    Calculate the area of a triangle.
    """
    return 0.5 * base * height

def circle_area(radius):
    """
    Calculate the area of a circle.
    """
    import math
    return math.pi * (radius ** 2)

area = int(input("Enter the area type (1 for rectangle, 2 for triangle, 3 for circle): "))

match area:
    case 1:
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        print(rectangle_area(length, width))
    case 2:
        base = float(input("Enter the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        print(triangle_area(base, height))
    case 3:
        radius = float(input("Enter the radius of the circle: "))
        print(circle_area(radius))