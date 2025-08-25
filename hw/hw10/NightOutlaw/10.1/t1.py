"""My way of solving task 1"""


class Polygon:
    """Base class: Polygon"""
    def __init__(self, sides):
        self.sides = sides  # List of side lengths


class Rectangle(Polygon):
    """Subclass: Rectangle"""
    def __init__(self, length, width):
        super().__init__([length, width, length, width])  # 4 sides
        self.length = length
        self.width = width

    def area(self):
        """Calculating the rectangle's area"""
        return self.length * self.width
