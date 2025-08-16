import math

def validate_point(func):
    """
    Decorator to check that the points are a list of 4 tuples,
    which contain numeric values.
    """
    def wrapper(self, points):
        if not isinstance(points, list):
            raise TypeError("Input data must be a list.")
        if not len(points) == 4:
            raise ValueError("List must contain 4 points.")
        for point in points:
            if not isinstance(point, tuple):
                raise TypeError("Each list element must be a tuple (point).")
            if not len(point) == 2:
                raise ValueError("Each point must contain 2 coordinates (x, y).")
            if not all(isinstance(coord, (int, float)) for coord in point):
                raise TypeError("Point coordinates must be numbers.")
        return func(self, points)
    return wrapper


class Polygon:
    """Base class for polygons."""
    @validate_point
    def __init__(self, points):
        self.__points = points

    @property
    def points(self):
        """Gets the list of polygon points."""
        return self.__points

    @points.setter
    @validate_point
    def points(self, points):
        """Sets a new list of polygon points with validation."""
        self.__points = points

class Rectangle(Polygon):
    """Rectangle class, inherited from Polygon."""
    def __init__(self, points):
        super().__init__(points)
        # Additional check that the points form a rectangle
        # (additional logic can be added, but it's not required for this basic task)

    def get_area(self):
        """Calculates and returns the area of the rectangle."""
        # Calculating the length of two adjacent sides
        side_ab = math.sqrt((self.points[1][0] - self.points[0][0])**2 + (self.points[1][1] - self.points[0][1])**2)
        side_bc = math.sqrt((self.points[2][0] - self.points[1][0])**2 + (self.points[2][1] - self.points[1][1])**2)
        return side_ab * side_bc

# Example usage
if __name__ == "__main__":
    rect_points = [(0, 0), (5, 0), (5, 3), (0, 3)]
    my_rectangle = Rectangle(rect_points)
    print(f"Rectangle area: {my_rectangle.get_area()}")

    # Example of using the setter
    my_rectangle.points = [(1, 1), (6, 1), (6, 4), (1, 4)]
    print(f"New points set. New area: {my_rectangle.get_area()}")

    # Example of a validation error
    try:
        my_rectangle.points = [(0, 0), (1, 1), (2, 2)]
    except ValueError as e:
        print(f"Error: {e}")
