import math

def validate_point(func):
    def wrapper(self, points):
        if not isinstance(points, list):
            raise TypeError("must be a list")
        if not len(points) == 4:
            raise ValueError("must have 4 points")
        for point in points:
            if not isinstance(point, tuple):
                raise TypeError("Invalid point")
            elif not all(map(lambda x: isinstance(x, (int, float)), point)):
                raise TypeError("must be a list of numbers")
        return func(self, points)
    return wrapper


class Polygon:
    @validate_point
    def __init__(self, points):
        self.__points = points

    @property
    def points(self):
        return self.__points

    @points.setter
    @validate_point
    def points(self, points):
        self.__points = points

class Rectangle(Polygon):
    def __init__(self, points):
        super().__init__(points)

    def get_area(self):
        side_ab =  math.sqrt((self.points[1][0] - self.points[0][0])**2 \
                             + (self.points[1][1] - self.points[0][1])**2)
        side_bc = math.sqrt((self.points[2][0] - self.points[1][0])**2 + \
                            (self.points[2][1] - self.points[1][1])**2)
        return side_ab * side_bc






