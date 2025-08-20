#I. Ball-super-ball
class Ball(object):
    def __init__(self, ball_type="regular"):
        self.ball_type = ball_type

#II. Color-ghost
import random

class Ghost:
    def __init__(self):
        self.color = random.choice(["white", "yellow", "purple", "red"])

#III. Basic-subclasses-Adam-and-Eve
class Human:
    pass

class Man(Human):
    pass

class Woman(Human):
    pass

def God():
    return [Man(), Woman()]

#IV. Classy-classes
class Person:
    def __init__(self, name, age):
        self._info = f"{name}s age is {age}"

    def getInfo(self):
        return self._info

    # або через property:
    @property
    def info(self):
        return self._info

#V. Building Spheres
import math

class Sphere:
    def __init__(self, radius, mass):
        self.radius = radius
        self.mass = mass

    def get_radius(self):
        return self.radius

    def get_mass(self):
        return self.mass

    def get_volume(self):
        volume = (4/3) * math.pi * self.radius**3
        return round(volume, 5)

    def get_surface_area(self):
        surface_area = 4 * math.pi * self.radius**2
        return round(surface_area, 5)

    def get_density(self):
        volume = (4/3) * math.pi * self.radius**3
        density = self.mass / volume
        return round(density, 5)

#VI. Dynamic Classes
def class_name_changer(cls, new_name):
    if not new_name.isalnum() or not new_name[0].isupper():
        raise Exception("Invalid class name")
    cls.__name__ = new_name