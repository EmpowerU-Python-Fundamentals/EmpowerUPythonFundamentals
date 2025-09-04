# I. Ball-super-ball
class Ball(object):
    def __init__(self, ball_type="regular"):
        self.ball_type = ball_type

ball1 = Ball()
ball2 = Ball("super")

print(ball1.ball_type)
print(ball2.ball_type)


#II. Color-ghost
import random

class Ghost(object):
    def __init__(self):
        self.color = random.choice(["white", "yellow", "purple", "red"])


#III. Basic-subclasses-Adam-and-Eve
def God():
    return [Man(), Woman()]

class Human:
    pass

class Man(Human):
    pass

class Woman(Human):
    pass

creation = God()
print(isinstance(creation[0], Man))
print(isinstance(creation[1], Woman))
print(isinstance(creation[0], Human))
print(isinstance(creation[1], Human))


#IV. Classy-classes
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.info = f"{self.name}s age is {self.age}"

person = Person("John", 34)
print(person.info)


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
        raise ValueError("Class name must start with an uppercase letter and contain only alphanumeric characters.")
    
    cls.__name__ = new_name
    return cls

class MyClass:
    pass

print(MyClass.__name__)

class_name_changer(MyClass, "UsefulClass")
print(MyClass.__name__)

class_name_changer(MyClass, "SecondUsefulClass")
print(MyClass.__name__)