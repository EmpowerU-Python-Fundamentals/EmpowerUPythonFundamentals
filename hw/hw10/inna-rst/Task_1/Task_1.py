class Polygon:
    def __init__(self, sides):
        self.sides = sides

    def __str__(self):
        return f"Polygon with {self.sides} sides"

class Rectangle(Polygon):
    def __init__(self, width, height):
        super().__init__(4)
        self.width = width
        self.height = height

    def __str__(self):
        return f"Rectangle {self.width}x{self.height} with area {self.area()}"

    def area(self):
        return self.width * self.height

r=Rectangle(4, 6)
print(r)