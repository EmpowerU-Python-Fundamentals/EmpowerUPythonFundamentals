class Human:
    species_name = "Homosapiens"

    def __init__(self, name: str):
        self.name = name

    def greet(self) -> None:
        print(f"Привіт, {self.name}!")

    @classmethod
    def species(cls) -> str:
        return f"Species: {cls.species_name}"

    @staticmethod
    def random_message() -> str:
        return "Майте гарний день!"
