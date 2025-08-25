# Task 1: Polygon & Rectangle

class Polygon:
    def __init__(self, sides):
        self.sides = sides

    def display_sides(self):
        print("Sides of the polygon:", self.sides)


class Rectangle(Polygon):
    def __init__(self, length, width):
        super().__init__([length, width, length, width])
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


# User input
length = int(input("Enter the length of the rectangle: "))
width = int(input("Enter the width of the rectangle: "))

rect = Rectangle(length, width)

rect.display_sides()
print("Area of the rectangle:", rect.area())
