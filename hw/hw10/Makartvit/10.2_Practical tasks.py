# Ball-super-ball

class Ball(object):
    def __init__(self, ball_type="regular"):
        self.ball_type = ball_type


# Color-ghost

from random import choice


class Ghost(object):
    def __init__(self):
        self.color = choice(("white", "yellow", "purple", "red"))


# Basic-subclasses-Adam-and-Eve
class Human:
    pass


class Man(Human):
    pass


class Woman(Human):
    pass


def God():
    return [Man(), Woman()]


# Classy-classes

class Person:
    def __init__(self, name, age):
        self.info = f"{name}s age is {age}"


# Building Spheres

from math import pi


class Sphere:
    def __init__(self, r, m):
        self.r, self.m = r, m

    def get_radius(self): return self.r

    def get_mass(self): return self.m

    def get_volume(self): return round(4 / 3 * pi * self.r ** 3, 5)

    def get_surface_area(self): return round(4 * pi * self.r ** 2, 5)

    def get_density(self): return round(self.m / (4 / 3 * pi * self.r ** 3), 5)


# Dynamic Classes

def class_name_changer(cls, new_name):
    if not new_name or not new_name[0].isupper() or not new_name.isidentifier():
        raise ValueError
    cls.__name__ = new_name
