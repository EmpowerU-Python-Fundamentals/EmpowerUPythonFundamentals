class Polygon:
    def __init__(self, sides):
        self.sides = sides

class Rectangle(Polygon):
    def __init__(self, length, width):
        super().__init__(4)
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

rect = Rectangle(5, 4)
print(f"Rectangle has {rect.sides} sides.")
print(f"Area of rectangle: {rect.area()}")