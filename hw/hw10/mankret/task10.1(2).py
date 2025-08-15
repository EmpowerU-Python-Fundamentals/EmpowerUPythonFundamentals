# Create a class Human, everyone has a name, create a method in the class that display a welcome message to each
# person. Create a class method in the class that returns information that it is a species of "Homosapiens". And in
# the class create static method that returns an arbitrary message.


class Human:
    species = "Homo sapiens"

    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print(f"Hello, {self.name}! Welcome.")

    @classmethod
    def get_species_info(cls):
        return f"This is a species {cls.species}."

    @staticmethod
    def get_arbitrary_message():
        return "This is static method"


person1 = Human("Sid")
person2 = Human("Nancy")

print("--- Instance methods ---")
person1.say_hello()
person2.say_hello()

# Виклик методу класу
print("\n--- Class methods ---")
print(Human.get_species_info())
print(person1.get_species_info())  # Not best practice

print("\n--- Static method ---")
print(Human.get_arbitrary_message())
print(person2.get_arbitrary_message())
