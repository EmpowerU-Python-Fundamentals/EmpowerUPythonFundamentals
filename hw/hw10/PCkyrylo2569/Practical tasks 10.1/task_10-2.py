class Human:
    def __init__(self, name):
        self.name = name

    def welcome(self):
        return f"Hello, my name is {self.name}"
    @classmethod
    def species(cls):
        return "Homosapiens"
    @staticmethod
    def arbitrary_message():
        return "Python is cool just like Vim or Neovim"
    
person1 = Human("Alice")
person2 = Human("Bob")

print(person1.welcome())
print(person2.welcome())

print(Human.species())
print(Human.arbitrary_message())