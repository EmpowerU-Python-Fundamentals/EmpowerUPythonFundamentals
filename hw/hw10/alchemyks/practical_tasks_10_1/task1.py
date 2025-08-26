class Polygon:
    pass


class Rectangle(Polygon):
    def __init__(self, width, height):
        self.width = width
        self.height = height
   
    def square(self):
        return self.width == self.height
    

