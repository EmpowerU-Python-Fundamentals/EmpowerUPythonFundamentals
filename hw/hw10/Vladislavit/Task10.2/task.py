import re
import math
import random

#Task 1
class Ball:
    def __init__(self, ball_type="regular"):
        self.ball_type = ball_type

#Task 2
class Ghost:
    def __init__(self):
        self.color = random.choice(["white", "yellow", "purple", "red"])

#Task 3
class Human:
    pass

class Man(Human):
    pass

class Woman(Human):
    pass

def God():
    return [Man(), Woman()]

#Task 4
class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    @property
    def info(self):
        return f"{self.name}s age is {self.age}"

#Task 5
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
        return round((4/3) * math.pi * self.radius**3, 5)

    def get_surface_area(self):
        return round(4 * math.pi * self.radius**2, 5)

    def get_density(self):
        return round(self.mass / self.get_volume(), 5)
    
#Task 6
def class_name_changer(cls, new_name: str):
    if not re.match(r"^[A-Z][A-Za-z0-9]*$", new_name):
        raise Exception("Invalid class name")
    cls.__name__ = new_name
    return cls