class Human():
    def __init__(self, name: str):
        self.name = name.capitalize()
        
    def display_message (self):
        return f"Welcome {(self.name)}"
    
    @classmethod
    def display_species(cls):
        return "You belongs to Homosapiens."
    
    @staticmethod
    def years_until_retirement(current_age: int):
        retirement_age = 65
        years_left = retirement_age - current_age
        result = years_left if years_left > 0 else 0
        return f"You will retire in {result} years."
    
ivan = Human("ivan")
print(ivan.display_message())
print(ivan.display_species())
print(ivan.years_until_retirement(32))