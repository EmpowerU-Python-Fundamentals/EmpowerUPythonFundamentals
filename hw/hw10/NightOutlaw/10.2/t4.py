"""My way of solving task 4"""


class Person:
    """Base class: Person"""
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
        """Return person's info"""
        return f"{self.name}'s age is {self.age}"

    @property
    def info(self):
        """Property to display person's age """
        return self.get_info()
