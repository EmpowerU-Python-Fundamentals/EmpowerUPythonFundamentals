# a = list()
# print(type(list))
# print(type(a))

# class MyClass:
#     pass

# my_instance = MyClass()

# print(type(MyClass))
# print(type(my_instance))

# class Point:
#     """A class representing a point in 2D space."""
#     count = 0
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#         Point.count += 1
#     # def __str__(self):
#     #     return f"Point({self.x}, {self.y}) - Instance {Point.count}"
#     def calculate_distance_from_zero(obj):
#         """Calculate the distance from the origin (0, 0)."""
#         return (obj.x ** 2 + obj.y ** 2) ** 0.5

# p1 = Point(1, 2)
# p2 = Point(3, 4)
# print(p1)  # Output: Point(1, 2) - Instance 1
# print(p2)  # Output: Point(3, 4) - Instance 2

# # print(dir(Point))
# # print(dir(p1))
# # print(dir(p2))

# from pprint import pprint
# pprint(Point.__dict__)
# pprint(p1.__dict__)
# pprint(p2.__dict__)
# print(p1.count)
# print(p1.calculate_distance_from_zero())  # Output: 2.23606797749979
# print(p2.calculate_distance_from_zero())  # Output: 5.0
# f = Point.calculate_distance_from_zero
# # f() #TypeError: Point.calculate_distance_from_zero() missing 1 required positional argument: 'obj'
# print(f(p1))  # Output: 2.23606797749979
# print(f(p2))  # Output: 5.0

# def print_point(point):
#     """Print the coordinates of a point."""
#     print(f"Point coordinates: ({point.x}, {point.y})")
# print_point(p1)  # Output: Point coordinates: (1, 2)
# print_point(p2)  # Output: Point coordinates: (3, 4)
# Point.pprint = print_point
# p1.pprint()  # Output: Point coordinates: (1, 2)
# p2.pprint()  # Output: Point coordinates: (3, 4)    



class Point:
    def __init__(self, x=0, y=0):
        print(f"Creating a Point instance ({x}, {y})")
        self.x = x
        self.y = y

    def __del__(self):
        print(f"Deleting Point instance ({self.x}, {self.y})")

    def __add__(self, other):
        """Add two Point instances."""
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        return NotImplemented
    def __str__(self):
        """String representation of the Point instance."""
        return f"Point({self.x}, {self.y})"
    def __repr__(self):
        """String representation of the Point instance."""
        return f"({self.x}, {self.y})"
    def distance_from_zero(self):
        """Calculate the distance from the origin (0, 0)."""
        return (self.x ** 2 + self.y ** 2) ** 0.5
    def __lt__(self, other):
        """Less than comparison based on x and y coordinates."""
        if isinstance(other, Point):
            return self.distance_from_zero() < other.distance_from_zero()
        return NotImplemented
    def distance_from(self, other):
        """Calculate the distance from another Point instance."""
        if isinstance(other, Point):
            return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5
        return NotImplemented



# p1 = Point(1, 2)
# p2 = Point()
# def create_point_and_delete(x=0, y=0, return_value=False):
#     p3 = Point(x, y)
#     if return_value:
#         return p3

# create_point_and_delete(10, 20)
# p4 = create_point_and_delete(5, 6, True)
# print("End of main program")

p1 = Point(3, 2)
p2 = Point(1, 2)
p3 = p1 + p2
print(p3)  # Output: Point(4, 6)
points = [p1, p2, p3]
print(points)  # Output: [Point(1, 2), Point(3, 4), Point(4, 6)]
points.sort()
print(points)  # Output: [Point(1, 2), Point(3, 4), Point(4, 6)]

for point in points:
    for point2 in points:
        if point is not point2:
            print(f"Distance from {point} to {point2}: {point.distance_from(point2)}")

