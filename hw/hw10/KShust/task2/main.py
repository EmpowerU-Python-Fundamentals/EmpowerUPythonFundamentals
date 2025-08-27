#Regular Ball Super Ball
class Ball(object):
  def __init__(self, type = "regular"):
    self.ball_type = type

#Ghost color
import random

class Ghost(object):
  def __init__(self):
    self.color = random.choice(["white", "yellow", "purple", "red"])

#Adam and Eve
def God():
    return [Man(), Woman()]

class Human(object):
    pass

class Man(Human):
    pass
    
class Woman(Human):
    pass

#Classy Classes
class Person:
    def __init__(self, name, age):
        self.info = f"{name}s age is {age}"

#Building Spheres
import math
class Sphere(object):
	
    def __init__(self, *object):
        self.radius, self.mass = object
        
    def get_radius(self):
        return self.radius
    def get_mass(self):
        return self.mass
    def get_volume(self):
        return round((self.radius ** 3 * math.pi * 4 / 3), 5)
    def get_surface_area(self):
        return round((self.radius ** 2 * 4 * math.pi), 5)
    def get_density(self):
        return round((self.mass / self.get_volume()), 5)

#Python's Dynamic Classes #1
def class_name_changer(cls, new_name) :
    if not new_name[0].isupper() or not new_name.isalnum():
        raise NameError('Invalid class name!')
    cls.__name__ = new_name
