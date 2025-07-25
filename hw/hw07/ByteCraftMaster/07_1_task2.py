def calculate_rectangle_area (length, width):
    """
    Function for calculation of the rectangle area.

    Parameters:
    length (float): The length of the rectangle.
    width (float): The width of the rectangle.

    Returns:
    float: The area of the rectangle.
    """
    return length*width

def calculate_triangle_area(base, height):
    """
    Function for calculation of the triangle area.

    Parameters:
    base (float): The base of the triangle.
    height (float): The height of the triangle.

    Returns:
    float: The area of the triangle.
    """
    return 0.5 * base * height

def calculate_circle_area(radius):
    """
    Function for calculation of the circle area.

    Parameters:
    radius (float): The radius of the circle.

    Returns:
    float: The area of the circle.
    """
    return 3.14 * radius ** 2


shape = input("Input a shape to calculate the area (support only rectangle, triangle and circle): \n")
if shape.lower()=="rectangle":
    length = float(input("Input the length of the rectangle: \n" ))
    width = float(input("Input the width of the rectangle: \n" ))
    area = calculate_rectangle_area(length, width)
    print(f"The area of the rectangle is: {area}")
elif shape.lower()=="triangle":
    base = float(input("Input the base of the triangle: \n" ))
    height = float(input("Input the height of the triangle: \n" ))
    area = calculate_triangle_area(base, height)
    print(f"The area of the triangle is: {area}")
elif shape.lower()=="circle":
    radius = float(input("Input the radius of the circle: \n" ))
    area= calculate_circle_area(radius)
    print(f"The area of the circle is: {area}")
else:
    print(f"{shape} is unsupported by our program")