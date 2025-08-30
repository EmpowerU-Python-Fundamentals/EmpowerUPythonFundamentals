# Task 2: Human

class Human:
    species = "Homosapiens"

    def __init__(self, name):
        self.name = name

    def welcome(self):
        return f"Welcome, {self.name}!"

    @classmethod
    def get_species(cls):
        return f"This is a species of {cls.species}"

    @staticmethod
    def info():
        return "Humans are capable of abstract reasoning and language."


# Example usage
person = Human("Olga")

print(person.welcome())
print(Human.get_species())
print(Human.info())
