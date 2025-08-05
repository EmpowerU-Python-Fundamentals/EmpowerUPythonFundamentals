import math


def calculate_rectangle_area(length, width):
    """
    Calculates the area of a rectangle.

    Args:
        length (float): The length of the rectangle.
        width (float): The width of the rectangle.

    Returns:
        float: The area of the rectangle.
    """
    if length < 0 or width < 0:
        print("Error: Length and width cannot be negative.")
        return None
    return length * width


def calculate_triangle_area(base, height):
    """
    Calculates the area of a triangle.

    Args:
        base (float): The base of the triangle.
        height (float): The height of the triangle.

    Returns:
        float: The area of the triangle.
    """
    if base < 0 or height < 0:
        print("Error: Base and height cannot be negative.")
        return None
    return 0.5 * base * height


def calculate_circle_area(radius):
    """
    Calculates the area of a circle.

    Args:
        radius (float): The radius of the circle.

    Returns:
        float: The area of the circle.
    """
    if radius < 0:
        print("Error: Radius cannot be negative.")
        return None
    # Using math.pi and math.pow for pi*r**2
    return math.pi * math.pow(radius, 2)
