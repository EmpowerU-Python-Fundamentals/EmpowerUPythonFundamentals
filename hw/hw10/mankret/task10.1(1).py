# Create a polygon class and rectangle class that inherits from the polygon class and finds the square of rectangle

class Polygon:
    """
    Base class
    """

    def __init__(self, sides):
        """
        Initializes a polygon
        """
        self.sides = sides

    def display_info(self):
        """Displays information about the polygon"""
        print(f"This is the polygon with {len(self.sides)} sides.")
        print(f"Side lengths: {self.sides}")


class Rectangle(Polygon):
    """
    Rectangle class inherited from Polygon
    """

    def __init__(self, length, width):
        """
        Initializes a rectangle
        """
        super().__init__([length, width, length, width])
        self.length = length
        self.width = width

    def find_area(self):
        """
        Calculates and returns the area of a rectangle.
        """
        return self.length * self.width


my_rect = Rectangle(length=10, width=5)

my_rect.display_info()

area = my_rect.find_area()
print(f"The area of a rectangle: {area}")

another_rectangle = Rectangle(15.5, 8)
another_rectangle.display_info()
print(f"the area of a another rectangle: {another_rectangle.find_area()}")
