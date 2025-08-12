"""Regular Ball Super Ball"""
class Ball():

    def __init__(self, ball_type="regular"):
        self.ball_type = ball_type


"""Color Ghost"""
import random


class Ghost(object):

    def __init__(self):
        self.color = random.choice(['white', 'yellow', 'purple', 'red'])


"""Basic subclasses - Adam and Eve"""
class Human():
    pass

class Man(Human):
    pass

class Woman(Human):
    pass

def God():
    return [Man(), Woman()]


"""Classy Classes"""
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.info = f"{self.name}s age is {self.age}"


"""Building Spheres"""
import math


class Sphere(object):
    def __init__(self, radius, mass):
        self.radius = radius
        self.mass = mass

    def get_radius(self):
        return self.radius

    def get_mass(self):
        return self.mass

    def get_volume(self):
        return round(4 * math.pi * pow(self.radius, 3) / 3, 5)

    def get_surface_area(self):
        return round(4 * math.pi * pow(self.radius, 2), 5)

    def get_density(self):
        return round(self.mass / self.get_volume(), 5)


    """Python's Dynamic Classes #1"""
import re

class MyClass():
    pass

def check_string(text):
    pattern = r"^[A-Z][a-zA-Z0-9]*$"
    return bool(re.match(pattern, text))

def class_name_changer(cls, new_name):
    if check_string(new_name):
        cls.__name__= new_name
    else:
        raise Exception('error')