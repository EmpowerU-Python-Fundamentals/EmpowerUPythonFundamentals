class Human:
    species = "Homosapiens"

    def __init__(self, name):
        self.name = name

    def greeting(self):
        return f"Welcome, {self.name}!"

    @classmethod
    def get_species(cls):
        return f"You are {cls.species}."

    @staticmethod
    def arbitary_message():
        return "Have a nice day!"

name = input("Input your name: ")
person = Human(name)

print(person.greeting())
print(person.get_species())
print(person.arbitary_message())