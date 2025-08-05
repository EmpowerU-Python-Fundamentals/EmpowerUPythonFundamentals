class Human:
    species = "Homosapiens"

    def __init__(self, name):
        self.name = name

    def welcome(self):
        print(f"Welcome, {self.name}!")

    @classmethod
    def get_species(cls):
        return f"This human is a species of {cls.species}"

    @staticmethod
    def arbitrary_message():
        return "Have a great day!"

person = Human("Anna")
person.welcome()
print(Human.get_species())
print(Human.arbitrary_message())
