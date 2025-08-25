class Human:
    species = "Homosapiens"

    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, {self.name}! Welcome!")

    @classmethod
    def get_species(cls):
        return f"This species is {cls.species}."

    @staticmethod
    def random_message():
        return "This is random message"

name = input("Input your name: ")
person = Human(name)

person.greet()

print(person.get_species())
print(person.random_message())