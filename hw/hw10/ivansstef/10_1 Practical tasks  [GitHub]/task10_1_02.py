class Human:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, {self.name}!")

    @classmethod
    def species(cls):
        return "Homosapiens"

    @staticmethod
    def random_message():
        return "Who are you, Duddy!"

# Приклад:
person = Human("Alice")
#  Hello, Alice!
person.greet()  
# Homosapiens
print (Human.species())
# Who are you, Duddy!
print (Human.random_message())  
