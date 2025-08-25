# I - Ball-super-Ball
class Ball:
    def __init__(self, ball_type="regular"):
        self.ball_type = ball_type
# ==============================================


# II - Color Ghost
import random

class Ghost:
    COLORS = ("white", "yellow", "purple", "red")

    def __init__(self):
        self.color = random.choice(self.COLORS)
# ==============================================


# III - Basic-subclasses-Adam-and-Eve
class Human:
    pass

class Man(Human):
    pass

class Woman(Human):
    pass

def create():
    return [Man(), Woman()]
# ==============================================


# IV - Classy-classes
class Person:
    def __init__(self, name: str, age: int):
        self.name = str(name)
        self.age = int(age)

    @property
    def info(self) -> str:
        return f"{self.name}s age is {self.age}"

    def getInfo(self) -> str:
        return self.info
# ==============================================


# V - Building Spheres
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
        volume = (4/3) * math.pi * (self.radius ** 3)
        return round(volume, 5)

    def get_surface_area(self):
        surface_area = 4 * math.pi * (self.radius ** 2)
        return round(surface_area, 5)

    def get_density(self):
        density = self.mass / ((4/3) * math.pi * (self.radius ** 3))
        return round(density, 5)
# ==============================================


# VI - Dynamic Classes
def rename_class(cls, new_name):
    if not (new_name and new_name[0].isupper() and new_name.isalnum()):
        raise ValueError("Invalid class name: must start with uppercase letter and contain only alphanumeric characters")

    cls.__name__ = new_name
    return cls