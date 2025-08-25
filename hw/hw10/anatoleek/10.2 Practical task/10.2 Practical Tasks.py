#I. Ball-super-ball
class Ball(object):
    def __init__(self, ball_type="regular"):
        self.ball_type = ball_type

#II. Color-ghost
import random
class Ghost(object):
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
print(God())

#IV. Classy-classes
class Person:
    def __init__(self, name: str, age: int):
        self.name=name
        self.age=age
        self.info=f"{name}s age is {age}"

#V. Building Spheres
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
        return round((4/3)*math.pi*(self.radius**3),5)
    def get_surface_area(self):
        return round(4*math.pi*(self.radius**2),5)
    def get_density(self):
        return round(self.mass/((4/3)*math.pi*(self.radius ** 3)),5)

#VI. Dynamic Classes
def class_name_changer(cls, new_name):
        if not (new_name.isalnum() and new_name[0].isupper()):
            raise ValueError("Error")
        cls.__name__ = new_name
        return cls