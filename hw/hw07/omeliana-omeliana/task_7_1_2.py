def circle_area(radius):
    """Calculate the area of a circle"""
    return round(3.14 * radius ** 2, 2)

def triangle_area(base, height):
    """Calculate the area of a triangle"""
    return round(0.5 * base * height, 2)

def rectangle_area(length, width):
    """Calculate the area of a rectangle"""
    return round(length * width, 2)


shape = input("Please choose a shape:\n\ncircle - 1, triangle - 2, rectangle - 3\n ")

if shape == '1':
    radius = float(input("Enter radius: "))
    area = circle_area(radius)
    print(f"Area of circle: {area}")

elif shape == '2':
    base = float(input("Enter base: "))
    height = float(input("Enter height: "))
    area = triangle_area(base, height)
    print(f"Area of triangle: {area}")

elif shape == '3':
    length = float(input("Enter length: "))
    width = float(input("Enter width: "))
    area = rectangle_area(length, width)
    print(f"Area of rectangle: {area}")
