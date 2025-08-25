class Polygon:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
class Rectangle(Polygon):
    def area(self):
        return self.a * self.b
    
    
rectangle = Rectangle(5, 10)
print(rectangle.area())