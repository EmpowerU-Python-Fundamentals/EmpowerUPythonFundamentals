"""Task 1: Poligon and Rectangle classes"""

class Poligon:
    """base Poligon class"""
    def __init__(self, segments=4):
        self.name = segments

    def area(self):
        return 0

class Rectangle(Poligon):
    """Rectangle class, based on Poligon"""
    def __init__(self, width=1, height=1):
        self.segments = 4
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

rect = Rectangle(2, 4)

print(f"Rectangle area is: {rect.area()} cm2")