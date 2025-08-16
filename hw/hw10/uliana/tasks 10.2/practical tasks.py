#Task 1
# class Ball:
#
#     def __init__(self, ball_type="regular"):
#         self.ballType = ball_type

#Task 2

# import random
#
# class Ghost:
#
#     colors = ["white", "yellow", "purple", "red"]
#
#     def __init__(self):
#         self.color = random.choice(Ghost.colors)

#Task 3

# class Human:
#     def __init__(self, name=None):
#         self.name = name
#
# class Man(Human):
#     def __init__(self, name="Adam"):
#         super().__init__(name)
#
# class Woman(Human):
#     def __init__(self, name="Eve"):
#         super().__init__(name)
#
# def creation():
#         return [Man(), Woman()]

#Task 4

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     @property
#     def constructor(self):
#         return f"{self.name}'s age is {self.age}"

#Task 5

# import math
#
# class Sphere:
#     def __init__(self, radius, mass):
#         self.radius = radius
#         self.mass = mass
#
#     def get_radius(self):
#         return self.radius
#
#     def get_mass(self):
#         return self.mass
#
#     def get_volume(self):
#         volume = (4/3)*math.pi*self.radius**3
#         return round(volume, 5)
#
#     def get_surface_area(self):
#         surface = 4 * math.pi * self.radius ** 2
#         return round(surface, 5)
#
#     def get_density(self):
#         dencity = self.mass / ((4/3)*math.pi*self.radius**3)
#         return round(dencity, 5)

#Task 6

# import re
#
# def change_name(cls, new_name):
#     if not re.fullmatch(r"[A-Z][a-zA-Z0-9]*", new_name):
#         raise ValueError("Name must start with uppercase and contain only alphanumeric characters")
#     cls.__name__ = new_name
#     globals()[new_name] = cls
#     return cls
