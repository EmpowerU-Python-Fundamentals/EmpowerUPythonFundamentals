class Human:
    def __init__(self, name):
        self.name = name

    def welcome_message(self):
        return f"Welcome, {self.name}!"

    @classmethod
    def species_info(cls):
        return "This is a species of 'Homo sapiens'."

    @staticmethod
    def arbitrary_message():
        return "This is an arbitrary message for you."

print(Human("Gogi").welcome_message())
print(Human("Gogi").species_info())
print(Human("Gogi").arbitrary_message())