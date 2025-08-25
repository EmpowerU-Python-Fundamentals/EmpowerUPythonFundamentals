class Polygon:
    def __init__(self, length, width):
        self.length = length
        self.width = width

class Rectangle(Polygon):
    def area(self):
        return self.length * self.width

length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

rect = Rectangle(length, width)

print(f"The area of the rectangle is: {rect.area()}")