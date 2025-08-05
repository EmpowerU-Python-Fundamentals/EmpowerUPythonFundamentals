class Polygon():
    def __init__(self):
        pass

class Rectangle(Polygon):
    def __init__(self, width, height):
        super().__init__()
        self.width=width
        self.height=height
    def area(self):
        return self.width*self.height