import math


def calculate_area(shape, **kwargs):
    """Calculate the area of triangle, rectangle and circle"""
    shape = shape.lower()

    if shape == "triangle":
        width = kwargs.get("width")
        height = kwargs.get("height")
        if width is None or height is None:
            return "Missing width or height for triangle"
        return 0.5 * width * height

    elif shape == "rectangle":
        width = kwargs.get("width")
        height = kwargs.get("height")
        if width is None or height is None:
            return "Missing width or height for rectangle"
        return width * height

    elif shape == "circle":
        radius = kwargs.get("radius")
        if radius is None:
            return "Missing radius for circle"
        return math.pi * radius**2

    else:
        return "Unknown shape"


print("Triangle:", calculate_area("triangle", width=10, height=5))
print("Rectangle:", calculate_area("rectangle", width=4, height=7))
print("Circle:", calculate_area("circle", radius=3))
print("Invalid:", calculate_area("square", side=4))
