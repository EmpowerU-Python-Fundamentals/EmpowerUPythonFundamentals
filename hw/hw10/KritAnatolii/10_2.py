#Regular Ball Super Ball
class Ball(object):
   def __init__(self, ball_type="regular"):
    self.ball_type = ball_type

#Color Ghost
import random
class Ghost(object):
    list_color = ["white", "yellow", "purple", "red"] 
    
    def __init__(self):
        self.color = random.choice(Ghost.list_color)

#Basic subclasses - Adam and Eve
def God():
    return [Man(),Woman()]
    
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
from math import pi

class Sphere(object):
    def __init__(self, radius, mass):
        self.radius = radius
        self.mass = mass
        
    def get_radius(self):
        return self.radius
    
    def get_mass(self):
        return self.mass
    
    def get_volume(self):
        self.volume = round( (4/3) * pi * self.radius**3, 5)
        return self.volume
    
    def get_surface_area(self): 
        self.surface_area = round( 4 * pi * self.radius**2, 5)
        return self.surface_area
    
    def get_density(self):
        self.density = round( self.mass / ((4/3) * pi * self.radius**3), 5)
        return self.density
    
#Python's Dynamic Classes #1
def class_name_changer(cls, new_name):
    if not new_name[0].isupper() or not new_name.isalnum():
         raise ValueError("only names with alphanumeric chars, but starting only with upper case letter.")
    cls.__name__ = new_name
    