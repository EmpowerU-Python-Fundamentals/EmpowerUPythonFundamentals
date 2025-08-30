# 1. Ball-super-ball

class Ball(object):
    # your code goes here
    def __init__(self, ball_type = "regular"):
        self.ball_type = ball_type


# 2. Color-ghost

class Ghost(object):
    colors = ['white', 'yellow', 'purple', 'red']
    
    @property
    def color(self):
        import random
        return random.choice(self.colors)
    
# 3. Basic-subclasses-Adam-and-Eve

class Human():
    pass

class Man(Human):
    pass

class Woman(Human):
    pass


def God():
    return [Man(), Woman()]

print(God())


# 4. Classy-classes


class Person:
    def __init__(self, name, age):
        self.info=f"{name}s age is {age}"


# 5. Building Spheres

class Sphere:
    def __init__(self, radius, mass):
        self.radius = radius
        self.mass = mass

    def get_radius(self):
        return self.radius

    def get_mass(self):
        return self.mass

    def get_volume(self):
        return (4/3) * 3.14159 * (self.radius ** 3)

    def get_surface_area(self):
        return 4 * 3.14159 * (self.radius ** 2)
    
    def get_density(self):
        return self.get_mass() / self.get_volume()


# 6. Classy-Classes-2

def class_name_changer(cls, new_name):
    cls.__name__ = new_name
    return cls
