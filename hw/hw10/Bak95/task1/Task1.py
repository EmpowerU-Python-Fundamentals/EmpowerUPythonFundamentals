class Polygon:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

class Rectangle(Polygon):
    def area(self):
        return self.length * self.breadth

rect = Rectangle(10, 5)
print("Площа прямокутника:", rect.area())
