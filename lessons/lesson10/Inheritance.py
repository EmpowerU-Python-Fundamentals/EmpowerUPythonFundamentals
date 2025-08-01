# class Point:
#     count = 0
#     def __init__(self, x, y):
#         print(f"init a Point instance with coordinates ({x}, {y})")
#         Point.count += 10
#         self.x = x
#         self.y = y

#     def __str__(self):
#         return f"Point({self.x}, {self.y})"

#     def __repr__(self):
#         return f"({self.x}, {self.y})"

#     def print_coordinates(self):
#         print(f"Coordinates: ({self.x}, {self.y})")

# class Point3D(Point):
#     count = 0
#     def __init__(self, x, y, z):
#         print(f"init a Point3D instance with coordinates ({x}, {y}, {z})")
#         Point3D.count += 1
#         super().__init__(x, y)
#         self.z = z

#     def __str__(self):
#         return f"Point3D({self.x}, {self.y}, {self.z})"
    
#     def parent_count(self):
#         return super().count



# # points = [Point(1, 2), Point(1, 2),Point3D(5, 6, 7)]
# # for point in points:
# #     print(point)  # Calls __str__
# #     print(repr(point))  # Calls __repr__
# #     point.print_coordinates()  # Calls print_coordinates
# # from pprint import pprint
# # print(points[0].__dict__)  # Accessing attributes of Point
# # print(points[1].__dict__)  # Accessing attributes of Point3D
# # pprint(Point.__dict__)  # Accessing attributes of Point3D
# # pprint(Point3D.__dict__)  # Accessing attributes of Point3D
# # print(id(points[1].print_coordinates)) 

# # print(Point.count)  # Accessing class variable count from Point
# # print(Point3D.count)  # Accessing class variable count from Point3D

# # print(points[0].count)  # Accessing class variable count from Point instance
# # print(points[2].count)  # Accessing class variable count from Point3D instance


# print("\ncreating instances of Point")
# point = Point(1, 2)
# print("\ncreating instances of Point3D")
# point3d = Point3D(3, 4, 5)

# print(point3d.count)
# print(point3d.parent_count())  # Accessing parent class count from Point3D instance


# class A:
#     def __init__(self):
#         self.value = "A"
#         self.display()
#     def display(self):
#         print(f"Class A: {self.value}")

# class B(A):
#     def __init__(self):
#         super().__init__()
#         self.value = "B"
#     def display(self):
#         print(f"Class B: {self.value}")

# a = A()
# a.display()  # Calls A's display method
# b = B()
# b.display()  # Calls B's display method

# print(f"{isinstance(b, B)=}")  # True
# print(f"{isinstance(b, A)=}")  # True, because B is a subclass of A
# print(f"{isinstance(b, object)=}")  # True, because B is a subclass of object
# print(f"{isinstance(a, A)=}")  # True, because all classes in Python inherit from object
# print(f"{isinstance(a, B)=}")  # True, because all classes in Python inherit from object
# print(f"{issubclass(B, A)=}")  # True, because B is a subclass of A
# print(f"{issubclass(A, B)=}")  # False, because A is not a subclass
# print(f"{issubclass(B, object)=}")  # True, because B is a subclass of object
# print(f"{issubclass(B, B)=}")  # True, because B is a subclass of object


# class Matrix:
#     def __init__(self, rows, cols):
#         self.rows = rows
#         self.cols = cols
#         self.data = [[0 for _ in range(cols)] for _ in range(rows)]

#     def __str__(self):
#         result = "Matrix:\n"
#         for row in self.data:
#             result += ' '.join(map(str, row)) + '\n'
#         return result
    
#     def set_value(self, row, col, value):
#         if 0 <= row < self.rows and 0 <= col < self.cols:
#             self.data[row][col] = value
#         else:
#             print("Index out of bounds")

#     def get_value(self, row, col):
#         if 0 <= row < self.rows and 0 <= col < self.cols:
#             return self.data[row][col]
#         else:
#             print("Index out of bounds")
#             return None
#     def max_value(self):
#         return max(max(row) for row in self.data)
    
#     def get_sum(self):
#         return sum(sum(row) for row in self.data)
# m = Matrix(3, 3)
# print(m)  # Initial empty matrix
# m = Matrix(5, 4)
# print(m)  # Initial empty matrix
# m.set_value(0, 0, 1)
# m.set_value(1, 1, 2)
# m.set_value(2, 2, 3)
# m.set_value(3, 3, 4)
# print(m)  # Matrix after setting some values
# print("Max value in the matrix:", m.max_value())  # Should print 4
# print("Sum of all values in the matrix:", m.get_sum())  # Should print 10

class Human:
    def __init__(self, name, age, city="Unknown"):
        self.name = name
        self.age = age
        self.city = city

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, City: {self.city}")
    def set_city(self, city):
        self.city = city
    


class Student(Human):
    def __init__(self, name, age, city, student_id):
        super().__init__(name, age, city)
        self.student_id = student_id

    def display_info(self):
        super().display_info()
        print(f"Student ID: {self.student_id}")
    def eat(self):
        print(f"{self.name} is eating.")

class Teacher(Human):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def display_info(self):
        super().display_info()
        print(f"Subject: {self.subject}")

    def set_subject(self, subject):
        self.subject = subject
        