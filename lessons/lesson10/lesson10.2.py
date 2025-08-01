# class User:
#     count = 0
#     def __init__(self, username, email):
#         self.username = username
#         self.email = email
#         User.count += 1

#     def display_info(self):
#         print(f"Username: {self.username}")
#         print(f"Email: {self.email}")

#     def display_info(self, show_email=True):
#         print(f">> Username: {self.username}")
#         if show_email:
#             print(f">> Email: {self.email}")

# user = User("john_doe", "john@example.com")
# user.display_info()
# user.display_info(show_email=False)
# from pprint import pprint

# pprint(User.__dict__)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point({self.x}, {self.y})"

    def __repr__(self):
        return f"({self.x},{self.y})"
    
    def print_coordinates(self):
        print(f"Coordinates: ({self.x}, {self.y})")
    
class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def __str__(self):
        return f"Point3D({self.x}, {self.y}, {self.z})"
    def __repr__(self):
        return f"({self.x}, {self.y}, {self.z})"
    def print_coordinates(self):
        print(f"Coordinates: ({self.x}, {self.y}, {self.z})")
    
list_of_points = [Point(1, 2), Point(3, 4), Point3D(5, 6, 7)]
for point in list_of_points:
    print(point)  # Calls __str__
    print(repr(point))  # Calls __repr__
    point.print_coordinates()  # Calls print_coordinates