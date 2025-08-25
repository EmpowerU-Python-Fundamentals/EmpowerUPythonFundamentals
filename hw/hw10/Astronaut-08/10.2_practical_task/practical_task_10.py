'''Practical tasks of module 10 by Astronaut_08'''
import random
import math
#Create a class Ball. Ball objects should accept one argument for "ball type" when instantiated.
#If no arguments are given, ball objects should instantiate with a "ball type" of "regular."
class Ball:
    '''DOC for Ball'''
    def __init__(self, types = 'regular'):
        self.types = types

    @property
    def ball_type(self):
        '''Return ball type'''
        return self.types

ball1 = Ball()
ball2 = Ball('super')
print(ball1.ball_type)
print(ball2.ball_type)

#Create a class Ghost
#Ghost objects are instantiated without any arguments.
#Ghost objects are given a random color attribute of "white" or
#"yellow" or "purple" or "red" when instantiated
class Ghost:
    '''This is DOC of class Ghost'''
    def __init__(self):
        self.col = ['white', 'yellow', 'purple', 'red'][random.randint(0, 3)]

    @property
    def color(self):
        '''Return color'''
        return self.col

ghost = Ghost()
print(ghost.color)

# According to the creation myths of the Abrahamic religions, Adam and Eve were the first
# Humans to wander the Earth.
# You have to do God's job. The creation method must return an array of length 2 containing objects
# (representing Adam and Eve). The first object in the array should be an instance of the class Man.
# The second should be an instance of the class Woman. Both objects have to be subclasses of Human.
# Your job is to implement the Human, Man and Woman classes.
class Human:
    '''DOC of class Human'''
    pass

class Man(Human):
    '''DOC of class Man'''
    pass

class Woman(Human):
    '''DOC of class Woman'''
    pass

def god():
    '''make human'''
    man = Man()
    woman = Woman()
    return [man, woman]

print(god())

# Your task is to complete this Class, the Person class has been created.
# You must fill in the Constructor method to accept a name as string and an age as number,
# complete the get Info property and getInfo method/Info getter which should return johns age is 34
# class Person
#    def __init__(name,age)
#         self.info="#{name}s age is #{age}"
class Person:
    '''This is DOC of class Person'''
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.info = f'{self.name}s age is {self.age}'

person = Person('Vova', 27)
print(person.info)

# Now that we have a Block let's move on to something slightly more complex: a Sphere.
# Arguments for the constructor
# radius -> integer or float (do not round it)
# mass -> integer or float (do not round it)
# Methods to be defined
# get_radius()       =>  radius of the Sphere (do not round it)
# get_mass()         =>  mass of the Sphere (do not round it)
# get_volume()       =>  volume of the Sphere (rounded to 5 place after the decimal)
# get_surface_area() =>  surface area of the Sphere (rounded to 5 place after the decimal)
# get_density()      =>  density of the Sphere (rounded to 5 place after the decimal)
# Example
# ball = Sphere(2,50)
# ball.get_radius() ->       2
# ball.get_mass() ->         50
# ball.get_volume() ->       33.51032
# ball.get_surface_area() -> 50.26548
# ball.get_density() ->      1.49208
# Any feedback would be much appreciated
class Sphere:
    '''DOC string Sphere'''
    def __init__(self, radius: float, mass: float):
        self.radius = radius
        self.mass = mass
        self.volume = None
        self.surface = None
        self.rho = None

    def get_radius(self):
        '''Method return radius'''
        return self.radius

    def get_mass(self):
        '''Method return mass'''
        return self.mass

    def get_volume(self):
        '''Method return volume'''
        self.volume = (4/3) * math.pi * self.radius ** 3
        return round(self.volume, 5)

    def get_surface_area(self):
        '''Method return surface'''
        self.surface = 4 * math.pi * self.radius ** 2
        return round(self.surface, 5)

    def get_density(self):
        '''Method return density'''
        self.volume = (4/3) * math.pi * self.radius ** 3
        self.rho = self.mass / self.volume
        return round(self.rho, 5)

ball = Sphere(2, 50)
print(ball.get_radius())
print(ball.get_mass())
print(ball.get_volume())
print(ball.get_surface_area())
print(ball.get_density())

# Timmy's quiet and calm work has been suddenly stopped by his project manager
# (let's call him boss) yelling:
# - Who named these classes?! Class MyClass? It's ridiculous! I want you
# to change it to UsefulClass!
# Tim sighed, he already knew it's gonna be a long day.
# Few hours later, boss came again:
# Much better - he said - but now I want to change that class name to SecondUsefulClass,
# and went off. Although Timmy had no idea why changing name is so important for his boss,
# he realized, that it's not the end, so he turned to you, his guru, to help him and asked
# you to prepare some function, which could change name of given class.
# Note: Proposed function should allow only names with alphanumeric chars (upper & lower
# letters plus ciphers), but starting only with upper case letter. In other case it should
# raise an exception.
# Disclaimer: there are obviously betters way to check class name than in example cases,
# but let's stick with that, that Timmy yet has to learn them.
class MyClass:
    '''This class can change self-name'''
    @classmethod
    def class_name_changer(cls, new_name: str):
        '''This method change name class'''
        assert new_name[0].isupper() and new_name.isalnum()
        cls.__name__ = new_name

myclass = MyClass()
print(myclass.__class__.__name__)
myclass.class_name_changer('Super')
print(myclass.__class__.__name__)
