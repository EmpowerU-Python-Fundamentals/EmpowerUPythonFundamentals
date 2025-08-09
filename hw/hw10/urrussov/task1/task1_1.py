class Polygon:
    """
    A class representing a polygon with a specified number of sides.

    """
    def __init__(self, sides):
        self.sides = sides


class Rectangle(Polygon):
    """
    Rectangle class representing a rectangle polygon.

    Inherits from:
        Polygon

    Attributes:
        length (float): The length of the rectangle.
        width (float): The width of the rectangle.

    Methods:
        area():
            Calculates and returns the area of the rectangle.

        __str__():
            Returns a string representation of the rectangle, including the number of sides and its area.
    """
    def __init__(self, length, width):
        super().__init__(4)
        self.length = length
        self.width = width
    def area(self):
        """
        Calculates and returns the area of the rectangle.

        """
        return self.width * self.length
    def __str__(self):
        return f'Rectangle has {self.sides} sides\nArea of rectangle (width = {self.width}, length = {self.length}) = {self.area()}'

rectangle_1 = Rectangle(5,5)
rectangle_2 = Rectangle(5,10)

print(f'{rectangle_1}\n{rectangle_2}')