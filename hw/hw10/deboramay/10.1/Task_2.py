class Human:

    def __init__(self, name: str):
        self.name = name

    def display_welcome_message(self):
        print(f"Привіт, {self.name}! Ласкаво просимо!")

    @classmethod
    def species_info(cls) -> str:
        return f"Цей вид {cls.__name__}s, наукова назва: Homosapiens."

    @staticmethod
    def arbitrary_message() -> str:
        return "Важливе повідомлення."

#Test:
person1 = Human("Ольга")
person1.display_welcome_message()
print(person1.species_info())
print(person1.arbitrary_message())
