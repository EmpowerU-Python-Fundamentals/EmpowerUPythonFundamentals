class Polygon:
    def __init__(self, side_a, side_b):
        self.side_a = side_a
        self.side_b = side_b

    def square(self):
        return self.side_a * self.side_b

class Rectangle(Polygon):
    pass

p = Rectangle(4,5)
print(p.square())