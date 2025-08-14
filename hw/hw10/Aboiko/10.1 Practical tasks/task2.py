class Human:
    species = "Homosapiens"

    def __init__(self, name):
        self.name = name

    def welcome(self):
        return f"Welcome, {self.name}!"

    @classmethod
    def get_species(cls):
        return f"This is a species of '{cls.species}'."

    @staticmethod
    def arbitrary_message():
        return "This is arbitrary message."

person1 = Human("Anton")
print(person1.welcome())
print(Human.get_species())
print(Human.arbitrary_message())
