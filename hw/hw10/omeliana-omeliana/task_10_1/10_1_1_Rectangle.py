class Polygon:
    def __init__(self, side1, side2, side3, side4):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self.side4 = side4

class Rectangle(Polygon):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
   
rect = Rectangle(5, 6)
print(rect.area())
