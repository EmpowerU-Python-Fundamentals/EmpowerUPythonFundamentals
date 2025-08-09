class Polygon:
    def __init__(self, length, width):
        self.length = length
        self.width = width

class Rectangle(Polygon):
    def area(self):
        return self.length * self.width

# Використання класу Rectangle для обчислення площі прямокутника
r = Rectangle(5, 10)
print("Area of rectangle:", r.area())
