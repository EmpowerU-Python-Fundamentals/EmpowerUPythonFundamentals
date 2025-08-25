class Human:
    def __init__(self, name):
        self.name = name

    def welcome(self):
        return f"Hello, {self.name}! Nice to meet you!"

    @classmethod
    def Species(cls):
        return "Homo sapiens species"
    
    @staticmethod
    def Message():
        return "Life is good!"
    
    
person = Human("Yulia")
print(person.welcome())
print(Human.Species())
print(Human.Message())
