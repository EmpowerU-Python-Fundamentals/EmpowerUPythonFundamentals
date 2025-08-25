# task1
class Ball:
    def __init__(self, ball_type='regular'):
        self.ball_type = ball_type


# task2
import random

class Ghost:
    def __init__(self):
        self.color = random.choice(('white', 'yellow', 'purple', 'red'))


# task3
class Human:
    def __init__(self, name):
        self.name = name

class Man(Human):
    pass

class Woman(Human):
    pass

def God():
    return Man('Adam'), Woman('Eve')


# task4
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def info(self):
        return f'{self.name}s age is {self.age}'


# task5
from math import pi
class Sphere():
    def __init__(self, radius, mass):
        self.radius=radius
        self.mass=mass

    def get_radius(self):
        return self.radius

    def get_mass(self):
        return self.mass

    def get_volume(self):
        return round(4/3*pi*self.radius**3, 5)

    def get_surface_area(self):
        return round(4*pi*self.radius**2, 5)

    def get_density(self):
        return round(self.mass/self.get_volume(), 5)


# task6
def class_name_changer(cls, new_name):
    if new_name.isalnum() and new_name[0].isupper():
        cls.__name__ = new_name
    else:
        raise ValueError
