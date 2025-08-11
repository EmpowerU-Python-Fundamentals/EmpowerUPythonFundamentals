class Polygon:
    def __init__(self, sides):
        self.sides = sides

class Rectangle(Polygon):
    def __init__(self, length, width):
        super().__init__([length, width])
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
    
rect = Rectangle(3, 5)
print(f"Площа прямокутника: {rect.area()}")