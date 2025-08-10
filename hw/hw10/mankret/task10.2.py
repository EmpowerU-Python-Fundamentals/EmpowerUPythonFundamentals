#  I. Ball-super-ball
#
# class Ball(object):
#     def __init__(self, ball_type='regular'):
#         self.ball_type = ball_type
#         print(f"{self.ball_type}")
#
#
# ball1 = Ball()
# ball2 = Ball("super")
# ball1.ball_type
# ball2.ball_type
#


# II. Color-ghost
# import random
#
#
# class Ghost:
#     def __init__(self, color=None):
#         self.color = random.choice(['white', 'yellow', 'purple', 'red'])


# III. Basic-subclasses-Adam-and-Eve

# class Human:
#     pass
# class Man(Human):
#     pass
# class Woman(Human):
#     pass
# def God():
#     return [Man(), Woman()]


# IV. Classy-classes
# class Person:
#     def __init__(self, name, age):
#         self.info=f"{name}s age is {age}"


# V. Building Spheres

# import math
#
#
# class Sphere(object):
#
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
#         return round(float((4 / 3) * math.pi * (self.radius ** 3)), 5)
#
#     def get_surface_area(self):
#         return round(float(4 * math.pi * (self.radius ** 2)), 5)
#
#     def get_density(self):
#         return round(float(self.mass / self.get_volume()), 5)
#

# VI. Dynamic Classes

# def class_name_changer(cls, new_name):
#     if not new_name or not new_name[0].isupper():
#         raise ValueError("The name must start with a capital letter.")
#
#     if not new_name.isalnum():
#         raise ValueError("The name can only contain letters and numbers.")
#
#     cls.__name__ = new_name
