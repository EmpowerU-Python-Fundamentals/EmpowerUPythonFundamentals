# Task2.
# Create a class Human, everyone has a name,
# create a method in the class that displays a welcome message to each person.
# Create a class method in the class
#   that returns information
#   that it is a species of "Homosapiens".
# And in the class create a static method
#   that returns an arbitrary message.

class Human():
    def __init__(self, name: str):
        self._name = name
    
    @property
    def name(self):
        return self._name
    
    def welcome(self):
        print(f"Welcome, {self.name}")
    
    def species(self):
        return f"{self.name} is an exemplar of species 'Homosapiens'."
    
    @staticmethod
    def arbitrary_message():
        return "An arbitrary message."


#########################
# h1 = Human("Basil")
# h1.welcome()
# print(f"{h1.species() = }")
# print(f"{h1.arbitrary_message() = }")
# print(f"{Human.arbitrary_message() = }")
# h1.name = "sdfd"