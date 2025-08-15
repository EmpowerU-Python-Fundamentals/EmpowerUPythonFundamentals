class Polygon:
    def __init__(self, sides):
        self.sides = sides


class Rectangle(Polygon):
    def __init__(self, length, width):
        super().__init__(4)  # Rectangle has 4 sides
        self.length = length
        self.width = width

    def square(self):
        print(self.length * self.width)

Rectangle(1.3533,113).square()