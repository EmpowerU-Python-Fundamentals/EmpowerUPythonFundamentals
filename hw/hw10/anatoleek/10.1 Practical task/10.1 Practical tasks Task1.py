class Polygon:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def display_sides(self):
        print(f"Length: {self.length}, Width: {self.width}")

class Rectangle(Polygon):
    def __init__(self, length, width):
        super().__init__(length, width)

    def area(self):
        return self.length * self.width
    
rect = Rectangle(6, 4)
rect.display_sides()
print("Square of rectangle:", rect.area())