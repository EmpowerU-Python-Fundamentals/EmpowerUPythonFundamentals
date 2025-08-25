class Polygon:
    def __init__(self, height_edge, width_edge):
        self.height_edge = height_edge
        self.width_edge = width_edge

    def rectangle_square(self):
        if self.height_edge <= 0 or self.width_edge <= 0:
            return("Please enter numbers greater than 0")
        return self.height_edge * self.width_edge

class Rectangle(Polygon):
    def __init__(self, height_edge, width_edge):
        super().__init__(height_edge, width_edge)

my_rectangle = Rectangle(9, 8)
print(f"Area of rectangle = ", my_rectangle.rectangle_square()) 