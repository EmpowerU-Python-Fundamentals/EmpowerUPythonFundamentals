#IV. Classy-classes

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def info(self):
        return f"{self.name}s age is {self.age}"


person = Person("Igor", 30)
print(person.info) 

