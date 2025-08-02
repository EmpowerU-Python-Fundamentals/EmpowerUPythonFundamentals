from classes.polygon import Polygon


class Rectangle(Polygon):
    def __init__(self, width, height):
        super().__init__(sides=4)
        self.width = width
        self.height = height

    def square(self):
        return self.width * self.height

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height}, area={self.square()})"