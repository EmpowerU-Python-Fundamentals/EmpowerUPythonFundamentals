class Human:

    def __init__(self, name):
        self.name = name

    def welcome_message(self):
        return f"Вітаємо, {self.name}!"

    @classmethod
    def species_info(cls):
        return "Цей вид: Homosapiens."

    @staticmethod
    def arbitrary_message():
        return "Це довільне повідомлення."

# Приклад використання
person = Human("Олександр")
print(person.welcome_message())
print(Human.species_info())
print(Human.arbitrary_message())