class Human:
    species = 'Homosapiens'
    def __init__(self, name: str):
        self.name = name

    def greetings(self) -> None:
        print(f"Greetings, {self.name}")

    @classmethod
    def get_species(cls) -> str:
        return cls.species
    
    @staticmethod
    def print_lalala():
        print("la-la-la")

# Test
alice = Human('Alice')
alice.greetings()
print(Human.get_species())
Human.print_lalala()
