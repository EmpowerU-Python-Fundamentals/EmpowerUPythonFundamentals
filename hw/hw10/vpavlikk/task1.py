class Polygon:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    @property
    def square_of_rectangle(self):
        return self.length * self.width


class Rectangle(Polygon):
    def __init__(self, length, width):
        super().__init__(length, width)


rectangle_square = Rectangle(2, 2)
print(rectangle_square.square_of_rectangle)
