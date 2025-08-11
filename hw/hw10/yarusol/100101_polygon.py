# Task1.
# Create a polygon class 
# and a rectangle class that inherits from the polygon class 
#   and finds square of rectangle.

class polygon():
    def square(self):
        pass

class rectangle(polygon):
    def __init__(self,
                 width: float,
                 height: float
                 ):
        self._width = width
        self._height = height
    
    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    def square(self):
        return self._width * self._height


############################
# r1 = rectangle(12.34, 23.45)
# print(f"{r1.width = }")
# print(f"{r1.height = }")
# print(f"{r1.square() = }")

# r1.width = 1
