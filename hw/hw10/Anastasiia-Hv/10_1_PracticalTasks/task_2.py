class Human:
    species = "Homo sapiens"

    def __init__(self, name):
        self.name = name

    def welcome(self):
        print(f"Welcome, {self.name}!")

    @classmethod
    def get_species(cls):
        return f"Species: {cls.species}"

    @staticmethod
    def message():
        return "Have a great day!"


person1 = Human("Alice")
person2 = Human("Bob")

person1.welcome()
person2.welcome()

print(Human.get_species())
print(Human.message())