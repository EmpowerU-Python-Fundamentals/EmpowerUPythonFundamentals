class Polygon:
    def __init__(self, sides):
        self.sides = sides

    def get_sides(self):
        return self.sides


class Rectangle(Polygon):
    def __init__(self, width, height):
        super().__init__([width, height])
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


if __name__ == '__main__':
    R=Rectangle(10, 20)
    print(R.area())
