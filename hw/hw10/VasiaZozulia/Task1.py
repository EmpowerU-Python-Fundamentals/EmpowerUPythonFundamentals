class Polygon:
    def __init__(self, sides):
        self.sides = sides

    def area(self):
        pass


class Rectangle(Polygon):
    def __init__(self, length, width):
        super().__init__([length, width])
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
