"""Task 2: Human class"""

class Human:
    """Human class"""
    species = "Homosapiens"

    def __init__(self, name):
        self.name = name

    def type(self):
        return self.species
    
    def greet(self):
        print(f"Hello, {self.name}.")

    @classmethod
    def get_species(cls):
        return cls.species

    @staticmethod
    def message():
        return "Some random human message"

# person1 = Human("John")
# person1.greet()
# print(person1.name)
# print(person1.get_species())
# print(person1.message())
