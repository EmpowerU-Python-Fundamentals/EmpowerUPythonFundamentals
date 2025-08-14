# Practical Tasks

# I. Ball-super-ball
# Create a class Ball. Ball objects should accept one argument for "ball type" when instantiated.
# If no arguments are given, ball objects should instantiate with a "ball type" of "regular."
class Ball:
    def __init__(self, ball_type="regular"):
        self.ball_type=ball_type

ball1 = Ball()
ball2 = Ball("super")
ball1.ball_type  #=> "regular"
ball2.ball_type  #=> "super"


# II. Color-ghost
# Create a class Ghost
# Ghost objects are instantiated without any arguments.
# Ghost objects are given a random color attribute of "white" or "yellow" or "purple" or "red" when instantiated
import random

class Ghost():
    def __init__(self):
        self.color = random.choice(["white", "yellow", "purple", "red"])

ghost = Ghost()
ghost.color  #=> "white" or "yellow" or "purple" or "red"


# III. Basic-subclasses-Adam-and-Eve
# According to the creation myths of the Abrahamic religions, Adam and Eve were the first Humans to wander the Earth.
# You have to do God's job. The creation method must return an array of length 2 containing objects (representing Adam and Eve).
# The first object in the array should be an instance of the class Man. The second should be an instance of the class Woman.
# Both objects have to be subclasses of Human. Your job is to implement the Human, Man and Woman classes.
def God():
    return [Man(), Woman()]

class Human():
    def __init__(self, name):
        self.name=name
        
class Man(Human):
    def __init__(self):
        super().__init__(name="Adam")
        
class Woman(Human):
    def __init__(self):
        super().__init__(name="Eve")


# IV. Classy-classes
# Your task is to complete this Class, the Person class has been created.
# You must fill in the Constructor method to accept a name as string and an age as number, 
# complete the get Info property and getInfo method/Info getter which should return johns age is 34
class Person:
    def __init__(self, name: str, age: int):
        self.name=name
        self.age=age
        
    @property
    def info(self):
        return f"{self.name}s age is {self.age}"


# V. Building Spheres
# Now that we have a Block let's move on to something slightly more complex: a Sphere.
import math
class Sphere:
    def __init__(self, radius, mass):
        self.radius=radius
        self.mass=mass
        
    def get_radius(self):
        return self.radius
        
    def get_mass(self):
        return self.mass
    
    def get_volume(self):
        return (4/3)*math.pi*self.radius**3
    
    def get_surface_area(self):
        return 4*math.pi*self.radius**2
        
    def get_density(self):
        return self.mass/self.get_volume()


# VI. Dynamic Classes
# ...prepare some function, which could change name of given class.
import re

def class_name_changer(cls, new_name):
    if not re.match(r'^[A-Z][A-Za-z0-9]*$', new_name):
        raise Exception("Invalid class name!")

    cls.__name__ = new_name