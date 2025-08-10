#Regular Ball Super Ball
#If no arguments are given, ball objects should instantiate with a "ball type" of "regular."
class Ball():
  def __init__(self, ball_type="regular"):
    self.ball_type = ball_type

#Color Ghost 
# Ghost objects are given a random color attribute of "white" or "yellow" or "purple" or "red" when instantiated
from random import choice
class Ghost(object):
    def __init__(self):
        self.color = choice(["red","yellow","purple","white"])

#Basic subclasses - Adam and Eve
#The first object in the array should be an instance of the class Man. 
# The second should be an instance of the class Woman. 
# Both objects have to be subclasses of Human
class Human():
    def __init__(self):
        pass

class Man(Human):
    def __init__(self):
        pass
        
class Woman(Human):
    def __init__(self):
        pass
        
def God():
    return [Man(), Woman()]
  
#Classy Classes
#task is complete class Person
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.info = f"{self.name}s age is {self.age}"
        
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
        self.volume = round(4/3 * pi * self.radius ** 3, 5)
        return self.volume

    def get_surface_area(self):
        return round(4 * pi * self.radius ** 2, 5)
    
    def get_density(self):
        return round(self.mass / self.volume, 5)
      
#Dynamic Classes
def class_name_changer(cls, new_name):
    if not (new_name[0].isupper() and new_name.isalnum()):
        raise ValueError("Class name must start with an uppercase letter and contain only alphanumeric characters.")
    
    cls.__name__ = new_name