class Polygon:
    def __init__(self, a, b):
        self.a = a
        self.b = b

class Rectangle(Polygon):
    def area(self):
        return self.a * self.b


if __name__ == '__main__':
    rectangle = Rectangle(10, 20)
    print(rectangle.area())