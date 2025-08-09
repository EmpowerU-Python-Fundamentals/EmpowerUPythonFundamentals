class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def info(self):
        return f"{self.name} має {self.age} років"

person = Person("Іван", 34)
print(person.info)
