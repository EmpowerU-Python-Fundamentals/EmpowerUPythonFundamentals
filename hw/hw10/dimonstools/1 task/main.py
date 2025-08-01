class Polygon:
    def __init__(self, sides):
        self.sides = sides 

class Rectangle(Polygon):
    def __init__(self, length, width):
        super().__init__([length, width, length, width])
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

rect = Rectangle(length, width)

print(f"The area of the rectangle is: {rect.area()}")
