"""rectangle area"""
class Polygon:
    def __init__(self, sides):
        self.sides = sides
class Rectangle(Polygon):
    def __init__(self, length, width):
        super().__init__([length, width, length, width])
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width

rect = Rectangle(5, 3)
print(rect.area())
