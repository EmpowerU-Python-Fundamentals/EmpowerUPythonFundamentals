class Polygon:
    def __init__(self, sides):
        self.sides = sides

    def display_sides(self):
        print(f"This polygon has {self.sides} sides.")


class Rectangle(Polygon):
    def __init__(self, length, width):
        super().__init__(4)
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

rect = Rectangle(length, width)
rect.display_sides()
print("Area of ​​the rectangle: ", rect.area())
