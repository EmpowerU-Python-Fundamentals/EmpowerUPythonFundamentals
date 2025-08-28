class Polygon:
    def __init__(self, sides):
        self.sides = sides

    pass


class Rectangle(Polygon):
    def __init__(self, width, height):
        super().__init__(sides=4)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


# example
p = Rectangle(5, 5)
print(f"Area: {p.area()}")
