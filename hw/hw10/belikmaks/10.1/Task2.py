class Human:
    def __init__(self, name):
        self.name = name

    def welcome(self):
        return f"Welcome, {self.name}!"

    @classmethod
    def species(cls):
        return "Homosapiens"

    @staticmethod
    def random_message():
        return "Learning Python is fun!"


h1 = Human("Maksym")
print(h1.welcome())
print(Human.species())
print(Human.random_message())
