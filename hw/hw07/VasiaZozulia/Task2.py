import math
def area_rectangle(width, length):
    """
    Calculate the area of a rectangle given its width and length.

    Parameters:
        width (int): The width of the rectangle.
        length (int): The length of the rectangle.

    Returns:
        int: Area of the rectangle if both inputs are integers.
        None: If either input is not an integer.
    """    
    if type(width) is int and type(length) is int:
        return width * length
    else:
        return None

def area_triangle_sides(first_side, second_side, third_side):
    """
        Calculate the area of a triangle using Heron's formula.
    
        Parameters:
            first_side (int): Length of the first side of the triangle.
            second_side (int): Length of the second side of the triangle.
            third_side (int): Length of the third side of the triangle.
    
        Returns:
            float: Area of the triangle if all inputs are integers.
            None: If any input is not an integer.
        """    
    if type(first_side) is int and type(second_side) is int and type(third_side) is int:
        p = (first_side + second_side + third_side) / 2
        return math.sqrt(p * (p - first_side) * (p - second_side) * (p - third_side))
    else:
        return None
    
def area_triangle_side_height(side, height):
    """
        Calculate the area of a triangle given its base (side) and height.
    
        Parameters:
            side (int): The base of the triangle.
            height (int): The height of the triangle corresponding to the base.
    
        Returns:
            float: Area of the triangle if inputs are integers.
            None: If any input is not an integer.
        """    
    if type(side) is int and type(height) is int:
        return 1 / 2 * side * height
    else:
        return None
    
def area_triangle_sides_angle(first_side, second_side, angle):
    """
        Calculate the area of a triangle given two sides and the included angle (in radians).
    
        Parameters:
            first_side (int): Length of the first side.
            second_side (int): Length of the second side.
            angle (int): Included angle between the two sides, in radians.
    
        Returns:
            float: Area of the triangle if all inputs are integers.
            None: If any input is not an integer.
        """    
    if type(first_side) is int and type(second_side) is int and type(angle) is int:
        return 1 / 2 * first_side * second_side * math.sin(angle)
    else:
        return None
    
def area_circle(radius):
    """
        Calculate the area of a circle given its radius.
    
        Parameters:
            radius (int): Radius of the circle.
    
        Returns:
            float: Area of the circle if radius is an integer.
            None: If the input is not an integer.
        """    
    if type(radius) is int:
        return math.pi * radius ** 2
    else:
        return None

print("\t\tAttantion! Only positive integers are allowed!")
choice = int(input("Which shape's area do you want to calculate?\n(1 - Rectangle, 2 - Triangle, 3 - Cirle): "))
match choice:
    case 1:
        print("Rectangle")
        width = int(input("What is the width of the rectangle? "))
        length = int(input("What is the length of the rectangle? "))
        print(f"The area of the rectangle with sides ({width}, {length})  is {area_rectangle(width, length)}")
    case 2:
        print("Triangle")
        first_side = int(input("What is the first side of the triangle? "))
        second_side = int(input("What is the second side of the triangle? "))
        third_side = int(input("What is the third side of the triangle? "))
        print("Additional parameters!")
        height = int(input("What is the perpendicular distance from the third side to the opposite vertex? "))
        angle = int(input("What is the the angle between the first and the second side? "))
        print("The area of the triangle is")
        print(f" Three sides {area_triangle_sides(first_side, second_side, third_side)}")
        print(f"The first side and the height {area_triangle_side_height(first_side, height)}")
        print(f"The second side and the height {area_triangle_side_height(second_side, height)}")
        print(f"The third side and the height {area_triangle_side_height(third_side, height)}")
        print(f"The first sidem the second side and the angle between them {area_triangle_sides_angle(first_side, second_side, angle)}")
    case 3:
        print("Circle")
        radius = int(input("What is the radius of the cirle? "))
        print(f"The area of the cirlce is {area_circle(radius)}")
    case _:
        print("Exit. Only 1, 2, 3 are allowed!")